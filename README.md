# readSerial

This is a Python script that reads all incoming data on the serial port on Raspberry Pi and writes to an SQLite database. The SQLite table is created if it doesn’t exist.

This script is created to read data from an RFM69 Gateway that’s connected to a Raspberry Pi via USB. The gateway receives data wirelessly from sensor nodes, each identified by their node IDs. All incoming data is expected to be terminated by line break (\n or println in Arduino) and in the following format:

<i>i:1,t:25.44,h:40.23,l:34.00</i> (example)

The letters indicate sensor type, and the numbers indicate sensor value. In the above example, i is node ID, t is temperature, h is relative humidity and l is light intensity. The script splits each data set by commas and makes a dictionary of the data split by colons. The actual sensor type, sensor value or number of sensor types is not relevant, as the script splits any incoming data, as long as it is formatted correctly. A full list of all sensor types is in the file _dictionary.py_

The SQLite database is overwritten each time new data comes in from the same node. The Node ID and the sensor type are set as primary keys in the database. This database is meant to act as a temporary place for all incoming data which can then be requested by any backend service.

All incoming data is then published to Home Assistant via RESTful API. When a new node is detected in the network, the configuration files are automatically updated and Home Assistant is rebooted to register the node into the network. Sensor data for each node is updated each time the gateway receives incoming data.

This python script should run on boot as a cron job. Open cron in terminal by typing `crontab -e` and paste the following at the end of the file: 

`@reboot /usr/bin/python /home/pi/readSerial.py &`


