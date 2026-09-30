def phone_number(phone):
    return "****" + phone[-4:]

phone=input("Enter your phone number: ")
print("Masked Phone Number:", phone_number(phone))