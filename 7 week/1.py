import time

def time_decorator(func):
    def wrapper():
        start_time = time.time()      
        result = func()                
        end_time = time.time()        
        elapsed_time = round(end_time - start_time) 
        print(elapsed_time)           
        return result               
    return wrapper
