# Name: Mohan Dixit
# Date: March 21st
# Purpose: A BMI Calculator

def main():

    # Get their weight and height in pounds and inches

    height = int(input("Enter your height in inches: "))
    weight = int(input("Enter your weight in pounds: "))


    # Convert it into kg and m
    height_in_m = height*0.0254
    weight_in_kg = weight/2.20462

    # Find their BMI

    BMI = weight_in_kg/(height_in_m)**2



    # Check which range their BMI falls under and print the according message

    if BMI < 18.5:
        print("According to the BMI classficiation, your BMI of "
              + format(BMI,'.2f') +  " means you are underweight.",
              "Your risk of developing problems is relatively high.",
              "So, you should add some weight to your build.")
    elif BMI < 25.0:
        print("According to the BMI classficiation, your BMI of "
              + format(BMI,'.2f') +  " means you are normal weight.",
              "Your risk of developing problems is relatively low.",
              "So, you have nothing to worry about.")
    elif BMI < 30:
        print("According to the BMI classficiation, your BMI of "
              + format(BMI,'.2f') +  " means you are overweight.",
              "Your risk of developing problems is very high.",
              "So, you should lose some weight to lower your BMI.")

    else:
        print("According to the BMI classficiation, your BMI of "
              + format(BMI,'.2f') +  " means you are morbidly obese.",
              "Your risk of developing problems is extremely high.",
              "So, you should quickly lose some weight to lower your BMI.")

main()
