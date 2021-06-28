from disfunctools import *

dict_drop(
    dict(name='A', cost=20),
    'name'
)
# {'cost': 20}
merge_dicts(
    dict(name='A', cost=20),
    dict(type='X')
)

{'name': 'A', 'cost': 20, 'type': 'X'}