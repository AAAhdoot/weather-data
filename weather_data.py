import sys
import json
import requests

def read_and_write(file,output_file,errors_file):
	output_file.write("Location,Temperature,Wind Speed,Weather Description")
	errors_file.write("Location")
	file.readline()
	for line in file:	
		url = "http://api.openweathermap.org/data/2.5/weather?q={},US&APPID=????????????&units=imperial".format(line.strip())
		response = requests.get(url)
		json_data = json.loads(response.text)
		if json_data['cod'] == 200:
			if validate(json_data['id'],json_data['name']) == True:
				output_file.write("\n{},{},{},{}".format(json_data['name'], json_data['main']['temp'], json_data['wind']['speed'], json_data['weather'][0]['description']))
			else:
		 		errors_file.write("\n{}".format(json_data['name']))
		else:
			errors_file.write("\n{}".format(line.strip()))

def validate(id,name):
	url = "http://api.openweathermap.org/data/2.5/weather?id={}&APPID=046bd27d3183cf3d21c91fb02eb86f4f".format(id);
	response = requests.get(url)
	json_data = json.loads(response.text)
	if name != json_data['name']:
		return False
	else:
		return True

if __name__ == '__main__':
	try:
		filename = sys.argv[1]
		file = open(filename,"r")
		output_file = open("output_file.csv","w")
		errors_file = open("errors_file.csv","w")
		read_and_write(file,output_file,errors_file)
	except Exception as e:
		print(e)
	else:
		file.close()
		output_file.close()
		errors_file.close()
