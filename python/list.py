#!/usr/bin/env python
#coding=utf-8

list1 = ['physics','chemistry',1997,2001]
list2 = [1, 2, 3, 4, 5, 6, 7]

print list1[2]
print list1[1:3]

print list1 + list2
list1[2] = 1998

print list1

print len(list1)
print ['H']*5
print 3 in list2

for x in list2:
	print "x: ", x,


print cmp(list1,list2)
print max(list2)

print list1.append('2003')
print list2.count('2')
print list1.extend(list2)

print list2.reverse()
