from translate import Translator

# Offline translator
# Write text to translate.txt that you want to translate.
# Run script. You will be asked to choose to which language you want to translate.
# The tranlsated text is printed in terminal and saved to translation.txt.

try:
    with open('translate.txt', mode='r') as x:
        original = x.readlines()
except FileNotFoundError as e:
    print('File not found')

languages = ['en', 'es', 'pt', 'zh']

while True:
    to_language = input(f'\nSupported languages {languages}\nTranslate to: ')
    print()
    if to_language in languages:
        break
    else:
        print('!!!! Languages is not supported !!!!')


translator = Translator(to_lang=to_language)


print('//// Original ////')
print()
for line in original:
    print(f'{line[:-1]}')

print()
print('//// Translation ////')
print()
for line in original:
    print(f'{translator.translate(line)}')

print()

with open('translation.txt', mode='w') as y:
    for line in original:
        y.write(translator.translate(line)+'\n')

print('* Saved to translation.txt')
print()