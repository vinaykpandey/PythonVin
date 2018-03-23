'''
def <func-name> (fargs, *args, **kwargs):
    <statements>
 fargs => fomral argument
 args => variable argument
 kwargs => keyworded variable argument
'''

def get_data(engine, *queries, **properties):
     print(engine, queries, properties)


get_data('google', 'python', 'flask', 'django', limit=10, offset=0,)
