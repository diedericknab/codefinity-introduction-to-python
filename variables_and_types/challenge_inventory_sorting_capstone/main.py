items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slice items
candy1    = items[0:9]    # "Bubblegum"
candy2    = items[11:20]  # "Chocolate"
dry_goods = items[22:27]  # "Pasta"

# Slice categories
category1 = categories[0:11]   # "Candy Aisle"
category2 = categories[13:24]  # "Pasta Aisle"

# Price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price     = "$5.40"

# Print output
print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")