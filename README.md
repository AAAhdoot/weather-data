# weather-data

### Goals: 
Get weather data for list of locations in the United States.

### Input: CSV containing
* Location

### Output: CSV containing
* Location
* Temperature
* Wind Speed
* Weather Description

### Requirements
* Python 3

### Required external libraries
* requests

#### To install requests, you will need pip, and you can check the following link to determine how to install pip given your Operating System: https://www.makeuseof.com/tag/install-pip-for-python/

Once you have pip,  you should be able to install requests using the following command:

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
* Certain cities in locations.csv did not return information due to incorrectly spelled names (e.g. Clevland, BatonRouge, New Orlens, Talahassee)
* Only locations within the United States were requested, however due to incorrect data, certain non-US cities (e.g. Quebec) still return information because there exists a result with that city containing the US country code, while certain others (e.g. British Columbia) were succesfully ignored
* Temperature results are by default set to Kelvin, but were changed to Fahrenheit because U.S. locations are being requested
