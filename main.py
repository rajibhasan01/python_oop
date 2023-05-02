# import csv

# class Item:
#     pay_rate = 0.8 # The pay rate after 20% discount
#     all = [];
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)


#     def calculate_total_price(self):
#         return self.price * self.quantity;


#     def apply_discount(self):
#         self.price = self.price * self.pay_rate;


#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv', 'r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)

#         for item in items:
#             Item(
#                 name=item.get('name'),
#                 price=float(item.get('price')),
#                 quantity=int(item.get('quantity'))
#             )

#     @staticmethod
#     def is_integer(num):
#         # We will count out the floats that are pont zero
#         # For i.e: 5.0, 10.0
#         if isinstance(num, float):
#             # Count out the floats that are point zero
#             return num.is_integer()

#         elif isinstance(num, int):
#             return True

#         else:
#             return False


#     def __repr__(self) -> str:
#         return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})";




# item = Item("Phone", 100, 5);

# item2 = Item("Laptop", 200, 2);

# item.apply_discount();

# item2.pay_rate = 0.7;
# item2.apply_discount();

# total = item.calculate_total_price();
# total2 = item2.calculate_total_price();


# print(total);
# print(total2);

# print(Item.__dict__); # All the attributes for Class level
# print(item2.__dict__); # All the attributes for instance level


# item1 = Item("Phone", 100, 1);
# item2 = Item("Laptop", 1000, 3);
# item3 = Item("Cable", 10, 5);
# item4 = Item("Mouse", 50, 5);
# item5 = Item("Keyboard", 75, 5);


# for instance in Item.all:
#     print(instance.name);

# print(Item.all);
# Item.instantiate_from_csv();
# print(Item.all)

# print(Item.is_integer(5.00))



# class Phone(Item):
#     def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
#         # Call to super function to have access to all attributes / methods
#         super().__init__(
#             name, price, quantity
#         )

#         # Run validations to the received arguments
#         assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than zero!";

#         # Assign to self object
#         self.broken_phones = broken_phones;



# phone1 = Phone("jscPhonev10", 500, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20", 700, 5, 1)

# print(Item.all)
# print(Phone.all)


from item import Item
from phone import Phone

Item.instantiate_from_csv();
print(Item.all)

item1 = Item("MyItemistooLong", 750)
item1.name = 'otherItem'
print(item1.name)

# item1.price = 500;
print(item1.price);

item1.apply_increment(0.5);
item1.apply_discount()

print(item1.price)
