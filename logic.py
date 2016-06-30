import os
import urllib.request
import io
from tld import get_tld
from socket import gethostbyname


def getTopLevelDomain(URL):
    return get_tld(URL)

def getIPAdress(URL):
     return gethostbyname(URL)

def getPortData(IP,option):
    bashCommand = "nmap " + option + " " + IP
    process = os.popen(bashCommand)
    results = str(process.read())
    return results

def getRobot(URL):
    if URL.endswith('/'):
        path = URL
    else:
        path = URL + "/"
    request = urllib.request.urlopen(path + "robot.txt", data=NONE)
    data = io.TextIOWrapper(request, encoding='UTF-8')
    return data.read()

def getDomainNameInfo(TLD):
    bashCommand = "whois " + TLD
    process = os.popen(bashCommand)
    results = str(process.read())
    return results

def gather(URL):
    TLD = getTopLevelDomain(URL)
    ipAddress = getIPAdress(URL)
    portMap = getPortData(ipAddress, " ")
    robots = getRobot(URL)
    whois = getDomainNameInfo(TLD)