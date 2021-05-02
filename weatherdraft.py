#A Python program to check the weather
#Brian Majurinen
#CIS245 May 2, 2021
import requests, json
#welcome message
print("Welcome to the weather program")
#weather function that builds the api call
def weatherStart():
    apiKey = "57116fd23a5b7fdae70715d1ebfbb412"

    baseUrl = "http://api.openweathermap.org/data/2.5/weather?zip="

    zipCode = input("Enter the zip code to search: ")
    #the entire api call
    wholeUrl = baseUrl + zipCode + ",us&appid=" + apiKey

    response = requests.get(wholeUrl)

    x = response.json()
#This function is borrowed code. I am not quite sure how it works yet
def weatherPrint(weatherStart):
    if x["cod"] == "404":
        print("Zip code not found")
    else:
        y = x["main"]
        currentTemperature = y["temp"]
        currentPressure = y["pressure"]
        currentHumidity = y["humidity"]
        z = x["weather"]
        weatherDescription = z[0]["description"]
        print(" Temperature =" + str(currentTemperature) +
        "/n atmospheric temperature = " + str(currentPressure) +
        "/n humidity = " + str(currentHumidity) + 
        "/n description = " + str(weatherDescription))
#This is a function to let the user rerun the program
def rerun():
    input("Would you like to run the program again? y/n ")
    while input == "y":
        weatherStart()
    else:
        print("Thank you for using the program")

weatherStart()
rerun
