#Exercise 10
print('<<Death Calculator>>');
print();
cigarettes = int(input('How many cigarettes do you smoke a day: '));
lost = cigarettes * 10;
print();
years = float(input('How many years have you been smoking: '));
days = years * 365;
print();
print(f'You lost {int((lost * days) / 1440)} days of life');
