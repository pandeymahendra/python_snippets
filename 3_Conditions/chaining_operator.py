# age should be between 18 and 65
age = 25
if 18 <= age < 65:
    # if age >= 18 and age < 65:
    print("Eligible")

#########
a = 10
b = 20
c = 5
# c < a < b is same as c <a and a < b
print(c < a)
print(a < b)
print(c < a < b)
# b is not in between 40 and 60
print(40 <= b <= 60)
# a is 10, which is greater than c
print(a == 10 > c)

#######
u = 5
v = 10
w = 15
x = 0
y = 7
z = 15
# The w is same as z but not same as v, v is greater than x, which is less than y
print(z is w is not v > x < y)
# Check whether w and z are same and x < z > y or not
print(x < w == z > y)
