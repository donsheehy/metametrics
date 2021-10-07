# metametrics/metametrics/tests/test_config/timer.py

from time import time

def timer(test):
    def wrapper(*args,**kwargs):
        start = time()
        test(*args,**kwargs)
        end = time()
        print(f'Test: {test.__name__} Time: {(end-start):.4f}s')
        return
    return wrapper

