import time
def find_pythagorean_triplets(s):
    triplets = []
    for a in range(1, s):
        for b in range(a, s - a):
            c = s - a - b
            if a**2 + b**2 == c**2:
                triplets.append((a, b, c))
    return triplets
start_time = time.time()
s = 1000
triplets = find_pythagorean_triplets(s)
end_time = time.time()
elapsed_time = end_time - start_time
if triplets:
    print("满足条件的组合有：")
    for triplet in triplets:
        print(f"a = {triplet[0]}, b = {triplet[1]}, c = {triplet[2]}")
else:
    print("没有找到满足条件的组合。")
print(f"运行时间:{elapsed_time:.6f}秒")