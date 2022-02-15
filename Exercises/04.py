#Exercise 04
print('<<Salary Increase>>');
print();
salary = float(input('Enter your salary: '));
print();
percent = int(input('Enter the percentage increase: '));
increase = (percent * salary) / 100;
print();
print(f'RESULT: With the {percent}%(+{increase:.2f}) increase, your salary went from {salary:.2f} to {(salary + increase):.2f}');
