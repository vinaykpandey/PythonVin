# input_data = {"Dravid": "Cricket", "Messi": "Football", "Sachin": "Cricket", "Ronaldo": "Football"}
# output_data = {}
# for k, v in input_data.items():
#     if v in output_data:
#         output_data[v].append(k)
#     else:
#         output_data.update({v: [k]})
#
# print(output_data)


s = "devendraKumarPandeySiyapokhar"

s_new = ""
for element in s:
    if element.isupper() is False:
        s_new += element
    else:
        s_new = s_new + " " + element

print(s_new.title())