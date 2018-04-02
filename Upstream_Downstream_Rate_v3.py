import time
import os
log_file = 'net_data.log'
md_file = 'net_data.md'
#head = '|test from|hosted by|download|upload|round trip|packet loss|\n'
#limiter = '|----|----|----|----|----|----|\n'


class Funs():
	def __init__(self):
		self.asc_start_time = 'Sun Apr 1 10:10:00 2018'
		self.asc_end_time = 'Sun Apr 1 11:40:00 2018'
		#self.log_file = './rate.log'
		self.timestamp_start = time.mktime(time.strptime(self.asc_start_time))
		self.timestamp_end = time.mktime(time.strptime(self.asc_end_time))
		self.interval = 60*2
		self.ping_command = 'ping -c 10 www.baidu.com'

	def run(self, target_file):
		if target_file in os.listdir():
			print("**********   updating   **********")
			os.remove(target_file)
		self.log_data(target_file)

	def log_data(self, target_file):
		time_order = self.timestamp_start
		self.write_head(target_file)
		while True:
			now = time.time()
			if now > time_order and now < self.timestamp_end:
				time_order += self.interval
				self.write_data(target_file)
			if now > self.timestamp_end:
				break

	def write_head(self, target_file):
		print("********** writing head **********")
		head = '|test from|hosted by|download|upload|round trip|packet loss|\n'
		limiter = '|----|----|----|----|----|----|\n'
		with open(target_file, 'a+') as f:
			f.write(head)
			f.write(limiter)

	def write_data(self, target_file):
		print("********** writing data **********")
		content = self.data()
		with open(target_file, 'a+') as f:
			f.write(content)

	def data(self):
		merged = '|'
		thdu = self.tf_hb_dn_up()
		rp = self.rt_pl()
		for e in thdu:
			merged += e + '|'
		for e in rp:
			merged += e + '|'
		#print(merged)
		return merged+'\n'

	def rt_pl(self):
		rtn = [p for p in os.popen(self.ping_command)]
		rtn = rtn[-2:]
		pl = rtn[0].split(' ')[6]
		rt = rtn[1].split('/')[4]
		return [rt, pl]

	def tf_hb_dn_up(self):
		rtn = [p for p in os.popen('speedtest')]
		tf = rtn[1].split('(')[1].split(')')[0]
		hb = rtn[4].split('[')[1].split(']')[0]
		dn = rtn[6].split(':')[1][1:-1]
		up = rtn[8].split(':')[1][1:-1]
		return [tf, hb, dn, up]



if __name__ == "__main__":
	f = Funs()
	f.run(md_file)
