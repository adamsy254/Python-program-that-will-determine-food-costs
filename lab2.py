# Program Name: Lab2.py
# Whatsapp +254702896107
# Student Name: Adams muema
# Assignment Number: Lab 2
# Gmail. adamsmuema19@gail.com
# Purpose: This program calculates the food costs for the KSU CCSE hackathon using a GUI.
#          It allows users to input the number of pizza and salad orders and calculates
#          the total cost, applying discounts and a delivery charge.
# Specific Resources Used: Python documentation, course notes.

import tkinter as tk
from tkinter import messagebox

# Constants for pricing and configurations
PIZZA_PRICE = 15.99               # Cost of one pizza
SALAD_PRICE = 7.99                # Cost of one salad
PIZZA_SLICES_PER_PIZZA = 12       # Number of slices in one pizza
PIZZA_SLICES_PER_PERSON = 3       # Number of slices allocated per person
DELIVERY_CHARGE_PERCENT = 0.07    # Delivery charge as a percentage of total cost
MIN_DELIVERY_CHARGE = 20.0        # Minimum delivery charge
DISCOUNT_THRESHOLD = 10           # Threshold for discounts
DISCOUNT_RATE = 0.15              # Discount rate (15%)

# Function to calculate the costs and display results
def calculate_costs():
    """
    This function calculates the total cost of the order, including discounts and delivery charges,
    and displays the results in the GUI.
    """
    try:
        # Get user inputs
        pizza_orders = int(pizza_input.get())  # Number of people ordering pizza
        salad_orders = int(salad_input.get())  # Number of people ordering salads

        # Calculate the number of pizzas needed
        total_slices = pizza_orders * PIZZA_SLICES_PER_PERSON
        pizzas_needed = -(-total_slices // PIZZA_SLICES_PER_PIZZA)  # Ceiling division to get whole pizzas

        # Calculate initial costs before discounts
        pizza_cost = pizzas_needed * PIZZA_PRICE
        salad_cost = salad_orders * SALAD_PRICE
        total_cost = pizza_cost + salad_cost

        # Calculate discounts
        pizza_discount = pizza_cost * DISCOUNT_RATE if pizzas_needed > DISCOUNT_THRESHOLD else 0
        salad_discount = salad_cost * DISCOUNT_RATE if salad_orders > DISCOUNT_THRESHOLD else 0
        total_discount = pizza_discount + salad_discount

        # Calculate the delivery charge
        delivery_charge = max(total_cost * DELIVERY_CHARGE_PERCENT, MIN_DELIVERY_CHARGE)

        # Calculate the final total amount due
        total_due = total_cost - total_discount + delivery_charge

        # Display the results in the results label
        results.set(
            f"Pizzas ordered: {pizzas_needed}\n"
            f"Pizza cost: {pizza_cost}\n"
            f"Salad cost: {salad_cost}\n"
            f"Total (before discounts): {total_cost}\n"
            f"Discount: -{total_discount}\n"
            f"Delivery charge: {delivery_charge}\n"
            f"Total amount due: {total_due}"
        )
    except ValueError:
        # Display an error message if the user inputs invalid data
        messagebox.showerror("Input Error", "Please enter valid numbers for pizza and salad orders.")

# Create the main GUI window
root = tk.Tk()
root.title("KSU CCSE Hackathon Food Cost Calculator")

# Input fields for the number of pizza and salad orders
tk.Label(root, text="Number of Pizza Orders:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
pizza_input = tk.Entry(root)  # Input field for pizza orders
pizza_input.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Salad Orders:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
salad_input = tk.Entry(root)  # Input field for salad orders
salad_input.grid(row=1, column=1, padx=10, pady=5)

# Button to calculate the costs
calculate_button = tk.Button(root, text="Calculate", command=calculate_costs)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the results
results = tk.StringVar()  # Variable to hold the results text
tk.Label(root, textvariable=results, justify="left", anchor="w").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
