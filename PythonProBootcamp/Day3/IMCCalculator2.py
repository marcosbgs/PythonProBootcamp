height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

imc = weight / height ** 2

if imc < 18.5:
    print("Your BMI is " + str(imc) + ", you are underweight.")
elif imc < 25:
    print("Your BMI is " + str(imc) + ", you have a normal weight.")
elif imc < 30:
    print("Your BMI is " + str(imc) + ", you are slightly overweight.")
elif imc < 35:
    print("Your BMI is " + str(imc) + ", you are obese.")
else:
    print("Your BMI is " + str(imc) + ", you are clinically obese.")






