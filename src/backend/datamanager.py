from . pattern import *
import re, os, csv
from pathlib import Path

class DataManager:
    def __init__(self, data):
        self.__data = data

        self.__bussiness_city = ''
        self.__bussiness_country = ''
        self.__bussiness_description = ''
        self.__bussiness_name = ''
        self.__bussiness_street_address = ''
        self.__bussiness_zipcode = ''
        self.__customer_address_line1 = ''
        self.__customer_address_line2 = ''
        self.__customer_email = ''
        self.__customer_name = ''
        self.__customer_phone_number = ''
        self.__invoice_bill_details = []
        self.__invoice_description = ''
        self.__invoice_duedate = ''
        self.__invoice_issuedate = ''
        self.__invoice_number = ''
        self.__invoice_tax = ''

    
    def set_bussiness_details(self, **kwargs):
        details = self.__data[:kwargs.get('bill_to_idx')]
        invoice_idx = kwargs.get('invoice_no')
        address = ",".join(self.__data[1: invoice_idx]).split(",")
        address = [x.strip() for x in address if x]

        self.__bussiness_name = details[0]
        self.__bussiness_street_address = address[0]
        self.__bussiness_city = address[1]
        self.__bussiness_country = f'{address[2]}, {address[3]}'
        self.__bussiness_description = details[(details.index(self.__bussiness_name, 1) + 1)]
        self.__bussiness_zipcode = address[4]


    def set_customer_details_and_invoice_description(self, **kwargs):
        details = self.__data[kwargs.get('bill_to_idx'): kwargs.get('item_idx')]
        if "BILL TO" in details:
            details.remove("BILL TO")
        if "DETAILS" in details:
            details.remove("DETAILS")
        if "PAYMENT" in details:
            details.remove("PAYMENT")

        name = get_customer_details(details, detail='name')
        if name:
            self.__customer_name = name[1]
            details.pop(name[0])

        email = get_customer_details(details, detail='email')
        if email:
            self.__customer_email = email[1]
            details.pop(email[0])

        phone_number = get_customer_details(details, detail='number')
        if phone_number:
            self.__customer_phone_number = phone_number[1]
            details.pop(phone_number[0])

        address_line1 = get_customer_details(details, detail='line1')
        if address_line1:
            self.__customer_address_line1 = address_line1[1]
            details.pop(address_line1[0])


        address_line2 = get_customer_details(details, detail='line2')
        if address_line2:
            self.__customer_address_line2 = address_line2[1]
            details.pop(address_line2[0])

        self.__invoice_description = get_invoice_description(details)


    def set_invoice_bill_details(self, **kwargs):
        details = self.__data[kwargs.get('item_idx'): kwargs.get('subtotal_idx')]
        for i in range(4, len(details), 4):
            self.__invoice_bill_details.append((details[i], \
                                                details[i+1], \
                                                details[i+2]))
            
    
    def set_invoice_details(self, **kwargs):
        self.__invoice_duedate = self.__data[kwargs.get('due_date_idx')].split(" ")[-1]

        invoice_info = self.__data[kwargs.get('invoice_no_idx'): self.__data.index(self.__data[0], 1)]
        invoice_info = " ".join(invoice_info).split(" ")
        self.__invoice_number = invoice_info[1]
        self.__invoice_issuedate = invoice_info[-1]

        tax_info = self.__data[kwargs.get('subtotal_idx'):]
        tax_pattern = re.compile(r'^\d{2}$')
        for s in tax_info:
            if tax_pattern.match(s):
                match_obj = tax_pattern.match(s)
                if match_obj:                
                    self.__invoice_tax = match_obj.group()

    def __to_dict(self):
        arr_dict = []
        for s in self.__invoice_bill_details:
            _dict = { \
                "Bussiness_City": self.__bussiness_city, \
                "Bussiness_Country": self.__bussiness_country, \
                "Bussiness_Description": self.__bussiness_description, \
                "Bussiness_Name": self.__bussiness_name, \
                "Bussiness_Street Address": self.__bussiness_street_address, \
                "Bussiness_Zipcode": self.__bussiness_zipcode, \
                "Customer_Address_line1": self.__customer_address_line1, \
                "Customer_Address_line2": self.__customer_address_line2, \
                "Customer_Email": self.__customer_email, \
                "Customer_Name": self.__customer_name, \
                "Customer_Phone Number": self.__customer_phone_number, \
                "Invoice_Bill Details_Name": s[0], \
                "Invoice_Bill Details_Quantitynbsp;":s[1], \
                "Invoice_Bill Details_Rate": s[2], \
                "Invoice_Description": self.__invoice_description, \
                "Invoice_Due Date": self.__invoice_duedate, \
                "Invoice_Issue Date": self.__invoice_issuedate, \
                "Invoice_Number": self.__invoice_number, \
                "Invoice_Tax": self.__invoice_tax \
                }
            arr_dict.append(_dict)
        return arr_dict

    def save_to_csv_file(self, dest_file_path):
        arr_dict = self.__to_dict()

        if not os.path.exists('ExtractedData'):
            os.makedirs('ExtractedData')

        file_path = Path(dest_file_path)
        if  not os.path.exists(file_path):
            file_path.touch()
            with open(file_path, 'w', newline='') as fin:
                writer = csv.DictWriter(fin, fieldnames=arr_dict[0].keys())
                writer.writeheader()
            fin.close()

        with open(dest_file_path, 'a', newline='') as fin:
            writer = csv.DictWriter(fin, fieldnames=arr_dict[0].keys())
            writer.writerows(arr_dict)
        fin.close()
        

    def __str__(self):
        return f'"Bussiness_City": {self.__bussiness_city},\n"Bussiness_Country": {self.__bussiness_country},\n"Bussiness_Description": {self.__bussiness_description},\n"Bussiness_Name": {self.__bussiness_name},\n"Bussiness_Street Address": {self.__bussiness_street_address},\n"Bussiness_Zipcode: {self.__bussiness_zipcode},\n"Customer_Address_line1": {self.__customer_address_line1},\n"Customer_Address_line2": {self.__customer_address_line2},\n"Customer_Email": {self.__customer_email},\n"Customer_name": {self.__customer_name},\n"Customer_Phone Number": {self.__customer_phone_number},\n"Invoice_Description": {self.__invoice_description},\n"Invoice_Bill Details: {self.__invoice_bill_details},\n"Invoice_Due Datenbsp;": {self.__invoice_duedate},\n"Invoice_Issue Date": {self.__invoice_issuedate},\n"Invoice_Number": {self.__invoice_number},\n"Invoice_Tax": {self.__invoice_tax}'
