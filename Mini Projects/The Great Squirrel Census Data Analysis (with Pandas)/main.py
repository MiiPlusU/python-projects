import csv
import pandas

'''
with open("weather_data.csv") as file:
    new_file = file.readlines()
    print(new_file)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(data["temp"].max())
# print(data["temp"].mean())

#Get Data in Columns
# print(data["condition"])
# print(data.condition) #attribute has to be a capital c

#Get Data in Rows
# print(data[data.day == "Monday"])
# data.temp.max()
# print(data[data.temp==max(data.temp)])
# monday = data[data.day=="Monday"]
# monday_temp_F = (int(monday.temp)*9/5)+32
# print(monday_temp_F)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
'''


data = pandas.read_csv("C:/Users/sesay/OneDrive/Desktop/Python-Projects/Mini Projects/The Great Squirrel Census Data Analysis (with Pandas)/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])

my_dict = {
    "Fur Color" : ["Black","Red","Gray"],
    "count" : [black_count,red_count,gray_count]
}

df = pandas.DataFrame(my_dict)
df.to_csv("Squirrel_Count.csv")