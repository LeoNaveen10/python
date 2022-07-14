
try:
    x= int(input('enter number'));
    print(123//x);
    print(x);
except ZeroDivisionError:
    print('divisor should not be zero');
except ValueError:
    print('it should be number');