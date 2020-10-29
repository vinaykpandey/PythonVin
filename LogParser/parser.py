import json
import sys
from os import path
import traceback
# parse log file
import parse_lib


def json_out_process(date_dict, date_ymd, user_name, ip):
    """
    :param date_dict:
    :param date_ymd:
    :param user_name:
    :param ip:
    :return:  date_dict (modified version)
    """
    if date_ymd in date_dict and user_name in date_dict[date_ymd]:
        item_count = date_dict[date_ymd][user_name]["total"]
        date_dict[date_ymd][user_name]["total"] = 1 + item_count
        if ip in date_dict[date_ymd][user_name]["iplist"]:
            ip_count = date_dict[date_ymd][user_name]["iplist"][ip]
            date_dict[date_ymd][user_name]["iplist"][ip] = 1 + ip_count
        else:
            date_dict[date_ymd][user_name]["iplist"][ip] = 1

    # print(date_dict)

    elif date_ymd in date_dict and user_name not in date_dict[date_ymd]:
        date_dict[date_ymd][user_name] = {}
        date_dict[date_ymd][user_name]["total"] = 1
        date_dict[date_ymd][user_name]["iplist"] = {ip: 1}
    # print(date_dict)

    elif date_ymd not in date_dict:
        date_dict[date_ymd] = {user_name: {}}
        date_dict[date_ymd][user_name]["total"] = 1
        date_dict[date_ymd][user_name]["iplist"] = {ip: 1}

    return date_dict


# print(date_dict)


def password_failed_process(file_name, date_val):
    """

    :param file_name:
    :param date_val:
    :return: dict
    """
    forgot_password_dict = {}
    try:
        with open(file_name) as f:
            i = 0
            for line in f:
                i = i + 1
                # print(line)
                if "Failed password" in line or "Failed password".lower() in line:
                    date_ymd = parse_lib.extract_date(line)
                    if not date_ymd:
                        continue
                    ip = parse_lib.extract_ip(line)
                    if not ip:
                        continue
                    user_name = parse_lib.extract_user_name(line)
                    if not user_name:
                        continue
                    if date_val:
                        if date_val != date_ymd:
                            continue

                    forgot_password_dict = json_out_process(forgot_password_dict, date_ymd, user_name, ip)
            return forgot_password_dict
    except:
        print(traceback.format_exc())
        return {}




def reverse_mapping_process(file_name, date_val):
    """
    :param file_name:
    :param date_val:
    :return: dict
    """
    reverse_mapping_dict = {}
    try:
        with open(file_name) as f:
            i = 0
            for line in f:
                i = i + 1
                if ("Reverse mapping" in line) or ("reverse mapping".lower() in line):
                    date_ymd = parse_lib.extract_date(line)
                    if not date_ymd:
                        continue
                    ip = parse_lib.extract_ip(line)
                    if not ip:
                        continue
                    r_m_name = parse_lib.extract_name_reverse(line)
                    if not r_m_name:
                        continue
                    if date_val:
                        if date_val != date_ymd:
                            continue
                    reverse_mapping_dict = json_out_process(reverse_mapping_dict, date_ymd, r_m_name, ip)
            return reverse_mapping_dict
    except:
        print(traceback.format_exc())
        return {}


if __name__ == "__main__":
    print(sys.argv)
    date_val = ""
    arg_len = len(sys.argv)
    if arg_len < 3:
        print("some argument is missing")
        exit()
    file_param = sys.argv[1]
    if file_param != "-file":
        print("file argument is missing")
        exit()
    file_name = sys.argv[2]
    is_file = path.exists(file_name)
    if not is_file:
        print("log file does not exist")
        exit()

    if arg_len == 5:
        date_param = sys.argv[3]
        if date_param != "--date":
            print("date argument is missing")
            exit()
        date_val = sys.argv[4]

    forgot_password_dict = password_failed_process(file_name, date_val)
    print("failed password attempts")
    print(json.dumps(forgot_password_dict))
    print("reverse mapping attempts")
    reverse_mapping_dict = reverse_mapping_process(file_name, date_val)
    print(json.dumps(reverse_mapping_dict))