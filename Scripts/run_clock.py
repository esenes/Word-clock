import board
import neopixel
import time 
import datetime

ledNum = 142

strip = neopixel.NeoPixel(board.D18, ledNum)

color_set = (255, 255, 255)

def turn_on(idx, color=color_set):
	'''
	Usage: single LED, enter an int. 
	Alternatively enter a range [start, end]
	'''
	if type(idx) == int:
		strip[idx] = color
	elif type(idx) == list:
		for k in range(idx[0], idx[1]):
			strip[k] = color_set

def shoot():
	for i in range(ledNum):
		strip[i] = (255, 255, 255)
		time.sleep(0.01)
		strip[i] = (0, 0, 0)

def all_down():
	for i in range(ledNum):
		strip[i] = (0, 0, 0)

def parse_hour(h):
	if ((h==0) or (h==12)) or h==24:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([78,84])
	elif h == 1 or h == 13:
		turn_on(10)
		turn_on([15,19])
	elif h == 2 or h == 14:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([20,23])
	elif h == 3 or h == 15:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([25,28])
	elif h == 4 or h == 16:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([29,36])
	elif h == 5 or h == 17:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([37,43])
	elif h == 6 or h == 18:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([74,77])
	elif h == 7 or h == 19:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([55,60])
	elif h == 8 or h == 20:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([44, 48])
	elif h == 9 or h == 21:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([61,65])
	elif h == 10 or h == 22:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([49,54])
	elif h == 11 or h == 23:
		turn_on([5,9])
		turn_on([2,4])
		turn_on([66,72])

def parse_min(m):
	if m < 5:
		pass
	elif m < 10:
		turn_on(85)
		turn_on([96,102])
	elif m < 15:
		turn_on(85)
		turn_on([123,128])
	elif m < 20:
		turn_on(85)
		turn_on([92,94])
		turn_on([131,137])
	elif m < 25:
		turn_on(85)
		turn_on([108,113])
	elif m < 30:
		turn_on(85)
		turn_on([108,119])
	elif m < 35:
		turn_on(85)
		turn_on([137,142])
	elif m < 40:
		turn_on(85)
		turn_on([96,108])
	elif m < 45:
		turn_on([87,91])
		turn_on([108,113])
	elif m < 50:
		turn_on([87,91])
		turn_on([92,94])
		turn_on([131,137])
	elif m < 55:
		turn_on([87,91])
		turn_on([123,128])
	elif m < 60:
		turn_on([87,91])
		turn_on([96,102])

def parse_time(hh, mm):
	'''
	This basically fixes the +1h when minutes >35
	'''
	parse_min(mm)
	if mm < 40 :
		parse_hour(hh)
	elif mm >= 40:
		parse_hour(hh+1)

# init
all_down()
shoot()
all_down()

last_now = datetime.datetime.now()
print(last_now)

parse_time(last_now.hour, last_now.minute)

# here we go
while True:
	now = datetime.datetime.now()
	if now.minute is not last_now.minute:
		if now.minute%5 == 0:
			print(f'Last refresh at {now}')
			all_down()
			parse_time(now.hour, now.minute)
	last_now = now

	time.sleep(5)
