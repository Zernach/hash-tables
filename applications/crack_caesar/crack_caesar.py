"""
Use frequency analysis to find the key to ciphertext.txt, and then
decode it.
"""

# For checking if something is punctuation
import string
# For sorting a dictionary
import operator

# Dict of letters of overall frequency used in written English.
english_frequencies = {
    'E': 11.53,
    'T': 9.75,
    'A': 8.46,
    'O': 8.08,
    'H': 7.71,
    'N': 6.73,
    'R': 6.29,
    'I': 5.84,
    'S': 5.56,
    'D': 4.74,
    'L': 3.92,
    'W': 3.08,
    'U': 2.59,
    'G': 2.48,
    'F': 2.42,
    'B': 2.19,
    'M': 2.18,
    'Y': 2.02,
    'C': 1.58,
    'P': 1.08,
    'K': 0.84,
    'V': 0.59,
    'Q': 0.17,
    'J': 0.07,
    'X': 0.07,
    'Z': 0.03
}

# Dict used for counting frequency of letters in ciphertext file
freq = {}

with open('ciphertext.txt') as ciphertext:

    for char in ciphertext:

        # Don't count if it's punctuation.
        if char in string.punctuation:
                continue
        # If letter is already in freq, +1 the count...
        try:
            freq[char] += 1
        # ...or else create letter count within freq dict.
        except:
            freq[char] = 1 

# Count how many items have been counted in total.
sum = 0
for char in freq:
    sum += freq[char]

# Convert counts-of-freq to ratio-of-freq...
for char in freq:
    freq[char] = freq[char] / sum * 100

# Sort the dict
freq_sorted = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

# 
freq_sorted
for i in range(0, len(freq_sorted)):
    english_frequencies[i]
    if freq_sorted[i] in string.punctuation:
        continue