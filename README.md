# weather-data

### Goals: 
Get weather data for list of locations in the United States.

### Input: CSV containing
* Location

### Output: 

##### output_file.csv, containing
* Location
* Temperature
* Wind Speed
* Weather Description

##### errors_file.csv, containing
* Locations for which no result was found
* Locations which do not exist in the United States

### Requirements
* Python 3 (https://www.python.org/downloads/)

### Required external libraries
* requests

#### To install requests, you will need pip, and you can check the following link to determine how to install pip given your Operating System: https://www.makeuseof.com/tag/install-pip-for-python/

Once you have pip,  you should be able to install requests using the following command in your terminal/python interpreter:

```
pip install requests 
```
For more information or alternative options, check out https://www.pythonforbeginners.com/requests/using-requests-in-python

### Notes before running
* Make sure that your locations file (e.g. locations.csv) is located in the same directory as weather_data.py
* API key should be inserted instead of "???????????????" on line 9 of weather_data.py prior to running program 

### Running the program
To run (assuming your locations are located in a csv file named "locations.csv"):
```
python3 weather_data.py locations.csv
```
### Notes about results
* The results will be located in a csv file named "output_file.csv"
* Certain cities in locations.csv did not return information due to incorrectly spelled names (e.g. Clevland, BatonRouge, New Orlens, Talahassee), and non-US locations were similarly ignored (e.g. British Columbia).
* Our validate() function takes the 'id' and 'name' attributes from the json response and using an API call made with the 'id' instead of the location name, verifies whether the 'id' refers to the correct name. This allowed us to weed out non-US locations that are for some reason connected to a U.S. location (e.g. Quebec), as well as U.S. locations that do not refer to the cities they claim to refer to.
* Temperature results are by default set to Kelvin, but were changed to Fahrenheit because U.S. locations are being requested
