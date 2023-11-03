#kiarie zawadi muthoni
#sct211-0462/2022

user_weight = float(input("Enter your weight in kg: "))
user_height = float(input("Enter your height in metres: "))

def calculate_bmi(user_weight, user_height):
  user_bmi = user_weight / (user_height * user_height)
  if user_bmi >= 18.5 and user_bmi <= 24.9:
    print("You have normal weight")
  elif user_bmi < 18.5:
    print("You are underweight")
  elif user_bmi > 24.9:
    print("You are overweight")

calculate_bmi(user_weight, user_height)
