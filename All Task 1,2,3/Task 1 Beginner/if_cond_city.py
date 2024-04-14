city_country_map = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city_name = input("Enter a city name: ")

found = False
for country, cities in city_country_map.items():
    if city_name in cities:
        print(f"{city_name} is in {country}")
        found = True
        break

if not found:
    print("City not found in the list.")
