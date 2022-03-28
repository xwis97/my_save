
def update_dictionary(d,  key, value):
    if d.get(key) == None:
        if d.get(int(key)*2) == None:
            d[int(key)*2] += value
    
    else:
        print(d)
         
        
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}




'''
    if d.get(key) != '':
        d[key] += str(value)

'''