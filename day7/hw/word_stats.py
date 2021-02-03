from pprint import pprint
import string
from collections import Counter

with open('words.txt') as f:
    # list comprehension analogiczny do ponizszej petli for
    # lines = []
    # for line in f:
    #     stripped = line.strip()
    #     lines.append(stripped)
    lines = [line.strip() for line in f]
    words_sorted = Counter(lines).most_common()

    print(words_sorted[0])
    print(words_sorted[-1])
    the_longest = ''
    the_shortest = 'veryveryveryveryveryveryveryveryveryverylongword'
    characters = []

    for word in lines:
        characters.extend(list(word.lower()))
        if word.isalpha():
            if len(word) > len(the_longest):
                the_longest = word
            elif len(word) < len(the_shortest):
                the_shortest = word

    print(the_longest)
    print(the_shortest)

    vowels = 'aiouey'
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    special_chars_count = 0

    for char in characters:
        if char in vowels:
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1
        elif char.isdigit():
            digits_count += 1
        elif not char.isspace():
            special_chars_count += 1

    print(vowels_count)
    print(consonants_count)
    print(digits_count)
    print(special_chars_count)


