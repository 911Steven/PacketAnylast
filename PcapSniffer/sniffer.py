# -*- coding:utf-8 -*-

'''
网络流量过滤和获取
'''


# 全局配置ß
import sys
sys.path.append("..")


# 引入依赖的包
import pcap
from ProtocolAnylast.Ethernet.EthernetAnylast import EthernetPacket
from ProtocolAnylast.IPNetwork.IPAnylast import IPNetworkAnylast


# 定义嗅探器
class Sniffer(object):
    """定义抓包类"""
    def __init__(self,iftername):
        '''创建针对网卡的抓包嗅探器'''
        self.sniffer = pcap.pcap(name=iftername,immediate=True)


    def filter(self,filterString):
        '''设置过滤器'''
        self.sniffer.setfilter(filterString)

    def Anylast_Packet_Handler(self):
        for time,packet in self.sniffer:
            packet = EthernetPacket(packet)

            packet = IPNetworkAnylast(packet.getData())
            packet.getType()
            #pass

if __name__ == "__main__":
    sniffer = Sniffer("en4")
    sniffer.Anylast_Packet_Handler()
