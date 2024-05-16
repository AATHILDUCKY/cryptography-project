import hashlib
import json
import os

# Define the pattern for the input wordlist files
input_files = [f"small_rockyou_{str(i).zfill(2)}" for i in range(1, 73)]

for wordlist_file in input_files:
    output_file = f"{wordlist_file}.json"
    hashed_words = []

    # Read the wordlist file and compute MD5 hashes
    with open(wordlist_file, "r") as file:
        for word in file:
            word = word.strip()
            md5_hash = hashlib.md5(word.encode()).hexdigest()
            hashed_words.append({"word": word, "md5": md5_hash})

    # Write the hashed words to the JSON output file
    with open(output_file, "w") as file:
        json.dump(hashed_words, file, indent=4)

print("Processing complete!")
