#!/usr/bin/env python
#coding=utf8

import os
import glob
path = '/home/zhangjian/Coding/python'

print os.path.basename(path)
dir =  os.path.dirname(path)
print dir

info = os.path.split(path)
print info

path2 = os.path.join('/','home','zhangjian','Coding','test1')

print path2

print os.path.join(dir,'test2')


