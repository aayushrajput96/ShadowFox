total_jumping_jacks = 100

while total_jumping_jacks > 0:
    print(f"You have {total_jumping_jacks} jumping jacks remaining.")
    set_size = min(total_jumping_jacks, 10)  # Perform at most 10 jumping jacks in each set
    print(f"Perform {set_size} jumping jacks.")
    tired = input("Are you tired? (yes/no): ").lower()

    if tired in ["yes", "y"]:
        skip_remaining_sets = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip_remaining_sets in ["yes", "y"]:
            print(f"You completed a total of {100 - total_jumping_jacks} jumping jacks.")
            break
    total_jumping_jacks -= set_size

# If all jumping jacks are completed
if total_jumping_jacks == 0:
    print("Congratulations! You completed the workout.")
