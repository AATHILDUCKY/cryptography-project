import hashlib
import json

wordlist_file = "rockyou.txt"
output_file = "output.json"

hashed_words = []

with open(wordlist_file, "r") as file:
    for word in file:
        word = word.strip()
        md5_hash = hashlib.md5(word.encode()).hexdigest()
        hashed_words.append({"word": word, "md5": md5_hash})

with open(output_file, "w") as file:
    json.dump(hashed_words, file, indent=4)
