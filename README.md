# MQTT_DoS_attack

This is the final project for Data and System Security course at [University of Pisa](https://cysec.unipi.it/).

This project uses the [Eclipse Paho MQTT Python client library](https://pypi.org/project/paho-mqtt/), which implements versions 5.0, 3.1.1, and 3.1 of the MQTT protocol. This library provides a client class which enable applications to connect to an MQTT broker to publish messages, and to subscribe to topics and receive published messages. It supports Python 2.7.9+ or 3.5+.


## Description

**MQTT Protocol**

MQ Telemetry Transport (MQTT) is an application layer protocol nowadays adopted for different applications, such as handling mobility, monitoring data, notification systems and, since 2016, it is the reference standard for communications on Internet of Things (IoT) environments. 

The protocol has a publish/subscribe communication model based on a central node hosting the MQTT server, called broker. Clients are able to send or publish informations and messages on a given topic, and the broker will send such informations to the customers that previously subscribed the same topic.

MQTT was declared as the reference standard for IoT communications because it can be used on wireless networks with limited bandwidth constraints or through unreliable connections. Indeed, in MQTT, if the connection between a subscriber and a broker is interrupted, each message will be stored by the broker and sent only once the communication is re-established. 

**SlowITe attack**

The Slow DoS against Internet of Things Environments (SlowITe) attack is a denial of service threat targeting the MQTT protocol. It belongs to the category of Slow DoS attacks, which are able to target TCP-based protocols only, making use of minimum attack bandwidth and resources to target a network service executing a denial of service. Since MQTT runs over TCP, it is a target by SlowITe.

The aim of this attack is to instantiate a high number of connections with the MQTT broker, in order to seize all available connections the server is able to manage simultaneously. When DoS state is reached, the attacker keeps the MQTT broker busy as long as possible, using at the same time the least possible bandwidth. 

SlowITe exploits the CONNECT packet sent in MQTT to instantiate the communication with the broker. Once the server has received such packet, it has to keep the connection alive for a period of time (in seconds) equal to 1,5 * Keep-Alive (default value = 60 sec). The attack exploits a specific vulnerability of MQTT that makes the attacker able to set the Keep-Alive parameter to an arbitrary value. Such openness of the protocol should be considered a relevant weakness of the MQTT protocol. It is possible for the client to configure the behavior of the server, in terms of the expiration of the timeouts used for connection closures. Being 16 bits allocated to the value of Keep-Alive on the MQTT CONNECT packet, it is possible to specify a maximum value of Keep-Alive equal to 65.535. 


## Idea of the project

The purpose of the project is to experiment the SlowITe attack on MQTT and validate the results outlined in the article "*SlowITe, a Novel Denial of Service Attack Affecting MQTT*", written by I. Vaccari, M. Aiello and E. Cambiaso. To do this, we have used the following 4 Python scripts:

 - **MQTT_SlowDoS.py**: it runs SlowITe attack against an MQTT broker.
 - **MQTT_keepAlive.py**: it tests different values of the keep_alive parameter (used in connect() method) and their effects.
 - **client_pub.py**: it represents a publisher that send a message about a specific topic to the MQTT broker.
 - **client_sub.py**: it represents a subscriber that creates a topic and subscribes to it at the MQTT broker.

## Prerequisites

First of all, you have to type the following line on your shell in order to install and manage the other software packages, written in Python, used in this project (for more info click [here](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)).

```bash
sudo apt install python3-pip
```
Then, you have to install on Ubuntu:

 - [paho-mqtt](https://pypi.org/project/paho-mqtt/): provides a client class which enable applications to connect to an MQTT broker to publish messages, and to subscribe to topics and receive published messages.
	  ```bash
	 sudo pip3 install paho-mqtt
	```
 - [tqdm](https://pypi.org/project/tqdm/): shows a progress in a loop, using a smart progress meter.
	 ```bash
	 sudo pip3 install tqdm
	```
 - [Mosquitto MQTT Broker](https://mosquitto.org/): open source message broker that implements the MQTT protocol versions 5.0, 3.1.1 and 3.1. 
	 ```bash
	 sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
	 sudo apt-get update
	 sudo apt-get install mosquitto
	 sudo apt-get install mosquitto-clients
	```
	After that, Mosquitto is installed as a service and should start automatically after install. To test if it is running, use commands `netstat -at` (you should see the Mosquitto broker running on port 1883) or `sudo service mosquitto status`.

## Usage
**MQTT_SlowDoS.py**
```bash
$ python3 MQTT_SlowDoS.py -a broker_address [-p broker_port] [-k keep_alive] [-h | --help]
```


**Arguments:**
| Flag           | Description    | 
| :------------- | :----------: | 
|  -h, --help    | Show help message  | 
| -a             | IP address of the MQTT broker (mandatory flag) | 
| -p             | Port of the MQTT broker (default: 1883) | 
| -k             | Keep-Alive parameter used in the MQTT protocol (default: 60 sec) | 

<br>

**MQTT_keepAlive.py**
```bash
$ python3 MQTT_keepAlive.py -a broker_address [-p broker_port] [-k keep_alive] [-h | --help]
```


**Arguments:**
| Flag           | Description    | 
| :------------- | :----------: | 
|  -h, --help    | Show help message  | 
| -a             | IP address of the MQTT broker (mandatory flag) | 
| -p             | Port of the MQTT broker (default: 1883) | 
| -k             | Keep-Alive parameter used in the MQTT protocol (default: 60 sec) | 

<br>

**client_pub.py**
```bash
$ python3 client_pub.py -a broker_address [-p broker_port] [-k keep_alive] [-h | --help]
```


**Arguments:**
| Flag           | Description    | 
| :------------- | :----------: | 
|  -h, --help    | Show help message  | 
| -a             | IP address of the MQTT broker (mandatory flag) | 
| -p             | Port of the MQTT broker (default: 1883) | 
| -k             | Keep-Alive parameter used in the MQTT protocol (default: 60 sec) | 

<br>

**client_sub.py**
```bash
$ python3 client_sub.py -a broker_address [-p broker_port] [-k keep_alive] [-h | --help]
```


**Arguments:**
| Flag           | Description    | 
| :------------- | :----------: | 
|  -h, --help    | Show help message  | 
| -a             | IP address of the MQTT broker (mandatory flag) | 
| -p             | Port of the MQTT broker (default: 1883) | 
| -k             | Keep-Alive parameter used in the MQTT protocol (default: 60 sec) | 


## Examples


**MQTT_SlowDoS.py**
```bash
$ python3 MQTT_SlowDoS.py -a localhost -p 1883 -k 60

Requesting connections ...

100% 1024/1024 [00:03<00:00, 279,39 it/s]

Requests sent !

[ Press any key to stop the attack ]

.
.
/* Section where the attack is running 
 * The MQTT broker will be unavailable 
 */
.
.

[ Attack terminated ]
```
<br>

**client_pub.py**
```bash
$ python3 client_pub.py -a localhost -p 1883 -k 60

Publisher creating new message. 

[ Client connected successfully ]

[ Message publication ... ]

.
.
/* Section where the attack is running 
 * The MQTT broker will be unavailable 
 */
.
.

[ Client disconnected successfully ]
```
<br>

**client_sub.py**
```bash
$ python3 client_sub.py -a localhost -p 1883 -k 60

Subscriber creating new topic and subscribes to it. 

[ Client connected successfully ]

[ Publication of TestTopic ]

[ Waiting for messages ... ]

Someone published: TestTopic 'Hello World'

.
.
/* Section where the attack is running 
 * The MQTT broker will be unavailable 
 */
.
.

[ Client disconnected successfully ]
```




## Authors

 - [Francesco Carli](https://github.com/fcarli3)
 - [Gianluca Boschi](https://github.com/gianluca2414)
 - [Paola Petri](https://github.com/paolapetri)
