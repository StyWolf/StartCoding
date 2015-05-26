#!/usr/bin/env python
#coding=utf8

import re 
import datetime

filename = 'output_1981.10.21.txt'
time = re.search('\d{4}.\d{2}.\d{2}',filename)
timedate = re.sub('[^0-9]',',',time.group(0))
date = re.split(',',timedate)
print date


get_weekday = get_time.weekday() + 1

print get_weekday




