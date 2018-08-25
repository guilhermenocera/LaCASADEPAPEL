
from pox.core import core
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.ipv4 import ipv4
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.arp import arp
from pox.lib.util import str_to_bool, dpid_to_str
from pox.lib.addresses import IPAddr, EthAddr
import random

def _handle_PacketIn (event):
 
    #recebi o pacote
    pacote = event.parsed
    porta = event.port
    print "Novo PacketIN"
    msg = of.ofp_packet_out()
    msg.data = event.ofp
       
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)    
    
    #codigo para definir o fluxo
    msg = of.ofp_flow_mod()
    #campos
    mac_origem = pacote.src
    msg.match.dl_src = EthAddr(mac_origem)
    #acoes para enviar pacote
    msg.actions.append(of.ofp_action_output(port = porta))    
    event.connection.send(msg)    
   
def launch (reactive = False):
 core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
