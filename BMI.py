# Get input from the user
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m, e.g., 1.75): "))

# Calculate BMI (Weight divided by height squared)
bmi = weight / (height ** 2)

# Display the BMI result rounded to 2 decimal places
print(f"\nYour BMI is: {bmi:.2f}")

# Classify the BMI status based on standard Asian criteria
if bmi < 18.5:
    print("Status: Underweight")
elif 18.5 <= bmi < 23.0:
    print("Status: Normal weight (Healthy)")
elif 23.0 <= bmi < 25.0:
    print("Status: Overweight")
elif 25.0 <= bmi < 30.0:
    print("Status: Obese (Class 1)")
else:
    print("Status: Severely Obese (Class 2)")
