import csv


def get_name():
    with open("shops/data/shops.csv", "r") as file:
        reader = csv.DictReader(file)
        names = [row["Name"] for row in reader]
        while True:
            name = input("Name: ")
            if name in names:
                print("Shop already exists.")
            else:
                return name


get_name()