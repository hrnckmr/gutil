#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Call "service = gutil.service()" and
#get Resource in module googleapiclient.discovery object

#UNDER CONSTRUCTION!

import sys
argument = sys.argv
for i,x in enumerate(argument):
    print("received argument", i, x)

print("***SEARCH FOR*** ", argument[1])

#service
import gutil
service = gutil.service()
q_name="name="+"'"+argument[1]+"'"
print(q_name)
print("sample:","name='colab_temp'")

id1=gutil.gquery(service,q_name)
print("query result:",id1)
print("./"+argument[2],id1[0][2])

cmd="./"+argument[2],id1[0][2]
gutil.gupload(service,cmd[0],cmd[1])

