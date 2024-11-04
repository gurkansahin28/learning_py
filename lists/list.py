# a list or array in python
fruits = ['apple', 'banana', 'cherry', 'lemmon', 'orange']
print(fruits)

# the length of the list
flength = len(fruits)
print(flength)

# printing all items of the list
for item in fruits:
    print(item)
    
# printing all letters of the list item
for item in fruits[0]:
    print(item)
    
# breking to print accırding to the conditional
for item in fruits:
    print(item)
    if item == 'cherry':
        print(f"Breaking: because {item} was caught as 'cherry'...")
        break
        
for item in fruits:
    if item == 'lemmon':
        print(f"Continuing: item was caugth as {item}.")
        continue
    else:
        print(item)
