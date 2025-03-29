import time
import random
start_time = time.time()
a=[random.randint(1,30000000)for _ in range (20000000)]
a.sort(reverse=True)
end_time = time.time()
elapsed_time = end_time - start_time
print(a)
print(f"运行时间:{elapsed_time:.6f}秒")