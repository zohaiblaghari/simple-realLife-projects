item_names = []
quantities = []
prices = []

num_items = int(input("Enter the number of items on your shopping list:"))

for i in range(num_items):
    item_names.append(input(f"Enter the name of item {i + 1}:"))
    quantities.append(int(input(f"Enter the quantity of {item_names[i]}:")))
    prices.append(float(input(f"Enter the prices per {item_names[i]}:")))

total_cost = sum(quantities[i]*prices[i]for i in range(num_items))

budget = float(input("Enter your budget:"))
enough_budget = budget >= total_cost

print("\nShopping List:")
for i in range(num_items):
    print(f"{item_names[i]}-Quantity:{quantities[i]},Price:${prices[i]:.2f}")

print("\nTotal Cost:","${:.2f}".format(total_cost))
print("Budget is enough:", enough_budget)