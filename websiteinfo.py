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
# checking port open or close
a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

location = (website, 80)
result_of_check = a_socket.connect_ex(location)

if result_of_check == 0:
   print("Port is open")
else:
   print("Port is not open")
# website structure
print ("website requests :" ,res)
res = requests.get(url)

print(res.text)
print(res.status_code)
