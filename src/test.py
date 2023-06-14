import json, traceback, sys
import os.path
from zipfile import ZipFile
from extract import extract_info_from_json

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_list = os.listdir(base_path + '/output')
print(len(file_list))
# print(file_list)

error = 0
for zip_file_name in file_list:
    try:
        with ZipFile(f'{base_path}/output/{zip_file_name}', 'r') as zip_file:
            data_json = json.loads(zip_file.read('structuredData.json'))
            extract_info_from_json(data_json)
            # print(data_json)
    except IndexError as err:
        print(f'{zip_file_name}: Unexpected {err=}, {type(err)=}')
        error += 1
        # for element in data_json["elements"]:
        #     try:
        #         text = element["Text"].strip()
        #         print(text, end=" ")
        #     except KeyError:
        #         pass
        traceback.print_exc(file=sys.stdout)
        print('\n\n')
    except TypeError as err:
        pass
    except ValueError as err:
        pass

print(error)

# print('\uFFFD')