# -*- coding:utf-8 -*-

'''
网络层包解析
'''

import dpkt
import socket


#定义包解析类
class IPNetworkAnylast(object):
    '''数据报文网络层分解'''
    def __init__(self,packet):
        '''初始化网络层数据'''
        self.packet = packet

    def getSrc(self):
        '''返回源IP地址'''
        return socket.inet_ntoa(self.packet.src)

    def getDst(self):
        '''返回目的IP地址'''
        return socket.inet_ntoa(self.packet.dst)

    def getType(self):
        help(self.packet)
