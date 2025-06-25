fetch("http://0.0.0.0:5001/api/v1/places_search/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({})
})
.then(res => res.json())
.then(data => console.log(data))
