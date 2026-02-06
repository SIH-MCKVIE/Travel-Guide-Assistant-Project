async function search() {
  const budget = document.getElementById("budget").value;
  const interest = document.getElementById("interest").value;

  if (!budget || !interest) {
    alert("Please enter both budget and interest");
    return;
  }

  const res = await fetch("/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ budget, interest })
  });

  const data = await res.json();

  const results = document.getElementById("results");
  const map = document.getElementById("map");

  results.innerHTML = "";
  map.style.display = "none";

  if (!Array.isArray(data) || data.length === 0) {
    results.innerHTML =
      "<p style='text-align:center'>No destinations found 😕</p>";
    return;
  }

  data.forEach((place, index) => {
    let image = "https://picsum.photos/800/400";

    if (typeof place.image === "string" && place.image.startsWith("http")) {
      image = place.image.includes("images.unsplash.com")
        ? `${place.image}?w=800&auto=format&fit=crop`
        : place.image;
    }

    const itineraryHTML = Array.isArray(place.itinerary)
      ? place.itinerary
          .map(d => `<div>Day ${d.day}: ${d.plan}</div>`)
          .join("")
      : "<div>No itinerary available</div>";

    results.innerHTML += `
      <div class="card">
        <img
          src="${image}"
          alt="${place.name}"
          loading="lazy"
          referrerpolicy="no-referrer"
          onerror="this.onerror=null; this.src='https://picsum.photos/800/400';"
        >
        <div class="card-content">
          <h3>${place.name}</h3>
          <div class="badge">
            ₹${place.budget} • RAG Rank ${place.rag_rank ?? "N/A"}
          </div>
          <div class="itinerary">
            <strong>🗓 Itinerary</strong>
            ${itineraryHTML}
          </div>
        </div>
      </div>
    `;

    if (index === 0) {
      map.src = `https://www.google.com/maps?q=${encodeURIComponent(
        place.name
      )}&output=embed`;
      map.style.display = "block";
    }
  });
}
