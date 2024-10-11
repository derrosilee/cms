from datetime import date
import re
import csv

def get_store_name():
    with open("shops/data/shops.csv", "r") as file:
        reader = csv.DictReader(file)
        names = [row["Name"] for row in reader]

    while True:
        shop_name = input("Shop name: ").title()
        if shop_name in names:
            print("Shop name already exists.")
            continue
        if len(shop_name) < 4:
            print("Shop name must be at least 4 characters long.")
        elif len(shop_name) > 50:
            print("Shop name must not exceed 50 characters.")
        else:
            return shop_name


def get_phone_number():
    try:
        return int(input("Phone number: "))
    except ValueError:
        print("Please enter a valid phone number.")
        return get_phone_number()


def validate_email():
    while True:
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        email = input("Email: ").lower()
        email_pattern = email_pattern.match(email) is not None
        if email_pattern:
            return email
        else:
            print("Please enter a valid email.")


def get_category():
    categories = (
        "Fashion",
        "Electronics",
        "Food",
        "Health",
        "Beauty",
        "Home",
        "Sports",
        "Kids",
        "Books",
        "Others",
    )
    while True:
        category = input("Category: ").title()
        if category not in categories:
            print("Please enter a valid category.")

            print(f"Valid categories are: {categories}")
        else:
            return category


def shop_activity():
    while True:
        status = input("Shop status: ").title()
        if status not in ("Active", "Inactive"):
            print("Please enter a valid status.")
            print("Valid statuses are: [Active, Inactive]")
        else:
            return status


def get_date():
    while True:
        current_date = date.today()
        current_date = str(current_date)
        user_date = input("Enter a date (YYYY-MM-DD): ")
        if user_date != current_date:
            print("Invalid date")
            print(f"Current date is: {current_date}")
        else:
            return user_date


def get_location():
    counties = ("Nairobi", "Mombasa", "Kisumu")
    while True:
        location = input("Location: ").title()
        if location not in counties:
            print("Please enter a valid location.")
            print(f"Valid locations are: {counties}")
        else:
            return location


def get_description():
    while True:
        description = input("Description: ")
        if len(description) < 10:
            print("Description must be at least 10 characters long.")
        elif len(description) > 200:
            print("Description must not exceed 200 characters.")
        else:
            return description


