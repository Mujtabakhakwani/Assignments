def number_to_words(num):
    if num == 0:
        return "Zero"

    less_than_20 = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    tens = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    thousands = ["", "Thousand", "Million", "Billion"]

    def word(num, idx):
        if num == 0:
            return ""
        elif num < 20:
            return less_than_20[num] + " "
        elif num < 100:
            return tens[num // 10] + " " + word(num % 10, idx)
        else:
            return less_than_20[num // 100] + " Hundred " + word(num % 100, idx)

    res = ""
    for i, th in enumerate(thousands):
        if num % 1000 != 0:
            res = word(num % 1000, i) + th + " " + res
        num //= 1000

    return res.strip()


def total_characters(words):
    return len(words.replace(" ", ""))


def total_words(sentence):
    return len(sentence.split())


def process_number_and_sentence(num, sentence):
    english_words = number_to_words(num)
    char_count = total_characters(english_words)
    word_count = total_words(sentence)

    if char_count > word_count:
        english_words = english_words[::-1]

    print(english_words)


number = int(input("enter number "))
sentence = " "
process_number_and_sentence(number, sentence)
