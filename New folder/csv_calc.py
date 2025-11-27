import csv
import os

FILE_PATH = 'products_builtin.csv'

product_data_with_header = [
    ['Product_Name', 'Price_USD', 'Quantity'],
    ['Laptop', 1200.50, 1],
    ['Monitor', 299.99, 2],
    ['Keyboard', 75.00, 5],
    ['Mouse', 25.50, 4],
    ['Webcam', 45.99, 1],
    ['Microphone', 129.00, 3]
]

def create_csv_file(data, path):
    try:
        with open(path, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

        print(f"✅ Created CSV file: '{path}' with {len(data) - 1}")

    except Exception as e:
        print(f"❌ Error during CSV creation: {e}")


def analyze_csv_data(path):
    if not os.path.exists(path):
        print(f'❌ File not found at: {path}. Cannot analyze.')


    row_count = 0
    grand_total = 0.0

    print(f'\n--- Analysis of "{path}"')
    try:
        with open(path, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            print(f"Header found: {header}")

            for row in reader:
                try:
                    product_name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])

                    row_total = price * quantity
                    grand_total += row_total
                    row_count +=1
                except (ValueError, IndexError) as e:
                    print(f"🚩 Skipping malformed row: {row}. Error: {e}")
        print(f"Total data rows counted (excluding header): {row}")
        print(f"The calculated grand total value is: ${grand_total}")
    except Exception as e:
        print(f"❌ An error occurred during data analysis: {e}")

if __name__ == "__main__":
    create_csv_file(product_data_with_header,FILE_PATH)