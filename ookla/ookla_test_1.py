import csv


# field names
fields = ["Name", "Branch", "Year", "CGPA"]

# data rows of csv file
rows = [
    ["Nikhilddd", "COE", "2", "9.0"],
    ["Sanchitddd", "COE", "2", "9.1"],
    ["Aditya", "IT", "2", "9.3"],
    ["Sagar", "SE", "1", "9.5"],
    ["Prateek", "MCE", "3", "7.8"],
    ["Sahil", "EP", "2", "9.1"],
]

with open("GFG.csv", "w") as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(rows)

rows_ = [
    ["Nikhilddd", "COE", "2", "9.0"],
]

rows_ = [
    ["Mitsos", "COF", "2", "9.0"],
]

with open("GFG.csv", "a") as file:
    write = csv.writer(file)
    write.writerows(rows_)
