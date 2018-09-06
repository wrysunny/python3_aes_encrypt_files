#! -*- coding:utf-8 -*-
'''
AES encoding files
fu ck u d
'''
import os
import sys
import random
import string
import base64
from Crypto.Cipher import AES
from binascii import a2b_hex,b2a_hex


aes_key = ''.join(random.sample(string.ascii_letters + string.digits,32)).encode('utf-8')
aes_iv = ''.join(random.sample(string.ascii_letters + string.digits,16)).encode('utf-8')
print('aes key:',str(aes_key))
print('aes iv:',str(aes_iv))


def aeswork(workpath):
	cryptor = AES.new(aes_key,AES.MODE_CBC,aes_iv)
	with open(workpath,'rb') as fw:
		aes_files = fw.read()
	aes_files = b2a_hex(aes_files)
	length = 16 - (len(aes_files) % 16)
	aes_files += bytes([length])*length
	aes_enfiles = base64.b64encode(cryptor.encrypt(aes_files))
	with open(workpath + '.bak','wb') as fe:
		fe.write(aes_enfiles)
	os.remove(workpath)
	os.rename(workpath + '.bak', workpath)


if len(sys.argv) < 2:
	print('please input work path')
	os._exit(0)
else:
	workdir = sys.argv[1]

#workdir = '/media/wrysunny/5AD70001D6FFDAE9/TL-WR740N_V8_130417/'
for dirpath,dirnames,filenames in os.walk(workdir):
	for f in filenames:
		workpath = os.path.join(dirpath,f)
		print('workpath:',workpath)
		aeswork(workpath)

print('work dir :' + workdir)
with open(workdir + '/aesencrypt','w') as fq:
	fq.write('aes key:'+str(aes_key.decode('utf8'))+"\n"+'aes iv:'+str(aes_iv.decode('utf8')))
