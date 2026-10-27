class PaymentFailedError(Exception):
    pass

def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError("Payment failed!")
    else:
        print("Payment Successful")

try:
    amount = float(input("Enter amount: "))
    process_payment(amount)
except PaymentFailedError as e:
    print(e)