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

  if (data.length === 0) {
    results.innerHTML = "<p style='text-align:center'>No destinations found</p>";
    map.style.display = "none";
    return;
  }

  data.forEach(place => {
    results.innerHTML += `
      <div class="card">
        <img src="${place.image}">
        <div class="card-content">
          <h3>${place.name}</h3>
          <p><strong>Budget:</strong> ₹${place.budget}</p>
          <p><strong>RAG Rank:</strong> ${place.rag_rank ?? "N/A"}</p>
          <div class="itinerary">
            <strong>Itinerary:</strong>
            ${place.itinerary.map(d => `<div>Day ${d.day}: ${d.plan}</div>`).join("")}
          </div>
        </div>
      </div>
    `;

    // Update map for first result
    map.src = `https://www.google.com/maps?q=${place.name}&output=embed`;
    map.style.display = "block";
  });
}
