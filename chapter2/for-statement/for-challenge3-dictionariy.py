from tokenize import String


phones = {'James': '023209323', 'jane': '928329382983'}

for item in phones.items():
    if item[0].lower() == 'james':
        print(item[1])