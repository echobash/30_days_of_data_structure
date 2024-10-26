#key = "march 6"
def get_hash(key):
    sum = 0
    for char in key:
        sum += ord(char)
    return sum%100 # 100 is the size of array. So we want indices from 0 to 9 that's why we did sum%10

print(get_hash("march 6"))