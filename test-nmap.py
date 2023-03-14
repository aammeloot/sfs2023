import nmap

nm = nmap.PortScanner()

nm.scan('172.16.45.6', '20-443')
port_list = nm['172.16.45.6']['tcp'].keys()

print("Port list: ", port_list)
for port in port_list:
    print("Port: ", port)
    print("State: ", nm['172.16.45.6']['tcp'][port]['state'])
    print("Name: ", nm['172.16.45.6']['tcp'][port]['name'])



                    
                        