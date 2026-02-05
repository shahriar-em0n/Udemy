# ingredients = ["water", "milk", "black tea"]
# ingredients.append("sugar")
# print(f"Ingredients are: {ingredients}")
# ingredients.remove("water")
# print(f"Ingredients are: {ingredients}")

# spice_options = ["ginger", "cardamom"]
# chai_ingredients = ["water", "milk"]

# chai_ingredients.extend(spice_options)
# print(f"chai: {chai_ingredients}")
# chai_ingredients.insert(2, "black tea")
# print(f"chai: {chai_ingredients}")

# last_added = chai_ingredients.pop()
# print(f"{last_added}")
# print(f"chai: {chai_ingredients}")
# chai_ingredients.reverse()
# print(f"chai: {chai_ingredients}")
# chai_ingredients.sort()
# print(f"chai: {chai_ingredients}")

# sugar_levels = [1, 2, 3, 4, 5]
# print(f"Maximum sugar level: {max(sugar_levels)}")
# print(f"Minimum sugar level: {min(sugar_levels)}")

# base_liquid = ["water", "milk"]
# extra_flavor = ["ginger"]

# full_liquid_mix = base_liquid + extra_flavor
# print(f"Liquid mix: {full_liquid_mix}")

# strong_brew = ["black tea", "water"] * 3
# print(f"String brew: {strong_brew}")

# raw_spice_data = bytearray(b"CINNAMON")
# raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
# print(f"Bytes: {raw_spice_data}")

carList = ["BMW", "Mercedis", "Toyota"]
carList.append("Lexus")
print(f"car list: {carList}")

carList.remove("Mercedis")
print(f"car list: {carList}")

option = ["Supra", "Ford"]
carList.extend(option)
print(f"car list: {carList}")

carList.insert(3, "BYD")
print(f"car list: {carList}")

last_added = carList.pop()
print(f"car list: {last_added}")
print(f"car list: {carList}")

# index pop
last_added = carList.pop(3)
print(f"car list: {last_added}")
print(f"car list: {carList}")

carList.reverse()
print(f"Revers Car list: {carList}")

carList.sort()
print(f"Sort Car list: {carList}")


car_rating = [1, 2, 3, 4, 5]
print(f"Maximum Car Rating: {max(car_rating)}")
print(f"Minimum Car Rating: {min(car_rating)}")

car_type = ["Electric", "Fuel"]
car_color = ["Red", "White"]

full_Discription = car_type + car_color
print(f"Full Car Dis: {full_Discription}")

new_data = bytearray(b"Nissan")
print(f"new data: {new_data}")


print(carList)

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

exitsting_item = ["ketchup", "apples", "bananas", "milk", "bread"]
new_item = ["rice", "butter"]

exitsting_item.extend(new_item)
print(exitsting_item)

exitsting_item.sort()
print(exitsting_item)

# কাজগুলো যা করতে হবে:

# গrocery list তৈরি করা:

# একটি তালিকা তৈরি করতে হবে যার নাম my_cart এবং এতে "apples", "bananas", এবং "milk" থাকবে।

# তালিকা প্রিন্ট করা:

# আপনার তৈরি করা my_cart তালিকাটি প্রিন্ট করতে হবে।

# নতুন আইটেম যোগ করা:

# তালিকার শেষে "bread" আইটেম যোগ করতে হবে।

# তালিকা আপডেট প্রিন্ট করা:

# তালিকার আপডেট হওয়া ভার্সনটি আবার প্রিন্ট করতে হবে।

# তালিকার শুরুতে আইটেম যোগ করা:

# "ketchup" আইটেমটি তালিকার শুরুতে যোগ করতে হবে।

# আরও তালিকা আপডেট প্রিন্ট করা:

# আবার তালিকা প্রিন্ট করতে হবে।

# একটি আইটেম মুছে ফেলা:

# "bananas" আইটেমটি তালিকা থেকে মুছে ফেলতে হবে।

# তালিকা থেকে শেষের আইটেম মুছে ফেলা:

# তালিকার শেষের আইটেমটি মুছে ফেলে সেটি একটি নতুন ভেরিয়েবলে রাখা হবে, যার নাম হবে removed_item।

# মুছে ফেলা আইটেম প্রিন্ট করা:

# removed_item ভেরিয়েবলের মান প্রিন্ট করতে হবে, যা শেষের আইটেম হবে।

# তালিকায় নতুন আইটেম যোগ করা:

# "rice" এবং "butter" আইটেম দুটি তালিকায় যোগ করতে হবে।

# তালিকা সাজানো:

# তালিকাটি অ্যালফাবেটিক্যাল (বর্ণমালায়) ক্রমে সাজাতে হবে।

# তালিকার উল্টো করা:

# তালিকার আইটেমগুলোর অর্ডার উল্টো করতে হবে।

# তালিকা মার্জ করা:

# আরেকটি তালিকা (যার মধ্যে "juice" এবং "juice" থাকবে) যোগ করে দুটি তালিকা মার্জ করতে হবে।

# তালিকা দু'বার পুনরাবৃত্তি করা:

# একই তালিকাটি দুটি বার পুনরাবৃত্তি করে একটিভাবে প্রিন্ট করতে হবে।

# একটি স্ট্রিংকে তালিকায় রূপান্তর করা:

my_cart = ["apples", "bananas", "milk"]
print(my_cart)

my_cart.append("bread")
print(my_cart)

my_cart.insert(0, "ketchup")
print(my_cart)

removed_item = my_cart.pop()
print(removed_item)

new_items = ["rice", "butter"]
my_cart.extend(new_items)
print(my_cart)

my_cart.sort()
print(my_cart)
my_cart.reverse()
print(my_cart)

additional_items = ["juice", "jam"]
my_cart = my_cart + additional_items
print(my_cart)

print(my_cart * 3)

string = "tomato cucumber spinach"
converted_list = string.split()
print(converted_list)
