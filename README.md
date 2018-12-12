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

### Notes before running
* Make sure that your locations file (e.g. locations.csv) is located in the same directory as weather_data.py
* API key should be inserted instead of "???????????????" on line 9 of weather_data.py prior to running program 

### Running the program
To run (assuming your locations are located in a csv file named "locations.csv"):
```
python weather_data.py locations.csv
```
### Notes about results
* the results will be located in a csv file named "output_file.csv"
* Certain cities in locations.csv did not return information due to incorrectly spelled names (e.g. Clevland, BatonRouge, New Orlens, Talahassee)
* Only locations within the United States were requested, however due to incorrect data, certain non-US cities (e.g. Quebec) still return information because there exists a result with that city containing the US country code, while certain others (e.g. British Columbia) were succesfully ignored
