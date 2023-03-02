# About the beach water monitoring project

## Project purpose 
This project is intended as a personal project to help learn Python and to better understand programming applications.

The program assists with the analysis of tidal data to find the tidal period (high, medium, or low tide) 
associated with sample collection times for thirteen (13) monitoring locations throughout Broward County. 
The project is correlated to Healthy Beaches monitoring duties for a previous position I had with the FDOH in Broward 
and is neither endorsed nor supported by the agency itself.

## How it works
The program calls the NOAA Web Service API and returns tide prediction data for eight (8) tidal monitoring stations along 
the coast. For each of the thirteen (13) sample locations, data from the closest NOAA station is used to find
the tidal period timeframes for the location and the sample is determined to have been collected during
low, medium, or high tide by comparing the collection time to the calculated timeframes.

### The NOAA tidal stations of interest are:

1) Deerfield Beach
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722832

2) Hillsboro Inlet (ocean)
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722862

3) Lauderdale-By-The-Sea
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722899

4) Bahia Mar Yacht Club
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722939

5) South Port Everglades
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722956

6) Whiskey Creek (south enterance)
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722971

7) Hollywood Beach
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722979

8) Golden Beach, ICWW
https://tidesandcurrents.noaa.gov/stationhome.html?id=8723026

## Further information

### Information on Florida Healthy Beaches Program
Information about the program can be found on the FDOH Agency website
http://www.floridahealth.gov/environmental-health/beach-water-quality/index.html

Broward County sample locations and results are publicly accessible and can be found by using the previous link and 
navigating to the Broward webpage using the provided list of counties, although a direct link is also provided here
http://www.floridahealth.gov/environmental-health/beach-water-quality/county-detail.html?County=Broward&Zip=33315-2643

### Information on the NOAA Webservice:
Data is pulled using the U.S. National Oceanic & Atmospheric Administration (NOAA) Center for Operational 
Oceanographic Products and Services (CO-OPS) webservice API.

#### About NOAA Webservice
https://tidesandcurrents.noaa.gov/web_services_info.html

#### About CO-OPS Data Retreival API
https://tidesandcurrents.noaa.gov/api/

#### Available data types from CO-OPS
https://tidesandcurrents.noaa.gov/products.html

#### Available stations for tide predictions
https://tidesandcurrents.noaa.gov/tide_predictions.html?gid=1397

#### Note from the NOAA
"The list of stations available from the High/Low Tide Predictions section of our website includes all of the 
stations that we can provide predictions for along the U.S. coast. This list include presently operating and 
historically observed tidal stations. This list of stations is updated annually to include any newly observed 
or revised stations."
