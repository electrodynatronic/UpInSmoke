#!/usr/bin/env python

import random
num = random.randrange(150,350)		# This is our fake temperature measurement
					# We simply generate a random number in the
					# range 150 to 350
ff=open("temperaturedata.txt",'a') 	# Open a file in append mode

import datetime
timestamp = datetime.datetime.now()	# create a timestamp

ff.write(str(timestamp) + ", " + str(num) + "\n") # Turn everything into a string
			# and append it to the file with a newline.

ff.close()		# Close our file

