from shops import stores
from validators.email_shop import email_confirmation
import argparse

def main():
    parser = argparse.ArgumentParser(description="Store Management System")
    parser.add_argument("--add", help="Add a store", action="store_true")
    parser.add_argument("--view", help="View stores", action="store_true")
    args = parser.parse_args()

    if args.add:
        store_name, store_email = stores.Stores.add_store()
        email_confirmation(store_name, store_email)

    elif args.view:
        stores.Stores.view_stores()
    else:
        print("Please specify an option")
        print("Use --help for more information")


if __name__ == '__main__':
    main()