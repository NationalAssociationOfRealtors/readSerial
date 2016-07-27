#!/usr/bin/env python

import sqlite3
import sys

#set location of sqlite db & table name
db = '/home/pi/serial_db.sqlite'
tn = 'SERIAL_DB'

conn = sqlite3.connect(db) #connect to db
c = conn.cursor()

# check which argument is passed and return data respectively
#st = sys.argv[1] # sensor type
#id = sys.argv[2] # sensor id
#c.execute("SELECT ({sv}) FROM {tn} WHERE {node_id}='{id}' AND {s_type}='{st}'".format(sv='sensor_value', s_type='sensor_type', st=st, tn=tn, node_id='node_id',id=id))
c.execute("SELECT DISTINCT node_id FROM {tn}".format(tn=tn))
#data = c.fetchone() #returns one matching row; fetchall() returns all matching rows
ids = c.fetchall()
#print (ids)
#print ("\n")
#print(ids[2][0])
#print (data[0])

d = {}
for i in ids:
    d[i[0]] = []
    c.execute("SELECT DISTINCT sensor_type FROM {tn} WHERE {nodeid} = {id}".format(nodeid='node_id',tn=tn, id=i[0]))
    types = c.fetchall()
    d[i[0]] = [v[0] for v in types if v[0] != '#']

#print d

#print("\n")

for i in ids:
    #print (i[0]) # node ID
    #print (d[i[0]]) # list for specific node ID
    #print (len(d[i[0]])) # length for list for a particular node ID
    for k in d[i[0]]:
        if k == '': continue
        print k # key in list in dictionary
