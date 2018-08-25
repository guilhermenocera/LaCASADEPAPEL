
from pox.core import core
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.ipv4 import ipv4
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.arp import arp
from pox.lib.util import str_to_bool, dpid_to_str
from pox.lib.addresses import IPAddr, EthAddr
import random

def _handle_PacketIn (event):

    msg = of.ofp_flow_mod()
    #aqui
    
    #acoes
    msg.actions.append(of.ofp_action_output(port = of.OFPP_ALL))    
    event.connection.send(msg)
    
    print "Novo PacketIN"
    porta = event.port
    pacote = event.parsed   

   
def launch (reactive = False):
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
