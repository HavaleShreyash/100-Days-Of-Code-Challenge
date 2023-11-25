def getEgyptianFraction(numerator, denominator):
    result = []

    while numerator != 0:
        unit_denominator = -(-denominator // numerator)  # ceil division
        result.append(unit_denominator)

        numerator = numerator * unit_denominator - denominator
        denominator *= unit_denominator

    return result

if __name__ == "__main__":
    numerator = int(input())
    denominator = int(input())

    egyptian_fraction = getEgyptianFraction(numerator, denominator)
    for unit_denominator in egyptian_fraction:
        print(unit_denominator) 