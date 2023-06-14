import json
import os.path
from datamanager import DataManager

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def extract_info_from_json(data):

    data_json = data
    data_text = []
    (invoice_no_idx, email_idx, due_date_idx, bill_to_idx, item_idx, subtotal_idx) = (0, 0, 0, 0, 0, 0)
    
    # Get the Text Value of elements
    idx = 0
    for element in data_json["elements"]:
        try:
            text = element["Text"].strip()
            data_text.append(text)
            if '@' in text:
                email_idx = idx
            idx += 1
        except KeyError:
            pass
    
    # print(data_text)
    # Clean up email (In some files customer email is spanned over two elements)
    try:
        if data_text[email_idx + 1].endswith('m'):
            data_text[email_idx] += data_text[email_idx + 1]
            data_text.pop(email_idx + 1)
    except IndexError:
        print('Error occured while cleaning email')

    
    for (idx, text) in enumerate(data_text):
            if 'Invoice' in text:
                invoice_no_idx = idx
            elif '@' in text:
                email_idx = idx
            elif 'Due date' in text:
                due_date_idx = idx
            elif 'BILL TO' in text:
                bill_to_idx = idx
            elif 'ITEM' in text:
                item_idx = idx
            elif 'Subtotal' in text:
                subtotal_idx = idx
    
    # print((invoice_no_idx, email_idx, due_date_idx, bill_to_idx, item_idx, subtotal_idx))
    
    data_manager = DataManager(data_text)

    data_manager.set_bussiness_details(bill_to_idx=bill_to_idx)
    data_manager.set_customer_details_and_invoice_description(bill_to_idx=bill_to_idx, item_idx=item_idx)
    data_manager.set_invoice_bill_details(item_idx=item_idx, subtotal_idx=subtotal_idx)
    data_manager.set_invoice_details(invoice_no_idx=invoice_no_idx, due_date_idx=due_date_idx, subtotal_idx=subtotal_idx)

    # print(data_manager)   #invoice till bussiness name + 


if __name__ == '__main__':
    extract_info_from_json()