# BMI stands for Body Mass Index
weight = 65
height = 1.85
# the output states the BMI and the weight situation.
BMI = weight / (height**2)
if BMI < 18.5:
    category = "underweight"
elif 18.5 <= BMI <= 30:
    category = "normal weight"
else:
    category = "obese" 
# organise the outcome as a complete sentence including the BMI and the weight situation.
print ("The person's BMI is",BMI,"and he is considered",category,".")