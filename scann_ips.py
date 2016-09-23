from socket import * 
import sys

remoteServer = '192.168.100.'
try:
    for ip in range(0,254):
        remoteServerIP = gethostbyname(remoteServer+str(ip))
        print('# Scanning ip {}'.format(remoteServerIP)) 
        portOpen = 0
        for portTCP in range(100):
            sockTCP = socket(AF_INET, SOCK_STREAM)
            sockTCP.settimeout(0.05)
            result = sockTCP.connect_ex((remoteServerIP, portTCP))
            if(result == 0) :
                portOpen = portOpen + 1
                if portOpen == 1:
                    print('## Host {} is alive'.format(remoteServerIP))
               
                print('{}.- Port {} open'.format(portOpen,portTCP))
                sockTCP.close()
        
        #else:
        #    print('* Host {} is dead'.format(remoteServerIP))
except KeyboardInterrupt:
        print "### You pressed Ctrl+C"
        sys.exit()

except Exception, e:
    print('## Error: {}'.format(e))
    sys.exit()