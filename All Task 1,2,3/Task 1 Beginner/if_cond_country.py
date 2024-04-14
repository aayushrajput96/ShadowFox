city_country_map = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = next(
    (
        country
        for country, cities in city_country_map.items()
        if city1 in cities
    ),
    None,
)
country2 = next(
    (
        country
        for country, cities in city_country_map.items()
        if city2 in cities
    ),
    None,
)

if country1 is not None and country2 is not None and country1 == country2:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")
