# Maxwell Enger
# Lab 4- Web-scraping Current Weather Conditions
# Date: 09/20/2019
# Description: The script web-scrapes the weather.gov website to extract current weather conditions for Missoula,MT.
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: Current Weather Conditions
#Time: 5 minutes

# Import required libraries to begin the web scarping process
import requests
from bs4 import BeautifulSoup

# Providing the latitude and longitude for inputted location
# Lat/lon in decimal degrees provided for Missoula, MT
lat = '46.872131'
lon = '-113.994019'

# Creating the url for the weather forecasting office in Missoula, MT through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat=46.872131&lon=-113.994019#.XYT8xkZKiHt'

# Check if the URL exists
print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate element on page to be scraped
# This element is located within an id tag called current_conditions-summary
# find() locates the element in the BeautifulSoup object
cur_weather_conditions = soup.find(id="current_conditions_detail")

# Extract text from the selected BeautifulSoup object using .text
cur_weather_conditions = cur_weather_conditions.text

# Final Output
# Return scraped information about Missoula, MT
print 'The Current Weather Conditions at '+ lat +  ", " + lon + " are:" + cur_weather_conditions
