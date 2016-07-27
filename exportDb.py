#!/usr/bin/env python

import csv
import sqlite3
from glob import glob
from os.path import expanduser
import sys

#set location of sqlite db & table name
db = '/home/pi/serial_db.sqlite'
tn = 'SERIAL_DB'
id = sys.argv[1]

conn = sqlite3.connect(
    glob(expanduser(db))[0]
)

c = conn.cursor()
c.execute("SELECT * FROM {tn} WHERE {node_id} = '{id}' ".format(tn=tn, node_id='node_id', id=id))

with open("/home/pi/.homeassistant/www/exportdata.csv", "wb") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in c.description]) # write headers
    csv_writer.writerows(c)
