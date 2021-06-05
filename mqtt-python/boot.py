import time
from mqtt import MQTTClient
# import ubinascii
# import machine
# import micropython
# import network
# import esp
# esp.osdebug(None)
import gc
gc.collect()

# MQTT Configs 
mqtt_server = 'www.maqiatto.com'
# client_id = ubinascii.hexlify(machine.unique_id())
client_id = 'meomeo'
last_message = 0
message_interval = 5
counter = 0

# Update below credentials with yours
# ssid = 'YOUR_WIFI_SSID'
# password = 'YOUR_WIFI_PASSWORD'
mqtt_user = 'shipangei00@gmail.com'
mqtt_pass = '!n&$NoF4hD2iwYZ'
topic_sub = b'shipangei00@gmail.com/temp'
# topic_sub = b'shipangei00@gmail.com/temp'
# topic_sub = b'shipangei00@gmail.com/temp'

# topic_pub = b'YOUR_TEST_TOPIC_AGAIN'

# WiFi settings
# station = network.WLAN(network.STA_IF)
# station.active(True)
# station.connect(ssid, password)

# while station.isconnected() == False:
#   pass

# print('Connection successful')
# print(station.ifconfig())

def sub_cb(topic, msg):
  print((topic, msg))

def connect_and_subscribe():
#   global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server, 1883, mqtt_user, mqtt_pass)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
#   machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      msg = b'maqiatto test #%d' % counter
    #   client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()