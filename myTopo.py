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


def myTopo():

    net = Mininet(controller=RemoteController)
    c0 = net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)
    sw0 = net.addSwitch('sw0', ip=None, failMode='standalone')
    sw1 = net.addSwitch('sw1', ip=None, failMode='standalone')

    wap0 = net.addSwitch('wap0', ip=None, failMode='standalone')
    wap1 = net.addSwitch('wap1', ip=None, failMode='standalone')
    sta0 = net.addHost('sta0', ip="192.168.0.2")
    sta1 = net.addHost('sta1', ip="192.168.0.3")

    wifi = WIFISegment()
    wifi.addAp(wap0, channelNumber=2, ssid="myNetwork_0")
    wifi.addAp(wap1, channelNumber=10, ssid="myNetwork_1")

    wifi.addSta(sta0, channelNumber=2, ssid="myNetwork_0")
    wifi.addSta(sta1, channelNumber=10, ssid="myNetwork_1")

    net.addLink(c0, sw0)
    net.addLink(c0, sw1)

    net.addLink(sw0, wap0)
    net.addLink(sw1, wap1)

    net.start()
    mininet.ns3.start()
    CLI(net)

    mininet.ns3.stop()
    mininet.ns3.clear()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()