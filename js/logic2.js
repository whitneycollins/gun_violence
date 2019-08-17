// Creating map object
var map = L.map("map", {

    center: [39.8283, -108.5795],
    zoom: 4,
 
  });

  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 5,
    id: "mapbox.light",
    accessToken: API_KEY
  }).addTo(map);
  
  var link = "js/convertcsv.geojson";

  d3.json(link, function(response) {
    console.log(response)
    // Create a new marker cluster group
    var markers = L.markerClusterGroup();
  
    // Loop through data
    for (var i = 0; i < response.length; i++) {
  
      // Set the data location property to a variable
      var location = response[i].geometry;
  
      // Check for location property
      if (location) {
  
        // Add a new marker to the cluster group and bind a pop-up
        markers.addLayer(L.marker([location.coordinates[1], location.coordinates[0]])
          .bindPopup(response[i].geometry));
      }
  
    }
  
    // Add our marker cluster layer to the map
    map.addLayer(markers);
  
  });
  