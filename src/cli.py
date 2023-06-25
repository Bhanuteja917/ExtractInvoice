import os
import argparse
from pathlib import Path
from extractpdf.utils import get_time_stamp
import shutil

from extractpdf.apiclient import ApiClient
from extractpdf.extract import extract_info_from_json


base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists(f'{base_path}\\ExtractedData'):
    os.mkdir(f'{base_path}\\ExtractedData')
if not os.path.exists(f'{base_path}\\output'):
    os.mkdir(f'{base_path}\\output')


ts = str(get_time_stamp())
default_output = Path(f'{base_path}\\ExtractedData\\ExtractedData({ts}).csv')
default_api_key = Path(f'{base_path}\\pdfservices-api-credentials.json')


parser = argparse.ArgumentParser(
    prog='extractpdf',
    description='Extracts data from PDF files using Adobe API and save it in CSV format.',
    allow_abbrev=False)

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-i', '--input-file', action='store', nargs='+')
group.add_argument('-d', '--input-directory', action='store')
parser.add_argument('-o', '--output-file', action='store', default=default_output)
parser.add_argument('-k', '--api-key', action='store', default=default_api_key)

args = parser.parse_args()

input = list()
if args.input_file:
    input = [os.path.abspath(file) for file in args.input_file]
elif args.input_directory:
    input = [f'{os.path.abspath(args.input_directory)}\\{file}' for file in os.listdir(os.path.abspath(args.input_directory))]

input = list(filter(lambda f: '.pdf' in f, input))
output = os.path.abspath(args.output_file)

api_client = ApiClient(args.api_key)

for file in input:
    data_json = api_client.extract_info_from_pdf(file)
    extract_info_from_json(data_json, output)

shutil.rmtree(f'{base_path}/output')

print(f'Data extracted to {args.output_file}')
