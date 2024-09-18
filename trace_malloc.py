import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

# Code to monitor memory usage
x = [i for i in range(1000000)]

# Get the current memory usage
snapshot = tracemalloc.take_snapshot()
print(snapshot)

# Display memory statistics
for stat in snapshot.statistics('lineno')[:10]:
    print(stat)
