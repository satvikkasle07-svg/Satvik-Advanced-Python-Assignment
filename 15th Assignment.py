import gc
import time
import tracemalloc

class MemoryNode:
    def __init__(self, title):
        self.title = title
        self.link = None

def generate_circular_objects(total):
    for index in range(total):
        node1 = MemoryNode(f"Object A{index}")
        node2 = MemoryNode(f"Object B{index}")

        node1.link = node2
        node2.link = node1

def show_memory(info):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{info}")
    print(f"Current Memory: {current / 1024:.2f} KB")
    print(f"Peak Memory: {peak / 1024:.2f} KB")

tracemalloc.start()

print("Initial Garbage Collection Status:", gc.isenabled())

gc.disable()
print("\nAutomatic Garbage Collection Disabled")

generate_circular_objects(10000)

show_memory("\nBefore Manual Garbage Collection:")

print("Garbage Collection Counts:", gc.get_count())

start = time.perf_counter()
collected_objects = gc.collect()
end = time.perf_counter()

print("\nManual Garbage Collection Results")
print("Objects Collected:", collected_objects)
print("Time Taken:", end - start, "seconds")

show_memory("\nAfter Manual Garbage Collection:")

gc.enable()
print("\nAutomatic Garbage Collection Enabled:", gc.isenabled())

generate_circular_objects(10000)

show_memory("\nAfter Creating Objects with Automatic GC Enabled:")

start = time.perf_counter()
collected_objects = gc.collect()
end = time.perf_counter()

print("\nFinal Garbage Collection")
print("Objects Collected:", collected_objects)
print("Time Taken:", end - start, "seconds")

show_memory("\nFinal Memory Usage:")

tracemalloc.stop()
