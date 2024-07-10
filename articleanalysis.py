text=input("Input the string you want to Enter : ")
letters=[]
text=text.lower()
letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the second letter: ").lower())
letters.append(input("Enter the third letter: ").lower())

print("\n")
print("LETTER REPETITION")

letter_repetition1=text.count(letters[0])
letter_repetition2=text.count(letters[1])
letter_repetition3=text.count(letters[2])

print(f"We have found the letter '{letters[0]}' repeated {letter_repetition1} times")
print(f"We have found the letter '{letters[1]}' repeated {letter_repetition2} times")
print(f"We have found the letter '{letters[2]}' repeated {letter_repetition3} times")

print("\n")
print("NUMBER OF WORDS")

words=text.split()
print(f"We have found {len(words)} in the entered text")

print("\n")
print("INVERTEd")

words.reverse()
inverted_text=' '.join(words)
print(f"The inverted text is : {inverted_text}")

print("\n")
print("LOOKING FOR WORD PYTHON")

is_python='python' in text
dic={True: "is found", False:"isn't found"}
print(f"Python {dic[is_python]}")
