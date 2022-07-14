print('yes');

name = 'john';
age=25;
new_patient= False;

if(new_patient):
    print("patient name is ",name,"age is ", age," he is new patient");
else:
    print("patient name is ",name,"age is ", age," he is an old patient");


# name=input('what is your name? ');
# color=input('what is your fav color? ');
# print(name + ' likes ' + color);

# pound=input('what is your weight in pounds? ');
# print(int(pound)*0.453592);



#strings

str='python learning curve';
copy=str[:];  
temp=str[1:-1]; #print from y to v
print(copy," ",temp); 


multipleLine = '''
yes sir

no isr

thank you rolex
'''

print(multipleLine);



#formatted  strings
first = 'naveen'
last='sundar'
temp = f'{first} [{last}] is a footballer'
print(temp);

#string methods
print(len(first));
print(first.upper());
print(first.lower());
print(last.find('k'));
print(last.replace('r','rarajan'));
print(first.lstrip());

#arithmetic operators
# + -- addition
# - -- subtraction
# / -- return floting number
# // -- returns whole number
# % -- modulus
# * -- multiplication
# ** -- exponential


#if else

price = 1000000;
credit = False;

if credit:
    print('down payemnt must be', price*0.10);
else : 
    print('down payment must be ', price*0.20);
    
#logical operators
# and
# or
# not
# have to use string of values for logical operators   


#weight convertor program

# weight=input('enter your weight');
# range = input('L for (lbs) and k for (kg)?');

# if(range.lower()=='l'):
#     print(f'your weight in kg is {int(weight)*0.45}');
# else :
#     print(f'your weight in lbs is {int(weight)//0.45}');

#guessing game
temp = 6;
i=0;
while temp!='9' and i!=3:
    temp=input('guess');
    i+=1;
if(temp=='9'):
    print('you won');
else:
    print('you lost, only 3 chances');

