import sys
import itertools
import bisect

def valid_combinations(words_list, letters):
    valid_words=set()
    
    for i in range(1, len(letters)+1):
        for j in itertools.product(letters, repeat=i):
            #create combination of word
            word=''.join(j)

            n=bisect.bisect_left(words_list, word)
            if n<len(words_list) and words_list[n]==word:
                valid_words.add(word)

    return sorted(valid_words)

words_file = open("../assets/words.txt", "r")
words_list = (words_file.read()).split("\n")
output = open("../assets/output.txt", "w")

letters = sys.argv[1]

valid_words=valid_combinations(words_list, letters)
for word in valid_words:
    output.write(word+"\n")

output.close()