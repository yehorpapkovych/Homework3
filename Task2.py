phone_number = '0123450780'
if len(phone_number) == 10 and phone_number.isdigit():
    print('Your phone number is saved')
elif len(phone_number) != 10 and phone_number.isdigit():
    print('The number of digits is not right. Please, enter your phone number correctly.')
elif len(phone_number) == 10 and phone_number.isdigit() is False:
    print('Please, enter only digits!')
else:
    print('Please, enter your phone number according to the format')