import time
import os
import threading

class funs():
	def __init__(self):
		self.asc_start_time = 'Fri Mar 30 13:50:00 2018'
		self.asc_end_time = 'Fri Mar 30 14:50:00 2018'
		self.log_file = './rate.log'
		self.timestamp_start = time.mktime(time.strptime(self.asc_start_time))
		self.timestamp_end = time.mktime(time.strptime(self.asc_end_time))
		self.interval = 60*5
		self.time_to_run = True
		self.time_to_end = False
		#self.lock = threading.Lock()

	def run1(self):
		while True:
			if time.time() > self.timestamp_start:
				while True:
					if self.time_to_run:
						self.time_to_run = False
						self.data_to_log()
						if time.time() > self.timestamp_end:
							break
			if time.time() > self.timestamp_end:
				self.time_to_end = True
				break

	def run2(self):
		while not self.time_to_end:
			print("******* waitting ... ******")
			time.sleep(self.interval)
			self.time_to_run = True

	def data_to_log(self):
		print("******* logging data ... ******")
		pip = os.popen('speedtest')
		rtn = []
		for e in pip:
			rtn.append(e)
		rtn = [time.asctime()+'\n', rtn[1], rtn[6], rtn[8]]
		with open(fs.log_file, 'a+') as f:
			for r in rtn:
				f.write(r)

if __name__ == "__main__":
	fs = funs()
	if fs.log_file in os.listdir():
		os.remove(fs.log_file)
	# pip = os.popen('speedtest')
	rtn = [e for e in os.popen('speedtest')]
	if len(rtn) < 9:
		install_speedtest = [e for e in os.popen('speedtest')]	
	ts = [threading.Thread(target=fs.run1), threading.Thread(target=fs.run2)]
	for t in ts:
		t.start()
