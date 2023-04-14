# Steven Sousa - Python Bootcamp - Day 2 - 1-26-23

# This program calculates the total of a tab with tip

tab = float(input("What was the total of the tab without tip? "))

people_count = int(input("How many people are splitting this bill? "))
while people_count <= 0:
    print("Sorry, but the bill must be paid by at least 1 person.")
    people_count = int(input("How many people are splitting this bill? "))

tip_percentage = int(input("What percentage tip would you like to give? "))/100

tab_split = tab/people_count
tab_split_percentage = tab_split * tip_percentage
tab_split_total = tab_split + tab_split_percentage

print("Each person will pay $", tab_split_total)
