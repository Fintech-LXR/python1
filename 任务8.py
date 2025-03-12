years = [str(year) for year in range(1001,3000) if year % 7 == 0 and year % 5 != 0]
for group in zip(*[iter(years)]*5):
    print('#'.join(group))