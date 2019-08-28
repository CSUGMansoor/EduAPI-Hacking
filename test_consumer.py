from datetime import datetime
from dateutil.parser import parse
from azure.servicebus import ServiceBusClient
import json

connection_str='Endpoint=sb://eduapi.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=CkeuHxMqbJx8eNS8akhffctarEdSmpp+VxubldASl1A=;TransportType=Amqp'
topic='synceducationoffering'
subscription='demo_educationoffering_sub_b'
sb_client = ServiceBusClient.from_connection_string(connection_str)

topic_client = sb_client.get_subscription(topic,subscription)

messages = topic_client.get_receiver()
for message in messages:
   
   try:
      parsed_message = json.loads(str(message))
      start_date = parse(parsed_message["educationOffering"]["startDate"])
      if start_date.date() >= datetime.today().date():
         print(json.dumps(parsed_message, indent=4, sort_keys=True))

   except ValueError:
      print(message)
   

   message.complete()