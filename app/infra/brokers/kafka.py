from kafka import KafkaProducer


class Kafka:
  
  def __init__(self, host, port):
    connection = f'{host}:{port}'
    self.__producer = KafkaProducer(bootstrap_servers=connection)

  def publish(self, topic: str, message: str):
    self.__producer.send(topic, str.encode(message))