import time
import os
log_file = './net_data.log'


class funs():
	def __init__(self):
		self.asc_start_time = 'Sun Apr 1 11:06:50 2018'
		self.asc_end_time = 'Sun Apr 1 11:07:50 2018'
		#self.log_file = './rate.log'
		self.timestamp_start = time.mktime(time.strptime(self.asc_start_time))
		self.timestamp_end = time.mktime(time.strptime(self.asc_end_time))
		self.interval = 60
		self.ping_command = 'ping -c 100 www.baidu.com'

	def log_data(self, file):
		time_order = self.timestamp_start
		while True:
			now = time.time()
			if now > time_order and now < self.timestamp_end:
				time_order += self.interval
				self.logging(file)
			if now > self.timestamp_end:
				break
	def logging(self, file):
		print("******* logging data ... ******")
		rtn = [p for p in os.popen('speedtest')]
		rtn = [time.asctime()+'\n', rtn[1], rtn[6], rtn[8]]
		with open(file, 'a+') as f:
			for r in rtn:
				f.write(r)

if __name__ == "__main__":
	fs = funs()
	if log_file in os.listdir():
		os.remove(log_file)
	fs.log_data(log_file)
