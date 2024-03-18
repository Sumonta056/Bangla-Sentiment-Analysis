import string

# reading text file
text = open("input.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

stop_words = []
with open("stop_words.txt", "r", encoding="utf-8") as file:
    for line in file:
        stop_words.append(line.strip())

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

print(final_words)

