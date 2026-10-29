mock_database = [
    {"title": "Luxury Apartment with Burj Khalifa View", "city": "Dubai", "price": 3500},
    {"title": "Modern Budget Studio", "city": "Dubai", "price": 1800},
    {"title": "Marina Luxury Villa", "city": "Abu Dhabi", "price": 7500},
    {"title": "Sharjah Family Flat", "city": "Sharjah", "price": 2200}
]

def filter_properties(database, city, max_price, min_rooms=1):
    filtered = []
    for prop in database:
        if prop["city"].lower() == city.lower() and prop["price"] <= max_price:
            filtered.append(prop)
    return filtered