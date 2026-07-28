#Sales and profit analysis
import datetime
#used datetime for proper date validation, date comparison, and date-range-based sales analysis. It also helps future scalability for analytics and ML forecasting


# Initialize an empty list to store sales records
sales_data = []

def add_sale():
    """Gets sale details from the user and stores them."""

    product_name = input("Enter product name: ")
    category = input("Enter product category: ")
    supplier_name = input("Enter supplier name: ")
    product_sku = input("Enter product SKU: ")
    #Stock Keeping unit: Unique alphanumeric code that retailers and bussinesses assign to track stock levels .

    location_of_sale = input("Enter location of sale (Store/Online): ")
    customer_name = input("Enter customer name: ")

    # Cost Price
    while True:
        try:
            cost_price = float(input("Enter cost price (₹): "))
            if cost_price >= 0:
                break
            else:
                print("Cost price cannot be negative.")
        except ValueError:
            print("Invalid input. Enter a number.")

    # Selling Price
    while True:
        try:
            selling_price = float(input("Enter selling price (₹): "))
            if selling_price >= 0:
                break
            else:
                print("Selling price cannot be negative.")
        except ValueError:
            print("Invalid input. Enter a number.")

    # Quantity Sold
    while True:
        try:
            quantity_sold = int(input("Enter quantity sold: "))
            if quantity_sold >= 0:
                break
            else:
                print("Quantity cannot be negative.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    # Sale Date
    while True:
        try:
            sale_date_str = input("Enter sale date (YYYY-MM-DD): ")
            sale_date = datetime.datetime.strptime(
                sale_date_str,
                "%Y-%m-%d"
            ).date()
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    # Discount
    while True:
        try:
            discount = float(
                input("Enter discount percentage (0-100): ")
            )

            if 0 <= discount <= 100:
                break
            else:
                print("Discount must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")

    # Sales Tax
    while True:
        try:
            sales_tax = float(
                input("Enter sales tax percentage (0-100): ")
            )

            if 0 <= sales_tax <= 100:
                break
            else:
                print("Sales tax must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")

    payment_method = input(
        "Enter payment method (Cash/Card/UPI): "
    )

    # Store record
    sales_data.append({
        "Product": product_name,
        "Category": category,
        "Supplier": supplier_name,
        "SKU": product_sku,
        "Location": location_of_sale,
        "Customer": customer_name,
        "CP": cost_price,
        "SP": selling_price,
        "Quantity": quantity_sold,
        "Date": sale_date,
        "Discount (%)": discount,
        "Sales Tax (%)": sales_tax,
        "Payment Method": payment_method
    })

    print("\nSale record added successfully!\n")


def calculate_profit_loss():
    """Calculates and displays overall profit/loss."""

    if not sales_data:
        print("No sales data available.\n")
        return

    total_cost = 0
    total_revenue = 0

    for sale in sales_data:

        total_cost += sale["CP"] * sale["Quantity"]

        sale_revenue = (
            sale["SP"] * sale["Quantity"]
        ) * (1 - sale["Discount (%)"] / 100)

        # Add tax
        sale_revenue += (
            sale_revenue * sale["Sales Tax (%)"] / 100
        )

        total_revenue += sale_revenue

    total_profit = total_revenue - total_cost

    print("\n----- Overall Summary -----")
    print(f"Total Cost: ₹{total_cost:.2f}")
    print(f"Total Revenue: ₹{total_revenue:.2f}")

    if total_profit > 0:
        print(f"Overall Profit: ₹{total_profit:.2f}")

    elif total_profit < 0:
        print(f"Overall Loss: ₹{abs(total_profit):.2f}")

    else:
        print("Break-even (No profit, no loss)")


def analyze_by_product():
    """Analyzes sales data for a specific product."""

    search_product = input(
        "Enter product name to analyze: "
    )

    product_data = [
        sale for sale in sales_data
        if sale["Product"].lower() == search_product.lower()
    ]

    if not product_data:
        print("No sales data found.\n")
        return

    total_quantity_sold = sum(
        sale["Quantity"] for sale in product_data
    )

    total_revenue = 0
    total_profit = 0

    for sale in product_data:

        sale_revenue = (
            sale["SP"] * sale["Quantity"]
        ) * (1 - sale["Discount (%)"] / 100)

        sale_revenue += (
            sale_revenue * sale["Sales Tax (%)"] / 100
        )

        total_revenue += sale_revenue

        profit = (
            sale_revenue -
            (sale["CP"] * sale["Quantity"])
        )

        total_profit += profit

    print("\n----- Product Summary -----")
    print(f"Total Quantity Sold: {total_quantity_sold}")
    print(f"Total Revenue: ₹{total_revenue:.2f}")
    print(f"Total Profit: ₹{total_profit:.2f}")


def analyze_by_category():
    """Analyzes sales data for a category."""

    search_category = input(
        "Enter category to analyze: "
    )

    category_data = [
        sale for sale in sales_data
        if sale["Category"].lower() == search_category.lower()
    ]

    if not category_data:
        print("No category data found.\n")
        return

    total_quantity_sold = sum(
        sale["Quantity"] for sale in category_data
    )

    total_revenue = 0
    total_profit = 0

    for sale in category_data:

        sale_revenue = (
            sale["SP"] * sale["Quantity"]
        ) * (1 - sale["Discount (%)"] / 100)

        sale_revenue += (
            sale_revenue * sale["Sales Tax (%)"] / 100
        )

        total_revenue += sale_revenue

        profit = (
            sale_revenue -
            (sale["CP"] * sale["Quantity"])
        )

        total_profit += profit

    print("\n----- Category Summary -----")
    print(f"Total Quantity Sold: {total_quantity_sold}")
    print(f"Total Revenue: ₹{total_revenue:.2f}")
    print(f"Total Profit: ₹{total_profit:.2f}")


def analyze_by_date_range():
    """Analyzes sales within a date range."""

    while True:
        try:
            start_date_str = input(
                "Enter start date (YYYY-MM-DD): "
            )

            end_date_str = input(
                "Enter end date (YYYY-MM-DD): "
            )

            start_date = datetime.datetime.strptime(
                start_date_str,
                "%Y-%m-%d"
            ).date()

            end_date = datetime.datetime.strptime(
                end_date_str,
                "%Y-%m-%d"
            ).date()

            break

        except ValueError:
            print("Invalid date format.")

    date_range_data = [
        sale for sale in sales_data
        if start_date <= sale["Date"] <= end_date
    ]

    if not date_range_data:
        print("No data found in this date range.\n")
        return

    total_quantity_sold = sum(
        sale["Quantity"] for sale in date_range_data
    )

    total_revenue = 0
    total_profit = 0

    for sale in date_range_data:

        sale_revenue = (
            sale["SP"] * sale["Quantity"]
        ) * (1 - sale["Discount (%)"] / 100)

        sale_revenue += (
            sale_revenue * sale["Sales Tax (%)"] / 100
        )

        total_revenue += sale_revenue

        profit = (
            sale_revenue -
            (sale["CP"] * sale["Quantity"])
        )

        total_profit += profit

    print("\n----- Date Range Summary -----")
    print(f"Total Quantity Sold: {total_quantity_sold}")
    print(f"Total Revenue: ₹{total_revenue:.2f}")
    print(f"Total Profit: ₹{total_profit:.2f}")


def main():

    while True:

        print("\n===== Store Sales & Profit Analysis =====")
        print("1. Add Sale Record")
        print("2. Calculate Overall Profit/Loss")
        print("3. Analyze by Product")
        print("4. Analyze by Category")
        print("5. Analyze by Date Range")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale()

        elif choice == "2":
            calculate_profit_loss()

        elif choice == "3":
            analyze_by_product()

        elif choice == "4":
            analyze_by_category()

        elif choice == "5":
            analyze_by_date_range()

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()