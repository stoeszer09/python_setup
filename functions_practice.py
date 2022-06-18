def hello():
  print("Greetings and salutations!")

def pack(item_1, item_2, item_3):
  return [item_1, item_2, item_3]

def eat_lunch(food_list):
  if len(not len(food_list)):
    print("My lunchbox is empty!")
  else:
    print(f"First I eat {food_list[0]}")
    for i in range(1,len(food_list)):
      print(f"Next I eat {food_list[i]}")

hello()
pack('shirt', 'shorts', 'shoes')
eat_lunch(['apple', 'bananas', 'pizza'])