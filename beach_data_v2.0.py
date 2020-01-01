"""
Program Name = beach_data.py
Author = Andrew Frongello
Last Update = 01/01/2020
Program purpose: This program calls the NOAA Web Service API and return data 
for tide predictions for thirteen (13) sample locations along Broward County
coastline. There are eight (8) total NOAA stations that this program calls.
For each sample location, the program will call the closest NOAA station.
"""


# Import modules to help retreive data from NOAA api
import urllib.request
import json
import tkinter


class BeachwaterGUI:
    def __init__(self):

        
        # TOPLEVEL STUFF-------------------------------------------------------
        # Initialize main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("600x470")
        # Window title
        self.main_window.title("Healthy Beaches Tidal Analysis Program")
        
        
        # FRAME DESIGN---------------------------------------------------------
        # Main frames
        self.top_frame = tkinter.Frame(self.main_window, borderwidth=2, relief="groove")
        self.date_frame = tkinter.Frame(self.main_window, borderwidth=2, relief="groove")
        self.show_date_frame = tkinter.Frame(self.date_frame, borderwidth=2, relief="groove")
        self.data_entry_frame = tkinter.Frame(self.main_window, borderwidth=2, relief="groove")
        self.button_frame = tkinter.Frame(self.main_window, borderwidth=2, relief="groove")
        # Data entry sub-frames
        self.entry_label_frame = tkinter.Frame(self.data_entry_frame, borderwidth=2, relief="groove")
        self.entry_frame = tkinter.Frame(self.data_entry_frame, borderwidth=2, relief="groove")


        # WIDGETS--------------------------------------------------------------
        # Frame labels
        self.top_label = tkinter.Label(self.top_frame, text="Welcome to the Healthy Beaches tidal analysis program. \nPlease complete the form entirely and click Analyze Tides.", relief="groove")
        self.date_label = tkinter.Label(self.date_frame, text="Enter date of sample collection", relief="groove")
        self.show_date_label = tkinter.Label(self.show_date_frame, relief="groove", wraplength=120)
        self.entry_label = tkinter.Label(self.entry_frame, text="Enter sample times for each location using HHMM notation", relief="groove")
        self.header_location = tkinter.Label(self.entry_frame, text="Sample Location", relief="groove", anchor="w")
        self.header_time = tkinter.Label(self.entry_frame, text="Sample Time", relief="groove", anchor="w")
        self.header_result = tkinter.Label(self.entry_frame, text="Tidal Period", relief="groove", anchor="w")
        # Date frame
        self.month = tkinter.Label(self.date_frame, text="Month")
        self.day = tkinter.Label(self.date_frame, text="Day")
        self.year = tkinter.Label(self.date_frame, text="Year")
        self.month_entry = tkinter.Entry(self.date_frame, width=2)
        self.day_entry = tkinter.Entry(self.date_frame, width=2)
        self.year_entry = tkinter.Entry(self.date_frame, width=4)
        # Sample entry frame
        self.BahiaMar = tkinter.Label(self.entry_frame, text="Bahia Mar", relief="groove", anchor="w")
        self.Sebastian = tkinter.Label(self.entry_frame, text="Sebastian St", relief="groove", anchor="w")
        self.HughTaylor = tkinter.Label(self.entry_frame, text="Hugh Taylor Birch", relief="groove", anchor="w")
        self.Commercial = tkinter.Label(self.entry_frame, text="Commercial Pier", relief="groove", anchor="w")
        self.Pompano = tkinter.Label(self.entry_frame, text="Pompano Pier", relief="groove", anchor="w")
        self.NE16 = tkinter.Label(self.entry_frame, text="NE 16 St", relief="groove", anchor="w")
        self.Deerfield = tkinter.Label(self.entry_frame, text="Deerfield Pier", relief="groove", anchor="w")
        self.Hallandale = tkinter.Label(self.entry_frame, text="Hallandale Beach", relief="groove", anchor="w")
        self.Harrison = tkinter.Label(self.entry_frame, text="Harrison St", relief="groove", anchor="w")
        self.Minnesota = tkinter.Label(self.entry_frame, text="Minnesota St", relief="groove", anchor="w")
        self.Custer = tkinter.Label(self.entry_frame, text="Custer St", relief="groove", anchor="w")
        self.Dania = tkinter.Label(self.entry_frame, text="Dania Pier", relief="groove", anchor="w")
        self.JohnLloyd = tkinter.Label(self.entry_frame, text="John U Lloyd", relief="groove", anchor="w")
        self.entryBahiaMar = tkinter.Entry(self.entry_frame, width=6)
        self.entrySebastian = tkinter.Entry(self.entry_frame, width=6)
        self.entryHughTaylor = tkinter.Entry(self.entry_frame, width=6)
        self.entryCommercial = tkinter.Entry(self.entry_frame, width=6)
        self.entryPompano = tkinter.Entry(self.entry_frame, width=6)
        self.entryNE16 = tkinter.Entry(self.entry_frame, width=6)
        self.entryDeerfield = tkinter.Entry(self.entry_frame, width=6)
        self.entryHallandale = tkinter.Entry(self.entry_frame, width=6)
        self.entryHarrison = tkinter.Entry(self.entry_frame, width=6)
        self.entryMinnesota = tkinter.Entry(self.entry_frame, width=6)
        self.entryCuster = tkinter.Entry(self.entry_frame, width=6)
        self.entryDania = tkinter.Entry(self.entry_frame, width=6)
        self.entryJohnLloyd = tkinter.Entry(self.entry_frame, width=6)
        self.resultBahiaMar = tkinter.Label(self.entry_frame)
        self.resultSebastian = tkinter.Label(self.entry_frame)
        self.resultHughTaylor = tkinter.Label(self.entry_frame)
        self.resultCommercial = tkinter.Label(self.entry_frame)
        self.resultPompano = tkinter.Label(self.entry_frame)
        self.resultNE16 = tkinter.Label(self.entry_frame)
        self.resultDeerfield = tkinter.Label(self.entry_frame)
        self.resultHallandale = tkinter.Label(self.entry_frame)
        self.resultHarrison = tkinter.Label(self.entry_frame)
        self.resultMinnesota = tkinter.Label(self.entry_frame)
        self.resultCuster = tkinter.Label(self.entry_frame)
        self.resultDania = tkinter.Label(self.entry_frame)
        self.resultJohnLloyd = tkinter.Label(self.entry_frame)
        #self.sampleTimesColumn = [self.entryBahiaMar, self.entrySebastian, self.entryHughTaylor, self.entryCommercial, self.entryPompano, self.entryNE16, self.entryDeerfield, self.entryHallandale, self.entryHarrison, self.entryMinnesota, self.entryCuster, self.entryDania, self.entryJohnLloyd]
        # Button frame
        self.findTides_button = tkinter.Button(self.button_frame, text="Analyze Tides", relief="raised", command=self.analyzeTides)
        self.reset_button = tkinter.Button(self.button_frame, text="Reset", relief="raised", command=self.reset)


        # GEOMETRY MANAGEMENT--------------------------------------------------
        # Main frames
        self.top_frame.grid(column=0, row=0, sticky="w")
        self.date_frame.grid(column=0, row=1, sticky="w")
        self.data_entry_frame.grid(column=0, row=2, sticky="w")
        self.button_frame.grid(column=0, row=3, sticky="w")
        # Date frame
        self.date_label.grid(column=0, row=0, sticky="nw", columnspan=6)
        self.month.grid(column=0, row=1, sticky="e")
        self.month_entry.grid(column=1, row=1)
        self.day.grid(column=2, row=1, sticky="e")
        self.day_entry.grid(column=3, row=1)
        self.year.grid(column=4, row=1, sticky="e")
        self.year_entry.grid(column=5, row=1)
        self.show_date_label.grid(column=6, row=0)
        self.show_date_frame.grid(column=7, row=0, sticky="nw", padx=(10,0))
        # Sample entry frame 
        self.entry_label.grid(column=0, row=0, sticky="ew", columnspan=3)
        self.entry_frame.grid(column=0, row=1, sticky="w")
        self.header_location.grid(column=0, row=1, sticky="ew")
        self.header_time.grid(column=1, row=1, sticky="ew")
        self.header_result.grid(column=2, row=1, sticky="ew")
        self.BahiaMar.grid(column=0, row=2, sticky="ew")
        self.Sebastian.grid(column=0, row=3, sticky="ew")
        self.HughTaylor.grid(column=0, row=4, sticky="ew")
        self.Commercial.grid(column=0, row=5, sticky="ew")
        self.Pompano.grid(column=0, row=6, sticky="ew")
        self.NE16.grid(column=0, row=7, sticky="ew")
        self.Deerfield.grid(column=0, row=8, sticky="ew")
        self.Hallandale.grid(column=0, row=9, sticky="ew")
        self.Harrison.grid(column=0, row=10, sticky="ew")
        self.Minnesota.grid(column=0, row=11, sticky="ew")
        self.Custer.grid(column=0, row=12, sticky="ew")
        self.Dania.grid(column=0, row=13, sticky="ew")
        self.JohnLloyd.grid(column=0, row=14, sticky="ew")
        self.entryBahiaMar.grid(column=1, row=2, sticky="ew")
        self.entrySebastian.grid(column=1, row=3, sticky="ew")
        self.entryHughTaylor.grid(column=1, row=4, sticky="ew")
        self.entryCommercial.grid(column=1, row=5, sticky="ew")
        self.entryPompano.grid(column=1, row=6, sticky="ew")
        self.entryNE16.grid(column=1, row=7, sticky="ew")
        self.entryDeerfield.grid(column=1, row=8, sticky="ew")
        self.entryHallandale.grid(column=1, row=9, sticky="ew")
        self.entryHarrison.grid(column=1, row=10, sticky="ew")
        self.entryMinnesota.grid(column=1, row=11, sticky="ew")
        self.entryCuster.grid(column=1, row=12, sticky="ew")
        self.entryDania.grid(column=1, row=13, sticky="ew")
        self.entryJohnLloyd.grid(column=1, row=14, sticky="ew")
        self.resultBahiaMar.grid(column=2, row=2, sticky="w")
        self.resultSebastian.grid(column=2, row=3, sticky="w")
        self.resultHughTaylor.grid(column=2, row=4, sticky="w")
        self.resultCommercial.grid(column=2, row=5, sticky="w")
        self.resultPompano.grid(column=2, row=6, sticky="w")
        self.resultNE16.grid(column=2, row=7, sticky="w")
        self.resultDeerfield.grid(column=2, row=8, sticky="w")
        self.resultHallandale.grid(column=2, row=9, sticky="w")
        self.resultHarrison.grid(column=2, row=10, sticky="w")
        self.resultMinnesota.grid(column=2, row=11, sticky="w")
        self.resultCuster.grid(column=2, row=12, sticky="w")
        self.resultDania.grid(column=2, row=13, sticky="w")
        self.resultJohnLloyd.grid(column=2, row=14, sticky="w")
        # Button frame
        self.findTides_button.grid(column=0, row=0, sticky="ew", ipadx=(50))
        self.reset_button.grid(column=1, row=0, sticky="ew", ipadx=(50))


        # PACKING WIDGETS------------------------------------------------------
        # Packing not needed for frames managed with geometry manager
        self.top_label.pack()
        # Mainloop
        tkinter.mainloop()

    # define functionality for the 'reset' button
    def reset(self):
        self.month_entry.delete(0,"end")
        self.day_entry.delete(0,"end")
        self.year_entry.delete(0,"end")
        self.entryBahiaMar.delete(0,"end")
        self.entrySebastian.delete(0,"end")
        self.entryHughTaylor.delete(0,"end")
        self.entryCommercial.delete(0,"end")
        self.entryPompano.delete(0,"end")
        self.entryNE16.delete(0,"end")
        self.entryDeerfield.delete(0,"end")
        self.entryHallandale.delete(0,"end")
        self.entryHarrison.delete(0,"end")
        self.entryMinnesota.delete(0,"end")
        self.entryCuster.delete(0,"end")
        self.entryDania.delete(0,"end")
        self.entryJohnLloyd.delete(0,"end")
        self.show_date_label.config(text="")
        self.resultBahiaMar.config(text="")
        self.resultSebastian.config(text="")
        self.resultHughTaylor.config(text="")
        self.resultCommercial.config(text="")
        self.resultPompano.config(text="")
        self.resultNE16.config(text="")
        self.resultDeerfield.config(text="")
        self.resultHallandale.config(text="")
        self.resultHarrison.config(text="")
        self.resultMinnesota.config(text="")
        self.resultCuster.config(text="")
        self.resultDania.config(text="")
        self.resultJohnLloyd.config(text="")

    # analyze tides function
    def analyzeTides(self):
        
        # get the date
        month = str(self.month_entry.get())
        day = str(self.day_entry.get())
        year = str(self.year_entry.get())
        date = year + month + day
        self.show_date_label.config(text="Analyzing tidal data for " + month + '/' + day + '/' + year)
        
        # this list will be appended to add results for all locations
        results = []
        
        # provide the URL list for API calls
        stationRequests = ["https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722832&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
        "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722862&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
        "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722899&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
        "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722939&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
        "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722956&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
        "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722971&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
        "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8722979&time_zone=lst_ldt&units=english&interval=hilo&format=json", \
        "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=" + date + "&end_date=" + date + "&datum=MLLW&station=8723026&time_zone=lst_ldt&units=english&interval=hilo&format=json"]
        
        # provide dictionary to associate sample times with locations
        sampleLocations = {"Bahia Mar":"", "Sebastian St":"", "Hugh Taylor Birch":"", "Commercial Pier":"", "Pompano Pier":"", "NE 16 St":"", "Deerfield Pier":"", "Hallandale Beach":"", "Harrison St":"", "Minnesota St":"", "Custer St":"", "Dania Pier":"", "John U Lloyd":""}
        
        # create list of sample times
        sampleTimes = [self.entryBahiaMar.get(), self.entrySebastian.get(), self.entryHughTaylor.get(), self.entryCommercial.get(), self.entryPompano.get(), self.entryNE16.get(), self.entryDeerfield.get(), self.entryHallandale.get(), self.entryHarrison.get(), self.entryMinnesota.get(), self.entryMinnesota.get(), self.entryDania.get(), self.entryJohnLloyd.get()]
        
        print(sampleTimes)
        
        # append dictionary to associate sample times
        n = 0
        for location in sampleLocations:
            sampleTime = sampleTimes[n]
            print(sampleTime)
            hours = int(sampleTime[:2])
            minutes = int(sampleTime[2:])
            totalMinutesSample = (hours * 60) + minutes
            sampleLocations[location] = totalMinutesSample
            n += 1
            #for location in sampleLocations:
                #sampleLocations[location] = totalMinutesSample

        print(sampleLocations)

        # call the NOAA api for each of 8 tidal stations and store as variables
        def reqTides(url):

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
        dataDeerfield = reqTides(stationRequests[0])
        dataHillsboroInlet = reqTides(stationRequests[1])
        dataCommercial = reqTides(stationRequests[2])
        dataBahiaMar = reqTides(stationRequests[3])
        dataPortEverglades = reqTides(stationRequests[4])
        dataWhiskeyCreek = reqTides(stationRequests[5])
        dataHollywood = reqTides(stationRequests[6])
        dataGoldenBeach = reqTides(stationRequests[7])


        # this function finds the tidal period which occurred during sample collection
        # uses nearest available station 
        # stores output in 'results' list
        def findTidalPeriod(location):

            print("")

            print("Analyzing data for " + location.upper())

            # condition table to use data from closest station to sample location
            # tried to group locations together that use the same station but was...
            # encountering errors so went with condition for each location seperately
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

            # create variables for the four data values (tidal peaks/troughs) from NOAA
            first = data["predictions"][0]
            second = data["predictions"][1]
            third = data["predictions"][2]

            # exception handler
            # the fourth data value is called in the try-except fashion because some...
            # days only report three data values per station.
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

            print("First tide type = " + peakTideType1)

            # get time and type of tide for first value
            timeDataFirst = first["t"][11:]
            hoursFirst = int(timeDataFirst[:2])
            minutesFirst = int(timeDataFirst[3:])
            totalMinutesFirst = (hoursFirst * 60) + minutesFirst
            print("First tide peak @ " + str(timeDataFirst) + " or " + str(totalMinutesFirst) + " minutes")

            # get time and type of tide for second value
            timeDataSecond = second["t"][11:]
            hoursSecond = int(timeDataSecond[:2])
            minutesSecond = int(timeDataSecond[3:])
            totalMinutesSecond = (hoursSecond * 60) + minutesSecond
            print("Second tide peak @ " + str(timeDataSecond) + " or " + str(totalMinutesSecond) + " minutes")

            # get time and type of tide for third value
            timeDataThird = third["t"][11:]
            hoursThird = int(timeDataThird[:2])
            minutesThird = int(timeDataThird[3:])
            totalMinutesThird = (hoursThird * 60) + minutesThird
            print("Third tide peak @ " + str(timeDataThird) + " or " + str(totalMinutesThird) + " minutes")

            # get time and type of tide for fourth value
            try:
                timeDataFourth = fourth["t"][11:]
                hoursFourth = int(timeDataFourth[:2])
                minutesFourth = int(timeDataFourth[3:])
                totalMinutesFourth = (hoursFourth * 60) + minutesFourth
                print("Fourth tide peak @ " + str(timeDataFourth) + " or " + str(totalMinutesFourth) + " minutes")
                print("")

            except:
                fourth = "null"

            # calculate medium tide peaks
            med1 = (totalMinutesFirst + totalMinutesSecond) / 2
            print("First medium tide peak will be @ " + str(med1) + " minutes")
            med2 = (totalMinutesSecond + totalMinutesThird) / 2
            print("Second medium tide peak will be @ " + str(med2) + " minutes")
            try:
                med3 = (totalMinutesThird + totalMinutesFourth) / 2
                print("Third medium tide peak will be @ " + str(med3) + " minutes")
            except:
                fourth = "null"   
            print("")

            # calculate beginning and end of the medium tide periods
            med1_begin = (totalMinutesFirst + med1) / 2
            med1_end = (med1 + totalMinutesSecond) / 2
            print("The first medium tide period with be from " + str(med1_begin) + " to " + str(med1_end) + " minutes")
            med2_begin = (totalMinutesSecond + med2) / 2
            med2_end = (med2 + totalMinutesThird) / 2
            print("The second medium tide period with be from " + str(med2_begin) + " to " + str(med2_end) + " minutes") 
            try:
                med3_begin = (totalMinutesThird + med3) / 2
                med3_end = (med3 + totalMinutesFourth) / 2
                print("The third medium tide period with be from " + str(med3_begin) + " to " + str(med3_end) + " minutes")
            except:
                fourth = "null"
            print("")
            print(sampleTime)
            print("")

            # mapped tidal data with logic to determine results
            if totalMinutesFirst < sampleTime <= med1_begin:
                return peakTideType1

            elif med1_begin <= sampleTime < med1_end:
                return "medium"

            elif med1_end < sampleTime <= med2_begin:
                return peakTideType2

            elif med2_begin <= sampleTime < med2_end:
                return "medium"

            elif med2_end < sampleTime <= med3_begin:
                return peakTideType1

            elif med3_begin <= sampleTime < med3_end:
                return "medium"

            elif med3_end < sampleTime <= totalMinutesFourth:
                return peakTideType2

            else:
                return "Sample time is out of range"


        # iterating through sampleLocations to use as argument for findTidalPeriod()
        # results are appended to 'results' list
        for item in sampleLocations:
            sampleTime = sampleLocations.get(item)
            tidalPeriod = findTidalPeriod(item)
            results.append(tidalPeriod)
            print("")


        # iterating through 'results' to display tidal period for each sample location
        for item in results:
            # print(item)

            self.resultBahiaMar.config(text=results[0])
            self.resultSebastian.config(text=results[1])
            self.resultHughTaylor.config(text=results[2])
            self.resultCommercial.config(text=results[3])
            self.resultPompano.config(text=results[4])
            self.resultNE16.config(text=results[5])
            self.resultDeerfield.config(text=results[6])
            self.resultHallandale.config(text=results[7])
            self.resultHarrison.config(text=results[8])
            self.resultMinnesota.config(text=results[9])
            self.resultCuster.config(text=results[10])
            self.resultDania.config(text=results[11])
            self.resultJohnLloyd.config(text=results[12])

runGUI = BeachwaterGUI()