def update_dictionary(d, key, value):
    
    d[int(key)*2] = ['Ivan', 'Masha', 'Sasha']
    x = []
    x = d[int(key)*2]
    x.append('valuHUYe')
    d[int(key)*2] = x


d = {}
print(update_dictionary(d, 1, -1))
print(d) 
