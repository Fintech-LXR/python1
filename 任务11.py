import time
import random
start_time = time.time()
a=[random.randint(1,10001)for _ in range (20)]
a.sort(reverse=True)
end_time = time.time()
elapsed_time = end_time - start_time
print(a)
print(f"运行时间:{elapsed_time:.6f}秒")