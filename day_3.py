
#Replacing digits with charachters - LeetCode 1844
def shift(c, x):
    return chr(ord(c) + x)

def replaceDigits(s):
    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(s[i])
        else:
            result.append(shift(s[i - 1], int(s[i])))
    return ''.join(result)

# Example usage:
if __name__ =="__main__":    
    s = "a1b2c1"
    result = replaceDigits(s)
    print(result)  # Output: "abbdcd"
