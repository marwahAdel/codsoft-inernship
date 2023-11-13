import random
import string


def random_generation_password(length, complexity):

    if complexity == "weak":
        complexity_level=string.ascii_letters
    elif complexity == "medium":
        complexity_level=string.ascii_letters + string.digits
    elif complexity == "strong":
        complexity_level =string.ascii_letters + string.digits + string.punctuation
    else:
        print("please enter the correct choice (weak,medium,strong)")
    password_generated = ''.join(random.choice(complexity_level) for _ in range(length))
    return password_generated


def main():
    print("Password Generator")
    length = int(input("please enter length of password : "))
    complexity = input("please enter complexity of password (weak,medium,strong): ").lower()
    print("Generated Password:", random_generation_password(length, complexity))


if __name__ == "__main__":
    main()
