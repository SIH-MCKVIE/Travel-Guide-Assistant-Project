from services.budget import within_budget
from services.scaledown import get_place_image

def recommend_places(destinations, budget, interest):
    results = []
    interest = interest.lower().strip()

    for place in destinations:
        place_types = [t.lower() for t in place.get("type", [])]

        if within_budget(place["budget"], budget) and any(
    interest in t or t in interest for t in place_types
):

            item = place.copy()

            # Use JSON image first, fallback only if missing
            item["image"] = item.get("image") or get_place_image(place["name"])

            results.append(item)

    return results
