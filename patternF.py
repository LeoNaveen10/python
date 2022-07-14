let = [5,2,5,2,2];

for item in let:
        print('*' * item);
        
for item in let:
    temp=""
    while(item):
        temp+='$';
        item-=1;
    print(temp);

        