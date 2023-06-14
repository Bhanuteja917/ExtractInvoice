import re

def get_customer_details(string, **kwargs):
    date = re.compile(r"(0\d|1\d|2\d|3[01])-(0\d|1[012])-[12]\d{3}$")
    due_date = re.compile(r"Due date: (0\d|1\d|2\d|3[01])-(0\d|1[012])-[12]\d{3}$")
    name = re.compile(r"(^[A-Z][a-z]* [A-Z][a-z]*)")
    email= re.compile(r"^.*@.*[.]com$")
    number= re.compile(r"\d{3}-\d{3}-\d{4}")
    line1 = re.compile(r"(\d{3,5} [A-Z][a-zA-Z]+ [A-Z][a-zA-z]+$)|(\d{3,5} [A-Z][a-zA-z]+$)")
    line2 = re.compile(r"(^[A-Z][a-zA-z].+[- ][A-Z][a-zA-z].+$)|(^[A-Z][a-zA-z].+$)")
    total = re.compile(r"(^\$\d+\.\d+$)|(^\$\d+)")

    detail = kwargs.get('detail')

    match detail:
        case 'date':
            pattern = date
        case 'name':
            pattern = name
        case 'email':
            pattern = email
        case 'number':
            pattern = number
        case 'line1':
            pattern = line1
        case 'line2':
            # print(string)
            pattern = line2
        case 'total':
            pattern = total
        case 'due_date':
            pattern = due_date

    if detail != 'line2':
        for (idx, s) in enumerate(string):
            if(pattern.match(s)):
                pattern_match_obj = pattern.match(s)
                return (idx, pattern_match_obj.group())
    elif detail == 'line2':
        matched_patterns = []
        for (idx, s) in enumerate(string):
            # print(s)
            if(pattern.search(s)):
                pattern_match_obj = pattern.search(s)
                matched_patterns.append((idx, pattern_match_obj.group()))
        print(matched_patterns)
        
        return matched_patterns[-1]
        
     

def get_invoice_description(string):
    date = get_customer_details(string, detail='due_date')
    string.pop(date[0])
    total = get_customer_details(string, detail='total')
    string.pop(total[0])
    
    return " ".join(string) if string else ''







# details = ['BILL TO', 'DETAILS', 'PAYMENT', 'Jill Schowalter', 'Lorem cupidatat ullamco', 'Due date: 09-07-2023', 'Jill.Schowalter@gmail.com', 'culpa occaecat aliqua velit', '222-254-5978', 'do consectetur esse tempor', '$18932.1', '68910 Ahmad Centers', 'deserunt sint incididunt eu ad', 'Vilaplana', 'ad']
# print(get_customer_details(details, detail='date'))
