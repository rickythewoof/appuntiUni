import pox.openflow.libopenflow_01 as of
from pox.core import core
from pox.lib.recoco import Timer
from pox.lib.util import dpidToStr

class trafficMeter():

	def __init__(self, ip_src, ip_dst, time_period, dpid):
		self.src = ip_src
		self.dst = ip_dst
		self.traffic = 0
		self.time_period = time_period
		self.dpid = dpid
		self.connection = None
		core.openflow.addListeners(self)

	def _handle_ConnectionUp (self, event):
		if dpidToStr(event.dpid) == self.dpid:
			self.connection = event.connection
			self.launch_component()

	def launch_component(self):
		Timer(self.time_period, self.send_stat_req, recurring=True)

	def _handle_FlowStatsReceived(self, event):
		rec_bytes = 0
		for f in event.stats:
			if f.match.nw_src == self.src and f.match.nw_dst == self.dst:
				rec_bytes += f.byte_count
		rate = (rec_bytes - self.traffic) / self.time_period
		self.traffic = rec_bytes
		print("IP flow rate: " + str(rate))

	def send_stat_req(self):
		self.connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))

def launch(ip_src = "10.0.0.1", ip_dst = "10.0.0.2", time_period = 2, dpid = "7a-c4-ae-1c-40-46"):
	trafficMeter(ip_src, ip_dst, time_period, dpid)
