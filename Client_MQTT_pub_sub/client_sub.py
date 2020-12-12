#!/usr/bin/python3

#the entity which creates a topic and subscribe to it, waiting for some published message on that topic

import paho.mqtt.client as mqtt
import time
import sys
import subprocess



def parsing_parameters():
	l = len(sys.argv)
	port = 1883
	keepAlive = 60

    #Script with no parameters
	if(l == 1):
		print('''\n	Usage:

	python3 client_sub.py -a <Broker_Address> -p <Broker_Port> -k <Keep_Alive>

	-a
		IP address of MQTT broker

	-p
		port of MQTT broker (default 1883)

	-k
		keep alive parameter of MQTT protocol (default 60 sec)

            ''')
		exit()


	for i in range(1,l):
		if(sys.argv[i] == '-p' and i<l):
			port = sys.argv[i+1] #MQTT broker port
		elif(sys.argv[i] == '-k' and i<l):
			if(int(sys.argv[i+1]) > 65535 or int(sys.argv[i+1]) <= 0):
				keepAlive = 60
			else:
				keepAlive = sys.argv[i+1] #KeepAlive parameter of MQTT
		elif(sys.argv[i] == '-a' and i<l):
			broker_address = sys.argv[i+1] #IP broker address
		elif((sys.argv[i] == '--help' or sys.argv[i] == '-h') and i<=l):
			print('''\nUsage:

	python3 client_sub.py -a <Broker_Address> -p <Broker_Port> -k <Keep_Alive>

	-a
		IP address of MQTT broker

	-p
		port of MQTT broker (default 1883)

	-k
		keep alive parameter of MQTT protocol (default 60 sec)

            ''')
			exit()

	return broker_address, int(port), int(keepAlive)
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	if(rc == 0):
		print('\n[ Client connected successfully ]\n')
		
		#topic creation
		client.subscribe("TestTopic")
		print('[ Pubblication of TestTopic ]\n')
		print('[ Waiting for message ... ]\n')
		return
	elif(rc == 1):
		print('\n[ ERROR: Unacceptable protocol version ]')
	elif(rc == 2):
		print('\n[ ERROR: client identifier rejected ]')
	elif(rc == 3):
		print('\n[ ERROR: server unavailable ]')
	elif(rc == 4):
		print('\n[ ERROR: bad username or password ]')
	elif(rc == 5):
		print('\n[ ERROR: not authorized ]')
	
	exit() #error case

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f'\nSomeone published: {msg.topic} {str(msg.payload)}')
#---------------------------------------------------------------------------------------

try:
	print('\nSubscriber creating new topic and subscribe to it.\n')

	broker, port, keep = parsing_parameters()

	client = mqtt.Client(client_id="client_sub")
	client.on_connect = on_connect
	client.on_message = on_message

	client.connect(broker, port, keep)

	client.loop_forever()

except KeyboardInterrupt:
	client.disconnect()
	subprocess.call('clear', shell=True)
	print('[ Client disconnected successfully ]')

except ConnectionRefusedError:
	print('[ ERROR: connection refused ]')
