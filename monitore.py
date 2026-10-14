import pika
from car_rpc import StartEngine
from time import time

class Monitore:

    def __init__(self):
        self.fuel = 5.0
        self.accumulator_charge = 13.0
        self.temperature = -20
        self.temperature_start_engine = -21

        self.started = 0

    def get_fuel(self, body=None):
        return str(self.fuel)

    def get_accumulator_charge(self, body=None):
        return str(self.accumulator_charge)

    def get_temperature(self, body=None):
    	return str(self.temperature)

    def set_temperature_start_engine(self, temperature):
        self.temperature_start_engine = float(temperature.decode('utf-8'))
        return "success"

    def start_if_need(self):
        if (self.temperature <= self.temperature_start_engine) and (time() - self.started > 1200):
        	print("need to start engine")
        	start_engine = StartEngine()	
        	start_engine(wait=False)
        	self.started = time()

monitore = Monitore()

def main():

	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='monitore', exchange_type='direct')

	queue = channel.queue_declare(queue='', exclusive=True)
	queue_name = queue.method.queue

	channel.queue_bind(exchange='monitore', queue=queue_name, routing_key='set_temperature_start_engine')
	channel.queue_bind(exchange='monitore', queue=queue_name, routing_key='get_fuel')
	channel.queue_bind(exchange='monitore', queue=queue_name, routing_key='get_accumulator_charge')
	channel.queue_bind(exchange='monitore', queue=queue_name, routing_key='get_temperature')

	channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

	while True:
		monitore.start_if_need()
		connection.process_data_events(time_limit=1)

def callback(ch, method, properties, body):

	routing_key_map = {
		'set_temperature_start_engine': monitore.set_temperature_start_engine,
		'get_fuel': monitore.get_fuel,
		'get_accumulator_charge': monitore.get_accumulator_charge,
		'get_temperature': monitore.get_temperature
	}

	result = routing_key_map[method.routing_key](body)

	ch.basic_publish(
		exchange='', 
		routing_key=properties.reply_to, 
		properties=pika.BasicProperties(correlation_id=properties.correlation_id),
		body=result)

if __name__ == '__main__':
	main()