from logic import *


def gather(URL):
    TLD = getTopLevelDomain(URL)
    ipAddress = getIPAdress(URL)
    portMap = getPortData(ipAddress, " ")
    robots = getRobot(URL)
    whois = get_whois(TLD)
