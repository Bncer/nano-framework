from transliterate import translit

orig = input("Type: ")
#orig = "Как тебя зовут?"

print(translit(orig, "ru", reversed=True))
