class InvalidCouponCodeError(Exception):
    pass

def apply_coupon(code):
    valid_codes = ["ZOMATO10", "SAVE20"]

    if code not in valid_codes:
        raise InvalidCouponCodeError("Invalid coupon code!")
    else:
        print("Coupon applied successfully!")

try:
    apply_coupon(input("Enter coupon code: "))
except InvalidCouponCodeError as e:
    print(e)