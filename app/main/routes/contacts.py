from fastapi import APIRouter
from app.main.forms.contact import ContactPayload
from app.adapters.broker import Broker
from app.infra.brokers.kafka import Kafka
from app.main.configs import topics
from json import dumps

router = APIRouter(prefix="/contacts")
broker = Broker(
  broker_class=Kafka(host="localhost", port=9092),
)

@router.get("")
async def root():
  return { "message": "Api UP" }

@router.post("")
async def send_message_to_contact_topic(payload: ContactPayload):
  """
  Aqui eu vou receber o payload enviadp pelo front
  e enviar para fila contact.
  """
  message = dumps(payload.dict())
  broker.publish(topics.CONTACT, message)
  return "Message sent to contact queue"