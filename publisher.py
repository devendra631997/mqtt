import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags,rc):
	f=open("/proc/loadavg","r")
	contents=f.read()
	print("Connected with result code")
	client.publish("om",contents)

client = mqtt.Client()
client.on_connect = on_connect
#client.will_set("client/dead","",0,retain=True)

client.will_set("client/dead","client_disconnected",0,retain=False)

client.connect("192.168.75.228", 1883, 60)

client.loop_forever()
