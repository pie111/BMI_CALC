from pywebio.input import *
from pywebio.output import *

def bmi_calc():
    height = input("Please enter your Height in cm :",type=FLOAT)
    weight = input("Please enter your weight in kg :",type=FLOAT)

    bmi = weight/(height/100)**2

    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    
    for tuple1,tuple2 in bmi_output:
        if bmi <=  tuple1 :
            put_text("Your bmi is",bmi,",You are",tuple2)
            break

if __name__ == "__main__":
    bmi_calc()
