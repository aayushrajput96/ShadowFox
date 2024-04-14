import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://shadowfox.in/"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the desired data from the website
# For example, let's extract the title of the website
title = soup.title.string

# Print the extracted data
print("Title of the website:", title)
