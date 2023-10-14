#nHash algorithm properties:
# 1. "Avalanche effect" - the tiniest change in incoming data changes the result completely
# 2. The possibility of each resulting checksum (hash) is the same to any other
# 3. You can not recreate the original contents from the checksum easily
# print(ord('t'))
def my_hash(key: str):
    factor_1 = len(key)
    factor_2 = sum(ord(symbol) for symbol in key)
    factor_3 = factor_1 = 1
    # print(key)
    result = int(factor_2*factor_2/factor_1)%100

    return result

print(my_hash("CB8535"))
print(my_hash("6EDDF91"))
print(my_hash("AA2A61E"))
print(my_hash("EDDF917D"))
print(my_hash("29BF04AA"))
print(my_hash("E125EE6E"))
print(my_hash("F917DB"))
print(my_hash("F917DC"))

