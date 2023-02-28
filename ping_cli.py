import os

# Ping using command-line proxy
address = input("Enter the IP address or hostname you want to ping")
command = "ping -c 4 " + address

result = os.system(command)

if result == 0:
    print("Ping successful!")
else:
    print("Ping failed!")
    