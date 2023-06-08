import argparse
import csv
import os
import json




def read_customers_csv():
    csv_file_path = "input_data/starter/transactions"
    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("File not found. Please check the file path.")

    except csv.Error as e:
        print(f"CSV error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


def read_products_csv():
    csv_file_path = "input_data/starter/customers.csv"
    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("File not found. Please check the file path.")

    except csv.Error as e:
        print(f"CSV error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

def read_transactions_json():
    root_directory = "input_data/starter/products.csv"

    # Traverse through the directory structure
    for root, directories, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.json'):
                # Construct the file path
                file_path = os.path.join(root, file)

                # Read the JSON file
                with open(file_path, 'r') as json_file:
                    try:
                        # Parse the JSON data
                        json_data = json.loads(json_file.readline())

                        # Process the JSON data
                        # Example: Print the contents of the JSON file
                        print(json_data)
                        customer_count = {}

                        # Count the occurrences of each customer ID
                        customer_id = json_data['customer_id']
                        if customer_id in customer_count:
                            customer_count[customer_id] += 1
                        else:
                            customer_count[customer_id] = 1

                        # Print the count of each customer ID
                        for customer_id, count in customer_count.items():
                           print(f"Customer ID: {customer_id}, Purchase  Count: {count}")
                    except json.JSONDecodeError as e:
                        print(f"Error reading JSON file: {file_path}")
                        print(f"Error message: {str(e)}")

                    except Exception as e:
                        print(f"An error occurred: {str(e)}")

def output_json():
    #taken some saple records from each file.

    product_data = [
        ['P39', 'detergent', 'house'],
        ['P35', 'kitchen roll', 'house'],
        ['P32', 'bin liners', 'house'],
        # ... and so on
    ]

    customer_data = [
        ['C1', '7'],
        ['C2', '4'],
        ['C3', '8'],
        # ... and so on
    ]

    purchase_data = [
        {'customer_id': 'C1', 'basket': [{'product_id': 'P39', 'price': 147}],
         'date_of_purchase': '2018-12-01 11:43:00'},
        {'customer_id': 'C3', 'basket': [{'product_id': 'P35', 'price': 1579}],
         'date_of_purchase': '2018-12-02 16:55:00'},
        {'customer_id': 'C3', 'basket': [{'product_id': 'P32', 'price': 1978}],
         'date_of_purchase': '2018-12-03 04:08:00'},
        # ... and so on
    ]


# Prepare data for JSON file
    json_data = []

    try:
        for purchase in purchase_data:
            customer_id = purchase['customer_id']
            basket = purchase['basket']
            date_of_purchase = purchase['date_of_purchase']

            for item in basket:
                product_id = item['product_id']
                price = item['price']

                for customer in customer_data:
                    if customer[0] == customer_id:
                        loyalty_score = customer[1]
                        break

                for product in product_data:
                    if product[0] == product_id:
                        product_category = product[2]
                        break

                json_data.append({
                    'customer_id': customer_id,
                    'loyalty_score': loyalty_score,
                    'product_id': product_id,
                    'product_category': product_category,
                    'purchase_count': 1,
                })

        # Write data to JSON file
        with open('output file/data.json', 'w') as file:
            json.dump(json_data, file, indent=4)

    except KeyError as e:
        print(f"KeyError occurred: {str(e)}")
        # Handle the KeyError exception, such as skipping the current purchase or logging the error.

    except FileNotFoundError:
        print("File not found. Please check the file path.")
        # Handle the FileNotFoundError exception, such as displaying an error message or exiting the program.

    except json.JSONDecodeError as e:
        print(f"JSONDecodeError occurred: {str(e)}")
        # Handle the JSONDecodeError exception, such as skipping the current file or logging the error.

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Handle other general exceptions, such as displaying an error message or performing error recovery steps.


def main():
    read_products_csv()
    read_customers_csv()
    read_transactions_json()
    output_json()


if __name__ == "__main__":
    main()
