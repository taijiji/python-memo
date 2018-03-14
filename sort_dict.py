from pprint import pprint
d = {
    	'A' : 10,
    	'B' : 50,
    	'C' : 40,
}


print(sorted(d)) # ['A', 'B', 'C']
print(sorted(d, key=d.get)) # ['A', 'C', 'B']
print(sorted(d, key=d.get, reverse=True)) # ['B', 'C', 'A']

l = [
		{
			'id'		: 'A',
			'keyword'	: 10,
		},
		{
			'id'		: 'B',
			'keyword'	: 50,
		},
		{
			'id'		: 'C',
			'keyword'	: 40,
		},
]
pprint(sorted(l, key=lambda x:x['keyword'], reverse=True))
'''
[{'id': 'B', 'keyword': 50},
 {'id': 'C', 'keyword': 40},
 {'id': 'A', 'keyword': 10}]
'''
