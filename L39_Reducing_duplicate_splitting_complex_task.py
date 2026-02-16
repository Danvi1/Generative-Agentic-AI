# Task1 reducing Duplication
import asyncio


def print_order(name, chai_type):
    print(f"Hello {name} you have ordered : {chai_type} chai!")

print_order("Dhanvith", "Masala")
print_order("Prashanth", "Normal")
print_order("Ashboy", "Kanna")
print_order("nikde", "Ginger")


#Task2 Splitting Complex Tasks
def fetch_sales(outlet):
    print(f"Fetching the sales Data of {outlet}...")

def filter_valid_sales(outlet):
    print(f"Filtering valid sales of {outlet}...")

def summarize_data(outlet):
    print(f"Summarizing data of {outlet}...")

def generate_report(outlet):
    fetch_sales(outlet)
    filter_valid_sales(outlet)
    summarize_data(outlet)
    print("Report is ready")

generate_report("outlet1")
generate_report("outlet2")
generate_report("outlet3")

