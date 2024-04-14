import random

# Initialize variables to count statistics
num_6 = 0
num_1 = 0
num_two_6s_in_row = 0
prev_roll = None

# Simulate rolling the die at least 20 times
for _ in range(20):
    roll = random.randint(1, 6)  # Simulate rolling a six-sided die
    print("Roll:", roll)

    # Count statistics
    if roll == 6:
        num_6 += 1
        if prev_roll == 6:
            num_two_6s_in_row += 1
    elif roll == 1:
        num_1 += 1

    prev_roll = roll  # Update previous roll for checking consecutive 6s

# Print statistics
print("Number of times you rolled a 6:", num_6)
print("Number of times you rolled a 1:", num_1)
print("Number of times you rolled two 6s in a row:", num_two_6s_in_row)
