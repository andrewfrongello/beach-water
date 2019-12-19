"""
Program Name = beach_data.py
Author = Andrew Frongello
Last Update = 12/18/2019
Program purpose: This program calls the NOAA Web Service API and return data 
for tide predictions for thirteen (13) sample locations along Broward County
coastline. There are eight (8) total NOAA stations that this program calls.
For each sample location, the program will call the closest NOAA station.
"""


# import modules to help retreive data from NOAA api
import urllib.request
import json


# declare and define global references
# sampleTimes is an empty list that will be appended as user enters data
# DATE will be used for the NOAA api calls in getTides()
# sampleLocations is a dictionary with key = locations & value = sample times
# tidalStations is a list that will be used as an argument in getTides()
date = input("Please enter date in format YYYYMMDD: ")
sampleLocations = {"Deerfield Pier":"", "NE 16 St":"", "Pompano Pier":"", "Commercial Pier":"", "Hugh Taylor Birch":"", "Sebastian St":"", "Bahia Mar":"", "John U Lloyd":"", "Dania Pier":"","Custer St":"", "Minnesota St":"", "Harrison St":"", "Hallandale Beach":""}
tidalStations = ["DEERFIELD", "HILLSBORO_INLET", "COMMERCIAL", "BAHIA_MAR", "PORT_EVERGLADES", "WHISKEY_CREEK", "HOLLYWOOD", "GOLDEN_BEACH"]
results = []
stationRequests = ["https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722832&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
    "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722862&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
    "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722899&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
    "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722939&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
    "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722956&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
    "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722971&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
    "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722979&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
    "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8723026&time_zone=lst_ldt&units=english&interval=hilo&format=json"]


# this section will retreive the sample collection times from the user
print("")
print("Please enter sample times using HHMM format (including leading zeros but not including the colon character)")

# iterate through the 'sampleLocations' dictionary to associate sample time
# with sample location
for location in sampleLocations:

    sampleTime = input("Enter sample time for " + location + ": ")

    # convert sample time to total minutes and return to sampleTimes list
    hours = int(sampleTime[:2])

    minutes = int(sampleTime[2:])

    totalMinutesSample = (hours * 60) + minutes

    sampleLocations[location] = totalMinutesSample

print("")
print(sampleLocations)

# this function will call the NOAA api for each of 8 tidal stations
def getTides(url):

    req = urllib.request.urlopen(url)
    
    if req.code == 200:
        reqJSON = req.read()
        data = (json.loads(reqJSON))
        return data

    else:
        print(req.code)
        # 200 = successful
        # 400 = bad request
        # 403 = forbidden
        # 404 = not found

# now getting tidal data from NOAA and storing as variable for each station
dataDeerfield = getTides(stationRequests[0])
dataHillsboroInlet = getTides(stationRequests[1])
dataCommercial = getTides(stationRequests[2])
dataBahiaMar = getTides(stationRequests[3])
dataPortEverglades = getTides(stationRequests[4])
dataWhiskeyCreek = getTides(stationRequests[5])
dataHollywood = getTides(stationRequests[6])
dataGoldenBeach = getTides(stationRequests[7])

# this function finds the nearest station for a location and returns the tidal 
# period the sample was collected during
def findTidalPeriod(location):

    print("")

    print(location)

    # determines the closest station and uses corresponding data
    if location == "Deerfield Pier":

        data = dataDeerfield

        print(dataDeerfield)

    elif location == "NE 16 St":

        data = dataHillsboroInlet

        print(dataHillsboroInlet)

    elif location == "Pompano Pier":

        data = dataHillsboroInlet

        print(dataHillsboroInlet)

    elif location == "Commercial Pier":

        data = dataCommercial

        print(dataCommercial)

    elif location == "Hugh Taylor Birch":

        data = dataBahiaMar

        print(dataBahiaMar)

    elif location == "Sebastian St":

        data = dataBahiaMar

        print(dataBahiaMar)
    
    elif location == "Bahia Mar":
    
        data = dataBahiaMar
    
        print(dataBahiaMar)
    
    elif location == "John U Lloyd":
    
        data = dataPortEverglades
    
        print(dataPortEverglades)
    
    elif location == "Dania Pier":
    
        data = dataWhiskeyCreek
    
        print(dataWhiskeyCreek)
    
    elif location == "Custer St":
    
        data = dataHollywood
    
        print(dataHollywood)
    
    elif location == "Minnesota St":
    
        data = dataHollywood
    
        print(dataHollywood)
    
    elif location == "Harrison St":
    
        data = dataHollywood
    
        print(dataHollywood)
    
    elif location == "Hallandale Beach":
    
        data = dataGoldenBeach
    
        print(dataGoldenBeach)

    # create variables for the four data values from NOAA
    first = data["predictions"][0]

    second = data["predictions"][1]

    third = data["predictions"][2]

    # the fourth data value is called in the try-except fashion because some
    # days only report three data values per station
    try:

        fourth = data["predictions"][3]

    except IndexError:

        fourth = "null"

    # determine the type of tide for the first data to use later in the result
    # that will be returned to the calling object
    if first["type"] == "H":

        peakTideType1 = "high"

        peakTideType2 = "low"

    else:

        peakTideType1 = "low"

        peakTideType2 = "high"

    print("1 =" + peakTideType1, "2 =" + peakTideType2)

    # if fourth data value is null, calculate tidal period based off three data
    if fourth == "null":

        # get time and type of tide for first value
        timeDataFirst = first["t"][11:]
        print(timeDataFirst)
        # calculate total minutes for first value
        hoursFirst = int(timeDataFirst[:2])
        minutesFirst = int(timeDataFirst[3:])
        totalMinutesFirst = (hoursFirst * 60) + minutesFirst
        print(totalMinutesFirst)

        # get time and type of tide for second value
        timeDataSecond = second["t"][11:]
        print(timeDataSecond)
        # calculate total minutes for second value
        hoursSecond = int(timeDataSecond[:2])
        minutesSecond = int(timeDataSecond[3:])
        totalMinutesSecond = (hoursSecond * 60) + minutesSecond
        print(totalMinutesSecond)

        # get time and type of tide for third value
        timeDataThird = third["t"][11:]
        print(timeDataThird)
        # calculate total minutes for third value
        hoursThird = int(timeDataThird[:2])
        minutesThird = int(timeDataThird[3:])
        totalMinutesThird = (hoursThird * 60) + minutesThird
        print(totalMinutesThird)

        print("")

        # calculate medium tide peaks
        med1 = (totalMinutesFirst + totalMinutesSecond) / 2
        print(med1)

        med2 = (totalMinutesSecond + totalMinutesThird) / 2
        print(med2)

        print("")

        # calculate beginning and end of the medium tide periods
        med1_begin = (totalMinutesFirst + med1) / 2

        med1_end = (med1 + totalMinutesSecond) / 2

        print(med1_begin, med1_end)

        med2_begin = (totalMinutesSecond + med2) / 2

        med2_end = (med2 + totalMinutesThird) / 2

        print("")

        print(med2_begin, med2_end) 

        print("")

        # logic to determine results
        if totalMinutesFirst < sampleTime <= med1_begin:

            return "Sample for " + location + " was collected during " + peakTideType1 + " tide"

        elif med1_begin <= sampleTime < med1_end:

            return "Sample for " + location + " was collected during medium tide"

        elif med1_end < sampleTime <= med2_begin:

            return "Sample for " + location + " was collected during " + peakTideType2 + " tide"

        elif med2_begin <= sampleTime < med2_end:

            return "Sample for " + location + " was collected during medium tide"

        elif med2_end < sampleTime <= totalMinutesThird:

            return "Sample for " + location + " was collected during " + peakTideType1 + " tide"

    # if fourth data value from NOAA api call is not null, calculate results 
    # based on four data
    else:
        # get time and type of tide for first value
        timeDataFirst = first["t"][11:]
        print(timeDataFirst)
        # calculate total minutes for first value
        hoursFirst = int(timeDataFirst[:2])
        minutesFirst = int(timeDataFirst[3:])
        totalMinutesFirst = (hoursFirst * 60) + minutesFirst
        print(totalMinutesFirst)

        # get time and type of tide for second value
        timeDataSecond = second["t"][11:]
        print(timeDataSecond)
        # calculate total minutes for second value
        hoursSecond = int(timeDataSecond[:2])
        minutesSecond = int(timeDataSecond[3:])
        totalMinutesSecond = (hoursSecond * 60) + minutesSecond
        print(totalMinutesSecond)

        # get time and type of tide for third value
        timeDataThird = third["t"][11:]
        print(timeDataThird)
        # calculate total minutes for third value
        hoursThird = int(timeDataThird[:2])
        minutesThird = int(timeDataThird[3:])
        totalMinutesThird = (hoursThird * 60) + minutesThird
        print(totalMinutesThird)

        # get time and type of tide for fourth value
        timeDataFourth = fourth["t"][11:]
        print(timeDataFourth)
        # calculate total minutes for fourth value
        hoursFourth = int(timeDataFourth[:2])
        minutesFourth = int(timeDataFourth[3:])
        totalMinutesFourth = (hoursFourth * 60) + minutesFourth
        print(totalMinutesFourth)

        print("")

        # calculate medium tide peaks
        med1 = (totalMinutesFirst + totalMinutesSecond) / 2
        print(med1)

        med2 = (totalMinutesSecond + totalMinutesThird) / 2
        print(med2)

        med3 = (totalMinutesThird + totalMinutesFourth) / 2
        print(med3)

        print("")

        # calculate beginning and end of the medium tide periods
        med1_begin = (totalMinutesFirst + med1) / 2

        med1_end = (med1 + totalMinutesSecond) / 2

        print(med1_begin, med1_end)

        med2_begin = (totalMinutesSecond + med2) / 2

        med2_end = (med2 + totalMinutesThird) / 2

        print(med2_begin, med2_end) 

        med3_begin = (totalMinutesThird + med3) / 2

        med3_end = (med3 + totalMinutesFourth) / 2

        print(med3_begin, med3_end)

        print("")

        print(sampleTime)
        
        print("")

        # logic to determine results
        if totalMinutesFirst < sampleTime <= med1_begin:

            return "Sample for " + location + " was collected during " + peakTideType1 + " tide"

        elif med1_begin <= sampleTime < med1_end:

            return "Sample for " + location + " was collected during medium tide"

        elif med1_end < sampleTime <= med2_begin:

            return "Sample for " + location + " was collected during " + peakTideType2 + " tide"

        elif med2_begin <= sampleTime < med2_end:

            return "Sample for " + location + " was collected during medium tide"

        elif med2_end < sampleTime <= med3_begin:

            return "Sample for " + location + " was collected during " + peakTideType1 + " tide"

        elif med3_begin <= sampleTime < med3_end:

            return "Sample for " + location + " was collected during medium tide"

        elif med3_end < sampleTime <= totalMinutesFourth:

            return "Sample for " + location + " was collected during " + peakTideType2 + " tide"

        else:
            return "Sample time is out of range"



# iterating through sampleLocations to use as argument for findTidalPeriod()
# results are appended to 'results' list
for item in sampleLocations:

    sampleTime = sampleLocations.get(item,[])

    tidalPeriod = findTidalPeriod(item)

    results.append(tidalPeriod)

# iterating through 'results' to display tidal period for each sample location
for item in results:

    print(item)