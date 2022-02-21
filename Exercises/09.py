#Exercise 09
print('<<Rental Car Python for Zombies>>');
print();
km = float(input('What is the number of km traveled by your rental car: '));
km = km * 0.15;
print();
days = int(input('How many days was your car rented: '));
days = days * 60;
print();
print(f'RESULT: You must pay R${(days + km):.2f}');
