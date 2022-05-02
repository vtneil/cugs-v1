import paho.mqtt.client as mqttc
from lib.lib_log import Log

class MQTTClientHandler:
    def __init__(self, client_name: str, *, client_id: str = "") -> None:
        """
        An MQTT Client handler
        """
        self.logger = Log(target='LOG_MQTT')
        self.client_name = client_name
        self.client_id = client_id
        self.client = mqttc.Client(client_name)
        self.logger.info('MQTT Client initialized.')

    def connect(self, host_address: str, *, port=1883, keepalive=60, bind_address="") -> bool:
        self.client.connect(host_address, port, keepalive, bind_address)
        self.logger.info('Connected successfully!')
        return True

    def publish(self, topic: str, payload: str) -> bool:
        self.client.publish(topic, payload)
        self.logger.debug('Published successfully!')
        return True

    def subscribe(self, topic: str, qos=0):
        self.client.subscribe(topic, qos=qos)
        self.logger.debug('Subscribed successfully!')



class MQTTBrokerHandler:
    def __init__(self) -> None:
        """
        An MQTT Broker handler
        """