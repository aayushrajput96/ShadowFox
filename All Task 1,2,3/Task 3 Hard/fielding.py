import itertools
import pandas as pd
import random

# Function to generate random fielding data
def generate_fielding_data(player_name, match_no, innings, team, overs, venue):
    data = []
    positions = ['Deep Fine Leg', 'Long Off', 'Cover', 'Short Mid Wicket', 'Third Man', 'Point', 'Long On', 'Square Leg', 'Mid Off', 'Short Third Man']
    descriptions = ['Fielding', 'Throw', 'Catch', 'Run Out']
    picks = ['Clean Pick', 'Fumble', 'Drop Catch']
    throws = ['Run Out', 'Other']

    for over, ball in itertools.product(range(overs), range(1, 7)):
        position = random.choice(positions)
        description = random.choice(descriptions)
        pick = random.choice(picks) if description == 'Fielding' else ''
        throw = random.choice(throws) if description == 'Throw' else ''
        runs = random.randint(-2, 4)  # Random runs saved or conceded
        data.append([match_no, innings, team, player_name, ball, position, description, pick, throw, runs, over+1, venue])

    return data

# Generate random fielding data for Virat Kohli
virat_data = generate_fielding_data('Virat Kohli', match_no=1, innings=1, team='RCB', overs=20, venue='Dharamshala')

# Generate random fielding data for Faf du Plessis
faf_data = generate_fielding_data('Faf du Plessis', match_no=1, innings=1, team='CSK', overs=20, venue='Dharamshala')

# Combine data for both players
fielding_data = virat_data + faf_data

# Create DataFrame
df = pd.DataFrame(fielding_data, columns=['Match No.', 'Innings', 'Team', 'Player Name', 'Ballcount', 'Position', 'Short Description', 'Pick', 'Throw', 'Runs', 'Overcount', 'Venue'])

# Save data to CSV file
df.to_csv('fielding_data.csv', index=False)

print("Fielding data saved to 'fielding_data.csv'")
