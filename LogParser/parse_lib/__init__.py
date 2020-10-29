import traceback
import re
import datetime


def file_log(string):
    try:
        # file_name = "failed_password.log"
        file_name = "reverse_mapping.log"
        f = open(file_name, "a")
        f.write(string)
        # f.write("\n")
        f.close()
        return True
    except:
        print(traceback.format_exc())
        return False


def extract_date(line_str):
    """
    :param line_str: str
    :return: str(yyyy-mm-dd)
    """

    try:
        md_hms = re.search(r"([a-zA-z]+\s+\d{1,2})+\s+(\d{2}:\d{2}:\d{2})", line_str)
        y_m_d = datetime.datetime.strptime(md_hms.group(), '%b %d %H:%M:%S').strftime('2019' + '-%m-%d')
        # print("date yyyy-mm-dd: ",y_m_d)
        return y_m_d
    except:
        print(traceback.format_exc())
        return False


def extract_ip(line_str):
    """

    :param line_str:
    :return:  str (IP address)
    """
    try:
        ip_data = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line_str)
        # print("ip_data: " , ip_data)
        ip_add = ip_data.group()
        # print("ip_add: " ,ip_add)
        return ip_add
    except:
        print(traceback.format_exc())
        return False


def extract_user_name(line_str):
    """

    :param line_str:
    :return: str (username)
    """
    # print(line_str)
    # convert string to list by delimeter password for
    try:
        list_data = line_str.split("Failed password")
        last_element = list_data[-1]
        last_element = last_element.strip()
        list_data = last_element.split("from")
        first_element = list_data[0]
        first_element = first_element.strip()
        list_data = first_element.split(" ")  # ['for', 'invalid', 'user', 'support']
        user_name = list_data[-1]  # username
        # print(user_name)
        return user_name
    except:
        print(traceback.format_exc())
        return False


def extract_name_reverse(line_str):
    """

    :param line_str:
    :return: str (username)
    """
    # print(line_str)
    # convert string to list by delimeter password for
    try:
        list_data = line_str.split("reverse mapping")
        # print(list_data)
        last_element = list_data[-1]
        last_element = last_element.strip()
        # print(last_element)
        list_data = last_element.split("[")
        first_element = list_data[0]
        first_element = first_element.strip()
        list_data = first_element.split(" ")  # ['for', 'invalid', 'user', 'support']
        user_name = list_data[-1]  # username
        # print(user_name)
        return user_name
    except:
        print(traceback.format_exc())
        return False
