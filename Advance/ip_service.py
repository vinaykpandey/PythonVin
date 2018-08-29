#!/usr/bin/python
import logging  # this will be used for log file

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

        App_Services_List = [app_services_1, app_services_2, app_services_3, app_services_4, app_services_5, app_services_6]
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
