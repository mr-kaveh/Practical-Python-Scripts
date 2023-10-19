# Here's a more complex Python code example that defines a function with default argument values 
# to generate a customizable report for a list of sales transactions.

def generate_sales_report(sales_data, start_date=None, end_date=None, threshold=1000):
    """
    Generate a sales report based on specified criteria.

    :param sales_data: List of sales transactions.
    :param start_date: Start date for filtering transactions (default is None).
    :param end_date: End date for filtering transactions (default is None).
    :param threshold: Sales amount threshold for including transactions (default is 1000).
    :return: A filtered sales report.
    """
    filtered_sales = []
    for transaction in sales_data:
        date, amount = transaction
        if start_date and date < start_date:
            continue
        if end_date and date > end_date:
            continue
        if amount >= threshold:
            filtered_sales.append((date, amount))
    
    return filtered_sales

# Sample sales data
sales_data = [
    ("2023-01-05", 1500),
    ("2023-01-10", 800),
    ("2023-01-15", 1200),
    ("2023-02-02", 750),
    ("2023-02-10", 2000),
    ("2023-03-01", 950),
]

# Generate sales report with default arguments
default_report = generate_sales_report(sales_data)
print("Default Sales Report:")
print(default_report)

# Generate a custom sales report with date and threshold filters
custom_report = generate_sales_report(sales_data, start_date="2023-01-10", end_date="2023-02-20", threshold=1000)
print("\nCustom Sales Report:")
print(custom_report)
