with open('./day1.txt', 'r')as f:
    data = f.read().strip().split('\n')

f = []

for i in data:
    l = [c for c in i if c.isnumeric()]
    l = [l[0], l[-1]]
    f.append(int(''.join(l)))

print(f"part 1: {sum(f)}")

#inp = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
#inp = ["eighthree"]

def calculate_word_values(line):
    word_values = [
        (index % 9) + 1
        for start_index in range(len(line))
        for index, word in enumerate("one two three four five six seven eight nine 1 2 3 4 5 6 7 8 9".split())
        if line[start_index:start_index + len(word)] == word
    ]
    return word_values

total_sum = 0
for line in data:
    word_values = calculate_word_values(line)
    total_sum += word_values[0] * 10 + word_values[-1]

print(f"part 2: {total_sum}")

