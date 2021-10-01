# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

sample_insurance_cost = calculate_insurance_cost("Sample", 62, 0, 23.2, 2, 1)

#Add bmi calculator. Convert height in in to cm & weight in lbs to kg. 
#Calculate the BMI and round
#bmi= round(weight/((height/100)*(height/100)), 1)
#be sure to add ht & wt as parameters and take out bmi. Create local variable "bmi" for use in function. 
