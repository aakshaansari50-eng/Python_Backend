# recursion using fibo series with user input
# fibo series is a series of numbers where each number is the sum of the previous two
# the first two numbers are 0 and 1

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibo(i))

# constructor ka use karke fibo series
# class Fibo:
#     def __init__(self, n):
#         self.n = n
#         self.fibo = [0, 1]

#     def fibo_series(self):
#         if self.n == 0:
#             return 0
#         elif self.n == 1:
#             return 1
#         else:
#             self.fibo.append(self.fibo[self.n-1] + self.fibo[self.n-2])
#             return self.fibo[self.n]

# f = Fibo(n)
# print(f.fibo_series())


