
# Given a string, count the number of times a letter occurs
example_string = "The  quick brown fox jumps over the lazy dog"

# remove spaces and throw it all in a list 
string_list = example_string.split()
giant_string = "".join(string_list)

letter_counts = {}

# iterate over giant_string
for letter in giant_string:
    letter = letter.lower()
# check if letter in dict, 
    if letter in letter_counts:
    # if it is, increment count, 
        letter_counts[letter] += 1
    # if not add,
    else:
        letter_counts[letter] = 1

# print(letter_counts)

# Print each letter, starting with the most common, down to least common
# sort based on key’s count 
sorted_letter_counts = sorted(letter_counts.items(), key=lambda pair: pair[1], reverse=True)
for pair in sorted_letter_counts:
    print(pair[0])


# import operator
# sorted = sorted(letter_counts.items(), key=operator.itemgetter(1), reverse=True)