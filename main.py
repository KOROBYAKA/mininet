from os import system
from sys import exit

from mininet.node import Host
from mininet.topo import Topo
from mininet.util import quietRun
from mininet.log import error
import sys
from functools import partial
from mininet.node import Controller
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.topo import SingleSwitchTopo
from mininet.log import setLogLevel


class MyTopo( Topo ):

    def build( self):
        s1 = self.addSwitch('s1')
        hB = self.addHost('hB')


        hA = self.addHost('hA')


        for x in range (0,4):
            self.addLink('hB', 's1')
        self.addLink('hA', 's1')

topos = { 'mytopo': ( lambda: MyTopo() ) }

def test():
    net = Mininet(topo=MyTopo(), waitConnected=True)
    net.start()




    hA = net['hA']
    hA.cmd(f'ip link add name br0 type bridge')
    for x in range (0,4):
        hA.cmd(f'sudo ip link add link hA-eth0 name hA-eth0.10{x} type vlan id 10{x}')
        hA.cmd(f'ip link set dev hA-eth0.10{x} up')
        hA.cmd(f'ip link set hA-eth0.10{x} master br0')
        ''' ping po IP rabotaet hA.cmd(f'ip address add dev hA-eth0.10{x} 10.0.0.2{x}')'''
    hA.cmd('ip address add dev br0 10.0.0.111/24')
    hA.cmd('ip address add dev hA-eth0 10.0.0.11/24')
    hA.cmd('ip link set br0 up')
    hA.cmd('ip link set hA-eth0 up')


    CLI(net)
    net.stop()
def main():

   

    test()




if __name__ == "__main__":
    main()
