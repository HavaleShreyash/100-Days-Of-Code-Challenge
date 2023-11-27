import sys

def is_good_password(passwords):
    for i in range(len(passwords)):
        for j in range(i + 1, len(passwords)):
            if passwords[i] == passwords[j] or \
            passwords[i].startswith(passwords[j]) or \
            passwords[j].startswith(passwords[i]):
                return "BAD PASSWORD"
    return "GOOD PASSWORD"


if __name__ == "__main__":
    input_val = input("Password: ").split()
    output_val = is_good_password(input_val)
    print(output_val)