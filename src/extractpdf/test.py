from zipfile import ZipFile
import os.path, json, re
from pattern import get_customer_details
from extract import extract_info_from_json

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

input_list = os.listdir(f'{base_path}/output_1')

# print(input_list)

for (idx, file_name) in enumerate(input_list):
    print(idx)
    data_json = dict()
    file_name = file_name.split('.')[0]
    with ZipFile(f'{base_path}/output_1/{file_name}.zip', 'r') as zip_file:
        data_json = zip_file.read('structuredData.json')
        extract_info_from_json(data_json, 'output.csv')
# data_json = {}

# for i in range(1, 100):
#     with ZipFile(f'{base_path}/output_1/output{i}.zip', 'r') as zip_file:
#         data_json = json.loads(zip_file.read('structuredData.json'))

#     data = []

#     for element in data_json['elements']:
#         try:
#             data.append(element['Text'].strip())
#         except KeyError:
#             pass

#     # print(data)
#     customer_data = data[data.index('BILL TO'): data.index('ITEM')]
#     # print(customer_data)
#     if 'BILL TO' in customer_data:
#         customer_data.remove('BILL TO')
#     if 'DETAILS' in customer_data:
#         customer_data.remove('DETAILS')
#     if 'PAYMENT' in customer_data:
#         customer_data.remove('PAYMENT')

#     customer_data = " ".join(customer_data)
#     customer_data = customer_data.split(" ")
#     customer_data.remove('Due')
#     customer_data.remove("date:")
    
#     customer_name = " ".join(customer_data[:2])

#     # print(i, " ".join(customer_data[:2]))
#     customer_data = customer_data[2:]
#     # print(customer_data)

    
#     email_idx = -1000
#     for (idx, s) in enumerate(customer_data):
#         if '@' in s:
#             email_idx = idx

#     email = customer_data[email_idx]

#     customer_email = complete_email(email)
#     _difference = customer_email[len(email):]
#     # customer_data = customer_data.remove(email)
#     customer_data.remove(email)

#     difference_idx = None
#     for (idx, s) in enumerate(customer_data):
#         if _difference == s:
#             difference_idx = idx

#     # print(_difference)
#     if difference_idx != None:
#         # print(difference_idx)
#         customer_data.pop(difference_idx)

#     (phone_num_idx, customer_number) = get_customer_details(customer_data, detail='number')
#     customer_data.pop(phone_num_idx)

#     (date_idx, due_date) = get_customer_details(customer_data, detail='date')
#     customer_data.pop(date_idx)

    


#     line1 = []
#     for (idx, s) in enumerate(customer_data):
#         num_pattern = re.compile(r'\d{3,5}')

#         if num_pattern.match(s):
#             line1.append((idx, customer_data[idx]))
#             break
        
#     for (idx, s) in enumerate(customer_data):
#         sentence_case = re.compile(r'[A-Z][A-Za-z\']+')

#         if s != 'Lorem' and sentence_case.match(s):
#             line1.append((idx, customer_data[idx]))

#     customer_line1 = f'{line1[0][1]} {line1[1][1]} {line1[2][1]}'

#     customer_line2 = ''
#     if len(line1) == 4:
#         customer_line2 = line1[3][1]
#     elif len(line1) == 5:
#         customer_line2 = f'{line1[3][1]} {line1[4][1]}'
    
#     for (idx, s) in line1:
#         customer_data.remove(s)
#     desc = ''
#     print(' '.join(customer_data))
#     print('\n')
    





# # Customer Name ---- Done
# # 77 
# # Customer Email ----- Done
# # 
 