import csv, json

PATH_CSV = "products.csv"
PATH_JSON = "sales.json"


def create_csv_file(file_path):
    products = [
        {'product_id': 1, 'product_name': 'Product A'},
        {'product_id': 2, 'product_name': 'Product B'},
        {'product_id': 3, 'product_name': 'Product C'}
    ]
    fieldnames = ['product_id', 'product_name']
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)


def create_json_file(file_path):
    sales = [
        {"sale_id": 1, "product_id": 1, "amount": 10},
        {"sale_id": 2, "product_id": 2, "amount": 20},
        {"sale_id": 3, "product_id": 3, "amount": 30}
    ]
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(sales, file, ensure_ascii=False, indent=4)


def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def read_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)
    

def match_data(products, sales):
    products_dict = {int(product['product_id']): product['product_name'] for product in products}
    matched_sales = []
    for sale in sales:
        product_id = sale['product_id']
        if product_id in products_dict:
            matched_sales.append({
                'product_name': products_dict[product_id],
                'amount': sale['amount']
            })
    return matched_sales


def print_result(matched_sales):
    print("Product Name | Amount")
    print("-----------------------")
    for item in matched_sales:
        print(f"{item['product_name']} | {item['amount']}")


def main():
    csv_file = PATH_CSV
    json_file = PATH_JSON
    products_data = read_csv(csv_file)
    sales_data = read_json(json_file)
    result = match_data(products_data, sales_data)
    print_result(result)


create_csv_file(PATH_CSV)
create_json_file(PATH_JSON)
print(main())