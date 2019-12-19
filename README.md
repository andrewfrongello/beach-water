# About the beach water project

## Project purpose 
This project is intended first and foremost as a personal
project of mine to help learn the Python programming language and to
achieve a better overall understaning of programming in general by
finding real solutions to real problems. 

This program will assist in the analysis of tidal data to find the tidal 
period (high, medium, or low tide) associated with sample collection times 
for thirteen (13) locations throughout Broward County.

## How it works
The program will call the NOAA Web Service API and return data for tide 
predictions for eight (8) stations along the coast. For each of the thirteen (13)
sample locations, the program will use the tidal data from the closest NOAA station
to find the tidal period timeframes and determine which period the sample was
collected in by comparing the sample time to the calculated timeframes.

## Information on NOAA Webservice:
Data is pulled using the U.S. National Oceanic & Atmospheric Administration (NOAA) 
Center for Operational Oceanographic Products and Services (CO-OPS) webservice.

### About NOAA Webservice
https://tidesandcurrents.noaa.gov/web_services_info.html

### About CO-OPS Data Retreival API
https://tidesandcurrents.noaa.gov/api/

### Available data types from CO-OPS
https://tidesandcurrents.noaa.gov/products.html

### Available stations for tide predictions
https://tidesandcurrents.noaa.gov/tide_predictions.html?gid=1397

### Note
The list of stations available from the High/Low Tide Predictions section 
of our website includes all of the stations that we can provide predictions
for along the U.S. coast. This list include presently operating and 
historically observed tidal stations. This list of stations is updated 
annually to include any newly observed or revised stations.

### The stations of interest are:

1) Deerfield Beach
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722832

2) Hillsboro Inlet (ocean)
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722862

3) Lauderdale-By-The-Sea
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722899

4) Bahia Mar Yacht Club
https://tidesandcurrents.noaa.gov/stationhome.html?id=87229

5) South Port Everglades
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722956

6) Whiskey Creek (south enterance)
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722971

7) Hollywood Beach
https://tidesandcurrents.noaa.gov/stationhome.html?id=8722979

8) Golden Beach, ICWW
https://tidesandcurrents.noaa.gov/stationhome.html?id=8723026
