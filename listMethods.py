

# append() -- adds Element to the end
# pop() -- remove from end
# arr2=arr1.copy() -- copy one list to another
# 50 in arr  -- in operator give boolean if present or not
# arr.index(4) - gives the index of no:4  in list
# arr.sort()  -- sort the list
# arr.reverse() - reverse the list
# arr.count(3) -- returns  the no of 3's present in the list
# arr.clear() -- clears the list
# ar.remove(num) -- removes the particular num from the list


# exercise to remove the duplicate no from the list
arr = [1,2,3,1,2];
arr.sort();
i=0;

# while i<len(arr):
#     if arr[i]==arr[i+1]:
#        arr.remove(arr[i]);  
#     else: 
#         i+=1;

# print(arr);
     
uniques =[];
for number in arr:
    if number not in uniques:
        uniques.append(number);
print(uniques);