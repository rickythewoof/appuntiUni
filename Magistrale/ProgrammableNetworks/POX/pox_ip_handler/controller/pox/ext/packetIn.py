from pox.core import core
from pox.lib.util import dpid_to_str


class PacketListener (object):   
    def __init__ (self):
        core.openflow.addListeners(self)   
    def _handle_ConnectionUp (self, event):
        print(f"Switch {dpid_to_str(event.dpid)} has come up.") 
    
    def _handle_PacketIn(self, event):
        packet = event.parsed
        if packet.type == packet.IP_TYPE:
            ip = packet.find('ipv4')
            if ip is not None:
                print("source IP:\t", ip.srcip)
                print("destination IP:\t", ip.dstip)
        else:
            print(f"Packet is of another type other than IP, discarding ...")

def launch():    
      core.registerNew(PacketListener)
