def generate_itinerary(place, days=3):
    itinerary = []
    for day in range(1, days + 1):
        itinerary.append({
            "day": day,
            "plan": f"Explore popular attractions in {place}"
        })
    return itinerary
