from pox.core import core
from pox.lib.util import dpid_to_str 
log = core.getLogger()

class B (object):   
    def __init__(self):
        print("B started!")
        core.A.addListeners(self)
    def _handle_PacketInSeen(self, event):
        print("A has seen an OFP packetIn")

def launch ():
      core.registerNew(B)
      


