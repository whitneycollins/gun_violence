// Creating map object
var map = L.map("map", {
    center: [39.8283, -108.5795],
    zoom: 4,
  });

  // Adding tile layer
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  }).addTo(map);
  
  var link = "../static/js/convertcsv.geojson";

  // Grabbing our GeoJSON data..
  d3.json(link, function(error, data) {
    L.geoJson(data).addTo(map);
  });