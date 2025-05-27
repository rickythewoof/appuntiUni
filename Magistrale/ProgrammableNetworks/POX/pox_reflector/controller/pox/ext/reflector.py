from pox.core import core
from pox.lib.util import dpid_to_str
import pox.lib.packet as pkt
import pox.openflow.libopenflow_01 as of 

class Reflector (object):   
    def __init__ (self):
        core.openflow.addListeners(self)   
    def _handle_ConnectionUp (self, event):
        print(f"Switch {dpid_to_str(event.dpid)} has come up.") 
    
    def _handle_PacketIn(self, event):
        packet = event.parsed
        msg = of.ofp_packet_out()
        msg.data = pkt.ethernet()
        # Here we create the messagge
        msg.dst = packet.src
        msg.src = packet.dst
        msg.payload = packet.payload
        msg.actions.append(of.ofp_action_output(port = event.port))
        connection = event.connection
        connection.send(msg)
        print("Reflected the packet successfullye")

def launch():    
      core.registerNew(Reflector)
