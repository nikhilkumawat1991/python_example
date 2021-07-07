import collections;

lst = [4,
       "bcdef",
       "abcdefg",
       "bcde",
       "bcdef"]


def determine_distinct_word_count(lst):
    for wd in lst:
        if str(wd).isnumeric():
            lst.remove(wd)

    distinct_words = set(lst)
    distinct_count = len(distinct_words)
    dct = {}

    for word in distinct_words:
        count = 0
        for obj in lst:
            if word == obj:
                count = count + 1
        dct[word] = count

    lst_new = []
    for k,v in dct.items():
        lst_new.append(v)
    return distinct_count, lst_new


cnt, dt = determine_distinct_word_count(lst)
print(cnt)
print(dt)