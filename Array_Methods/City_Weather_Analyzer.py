# ------------------------------------------------------------
# Program: City Weather Analyzer 
# Author: Aviram Dhagat
# Description:
#   This script processes weather data for multiple cities.
#   It prints min, avg, and max temperatures for each city,
#   identifies the cities with the overall min and max temps,
#   and collects cities with min temps above 30°C.
#
#   Example Output:
#     Mumbai's Min temp is 28
#     Mumbai's Avg temp is 30
#     Mumbai's Max temp is 32
#     ...
#     City with min temp is: Bangalore
#     Min temp is: 25
#     City with max temp is: Delhi
#     Max temp is: 33
#     Cities with min temp > 30: ['Delhi', 'Chennai', 'Hyderabad']
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Define weather data for each city
#   Format: {City: [Min, Avg, Max]}
# ------------------------------------------------------------
weather = [
    {'Mumbai': [28, 30, 32]},
    {'Delhi': [33, 36, 39]},
    {'Chennai': [31, 34, 37]},
    {'Kolkata': [29, 32, 35]},
    {'Bangalore': [25, 27, 29]},
    {'Hyderabad': [30, 33, 36]}
]

# ------------------------------------------------------------
# Step 2: Initialize tracking variables
# ------------------------------------------------------------
min_temp = float('inf')     # Track lowest min temp
max_temp = float('-inf')    # Track highest min temp
min_city = ''               # City with lowest min temp
max_city = ''               # City with highest min temp
city_list = []              # Cities with min temp > 30
avg_temp_city = {}          # Dictionary to store city → avg temp

# ------------------------------------------------------------
# Step 3: Process each city's weather data
# ------------------------------------------------------------
for city_data in weather:
    for city, temps in city_data.items():
        print(f"{city}'s Min temp is {temps[0]}")
        print(f"{city}'s Avg temp is {temps[1]}")
        print(f"{city}'s Max temp is {temps[2]}")

        avg_temp_city[city] = temps[1]  # Store average temp

        # Update city with lowest min temp
        if temps[0] < min_temp:
            min_temp = temps[0]
            min_city = city

        # Update city with highest min temp
        if temps[0] > max_temp:
            max_temp = temps[0]
            max_city = city

        # Collect cities with min temp > 30°C
        if temps[0] > 30:
            city_list.append(city)

# ------------------------------------------------------------
# Step 4: Print summary results
# ------------------------------------------------------------
print(f'City with min temp is: {min_city}')
print(f'Min temp is: {min_temp}')

print(f'City with max temp is: {max_city}')
print(f'Max temp is: {max_temp}')

# Print cities with min temp > 30°C
for i in city_list:
    print(i)

# Print dictionary of average temperatures
print(avg_temp_city)
