from requests_html import HTMLSession
from dotenv import load_dotenv
import os

load_dotenv()


class weatherScraping:


#######################################################################
#                  Google Weather Information                         #
#######################################################################
    
    def getGoogleWeather(self,session,temp):
        
        url = 'https://www.google.com/search?q=weather+{}'.format(temp)
        results = self.QueryResults(session,url)
        temp = results.html.find(os.getenv('GOOGLE_TEMP'), first=True).text
        location = results.html.find(os.getenv('GOOGLE_LOCATION'), first=True).text
        dateTime = results.html.find(os.getenv('GOOGLE_DT_TIME'), first=True).text
        precipitation = results.html.find(os.getenv('GOOGLE_PRECIPITATION'), first=True).text
        humidity = results.html.find(os.getenv('GOOGLE_HUMIDITY'), first=True).text
        wind = results.html.find(os.getenv('GOOGLE_WIND'), first=True).text
        print("Google Weather service Details\nLocation: {}\nTemp: {}\nDateTime: {}\nPrecipitation:{}\nHumidity:{}\nWind:{}".format(location,temp,dateTime,precipitation,humidity,wind))

  
  ###########################################################################
  #                   National Weather Service Information                  #
  ###########################################################################   

    def getNationalWeather(self,session,city,state):
    
        url = "https://forecast.weather.gov/MapClick.php?CityName={}&state={}".format(city,state)
        results = self.QueryResults(session,url)

        location = results.html.find(os.getenv('NW_LOCATION'), first=True).text
        todayHigh = results.html.find(os.getenv('NW_HIGH_TEMP'), first=True).text
        todayLow = results.html.find(os.getenv('NW_LOW_TEMP'), first=True).text
        todayTimePeriod = results.html.find(os.getenv('NW_TIME_PERIOD'), first=True).text
        table = results.html.find(os.getenv('NW_TABLE'), first=True).text
        panel = results.html.find(os.getenv('NW_PANEL'), first=True).text
        print("\nNational Weather Service details\n{}\n{}\n{}\n{}\n{}\n{}".format(location,todayTimePeriod,todayHigh,todayLow,table,panel))
    

    #####################################################################
    #                         HTML Session Builder                      #
    #####################################################################
    def sessionBuilder(self):
        return  HTMLSession()
    
    #####################################################################
    #                      Get query results                            #
    #####################################################################
    def QueryResults(self,session,url):
        s =session
        return s.get(url, headers={'User-Agent': os.getenv("MY_USER_AGENT")})




class main: 
    weather = weatherScraping()
    weather.getGoogleWeather(weather.sessionBuilder(),"Lacrosse,WI")
    weather.getNationalWeather(weather.sessionBuilder(),"Dallas","TX")
