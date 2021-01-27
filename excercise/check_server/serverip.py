#!/usr/bin/python
import logging  # this will be used for log file
import os  # this will be used for run linux process (Linux Command)
def running_service(server_type):
    '''
    :param server_type:
    :return: this will return services running on app_server web_server
    '''
    servertype = server_type.lower()
    if servertype == 'app':
        #app_services_1  is list,  which storre all the services for app server 1

        app_services_1 = ['sudo kservice kyv-admin status', 'sudo service kyv-api status',
                        'sudo ervice activemq status', 'sudo yum list installed kyv*', 'sudo yum list installed markit*']
        app_services_2 = app_services_1 # services of app server 1 & app server 2 are same

        # app_services_3  is list,  which storre all the services for app server 3
        app_services_3 = ['sudo service kyv-buyer status', 'sudo yum list installed kyv*', 'sudo yum list installed markit*']
        app_services_4 = app_services_3 # services of app server 3 & app server 4 are same

        # app_services_5  is list,  which storre all the services for app server 5
        app_services_5 = ['sudo service kyv-vendor status', 'sudo yum list installed kyv*', 'sudo yum list installed markit*']
        app_services_6 = app_services_5 # services of app server 5 & app server 6 are same

        App_Services_List = [app_services_1, app_services_2, app_services_3, app_services_4, app_services_5,  app_services_6]
        return App_Services_List

    elif servertype == 'web':
        #app_services_1  is list,  which storre all the services for app server 1

        web_services_1 = ['service httpd status']
        web_services_2 = web_services_1 # services of web server 1 & web server 2 are same
        Web_Services_List = [web_services_1, web_services_2]
        return Web_Services_List

def services_ip(env_name):
    '''
    :param env_name:
    :return: This will check the ENV and return the ip's of app server and web server
    '''
    envname = env_name.lower()
    if envname == 'dev':
        list_app_ip = ['10.120.0.139', '10.120.0.140', '10.120.0.141', '10.120.0.142', '10.120.0.143', '10.120.0.144']
        lip_web_ip = ['10.120.0.75', '10.120.0.76']
        server_details = {'app_server': list_app_ip, 'web_server': lip_web_ip}
        return server_details
    elif envname == 'demo':
        list_app_ip = ['10.120.129.139', '10.120.129.140', '10.120.129.141', '10.120.129.142', '10.120.129.143',
                       '10.120.129.144']
        lip_web_ip = ['10.120.128.77', '10.120.128.78']
        server_details = {'app_server': list_app_ip, 'web_server': lip_web_ip}
        return server_details

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
    ListAppServices.append(App_Services[int(server_input)-1]) # get the ip of app array by index of list-1,  because list start with 0

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
        print(ip, 'check service run linux command, ', ServicetoCheck)
    #innerloop closed
    loopCount = loopCount + 1   # outer loop
    #print('ip{loopC}'.format(loopC=loopCount), ip)
    # we check service for app server