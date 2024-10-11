import csv
import os
import smtplib
from tabulate import tabulate

from validators.validate_inputs import (
    get_phone_number,
    validate_email,
    get_category,
    shop_activity,
    get_date,
    get_store_name,
    get_location,
    get_description,
)


class Stores:
    def __init__(
        self,
        name,
        address,
        phone_number,
        email,
        owner,
        registration_date,
        shop_status,
        category,
        location,
        description,
    ):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.owner = owner
        self.registration_date = registration_date
        self.shop_status = shop_status
        self.category = category
        self.location = location
        self.description = description

    @classmethod
    def add_store(cls):
        name = get_store_name()
        address = input("Address: ")
        phone_number = get_phone_number()
        email = validate_email()
        owner = input("Owner: ")
        registration_date = get_date()
        shop_status = shop_activity()
        category = get_category()
        location = get_location()
        description = get_description()

        os.makedirs("shops/data", exist_ok=True)
        try:
            with open("shops/data/shops.csv", "a", newline='') as file:
                field_names = [
                    "Name",
                    "Address",
                    "Phone Number",
                    "Email",
                    "Owner",
                    "Registration Date",
                    "Shop Status",
                    "Category",
                    "Location",
                    "Description",
                ]
                writer = csv.DictWriter(file, fieldnames=field_names)
                if file.tell() == 0:
                     writer.writeheader()
                writer.writerow(
                    {
                        "Name": name,
                        "Address": address,
                        "Phone Number": phone_number,
                        "Email": email,
                        "Owner": owner,
                        "Registration Date": registration_date,
                        "Shop Status": shop_status,
                        "Category": category,
                        "Location": location,
                        "Description": description,
                    }
                )
                print(f"Shop name: {name} added successfully.")
                return name, email

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except PermissionError as e:
            print(f"Error: {e}")


    @classmethod
    def view_stores(cls):
        with open("shops/data/shops.csv") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            print(tabulate(data, headers="keys", tablefmt="fancy_grid"))