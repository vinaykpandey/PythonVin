#!/usr/bin/python
# this will be used for log file
import logging

# this will be used for run linux process (Linux Command)
import os

from ip_service import *


# code run start from here
env = str(input("Enter ENV: ")) # python version  >=3  we used:  input()
print(env)
serverDetails = services_ip(env)
AppServerIP = serverDetails['app_server'] #App server Details
#print(AppServerIP)  # type => list  (indexed array)

WebServerIP = serverDetails['web_server'] #Web server Details
#print(WebServerIP) # type => list  (indexed array)

App_Services = running_service('app')  # Services on App Server
Web_Services = running_service('web') # Services on Web Server

server_input = str(input("Enter Server No b/w 1-6 for which you want to see the result or enter All for result of all servers: \n "))
# Enter 1-6 or all for app server services
print(server_input)
#print(type(server_input))
#rint(App_Services)
server_input = server_input.lower()
#find list of apis by choice enter by user
ListAppServerIP = []
if server_input == 'all':
    ListAppServerIP = AppServerIP
else:
    ListAppServerIP.append(AppServerIP[int(server_input)-1]) # get the ip of app array by index of list+1,  because list start with 0

#print(ListAppServerIP)


ListAppServices = []
if server_input == 'all':
    ListAppServices = App_Services
else:
    ListAppServices.append(App_Services[int(server_input)-1]) # get the service of AppServices array by index of list-1,  because list start with 0

#print(ListAppServices)

'''
Traversed the app ips to check the services on server
'''
loopCount = 0  # this is loop count
for ip in ListAppServerIP:
    ListServicesApp = ListAppServices[loopCount]
    #print(ip)
    #print(ListServicesApp)
    # traversed services for the given ips
    for ServicetoCheck in ListServicesApp:
        #print(ip, 'check service run linux command, ', ServicetoCheck)
        command = "ssh -t deploy@"+ip + " " + ServicetoCheck
        print(command)
        output = os.system(command)
        print(output)

    #innerloop closed
    loopCount = loopCount + 1   # outer loop
    #print('ip{loopC}'.format(loopC=loopCount), ip)
    # we check service for app server