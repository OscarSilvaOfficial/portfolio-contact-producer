class Broker:
  
  def __init__(self, broker_class):
    self.__broker = broker_class
    
  def publish(self, topic: str, message: str):
    self.__broker.publish(topic, message)