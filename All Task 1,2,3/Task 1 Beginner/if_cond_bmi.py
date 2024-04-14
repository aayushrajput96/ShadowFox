# Function to calculate BMI category
def calculate_bmi_category(weight, height):
    bmi = weight / (height ** 2)
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

# Ask user for input
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI category
bmi_category = calculate_bmi_category(weight, height)

# Print the result
print("BMI Category:", bmi_category)
