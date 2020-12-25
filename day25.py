input_string = '''5764801
17807724'''

pkey1, pkey2 = map(int, input_string.split('\n'))

n = 1
i = 0
while n != pkey1:
    n *= 7
    n %= 20201227
    i += 1

enc_key = 1
for _ in range(i):
    enc_key *= pkey2
    enc_key %= 20201227

print(enc_key)
