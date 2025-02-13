def typeBasedTransformer(**kwargs):
    for key, val in kwargs.items():
        if type(val) == int or type(val) == float:
            val = val**2
        elif type(val) == str:
            val = val[::-1]
        elif type(val) == bool:
            val = not val
        elif type(val) == list:
            val = val[::-1]
        elif type(val) == tuple:
            val = val[::-1]
        elif type(val) == dict:
            val = {v:k for k,v in val.items()}
        else:
            pass
