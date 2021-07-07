#First Recurring Character in a string

st="ABCAB"


def first_recurring_character(st):
    for i in st:
        char = i
        print(f"current character is {char}")
        next_value =  st.index(i)+1
        while next_value < len(st):
            print(f"next value is: {st[next_value]}")
            if char == st[next_value]:
                print("similar character found..!! breaking from the loop")
                return i
            else:
                print("No match found. Comparing next value")
                next_value = next_value + 1

    else:
        print("no recurring character found..!!")
        return None

def first_recurring_character_updated(st):
    #{"A":"2","B"="0"}
    dct = {}
    for letter in st:
        if letter in dct.keys():
            return letter
        else:
            dct[letter] = 1
    else:
        print("nothing found..!!")
        return None


if __name__ == '__main__':
    #char_found = first_recurring_character(st)
    #print(f"value found is: {char_found}")


    char = first_recurring_character_updated(st)
    print(char)
