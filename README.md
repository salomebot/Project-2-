
## Interactive Visualization of Police Incidents in the City and County of San Francisco

### Team Members:
* Abdullah ALfai
* Salome Botelho
* Beheshteh Mostaghni
* Alex Leontiev

### Project Description:
For this project, we used the San Francisco Police Department (SFPD) Incident Report, containing a detailed record of police incidents for 2016. The main goal was to produce a tool that can help increase safety related awareness of the user, using different views into the data set: a number of visualizations that display neighborhood-specific incident data; a heatmap-style calendar which depicts total number of incidents for a given day; and a search feature that reports the total number of incidents which occurred within a certain radius from a given coordinate.

### Data Sets Used:
##### Main Data Set:
* SF Police Department Incidents (2.16M rows total): https://data.sfgov.org/Public-Safety/Police-Department-Incidents/tmnf-yvry

This data set was first reduced to incidents that occurred during calendar 2016. These data were further culled by focusing on the top 10 incidents (by count). This was done to reduce the total number of records to process and yielded approximately 75 thousand records.

##### Supporting Data Set: 
* SF Neighborhood data from the City of San Francisco, through the SF OpenData Socrata API service: https://data.sfgov.org/

Neighborhood information for each incident was obtained using “mapping” code obtained from https://github.com/dylburger/sf-lat-long-mapper. This code provides a programmatic interface which returns the neighborhood name for a given latitude, longitude coordinate—available for each incident in the SFPD report.

### Data Engineering
The SFPD Incident Report data were very clean with no missing and/or duplicate info. The main challenge associated with this data set is its size. Since the primary objective is to increase awareness, data recency is more important than historical perspective. By focusing on the top 10 most frequent incidents, we further reduced the data set size.

These tactics were key to shortening the time-consuming task of obtaining neighborhood information for each record in the data set.  With this reduced size, this processing still took nearly a full day of processing to complete.

Another challenge relates to the addition of geospatial information to each incident, specifically polygon data for a given neighborhood.  This addition facilitated neighborhood-specific mapping using Carto; but doing so, increased the file size of our data set by over 20 fold to nearly 600MB, complicating data movement activities.



