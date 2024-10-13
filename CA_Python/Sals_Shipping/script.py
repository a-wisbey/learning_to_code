# Ask the user to input their package weight
# For testing purposes, using a fixed weight of 41.5
package_weight = 41.5

# Ground shipping cost calculation
if package_weight <= 2:
    g_price_per_lb = 1.50
elif package_weight <= 6:
    g_price_per_lb = 3.00
elif package_weight <= 10:
    g_price_per_lb = 4.00
elif package_weight > 10:
    g_price_per_lb = 4.75
else:
    print("Error")
    g_price_per_lb = 0  # Default value in case of an error

ground_shipping = g_price_per_lb * package_weight + 20

# Corrected print statement for ground shipping
print(f"Ground shipping fee: \n£{ground_shipping:.2f}\n")

# Premium ground shipping cost
cost_premium_ground_shipping = 125.00

# Print the premium ground shipping fee for the user
print(f"Premium ground shipping fee: \n£{cost_premium_ground_shipping:.2f}\n")

# Drone shipping cost calculation
if package_weight <= 2:
    d_price_per_lb = 4.50
elif package_weight <= 6:
    d_price_per_lb = 9.00
elif package_weight <= 10:
    d_price_per_lb = 12.00
elif package_weight > 10:
    d_price_per_lb = 14.25
else:
    print("Error")
    d_price_per_lb = 0  # Default value in case of an error

drone_shipping_cost = package_weight * d_price_per_lb

# Print the drone shipping fee
print(f"Drone shipping fee: \n£{drone_shipping_cost:.2f}\n")

# Calculate which method of shipping is cheapest
# Find the cheapest shipping option
cheapest_cost = min(ground_shipping, cost_premium_ground_shipping, drone_shipping_cost)

# Tell the user which shipping cost is cheapest
if cheapest_cost == ground_shipping:
    print("Ground shipping is the cheapest option.")
elif cheapest_cost == cost_premium_ground_shipping:
    print("Premium ground shipping is the cheapest option.")
elif cheapest_cost == drone_shipping_cost:
    print("Drone shipping is the cheapest option.")
else:
    print("Error in determining the cheapest shipping method.")

