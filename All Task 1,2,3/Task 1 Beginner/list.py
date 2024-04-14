# Initial Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# Calculate the number of members in the Justice League
num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

# Batman recruited Batgirl and Nightwing as new members
justice_league.extend(["Batgirl", "Nightwing"])
print("Batman recruited Batgirl and Nightwing:", justice_league)

# Wonder Woman is now the leader of the Justice League
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman is now the leader:", justice_league)

# Move either "Green Lantern" or "Superman" between Aquaman and Flash
justice_league.insert(justice_league.index("Aquaman") + 1, "Superman")
print("Superman moved between Aquaman and Flash:", justice_league)

# Replace the existing list with a new team assembled by Superman
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Superman assembled a new team:", justice_league)

# Sort the Justice League alphabetically, the hero at the 0th index becomes the new leader
justice_league.sort()
print("Justice League sorted alphabetically:", justice_league)
