#16.   Find all the digits in a given string
text = "My phone number is 9876 and my pin is 1234!"
digits = [i for i in text if i.isdigit()]

print(digits)