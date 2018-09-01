#! -*- coding:utf-8 -*-
'''
AES encoding files 
fu ck u d 
'''
import os
import random
import string
import base64
from Crypto.Cipher import AES
from binascii import a2b_hex,b2a_hex


aes_key = ''.join(random.sample(string.ascii_letters + string.digits,16)).encode('utf-8')
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


workdir = '/home/pi/python/test/'
for dirpath,dirnames,filenames in os.walk(workdir):
	for f in filenames:
		workpath = os.path.join(dirpath,f)
		print('workpath:',workpath)
		aeswork(workpath)
		
#aes加密文件.bak
#删除原文件 os.remove(file)
# 加密文件修改为原名称os.rename
#os.rename(src, dst)
#参数
#src -- 要修改的目录名
#dst -- 修改后的目录名
# 删除两边空字符 strip()
# 删除右边空字符 lstrip()
# 切片处理s[:4]


