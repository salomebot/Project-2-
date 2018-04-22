# This python script sets up two Flask end points used by the search
#   feature. The first one (for /) simply renders an html file
#   which displays a text input field for the user to input search
#   parameters.
# The second and more comprehensive end point (/send) returns
#   summary data of records in the data set that match the search
#   parameters. 
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

df = pd.read_csv('subset_data.csv')

@app.route("/")
def home():
    return render_template("index.html")

# This end point extracts the search parameters passed in as arguments
#   (when invoked by the browser), retireves drecords from the data set 
#   that match these parameters, aggregateds these records (by category
#   type) to obtain summary info, and returns the results as json object.
# The input parameters are expected to be a comma separated list of
#   three numbers: radius, lattitude and longitude. The order has to
#   match, and parameters need to be numbers (float).
#   The radius is expressed in feet, and lat/lon are geo coordinates
#   in decimal form.
@app.route("/send")
def send():
    categories = ['ASSAULT', 'BURGLARY', 'DRUG/NARCOTIC', 'FRAUD', 'LARCENY/THEFT',
                  'ROBBERY', 'SUSPICIOUS OCC', 'VANDALISM', 'VEHICLE THEFT', 'WEAPON LAWS']
    locations = []
    response = []
    user_input = request.args.get('textbox')
    in1, in2, in3 = user_input.split(',')
    radius = float(in1)
    lat = float(in2)
    lon = float(in3)
# The following loop performs a search of the data set and appends
#   records that match search critereon to a list (locations[]).
# The search critereon is the distance between the location supplied
#   in the input arguments and the location of each incident.
# Distance calculation is performed using the Pythogeres Theorm
#   which is good enough for this case--relatively small geographic
#   area for which the curvature of the earth can be ignored.
# The formula used is the square root of the sum of lat/long
#   differences squared, and multiplied by the circumfrence of the
#   earth (24901 miles) divided by 360 (total number of degrees).
    for i in range(0,len(df['lat'])):
      distance = float ((((lon - df['lng'][i])**2 + (lat - df['lat'][i])**2) ** 0.5) * (24901/360))
      if distance < radius/5280:
          record = {'category': df['category'][i], 'lat': df['lat'][i], 'lng': df['lng'][i]}
          locations.append(record)
# If any locations are found, summarize the data by calculating the
#   count of records found for each category, along with an adjusted
#   location for a given category.  This is so the markers used to
#   display summary info (count) are staggerred on the map (otherwise
#   they will all overlap and appear as a single marker to the user).
    if len(locations) > 0:
        k = 0
        for n in categories:
          count = 0
          for j in range(0,len(locations)):
            if locations[j]['category'] == n: count += 1
          if count > 0:
            adjusted_lat = lat + k*.0005
            adjusted_lon = lon + k*.0005
            response.append({'category':n, 'location':[adjusted_lat, adjusted_lon], 'count':count})
            k += 1
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
