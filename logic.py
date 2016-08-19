import os
import urllib
import io
from tld import get_tld
from socket import gethostbyname


def getTopLevelDomain(URL):
    return get_tld(URL)

def getIPAdress(TLD):
     return gethostbyname(TLD)

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
    request = urllib.urlopen(path + "robot.txt", data=None,proxies=None,context=None)
    data = io.TextIOWrapper(request,encoding="utf-8",errors=None,newline=None,line_buffering=False)
    return request.read()

def getDomainNameInfo(TLD):
    bashCommand = "whois " + TLD
    process = os.popen(bashCommand)
    results = str(process.read())
    return results

def gather(URL):
    if "http://www." or "https://www." not in URL:
        print "ERROR Requires full URL! Ex. https://www.yahoo.com"
        return
    TLD = getTopLevelDomain(URL)
    ipAddress = getIPAdress(TLD)
    portMap = getPortData(ipAddress, "-F")
    robots = getRobot(URL)
    whois = getDomainNameInfo(TLD)
    stringis = [TLD,ipAddress,portMap,robots,whois]
    return stringis


print getRobot("https://www.yahoo.com")