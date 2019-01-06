import re


def address(path):
    def wrapper(func):
        def wrap_func(*args, **kwargs):
            request = args[0]
            match_object = re.search(r'GET\s\/(\w+)|POST\s\/(\w+)', request).groups()
            print(match_object[0])
            if path == match_object[0]:
                func(*args, **kwargs)
            elif 'POST' in request:
                match1 = re.search(r'(?=.*(POST\s/(\w+)))(?=.*firstname=(\w+)&lastname=(\w+))', request)
                data = {'firstname': match1.group(3), 'lastname': match1.group(4)}
                print(data)
            else:
                kwargs['match'] = False
                func(*args, **kwargs)

        return wrap_func
    return wrapper






