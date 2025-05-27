from pox.core import core
from pox.lib.util import dpid_to_str 
from pox.lib.revent import *

log = core.getLogger()

class PacketInSeen(Event):
    def __init__(self):
        Event.__init__(self)

class A (EventMixin):
    _eventMixin_events = set([PacketInSeen])
    def __init__(self):
        print("A started!")
        core.openflow.addListeners(self)
    def _handle_PacketIn(self,event):
        print("Packet In event!")
        core.A.raiseEvent(PacketInSeen())

def launch ( ):
      core.registerNew(A)
