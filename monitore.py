import pika

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='monitore', exchange_type='direct')

	queue = channel.queue_declare(queue='', exclusive=True)
	queue_name = queue.method.queue

	channel.queue_bind(exchange='monitore', queue=queue_name, routing_key='set_temperature_start_engine')
	channel.queue_bind(exchange='monitore', queue=queue_name, routing_key='get_fuel')
	channel.queue_bind(exchange='monitore', queue=queue_name, routing_key='get_accumulator_charge')

	channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
	channel.start_consuming()

def callback(ch, method, properties, body):
	routing_key_map = {
		'set_temperature_start_engine': set_temperature_start_engine,
		'get_fuel': get_fuel,
		'get_accumulator_charge': get_accumulator_charge,
	}

	result = routing_key_map[method.routing_key]()

	ch.basic_publish(
		exchange='', 
		routing_key=properties.reply_to, 
		properties=pika.BasicProperties(correlation_id=properties.correlation_id),
		body=result)

def set_temperature_start_engine():
	return 'success'

def get_fuel():
	return '5'

def get_accumulator_charge():
	return '13'

def check_temperature_for_start():
	...

if __name__ == '__main__':
	main()