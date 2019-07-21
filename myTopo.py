"""
Russell Luther and Shane Brogan Basic Tree Topology
Contains:
Firewall (TBD?)
SDN OpenFlow Controller
Two Switches with a Wireless Access Point(WAP) and three Hosts directly connected per switch
Each WAP has three hosts connected via wifi

                                +-------+
                                |       |
                                |  WAN  |
                                |       |
                                +---+---+
+-----+                             |                              +-------+
|     |                             |                              |       |
|WAP0 |                             |                              |       |
+--+--+                             |                              |WAP1   |
   |                          +-----+------+                       +---+---+
   |       +-------+          |            |          +-------+        |
   |       |       |          |SDN OpenFlow|          |       |        |
   +-------+Switch0+----------+ Controller +----------+Switch1+--------+
           |       |          |            |          |       |
           +---+---+          |            |          +---+---+
               |              +------------+              |
               |                                          |
               +                                          +
      Host0, Host1, Host2                        Host3, Host4, Host5


"""

from mininet.net import Mininet
from mininet.node import Node, Switch, RemoteController
from mininet.link import Link, Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI

import mininet.ns3
from mininet.ns3 import WIFISegment

import ns.core
import ns.network
import ns.wifi
import ns.csma
import ns.wimax
import ns.uan
import ns.netanim

from mininet.opennet import *

def main():
    


if __name__ == '__main__':
    setLogLevel('info')
    main()
