def is_all_digits_odd(number):
    return all(int(a) % 2 != 0 for a in str(number))        
result = [str(num) for num in range(1000,3001) if is_all_digits_odd(num)]
print("@".join(result))