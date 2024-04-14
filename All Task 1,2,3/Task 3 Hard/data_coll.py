import pandas as pd

# Load the dataset from Excel file into a DataFrame
df = pd.read_excel('Task 3 Hard\IPLData.xlsx')

# Check the column names
print(df.columns)
# Calculate performance score for each player
df['Performance Score'] = (df['Clean Picks (CP)'] * 1) + \
                          (df['Good Throws (GT)'] * 1) + \
                          (df['Catches (C)'] * 3) + \
                          (df['Dropped Catches (DC)'] * -3) + \
                          (df['Stumpings (S)'] * 3) + \
                          (df['Run Outs (RO)'] * 3) + \
                          (df['Missed Run Outs (MR)'] * -2) + \
                          (df['Direct Hits (DH)'] * 2) + \
                          df['Runs Saved (RS)']

# Print performance scores for each player
print("Performance scores for each player:")
print(df[['Player Name', 'Performance Score']])

# Save the updated DataFrame with performance scores to a new Excel file
df.to_excel('updated_IPL_data.xlsx', index=False)