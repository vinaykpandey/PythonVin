import sys
import json

avl_parking_lot = [] # list of parking lot that is available
tkt_for_car = [] # this is list dict of all car parked ticket {"slot_no": slot_no, "plate_no": plate_no, "color": color}
total_number_of_parking = 0 # it will initially zero
query_key_dict = {"slot_numbers_": "slot_no", "slot_number_": "slot_no", "registration_numbers_": "plate_no", "_registration_number": "plate_no", "_cars_with_colour": "color"}

#
# def writeTktjson(data):
#     with open('car_tkt_data.json', 'w') as f:
#         json.dump(data, f)
#

def setMaxparkingLot(line_text):
    global total_number_of_parking
    list_p = line_text.split()
    total_number_of_parking = int(list_p[-1])
    # create entry in avl_parking_lot
    for i in range(1, total_number_of_parking+1):
        avl_parking_lot.append(i)
    print("Created a parking lot with", total_number_of_parking ,"slots")

def createTicketForParking(line_text):
    print(line_text)
    global avl_parking_lot
    print(avl_parking_lot)
    global tkt_for_car
    if len(tkt_for_car) >= total_number_of_parking:
        print("Sorry, parking lot is full")
        return False
    list_p = line_text.split()
    avl_parking_lot = sorted(avl_parking_lot, reverse=True) # sort this in DESC order
    # print(avl_parking_lot)
    slot_no = avl_parking_lot[-1] # take first available parking lost
    plate_no = list_p[1]
    color = list_p[2]
    parking_details = {"slot_no": slot_no, "plate_no": plate_no, "color": color}
    tkt_for_car.append(parking_details)
    print("Allocated slot number:", slot_no)
    #remove last element from (nearest parking lot)
    avl_parking_lot.pop()

def leaveParking(line_text):
    # print(line_text)
    # print("leaveParking")
    global avl_parking_lot
    global tkt_for_car
    list_p = line_text.split()
    slot_no = list_p[1]
    avl_parking_lot.append(slot_no) # slot_no is now available
    #remove car details from  tkt_for_car
    i = 0
    for chunk in tkt_for_car:
        # print(chunk)
        if int(chunk.get("slot_no", 0)) == int(slot_no):
            del tkt_for_car[i]
            print("Slot number ", slot_no, "is free")
            return True
        i = i+1

def queryProcessing(line_text):
    global tkt_for_car
    res_list = []
    # print(line_text)
    # line_text = line_text.strip()
    list_p = line_text.split("for")
    find = list_p[0]
    where_what = list_p[1]
    ww_list = where_what.split()
    # print("find : ", find)
    find = query_key_dict.get(find)
    # print("find : ", find)
    where = ww_list[0]
    what = ww_list[1]
    # print("where : ", where)
    where = query_key_dict.get(where)
    # print("where : ", where, "what : ", what)
    for chunk in tkt_for_car:
        # print(chunk.get(where))
        if chunk.get(where) == what.strip():
            value_find = chunk.get(find)
            res_list.append(value_find)
    if  res_list:
        print(res_list)
    else:
        print("Not found")

def lineTextProcessing(line_text):
    # print(line_text)
    if "Create_parking_lot" in line_text:
        setMaxparkingLot(line_text)
    elif "park" in line_text:
        createTicketForParking(line_text)
    elif "leave" in line_text:
        leaveParking(line_text)
    elif "for" in line_text:
        queryProcessing(line_text)

def processTxtFile():
    """
    @take txt file from CLI as args
    """
    arg_list = sys.argv
    if len(arg_list) != 2:
        print("input file path is missing")
        exit()

    file_name = arg_list[1]
    # print(file_name)
    with open(file_name) as fp:
        for cnt, line in enumerate(fp):
            # print("Line {}: {}".format(cnt, line))
            lineTextProcessing(line)

if __name__ == "__main__":
    processTxtFile()
    # print("total_number_of_parking : ", total_number_of_parking)
