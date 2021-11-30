dictionary=dict()
dictionary={'one':1,'two':2,'three':3,'four':4,'five':5}
print(dictionary)

print(dictionary.keys())

print(dictionary.values())

print(dictionary.items())

print(dictionary['one']) #O(1)

dictionary['six']=6 #O(1)
print(dictionary)

