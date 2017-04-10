import os
import time
import json
from socket import *

serverName = '192.168.0.208'
serverPort = 12000
socketAddress = (serverName, serverPort)

def emotion_read(jsond):
	data = json.loads(jsond)
	fflag = 0
	emotion = 'None'
	if len(data['FaceDetails'])>0:
		fflag = 1
		emotion_list = data['FaceDetails'][0]['Emotions']
		conf_list = [type['Confidence'] for type in emotion_list]
		max_conf = max(conf_list)
		max_index = conf_list.index(max_conf)
		emotion = str(emotion_list[max_index]['Type'])
	return(fflag, emotion)

def udpsend(text):
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.sendto(text.encode('utf-8'), socketAddress)
	returnMessage, serverAddrss = clientSocket.recvfrom(2048)
	if not returnMessage:
		return 'No return message'
	print "The return message is: %s" % returnMessage.decode('utf-8')

def call_api():
	os.system('fswebcam -r 1280x720 --jpeg 100 -S 13 - | aws s3 cp - s3://cam-snap2/test.jpg')
	r=os.popen('aws rekognition detect-faces \
			   --image \'{"S3Object":{"Bucket":"cam-snap2","Name":"test.jpg"}}\' \
				  --region us-west-2 \
					 --attributes "ALL"')
	udata=r.readlines()
	print '###################################'
	temp="".join(udata)
	e=emotion_read(temp)
	
	udpsend(e[1])

def main():
	while True:
		call_api()
		time.sleep(30)

if __name__ == '__main__':
	main()


