from flask import request, jsonify
from services.recommender import recommend_places
from services.itinerary import generate_itinerary
from utils.helpers import normalize
from utils.rag import rag_search
import os

def recommend(destinations):
    data = request.get_json()
    budget = int(data["budget"])
    interest = normalize(data["interest"])

    results = recommend_places(destinations, budget, interest)

    # RAG search
    guides_path = os.path.join(os.path.dirname(__file__), "..", "data", "guides")
    from utils.rag import load_guides
    docs = load_guides(guides_path)
    ranked_places = rag_search(interest, docs)

    # Attach itinerary
    for r in results:
        r["itinerary"] = generate_itinerary(r["name"], 3)
        r["rag_rank"] = ranked_places.index(r["name"].lower()) + 1 if r["name"].lower() in ranked_places else None

    return jsonify(results)
