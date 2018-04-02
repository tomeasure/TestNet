import time, os

class TestNet():
	'''
		该类用于测试网络的上下行带宽、时延以及丢包率
		调用外部命令ping向www.baidu.com，每次发100个包，每隔5分钟ping一次
		调用外部命令speedtest，每隔5分钟测一次
		使用时先创建实例，将目标文件名称作为参数，执行run即可
		最终的结果会保存在net_data.md中
	'''
	def __init__(self):
		self.asc_start_time, self.asc_end_time = self.start_end()
		#self.log_file = './rate.log'
		self.timestamp_start = time.mktime(time.strptime(self.asc_start_time))
		self.timestamp_end = time.mktime(time.strptime(self.asc_end_time))
		self.interval = 60*5
		self.ping_command = 'ping -c 100 www.baidu.com'

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
		head = '|test time|test from|hosted from|download|upload|round trip|packet loss|\n'
		limiter = '|----|----|----|----|----|----|----|\n'
		with open(target_file, 'a+') as f:
			f.write(head)
			f.write(limiter)

	def write_data(self, target_file):
		try:
			print("********** writing data **********")
			content = self.data()
			with open(target_file, 'a+') as f:
				f.write(content)
		except:
			pass

	def data(self):
		t = time.localtime()
		tm = str(t.tm_year)+'.'+str(t.tm_mon)+'.'+str(t.tm_mday)+' '+str(t.tm_hour)+':'+str(t.tm_min)+':00'
		merged = '|'+tm+'|'
		thdu = self.tf_hb_dn_up()
		rp = self.rt_pl()
		for e in thdu:
			merged += e + '|'
		for e in rp:
			merged += e + '|'
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
	def start_end(self):
		with open('./tools/start_end.conf', 'r') as fin:
			tm = fin.read()
		tm = tm.split('\n')
		return tm[0], tm[1]
