from memory_profiler import profile


@profile
def function():
    x = [i for i in range(1000000)]  # Memory allocation
    del x  # Freeing memory


function()
