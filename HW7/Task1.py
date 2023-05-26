def FindRhyme(poem):
    phrases = poem.split()
    consonantLetters = []
    for phrase in phrases:
        sum = 0
        for letter in phrase:
            if letter.lower() in "аиеёоуы":
                sum += 1
        consonantLetters.append(sum)
    if len(set(consonantLetters)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")


print("Enter poem")
poem = input()

FindRhyme(poem)
