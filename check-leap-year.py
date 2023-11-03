#kiarie zawadi muthoni
#sct211-0462/2022

year = int(input("Enter a year: "))

def check_leap_year(year):
  if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")

check_leap_year(year)