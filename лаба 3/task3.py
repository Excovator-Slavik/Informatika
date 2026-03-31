from collections import Counter
# TODO  Напишите функцию count_letters
def count_letters(text):
    counts = {}
    for char in text.lower():
        # Проверяем если ли истина символ-буква
      if char.isalpha():
          # Если букв нет, то будет 0 + 1
          counts[char] = counts.get(char, 0) + 1
    return counts
def calculate_frequency(letter_counts):
     total_letters = sum(letter_counts.values())
     frequencies = {}
     for letter, count in letter_counts.items():
         #Вычисляем кол-во букв от объема
        frequencies[letter] = count / total_letters
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
letters_data = count_letters(main_str)
letter_freq = calculate_frequency(letters_data)
# TODO Распечатайте в столбик букву и её частоту в тексте
for letter, freq in letter_freq.items():
    print(f"{letter}: {freq:.2f}")