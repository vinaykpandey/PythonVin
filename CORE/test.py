listA = [
    {
        "inboundNumber": "112233",
        "inboundNumberType": 1,
        "countryId": 2,
        "channel_type": [
            1,
            2
        ]
    },
    {
        "inboundNumber": "17203157982",
        "inboundNumberType": 2,
        "countryId": 1,
        "channel_type": [
            1
        ]
    },
    {
        "inboundNumber": "447860017073",
        "inboundNumberType": 3,
        "countryId": 2,
        "channel_type": [
            3
        ]
    },
    {
        "inboundNumber": "447860017097",
        "inboundNumberType": 1,
        "countryId": 2,
        "channel_type": [
            1
        ]
    },
    {
        "inboundNumber": "447937947405",
        "inboundNumberType": 1,
        "countryId": 2,
        "channel_type": [
            1
        ]
    },
    {
        "inboundNumber": "529993191671",
        "inboundNumberType": 2,
        "countryId": 3,
        "channel_type": [
            1
        ]
    }
]

output_dict = {}
for data in listA:
    inbound_number_type = data["inboundNumberType"]
    country_id = data["countryId"]
    inbound_number = data["inboundNumber"]
    if output_dict.get(inbound_number_type,""):
        if output_dict[inbound_number_type].get(country_id, ""):
            inbound_number_list = output_dict[inbound_number_type][country_id]
            inbound_number_list.append(inbound_number)
            output_dict[inbound_number_type][country_id] = inbound_number_list
            output_dict[inbound_number_type][country_id] = output_dict[inbound_number_type][country_id].append(inbound_number)
        else:
            output_dict[inbound_number_type][country_id] = [inbound_number]
    else:
        output_dict[inbound_number_type] ={country_id: [inbound_number] }

print(output_dict)


