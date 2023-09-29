from cs50 import get_string
# TODO

text = ''
words = 1
letters = 0
sentences = 0

while text == '':
    text = get_string("Text: ")

text = text.lower()


for c in text:
    if c == ' ':
        words += 1
    if c.isalpha() == True:
        letters += 1
    if c == '!' or c == '?' or c == '.':
        sentences += 1


L = 100.0 * letters / words
S = 100.0 * sentences / words

grade = 0.0588 * L - 0.296 * S - 15.8
# print(grade)
# print(L)
# print(S)

if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Before Grade 16+")
else:
    print(f"Grade {round(grade)}")