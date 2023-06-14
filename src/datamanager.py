from pattern import *
import re


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
        # print(details)
        details.remove("BILL TO")
        details.remove("DETAILS")
        details.remove("PAYMENT")

        name = get_customer_details(details, detail='name')
        self.__customer_name = name[1]
        details.pop(name[0])

        email = get_customer_details(details, detail='email')
        # print(email)
        self.__customer_email = email[1]
        details.pop(email[0])

        phone_number = get_customer_details(details, detail='number')
        self.__customer_phone_number = phone_number[1]
        details.pop(phone_number[0])

        address_line1 = get_customer_details(details, detail='line1')
        self.__customer_address_line1 = address_line1[1]
        details.pop(address_line1[0])


        address_line2 = get_customer_details(details, detail='line2')
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
                self.__invoice_tax = tax_pattern.match(s).group()


    def __str__(self):
        return f'"Bussiness_City": {self.__bussiness_city},\n"Bussiness_Country": {self.__bussiness_country},\n"Bussiness_Description": {self.__bussiness_description},\n"Bussiness_Name": {self.__bussiness_name},\n"Bussiness_Street Address": {self.__bussiness_street_address},\n"Bussiness_Zipcode: {self.__bussiness_zipcode},\n"Customer_Address_line1": {self.__customer_address_line1},\n"Customer_Address_line2": {self.__customer_address_line2},\n"Customer_Email": {self.__customer_email},\n"Customer_name": {self.__customer_name},\n"Customer_Phone Number": {self.__customer_phone_number},\n"Invoice_Description": {self.__invoice_description},\n"Invoice_Bill Details: {self.__invoice_bill_details},\n"Invoice_Due Datenbsp;": {self.__invoice_duedate},\n"Invoice_Issue Date": {self.__invoice_issuedate},\n"Invoice_Number": {self.__invoice_number},\n"Invoice_Tax": {self.__invoice_tax}'
