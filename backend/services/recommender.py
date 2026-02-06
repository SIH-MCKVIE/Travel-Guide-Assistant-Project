from services.budget import within_budget
from services.scaledown import get_place_image

def recommend_places(destinations, budget, interest):
    results = []
    interest = interest.lower().strip()

    for place in destinations:
        place_types = [t.lower() for t in place["type"]]

        if within_budget(place["budget"], budget) and interest in place_types:
            item = place.copy()

            # ✅ Preserve JSON image
            if not item.get("image"):
                item["image"] = get_place_image(place["name"])

            results.append(item)

    return results
