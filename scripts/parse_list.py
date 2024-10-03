#filters original list of scrabble words found online
word_list = open("../assets/scrabble_words_org.txt", "r")
unparsed_words = (word_list.read()).split("\n")

parsed_words = open("../assets/words.txt", "w")

for word in unparsed_words:
    if(len(word)>3):
        parsed_words.write(word+"\n")

parsed_words.close()
