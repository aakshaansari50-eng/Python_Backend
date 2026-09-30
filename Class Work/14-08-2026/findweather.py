celcius=float(input("Enter the temperature in Celsius: "))
if celcius>50:
    print("Invalid Temperature")
elif celcius>40 and celcius<=50:
    print("It is too hot outside.")
elif celcius>30 and celcius<=40:
    print("It is normally.")
elif celcius>20 and celcius<=30:
    print("It is a cold day.")
elif celcius>10 and celcius<=20:
    print("It is a too cold.")
else:
    print("Freeze.")