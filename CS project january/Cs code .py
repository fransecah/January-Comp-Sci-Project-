import csv
import statistics
import matplotlib.pyplot as plt

# Open the CSV file
file = open("ProjectData.csv", "r")  # Open CSV file
csvReader = csv.reader(file)

# Set up lists for rainfall and crash data
lrRain = []
lrCrash = []
lrCountries = []

# Loop through file and add data to lists, skipping header row
next(csvReader)  # Skips the header row

for row in csvReader:
    try:
        # Attempt to convert values to integers and add them to lists
        country = str(row[0])
        rain_value = int(row[1])  # Assuming the second column is rainfall data for 2018
        crash_value = (int(row[2]))/100  # Assuming the third column is crash data for 2019

        lrRain.append(rain_value)
    
        lrCrash.append(crash_value)
   
        lrCountries.append(country)

    except ValueError:
        # Handle cases where data is not valid or cannot be converted to int
        print(f"Skipping invalid data row: {row}")

file.close()

# Ensure there's data before calculating statistics
if len(lrRain) == 0 or len(lrCrash) == 0:
    print("Error: No valid data found for analysis.")
else:
    # Find mode of rainfall data
    try:
        modRain = statistics.mode(lrRain)  # Mode for rainfall
        print("Mode of rainfall:", modRain)
    except statistics.StatisticsError:
        print("Error: Multiple modes found for rainfall data.")

    # Find mode of crashes data
    try:
        modCrash = statistics.mode(lrCrash)  # Mode for crashes
        print("Mode of crashes:", modCrash)
    except statistics.StatisticsError:
        print("Error: Multiple modes found for crash data.")

    # Find mean of rainfall data
    meanRain = statistics.mean(lrRain)  # Mean for rainfall
    print("Mean of rainfall:", round(meanRain, 2))

    # Find mean of crashes data
    meanCrash = statistics.mean(lrCrash)  # Mean for crashes
    print("Mean of crashes:", round(meanCrash, 2))

    # Find median of rainfall data
    medRain = statistics.median(lrRain)  # Median for rainfall
    print("Median of rainfall:", medRain)

    # Find median of crashes data
    medCrash = statistics.median(lrCrash)  # Median for crashes
    print("Median of crashes:", medCrash)
    
print(lrRain)
print(lrCountries)
print(lrCrash)


plt.plot(lrCountries, lrRain)
plt.plot(lrCrash)

plt.title("Connection between traffic accidents and the weather")
plt.xlabel("Countries")
plt.ylabel("Annual Rainfall 2017 / Number of Crashes in 2017")
plt.legend(["Annual Rainfall 2017 (mm)"," Number of Crashes in 2017 (00')"])
# Adding grid for better readability
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()
