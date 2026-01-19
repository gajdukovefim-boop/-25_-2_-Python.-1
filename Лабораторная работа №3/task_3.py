# TODO Напишите функцию count_letters
def count_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_counts:
                letter_counts[char_lower] += 1
            else:
                letter_counts[char_lower] = 1
    return letter_counts


# TODO Напишите функцию calculate_frequency
def calculate_frequency(count_letters):
    total_letters = sum(count_letters.values())
    frequencies = {}
    for letter, count in count_letters.items():
        frequency = count / total_letters
        frequencies[letter] = round(frequency, 2)
    return frequencies


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# Подсчет и вычисление частот
letter_counts = count_letters(main_str)
frequencies = calculate_frequency(letter_counts)

# TODO Распечатайте в столбик букву и её частоту в тексте
# Выводим без сортировки, в том порядке, как они встречаются в словаре
for letter, freq in frequencies.items():
    print(f"{letter}: {freq:.2f}")
