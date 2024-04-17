import itertools
import pandas as pd
import random

# Function to generate random fielding data for an entire innings
def generate_innings_fielding_data(team1, team2, innings, overs, venue):
    data = []
    players = {'CSK': ['Ruturaj Gaikwad (C)', 'Rachin Ravindra', 'Ajinkya Rahane', 'Daryl Mitchell', 'Ravindra Jadeja', 'Sameer Rizvi', 'MS Dhoni (WK)', 'Deepak Chahar', 'Maheesh Theekshana', 'Mustafizur Rahman', 'Tushar Deshpande'],
               'RCB': ['Faf du Plessis(C)', 'Virat Kohli', 'Rajat Patidar', 'Glenn Maxwell', 'Cameron Green', 'Dinesh Karthik', 'Anuj Rawat(WK)', 'Karn Sharma', 'Alzarri Josheph', 'Mayank Dagar', 'Mohammed Siraj']}
    positions = ['Deep Fine Leg', 'Long Off', 'Cover', 'Short Mid Wicket', 'Third Man', 'Point', 'Long On', 'Square Leg', 'Mid Off', 'Short Third Man']
    descriptions = ['Fielding', 'Throw', 'Catch', 'Run Out']
    picks = ['Clean Pick', 'Fumble', 'Drop Catch']
    throws = ['Run Out', 'Other']

    for over, ball in itertools.product(range(overs), range(1, 7)):
        team = team1 if innings == 1 else team2
        player_name = random.choice(players[team])
        position = random.choice(positions)
        description = random.choice(descriptions)
        pick = random.choice(picks) if description == 'Fielding' else ''
        throw = random.choice(throws) if description == 'Throw' else ''
        runs = random.randint(-2, 4)  # Random runs saved or conceded
        data.append([innings, team, player_name, ball, position, description, pick, throw, runs, over+1, venue])

    return data

# Define match details
team1 = 'CSK'
team2 = 'RCB'
innings = 1  # First innings
overs = 20   # Total overs for the innings
venue = 'Dharamshala'

# Generate fielding data for CSK innings
csk_data = generate_innings_fielding_data(team1, team2, innings, overs, venue)

# Generate fielding data for RCB innings
rcb_data = generate_innings_fielding_data(team1, team2, innings=2, overs=overs, venue=venue)

# Combine data for both innings
fielding_data = csk_data + rcb_data

# Create DataFrame
df = pd.DataFrame(fielding_data, columns=['Innings', 'Team', 'Player Name', 'Ballcount', 'Position', 'Short Description', 'Pick', 'Throw', 'Runs', 'Overcount', 'Venue'])

# Save data to CSV file
df.to_csv('fielding_data.csv', index=False)

print("Fielding data saved to 'fielding_data.csv'")
