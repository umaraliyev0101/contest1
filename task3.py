import time

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"The function call executed in {execution_time:.4f} sec")
        return result
    return wrapper