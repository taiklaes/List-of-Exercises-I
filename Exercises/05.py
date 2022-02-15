#Exercise 05
print('<<Supermarket Python for Zombies>>');
print();
price = float(input('Enter the product price: '));
print();
percent = int(input('Enter the discount: '));
discount = (percent * price) / 100;
print();
print(f'RESULT: With the {percent}% discount (-{discount:.2f}), the product now costs {(price - discount):.2f}');
