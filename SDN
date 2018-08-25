#EXER1

from pox.core import core
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.ipv4 import ipv4
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.arp import arp
from pox.lib.util import str_to_bool, dpid_to_str
from pox.lib.addresses import IPAddr, EthAddr
import random

def _handle_PacketIn (event):
     
     
     msg = of.ofp_packet_out()
     msg.data = event.ofp
     msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
     event.connection.send(msg)
     
     print "Novo PacketIN"
     porta = event.port
     pacote = event.parsed   
     
     #ethernet define mac de origem e de destino     
     mac_origem = pacote.src
     mac_destino = pacote.dst
     print("Mac Origem: %s Mac Destino: %s" % (mac_origem, mac_destino))
     
     #se e ipv4
     if pacote.type == ethernet.IP_TYPE:
      ip_origem = pacote.next.srcip
      ip_destino = pacote.next.dstip
      print("IP Origem: %s IP Destino: %s" % (ip_origem, ip_destino))
      tcp = pacote.find('tcp')
      if tcp:
           porta_origem = tcp.srcport
           porta_destino = tcp.dstport
           print("Porta Origem: %s Porta Destino: %s" % (porta_origem, porta_destino))
           
def launch (reactive = False):
     core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
     
