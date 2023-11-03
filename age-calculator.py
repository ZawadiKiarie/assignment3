#kiarie zawadi muthoni
#sct211-0462/2022

birthyear = int(input("Enter your year of birth: "))
birthmonth = int(input("Enter your month of birth(1-12): "))
birthday = int(input("Enter your day of birth(1-31): "))

def calculate_age(birthyear, birthmonth, birthday):
  currentyear = 2023
  currentmonth = 11
  currentday = 29

  age_in_years = currentyear - birthyear
  age_in_months = currentmonth - birthmonth
  age_in_days = currentday - birthday

  print(f"You age is {age_in_years} years, {age_in_months} months, and {age_in_days} days")

calculate_age(birthyear, birthmonth, birthday)