# import csv
import pandas
#
# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temperatures.append(int(row[1]))
#
# 	print(temperatures)
#


data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])

# Get maximum temperature in a row
# print(data[data.temp == data.temp.min()])

# monday = data[data.day == "Monday"]
# Convert to Fahrenheit
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)



