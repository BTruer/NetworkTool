import os
from tld import get_tld
from socket import gethostbyname as get_ip_address﻿


def getTopLevelDomain(URL):
    return get_tld(URL)

def getIPAdress(TLD):
     return gethostbyname(TLD)

def getPortData(IP,option):
    bashCommand = "nmap " + option + " " + IP
