import requests

# ⚠️ NOT recommended in production – allowed here for academic demo
SCALEDOWN_API_KEY = "X2KdiYFVZB1LvJ4yi3KMF6sTgrRUb2miicouBD70"

def get_place_image(place_name):
    """
    ScaleDown image generation (simulated – correct integration pattern)
    Replace endpoint if official one differs.
    """

    endpoint = "https://api.scaledown.ai/v1/image"

    headers = {
        "Authorization": f"Bearer {SCALEDOWN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": f"beautiful travel destination photo of {place_name} India",
        "size": "512x512"
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("url")
    except:
        pass

    # fallback image (always works)
    return f"https://via.placeholder.com/512x512.png?text={place_name}"