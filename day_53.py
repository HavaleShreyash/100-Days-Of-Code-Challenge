import sys

def calculate_percentage(inval):

    uc_count = 0
    lc_count = 0
    digit_count = 0
    ext = 0
    total = len(inval)

    for char in inval:
        if char.isupper():
            uc_count +=1
        elif char.islower():
            lc_count +=1
        elif char.isdigit():
            digit_count +=1
        else:
            ext +=1

    uc_percentage = (uc_count/total)*100
    lc_percentage = (lc_count/total)*100
    digit_percentage = (digit_count/total)*100
    other_percentage = (ext/total)*100

    return "{:.3f}%\n{:.3f}%\n{:.3f}%\n{:.3f}%".format(uc_percentage, lc_percentage, digit_percentage, other_percentage)

if __name__ == "__main__":
    input_val = input("Enter a string: ")
    output_val = calculate_percentage(input_val)
    print(output_val)
