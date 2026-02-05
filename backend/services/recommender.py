from services.budget import within_budget
from services.scaledown import get_place_image

def recommend_places(destinations, budget, interest):
    results = []

    for place in destinations:
        if within_budget(place["budget"], budget) and interest in place["type"]:
            item = place.copy()
            item["image"] = place.get("image") or get_place_image(place["name"])


    return results
