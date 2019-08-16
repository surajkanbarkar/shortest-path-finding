edges = [('Mysore', 'Mandya', 66),
('Mysore', 'Chennapatna', 28),
('Mysore', 'Nanjangud', 60),
('Mysore', 'Bandipur', 34),
('Mysore', 'Nagarhole', 34),
('Mysore', 'Somnathpur', 3),
('Mysore', 'Bylakuppe', 108),
('Mandya', 'Chennapatna', 22),
('Mandya', 'Nanjangud', 12),
('Mandya', 'Bandipur', 91),
('Mandya', 'Nagarhole', 121),
('Mandya', 'Somnathpur', 111),
('Mandya', 'Bylakuppe', 71),
('Chennapatna', 'Nanjangud', 39),
('Chennapatna', 'Bandipur', 113),
('Chennapatna', 'Nagarhole', 130),
('Chennapatna', 'Somnathpur', 35),
('Chennapatna', 'Bylakuppe', 40),
('Nanjangud', 'Bandipur', 63),
('Nanjangud', 'Nagarhole', 21),
('Nanjangud', 'Somnathpur', 57),
('Nanjangud', 'Bylakuppe', 83),
('Bandipur', 'Nagarhole', 9),
('Bandipur', 'Somnathpur', 50),
('Bandipur', 'Bylakuppe', 60),
('Nagarhole', 'Somnathpur', 27),
('Nagarhole', 'Bylakuppe', 81),
('Somnathpur', 'Bylakuppe', 90)]

cities = []
for i,j,d in edges:
    cities.append(i)
    cities.append(j)
    
cities = list(set(cities))
print(cities)
mappers = dict()

for i,j,d in edges:
    mappers[i + 'to' + j] = d
    mappers[j + 'to' + i] = d
print(mappers)
combinations = []
l_path =None
l_dis = None

for ind, i in enumerate(cities):
    dis = 0
    s = i + '-->'
    for j in cities:
        if i == j:
            continue
        dis +=  mappers[i+ 'to'+ j]
        s = s + j + '-->'
    combinations.append((s, dis))
    if ind == 0:
        l_path = s
        l_dis = dis
    if dis < l_dis:
        l_dis = dis
        l_path = s
        
print(combinations)

print(l_path, l_dis)
