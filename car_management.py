import pika
from car_rpc import GetFuel, GetAccumulatorCharge

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='management', exchange_type='direct')

	channel.exchange_declare(exchange='monitore', exchange_type='direct')

	queue = channel.queue_declare(queue='', exclusive=True)
	queue_name = queue.method.queue

	channel.queue_bind(exchange='management', queue=queue_name, routing_key='open')
	channel.queue_bind(exchange='management', queue=queue_name, routing_key='open_windows')
	channel.queue_bind(exchange='management', queue=queue_name, routing_key='close')
	channel.queue_bind(exchange='management', queue=queue_name, routing_key='start_engine')

	channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
	channel.start_consuming()

def callback(ch, method, properties, body):
	routing_key_map = {
		'open': open_car,
		'close': close_car,
		'start_engine': start_engine,
		'open_windows': open_windows,
	}

	result = routing_key_map[method.routing_key]()

	ch.basic_publish(
		exchange='', 
		routing_key=properties.reply_to, 
		properties=pika.BasicProperties(correlation_id=properties.correlation_id),
		body=result)

def open_car():
	print('car opened')
	return 'car opened'

def close_car():
	print('car closed')
	return 'car closed'

def start_engine():
	get_fuel = GetFuel()
	accum_charge = GetAccumulatorCharge()

	if float(get_fuel()) < 1 or float(accum_charge()) < 12.4:
		print("engine didn't started")
		return "engine didn't started"

	print('engine started')
	return 'engine started'

def open_windows():
	print('windows opened')
	return 'windows opened'


if __name__ == '__main__':
	main()

