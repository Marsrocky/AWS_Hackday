# -* coding=utf-8
import pygame,sys, os
from socket import *
import subprocess
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print '****************************'
print 'Monitoring...'
print('Waiting for connection...')
message = ''
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	print('Receive Message: %s' % message.decode('utf-8'))
	returnMessage = 'Success'
	serverSocket.sendto(returnMessage.encode('utf-8'), clientAddress)
	if message.decode('utf-8') != 'None':
		flag = 1
		f = open('emotion_record.txt', 'a')
		f.write('Mun Kit\n')
		f.write(message+'\n')
		f.write('%s\n' % time.ctime())

		time.sleep(4)
		if 'HAPPY' in message:
			os.system('say You look so happy')
			sentence = 'say Can you share your happy story'
			os.system(sentence)
			time.sleep(8)
			os.system('say Awesome story recorded')
		else:
			sentence = 'say Are you %s' % message
			os.system(sentence)
			time.sleep(2)
			os.system('say Do you wanna listen to some music')
			time.sleep(4)	# Sure
			os.system('afplay mash2012.mp3')
			# subprocess.Popen('afplay Chopin-waltz-in-a-minor.mp3', shell=True)
		print 'Writing to database success!'
		print '****************************'
		print 'Monitoring...'