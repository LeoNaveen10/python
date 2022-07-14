# dictinories are same as objects in javaScripts which holds key value pair




oldDict = {
    "name" : "lionel messi",
    "age" : 89,
    "country" : 'argentina'
}

#get we can send default value if it not present in the dict like get(key,default_value)
# if the key is present it brings the origianl_value otherwise it gives default_value
print(oldDict.get("name"));


dict = {
    '1' : "one",
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
     '9' : 'nine'
}

x=input('enter the number to get alphabets');
ans = "";
for num in x:
    ans+=dict.get(num)+ " ";
print(ans);


emoji = {
    ':)' : '😔',
    ':(' : '😀'
}
words = input('enter the messsage');
word = words.split(' ');
newans=' ';
for x in word:
    newans+= emoji.get(x,x);
    
print(newans);