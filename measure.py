import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        # this measures start time
        start_time = time.time()  
        # execute the function and store the result in variable
        result = func(*args, **kwargs)  
        # end time
        end_time = time.time() 
        # difference in time for the start and end time
        # or this simply calculates how long the function takes time to execute
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.2f} seconds")
        return result
    return wrapper

@measure_time
def heavy_function():
    print("Starting function...")
    # delay 3 seconds for function to complete
    time.sleep(3)
    print("Finished function!")
    
    
heavy_function()
