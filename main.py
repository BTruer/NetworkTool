from logic import gather

stringInput = raw_input("Enter a full URL then a comma then an option <file,print>(write to a file, or print to shell) Ex.https://www.yahoo.com, print\n")
#To do: parse the string and write to file function
#also pip frezze virtual env and requriements.txt
TLD, ipAddress, portMap, robots, whois = gather(url)

