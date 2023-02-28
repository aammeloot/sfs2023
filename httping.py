# Another version of Ping, but this time
# We use it to see if a --website-- is up
# And we can collect HTTP error messages (404, 503 etc)
import socket

import urllib.error
import urllib.request
import urllib.response

# Set up low level networking timeout
socket.setdefaulttimeout(20)

# Ask for web address
url = input("Enter a *web* address to check its status")

# The URL request can potentially crash the program
# if there's no response from the website.
# So we use 'try' to handle potential errors
# (Exception handling)
try:
    response = urllib.request.urlopen(url)
except urllib.error.URLError as e:
    print("Error connecting to the server: ", e.reason)
except urllib.error.HTTPError as e:
    print("Error on the server side: ", e.code)
else:
    print(url, " has been reached.")


