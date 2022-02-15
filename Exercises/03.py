#Exercise 03
print('<<Second Calculator>>');
print();
day = int(input('Enter the number of days: '));
day = (day * 86400);
print();
hour = int(input('Enter the number of hours: '));
hour = (hour * 3600);
print();
minute = int(input('Enter the number of minutes: '));
minute = (minute * 60);
print();
second = int(input('Enter the number of seconds: '));
print();
print(f'RESULT: The sum of all values is {day + hour + minute + second} seconds');
