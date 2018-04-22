
## Search Feature

### Author:
* Alex Leontiev

### Description:
This portion of the repo contains the code for the search feature.
It is a full stack Flask based application which provides a search
mechanism.

### Components:
app.py: the python code for end points. <br/>
static subdirectory contains:
* app.js: javascript handling the logic which drives user interactions
* style.css: style file for leaflet styling.
<br/>templates subdirectory contains the html template file.

### Operational Model:
The search feature is implemented using typical Flask based applications:
1. Run the python script (app.py) using: python app.py
2. Once the server is running, invoke the home (/) end point via the browser by accessing: localhost:5000
3. Enter search parameters in the resulting page that is displayed.

The /send end point is also accessible directly via the browser by accessing: localhost:5000/send?textbox=radius,lat,long<br/>
The 'radius,lat,lo' is a list of three numbers: radius (in feet), latitude and longitude (geo coordinates in degrees).
