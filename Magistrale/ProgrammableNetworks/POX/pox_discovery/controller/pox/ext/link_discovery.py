import pox.openflow.libopenflow_01 as of
from pox.core import core
from pox.lib.recoco import Timer
from pox.lib.addresses import EthAddr
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.arp import arp
from pox.lib.util import dpidToStr

class Link():

	def __init__(self, sid1, sid2, dpid1, port1, dpid2, port2):
		self.name = str(sid1) + "_" + str(sid2)
		self.sid1 = sid1
		self.sid2 = sid2
		self.dpid1 = dpidToStr(dpid1)
		self.dpid2 = dpidToStr(dpid2)
		self.port1 = int(port1)
		self.port2 = int(port2)

class linkDiscovery():

	def __init__(self):
		self.switches = {} # <key: dpid; value: list of switch's ports>
		self.links = [] # list of link objects
		self.switch_id = {} # <key: a progressive ID; value: the dpid of the switch>
		self.id = 1 # use this to assign progressive IDs to connecting switches
		# add the current object to the openflow listeners
		core.openflow.addListeners(self)  
		Timer(5, self.sendProbes, recurring=True) # every 5 seconds executes the sendProbe method

	def _handle_ConnectionUp(self, event):
		print(f"Switch {dpidToStr(event.dpid)} has come up.") 
		
		self.switches[event.dpid] = event.ofp.ports
		self.switch_id[self.id] = event.dpid
		
		# update the defined dictionaries
		# run the install_flow_rule method 

		self.install_flow_rule(event.dpid)
		
		self.id += 1

	def _handle_PacketIn(self, event):
		eth_frame = event.parse # extract the ethernet frame from the incoming packet in
		if eth_frame.src == EthAddr("00:11:22:33:44:55"): # is this a discovery message?
			
			mac_str = eth_frame.dst.toStr().split(':')

			# parse the packet to extract the relevant information
			# sid1 and sid2 should contain the switch ID of the switches connected by the discovered link
			# dpid1 and dpid2 should contain the dpid of the switches connected by the discovered link
			sid1 = mac_str[4]
			dpid1 = self.switch_id[sid1]
			port1 = mac_str[5]
			dpid2 = event.dpid
			sid2 = False
			for sid in self.switch_id:
				if self.switch_id[sid] == dpid2:
					sid2 = sid
					break
			
			port2 = event.ofp.in_port

			link = Link(sid1, sid2, dpid1, port1, dpid2, port2)
			if link.name not in self.links:
				self.links[link.name] = link
				print("discovered new link: " + link.name)
				print(link.__dict__)

	def sendProbes(self):
		for sid in self.switch_id:
			dpid = self.switch_id[sid]
			for port in self.switches: # iterate over all the ports of the current switch
				if port != of.OFPP_CONTROLLER:
					mac_src = EthAddr("00:11:22:33:44:55") # set the mac address so that it allows to distinguish that the frame carries a discovery message
					mac_dst = EthAddr("00:00:00:00:{s:x}:{p:x}".format(s = sid, p = port)) # encode in the mac_dst the relevant information
					ether = ethernet() # create the message to inject in the data plane
					msg = of.ofp_packet_out()
					msg.data = ether.pack()
					msg.actions.append(of.ofp_action_output(port = 65534)) # instruct the switch to send the packet out of the current inspected port
					# send the packet_out message to the switch
					core.openflow.sendToDPID(dpid, msg)

	def install_flow_rule(self, dpid):
		msg = of.ofp_flow_mod()
		msg.priority = 50000
		match = of.ofp_match(dl_src = EthAddr("00:11:22:33:44:55"))
		msg.match = match
		msg.actions = [of.ofp_action_output(port = of.OFPP_CONTROLLER)]
		core.openflow.sendToDPID(dpid, msg)

def launch():
	core.registerNew(linkDiscovery)
