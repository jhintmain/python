'''
n → n / 2 (n이 짝수일 때)
n → 3 n + 1 (n이 홀수일 때)
'''

def hailstone_sequence(n, seq):
    if n == 1:
        return seq

    if n % 2 == 0:
        return hailstone_sequence(n / 2, seq + 1)
    else:
        return hailstone_sequence(3*n + 1, seq + 1)

hailstone_sequences = [0]

for n in range(1, 1_000_000):
    hailstone_sequences.append(hailstone_sequence(n, 0))

max_sequence = max(hailstone_sequences)
print(hailstone_sequences.index(max_sequence))