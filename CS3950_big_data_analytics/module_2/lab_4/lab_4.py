"""Lab 4: Pandas Module"""

import pandas as pd
import numpy as np

# Write a Pandas program to create and display a one-dimensional array-like
# object containing an array of data using Pandas module.

data = [1, 2, 3, 4, 1, 2, 3, 4]
s1 = pd.Series(data)
print(f"One-dimensional array-like object: {s1}")

# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])
addition = series1 + series2
print(f"Addition: {addition}")
subtraction = series1 - series2
print(f"Subtraction: {subtraction}")
multiplication = series1 * series2
print(f"Multiplication: {multiplication}")
division = series1 / series2
print(f"Division: {division}")
# Import the Automobile dataset.
try:
    # I have to do conda install xlrd to read the Excel file.
    df = pd.read_excel("Lab 4 - Automobile.xls", engine="xlrd")
except FileNotFoundError:
    print("File not found.")
    # break the program
    exit()
# From the given dataset print the first and last five rows.
print(f"First five rows: {df.head()}")
print(f"Last five rows: {df.tail()}")
# Clean the dataset and update the CSV file by removing any records that have?, n.a, or NaN.
df.replace(["?", "n.a"], pd.NA, inplace=True)
df.dropna(inplace=True)
df.to_csv("cleaned_automobile.csv", index=False)

print(f"Updated dataset: {df}")
# Find and print the most expensive car showing the price and company name.
df["price"] = pd.to_numeric(df["price"], errors="coerce")
most_expensive_car = df.loc[df["price"].idxmax()]
print("Most expensive car:\n", most_expensive_car[["company", "price"]])

# Print All Toyota Cars details
toyota_cars = df[df["company"] == "toyota"]
print("All Toyota cars:\n", toyota_cars)
# Count total cars per company
total_cars_per_company = df["company"].value_counts()
print("Total cars per company:\n", total_cars_per_company)
# Find each company’s highest priced car.
highest_priced_car_per_company = df.loc[df.groupby("company")["price"].idxmax()]
print("Highest priced car per company:\n", highest_priced_car_per_company)
# Find the average mileage of each car making company.
df["average-mileage"] = pd.to_numeric(df["average-mileage"], errors="coerce")
average_mileage = df.groupby("company")["average-mileage"].mean()
print(round(average_mileage, 2))
# Sort all cars by the price column.
sorted_cars = df.sort_values(by="price", ascending=False)
print(sorted_cars)

# Concatenate two data frames using the following two dictionaries:
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995,
# 135925 , 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995,
# 23600, 61500 , 58900]}
german_cars = pd.DataFrame(
    {
        "Company": ["Ford", "Mercedes", "BMV", "Audi"],
        "Price": [23845, 171995, 135925, 71400],
    }
)
japanese_cars = pd.DataFrame(
    {
        "Company": ["Toyota", "Honda", "Nissan", "Mitsubishi"],
        "Price": [29995, 23600, 61500, 58900],
    }
)
concatenated_df = pd.concat([german_cars, japanese_cars], ignore_index=True)
print(concatenated_df)

# Create two data frames using the following two Dicts. Merge two data frames,
# and append the second data frame as a new column to the first data frame.
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925
# , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80,
# 182 , 160]}

car_price = pd.DataFrame(
    {
        "Company": ["Toyota", "Honda", "BMV", "Audi"],
        "Price": [23845, 17995, 135925, 71400],
    }
)
car_horsepower = pd.DataFrame(
    {
        "Company": ["Toyota", "Honda", "BMV", "Audi"],
        "horsepower": [141, 80, 182, 160],
    }
)

merged_df = pd.merge(car_price, car_horsepower, on="Company")
print(merged_df)