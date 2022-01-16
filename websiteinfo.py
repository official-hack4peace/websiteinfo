
import socket
import requests
website = input("Enter website : ")
url = input("Enter url : ")
ip = socket.gethostbyname(website)
host = socket.gethostname()
print ("host: ", host)
print ("Website :" ,website)
print ("Website :" ,ip)
# security check
info = input("Chose which http you written in url (i) https or (ii) http: ")
if info==("https"): 
	print("Secure!") 
else: 
	print("Not Secure!")
# service name by port number

def printServiceOnPort(portNumber, protocol):

    serviceName = socket.getservbyport(portNumber, protocol);

    print("service running at port number %d : %s"%(portNumber, serviceName));

   


printServiceOnPort(80,  "tcp");

printServiceOnPort(443, "tcp");

# checking port open or close
a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

location = (website, 80)
result_of_check = a_socket.connect_ex(location)

if result_of_check == 0:
   print("Port is open")
else:
   print("Port is not open")
# website structure
page = requests.get(url)

print(page.text)
