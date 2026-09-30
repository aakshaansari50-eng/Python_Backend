durations = input("Enter song durations in minutes: ")

durations = list(map(int, durations.split()))

seconds = list(map(lambda x: x * 60, durations))

print("Durations in seconds:", seconds)