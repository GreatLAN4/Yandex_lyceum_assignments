def number_in_english(n):
    digits = []
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen", ]
    dozens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ""]
    hundreds = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred",
                "seven hundred", "eight hundred", "nine hundred"]

    n2 = str(n)
    for i in n2:
        digits.append(i)
    D_len = len(digits)
    if D_len == 1:
        if n == 0:
            return "zero"
        else:
            return units[int(digits[-1])]

    if D_len == 2:
        if 9 < n < 20:

            return_teen = teen[n % 10]
            return return_teen
        else:
            return_dozens = dozens[int(digits[0]) - 1]
            return_units = " " + units[int(digits[1])]
            if return_units == " ":
                return return_dozens
            else:
                return return_dozens + return_units
    AND = " and"
    if D_len == 3:
        return_hundreds = hundreds[int(digits[0]) - 1]
        teen_counter = int(digits[1] + digits[2])

        if 9 < teen_counter < 20:

            return_teen = " " + teen[teen_counter % 10]
            if return_teen == " ":
                return return_hundreds
            else:
                return return_hundreds + AND + return_teen

        else:

            return_dozens = " " + dozens[int(digits[1]) - 1]
            return_units = " " + units[int(digits[-1])]
            if return_dozens == " ":
                if return_units == " ":
                    return return_hundreds
                else:
                    return return_hundreds + AND + return_units
            else:
                if return_units == " ":
                    return return_hundreds + AND + return_dozens
                else:
                    return return_hundreds + AND + return_dozens + return_units
