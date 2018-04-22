/* This javascript contains the event handler for the submit
   button appearing on the html page.
   The basic operations are to retrieve the text entered in the
   input field (#textbox element), preparing the URL string used
   to invoke the search funtion associated with the /send end point,
   reading the response sent back, and preparing a map displaying the
   search results (as a number of markers within a circle rendered
   on a map of SF for the given location).
*/

const form = d3.select('form');
var myMap = null;

form.on('submit', () => {
  d3.event.preventDefault();
  const inputField = d3.select('#textbox');
  values = inputField.node().value;
// The following 6 lines of code perform the equivalent of one line
//   of python code: radius, lat, lng = values.split(','). It
//   would've really nice if javascript provided a similar method.
  var i = values.indexOf(',');
  var radius = values.slice(0,i).trim();
  i = values.lastIndexOf(',');
  var lng = values.slice(i+1, values.lenght);
  var s = radius.length+1;
  var lat = values.substr(s,(values.length-radius.length-lng.length-2));
  radius = +radius;
  lat = +lat;
  lng = +lng;

  var incidents = [];
  endpoint = '/send?textbox='.concat(inputField.node().value);
  d3.json(endpoint, function(error, response) { 
    if (error) return console.warn(error);
    for (i=0; i<response.length; i++){
        incidents.push(response[i])
    }
    console.log('got ' + incidents.length + ' incidents');
    var incidentMarkers = [];
    for (var i = 0; i < 5; i++) {
    // loop through the cities array, create a new marker, push it to the cityMarkers array
      incidentMarkers.push(
          L.marker(incidents[i].location).bindPopup("<h3>" + incidents[i].category + "</h3><hr>" + incidents[i].count)
      );
    };
    var incidentLayer = L.layerGroup(incidentMarkers);
    var overlayMap = {
        Incidents: incidentLayer
    };
    
    var light = L.tileLayer(
      "https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1IjoiYWxlb250aWV2IiwiYSI6ImNqZmVnYTd1YTFjc2kyd21zZjE2aDI4NzEifQ.lhQY5pddfZ0M45Yoz5E4sg"
    );

    if (myMap != undefined || myMap != null) { 
      myMap.off(); 
      myMap.remove();
    }

    var myMap = L.map("map", {
      center: [lat, lng],
      zoom: 15,
      layers: [light, incidentLayer]
    });
      // Add the map layers to the layer control, and
      // add the layer control to the map
    L.control.layers([light], overlayMap).addTo(myMap);
    
    L.circle([lat, lng], {
      color: "green",
      fillColor: "green",
      fillOpacity: 0.35,
      radius: 500
    }).bindPopup("<h1>" + 'Total Incidents XXX' + "</h1>")
      .addTo(myMap);
    })
})