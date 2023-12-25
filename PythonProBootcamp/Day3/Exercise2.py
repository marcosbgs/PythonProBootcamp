print("Find out if a year is a leap or not a leap year.")
year = int(input("Write a year: "))

if year % 100 != 0 and year % 4 == 0:
    print(f"{year} is a leap year!")
elif year % 400 == 0:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is NOT a leap year!")


# print("Find out if a year is a leap or not a leap year.")
# year = int(input("Write a year: "))
#
# if year % 4 == 0:
#     print(f"{year} is a leap year!")
# elif year % 100 != 0 and year % 400 == 0:
#     print(f"{year} is a leap year!")
# else:
#     print(f"{year} is NOT a leap year!")