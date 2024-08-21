def convert_date_to_words(date_string):
    days = {
        '01': 'First', '02': 'Second', '03': 'Third', '04': 'Fourth', '05': 'Fifth', '06': 'Sixth',
        '07': 'Seventh', '08': 'Eighth', '09': 'Ninth', '10': 'Tenth', '11': 'Eleventh', '12': 'Twelfth',
        '13': 'Thirteenth', '14': 'Fourteenth', '15': 'Fifteenth', '16': 'Sixteenth', '17': 'Seventeenth',
        '18': 'Eighteenth', '19': 'Nineteenth', '20': 'Twentieth', '21': 'Twenty-first', '22': 'Twenty-second',
        '23': 'Twenty-third', '24': 'Twenty-fourth', '25': 'Twenty-fifth', '26': 'Twenty-sixth',
        '27': 'Twenty-seventh', '28': 'Twenty-eighth', '29': 'Twenty-ninth', '30': 'Thirtieth', '31': 'Thirty-first'
    }

    months = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
        '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }

    day, month, year = date_string.split('-')
    day_in_words = days.get(day, 'Invalid day')
    month_in_words = months.get(month, 'Invalid month')
    year_in_words = convert_year_to_words(year)

    return f"The {day_in_words} of {month_in_words}, {year_in_words}"

def convert_year_to_words(year):
    # Split the year into two parts (e.g., "2020" -> "20", "20")
    first_part = int(year[:2])
    second_part = int(year[2:])

    # Convert the first and second parts to words
    year_in_words = f"{convert_two_digit_number_to_words(first_part)} {convert_two_digit_number_to_words(second_part)}"
    
    return year_in_words

def convert_two_digit_number_to_words(number):
    numbers_to_words = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
        40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    if 10 <= number <= 20:
        return numbers_to_words[number]
    elif number > 20 and number % 10 == 0:
        return numbers_to_words[number]
    else:
        tens = number // 10 * 10
        ones = number % 10
        return f"{numbers_to_words[tens]} {convert_digit_to_word(str(ones))}"

def convert_digit_to_word(digit):
    digits_to_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return digits_to_words.get(digit, 'Invalid')

user_input = input("Enter a date in the format dd-mm-yyyy: ")
print(convert_date_to_words(user_input))
