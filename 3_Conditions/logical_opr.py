# and
# or
# not

high_income = False
good_credit = True
student = False

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")

message = "Eligible" if (
    high_income or good_credit) and not student else "Not Eligible"
print(message)
