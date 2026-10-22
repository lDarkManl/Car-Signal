import pika
import uuid

CONNECTIONPARAMETERS = 'localhost'

class OpenCar:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='management', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='management',
			routing_key='open',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class CloseCar:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='management', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='management',
			routing_key='close',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class OpenWindows:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='management', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='management',
			routing_key='open_windows',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class StartEngine:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='management', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self, wait=True):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='management',
			routing_key='start_engine',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		if wait:
			self.response = None

			while self.response is None:
				self.connection.process_data_events(time_limit=None)
			return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class GetFuel:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='monitore', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='monitore',
			routing_key='get_fuel',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class GetAccumulatorCharge:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='monitore', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='monitore',
			routing_key='get_accumulator_charge',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class SetTemperatureStartEngine:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='monitore', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self, temp):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='monitore',
			routing_key='set_temperature_start_engine',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=str(temp)
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class GetOilTemp:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='monitore', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='monitore',
			routing_key='get_oil_temp',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

class GetEngineTemp:
	corr_id = None
	queue_name = None

	def __init__(self):
		self.connection = pika.BlockingConnection(
			pika.ConnectionParameters(CONNECTIONPARAMETERS)
		)

		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='monitore', exchange_type='direct')

		queue = self.channel.queue_declare(queue='', exclusive=True)
		self.queue_name = queue.method.queue

		self.channel.basic_consume(
			queue=self.queue_name,
			on_message_callback=self._response,
			auto_ack=True
		)

	def __call__(self):
		self.corr_id = str(uuid.uuid4())

		self.channel.basic_publish(
			exchange='monitore',
			routing_key='get_engine_temp',
			properties=pika.BasicProperties(
			    reply_to=self.queue_name,
			    correlation_id=self.corr_id,
			),
			body=''
		)

		self.response = None

		while self.response is None:
			self.connection.process_data_events(time_limit=None)
		return self.response

	def _response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body