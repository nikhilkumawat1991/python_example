vowels = ["a","e","i","o","u"]

def score_words(lst):
    count = 0
    for word in lst:
        for letter in word:
            if check(letter):
                count = count + 1

    print(count)
    if count % 2 == 0:
        return 2
    else:
        return 1


def check(letter):
    if letter in vowels:
        return True


lst = ["hacker", "book"]
cnt = score_words(lst)
print(cnt)
