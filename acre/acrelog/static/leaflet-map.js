// Giving credit to people who make Leaflet
const copy =
  "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
// Choosing a background tile. There are many other options to choose from
// if you like. Check this
// https://leaflet-extras.github.io/leaflet-providers/preview/
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
// Create a layer on the map
const layer = L.tileLayer(url, { attribution: copy });
// Finally, we create a map.
// This map will be placed on a HTML tag that has id "map"
const map = L.map("map", { layers: [layer] });

// We will tell the map to show the following location as a default.
// Otherwise, the starting view will be somewhere in Atlantic ocean


const data = JSON.parse(document.getElementById("data_geojson").textContent);

let feature = L.geoJSON(data.features)
  .bindPopup(function (layer) {
    return layer.feature.properties.message;
  })
  .addTo(map);

  map.fitBounds(feature.getBounds());


// L.geoJSON(data_geojson, {
//   style: function (feature) {
//     return { color: "blue", weight: 2, opacity: 0.6 };
//   }
//   }).addTo(map);