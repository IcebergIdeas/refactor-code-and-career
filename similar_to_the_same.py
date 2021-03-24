class RomanConverterBefore(object):
    def convert(self, numeral):
        roman = ""
        current_number = numeral

        for i in range(current_number):
            if current_number >= 10:
                roman += "X"
                current_number -= 10

        for i in range(0, current_number):
            roman += "I"

        return roman



class RomanConverterAfter(object):
    def convert(self, numeral):
        roman = ""
        digit = 10
        roman_value = "X"
        for _ in range(numeral):
            if numeral >= digit:
                roman += roman_value
                numeral -= digit

        digit = 1
        roman_value = "I"
        for _ in range(numeral):
            if numeral >= digit:
                roman += roman_value
                numeral -= digit

        return roman
