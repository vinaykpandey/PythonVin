'''
def <func-name> (fargs, *args, **kwargs):
    <statements>
 fargs => fomral argument
 args => variable argument
 kwargs => keyworded variable argument
'''

def get_data(engine, *queries, **properties):
     print('fomral argument, fargs: ',engine)
     print('variable argument, *args: ',queries)
     print ('keyworded variable argument, **kwargs: ',properties)


get_data('google', 'python', 'flask', 'django, REST API', limit=10, offset=0,)
