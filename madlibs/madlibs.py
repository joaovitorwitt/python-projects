
def main():
    adjective = get_adjective()
    verb1, verb2 = get_verbs()
    noun = get_noun()

    print(f"Hi my name is {adjective}, I am {verb1} years old and my favorite sport is {noun} and the quote of the day is {verb2}")


def get_adjective():
    return input("Enter an adjective: ")


def get_verbs():
    ver1, ver2 = input("Enter two verbs separated by space: ").split(" ")
    return ver1, ver2

def get_noun():
    return input("Enter a noun: ")


if __name__ == "__main__":
    main()

