word = input("enter a word: ")
for ch in word:
    if ch in "aeiouAEIOU":
        print("vowel found:", ch)
    else:
        print("not even one vowel found:", ch)
        