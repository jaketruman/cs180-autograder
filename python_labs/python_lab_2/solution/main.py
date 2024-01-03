import json
import string
import argparse
import os

def main(inputString):
    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"
    noPString = inputString.translate(str.maketrans('', '', string.punctuation)) # Removes all punctuation
    noCString = noPString.lower() # Makes everything lowercase
    words = noCString.split() # Splits string into separate words
    dict = {}

    # if the word exists in the key, add 1 to the value, otherwise instantiate it as 1
    for word in words:
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1

    # open filename to write the dictionary as a json
    with open("word-counts.json", "w") as f:
        json.dump(dict, f)

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
    