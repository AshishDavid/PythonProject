import sys
import os


def caeser(key):
    file = open(sys.argv[1], 'r')
    if sys.argv[3] == 'encryption' or sys.argv[3] == 'decryption':
        now_key = key if sys.argv[3] == 'encryption' else -key
        content = file.read()
        length = len(content)
        unlocked_content = ''
        for i in range(length):
            if content[i].isalpha():
                letter_case = 65 if content[i].isupper() else 97 if content[i].islower() else 0
                unlocked_content += chr((ord(content[i]) + now_key - letter_case) % 26 + letter_case)
            else:
                unlocked_content += content[i]
        print(unlocked_content)
    if sys.argv[3] == 'automatic':
        content = file.read()
        length = len(content)
        most = 'etaoinhsrdlumwc'
        most_freq_dict = {}
        for i in range(length):
            if content[i].isalpha():
                if content[i] in most_freq_dict:
                    most_freq_dict[content[i]] += 1
                else:
                    most_freq_dict[content[i]] = 1
        max_key = max(most_freq_dict, key=most_freq_dict.get)
        while True:
            decrypted_file = ''
            for i in most:
                for j in range(length):
                    if content[j].isalpha():
                        if content[j] == max_key:
                            decrypted_file += i
                        else:
                            decrypted_file += content[j]
                    else:
                        decrypted_file += content[j]
                print(decrypted_file)
                print('Would you like to continue with this or change the most frequent'
                      ' letter ?')
                print('Press "Y" to continue and guess other letters or "N" to change the most'
                      ' frequent letter or "E" to exit')
                choice = input()
                if choice == 'E':
                    file.close()
                    return
                if choice == 'N':
                    decrypted_file = ''
                    continue
                if choice == 'Y':
                    while True:
                        new_file = decrypted_file
                        decrypted_file = ''
                        print('Which letter do you want to replace ?')
                        print('Input the letter you want to replace')
                        old_letter = input()
                        print('Input the new letter')
                        new_letter = input()
                        for k in range(length):
                            if new_file[k].isalpha():
                                if new_file[k] == old_letter:
                                    decrypted_file += new_letter
                                else:
                                    decrypted_file += content[k]
                            else:
                                decrypted_file += content[k]
                        print(decrypted_file)
                        print('Enter "Yes" to continue or "No" to exit')
                        choice_again = input()
                        if choice_again == 'Yes':
                            continue
                        if choice_again == 'No':
                            file.close()
                            return
                        elif choice_again != 'Yes' and choice_again != 'No':
                            print('Wrong choice')
                            return
                else:
                    print('Wrong Choice')
                    return
    elif sys.argv[3] != 'decryption' and sys.argv[3] != 'encryption'\
            and sys.argv[3] != 'automatic':
        print("No such function available")
    file.close()


def vignere(key):
    file = open(sys.argv[1], 'r')
    if sys.argv[3] == 'encryption' or sys.argv[3] == 'decryption':
        content = file.read()
        length = len(content)
        content = content.upper()
        length_with_only_letters = 0
        for y in range(length):
            if content[y].isalpha():
                length_with_only_letters += 1
        count = length_with_only_letters - len(key)
        c = 0
        for z in range(count):
            if c != length:
                key += key[c]
                c += 1
            else:
                c = 0
                key += key[c]
        key = key.upper()
        unlocked_file = ''
        key_count = 0
        for i in range(length):
            if content[i].isalpha():
                unlocked_file = unlocked_file + ((chr(((ord(content[i]) + ord(key[key_count])) % 26) + 65))
                                                 if sys.argv[3] == 'encryption' else
                                                 chr(((ord(content[i]) - ord(key[key_count]) + 26) % 26) + 65)
                                                 if sys.argv[3] == 'decryption' else 0)
            else:
                unlocked_file += content[i]
            key_count = key_count + (1 if content[i].isupper() else 0)
        print(unlocked_file)
    elif sys.argv[3] != 'encryption' and sys.argv[3] != 'decryption':
        print('No such function available')
    file.close()


def vernam():
    file = open(sys.argv[1], 'r')
    content = file.read()
    if sys.argv[3] == 'encryption' or sys.argv[3] == 'decryption':
        count_only_letters = 0
        length = len(content)
        for y in range(length):
            if content[y].isalpha():
                count_only_letters += 1
        letters = str(count_only_letters)
        key = input('Enter the keyword. It should have ' + letters +
                    ' alphabets without any space and special '
                    'characters.\n')
        for q in key:
            if not q.isalpha():
                print('Not a proper keyword')
                return
        if len(key) != count_only_letters:
            print('Not a suitable keyword')
            return
        key_count = 0
        if sys.argv[3] == 'encryption':
            encrypted_content = ''
            for i in range(length):
                if content[i].isalpha():
                    letter_case = 97 if content[i].islower() else 65
                    sum_of = ord(content[i]) + ord(key[key_count]) - 2 * letter_case
                    add_num = 26 if sum_of > 25 else 0
                    encrypted_content += chr(sum_of - add_num + letter_case)
                    key_count += 1
                else:
                    encrypted_content += content[i]
            print(encrypted_content)
        if sys.argv[3] == 'decryption':
            decrypted_content = ''
            for i in range(length):
                if content[i].isalpha():
                    letter_case = 97 if content[i].islower() else 65
                    case = 26 if ord(content[i]) - 97 - ord(key[key_count]) + 97 < 0 else 0
                    sum_of = case + (ord(content[i]) - letter_case) - (ord(key[key_count]) - letter_case)
                    decrypted_content += chr(sum_of + letter_case)
                    key_count += 1
                else:
                    decrypted_content += content[i]
            print(decrypted_content)
    elif sys.argv[3] != 'encryption' and sys.argv[3] != 'decryption':
        print('No such function available')
    file.close()


if len(sys.argv) != 4:
    print('Put correct number of arguments')
else:
    if os.path.exists(sys.argv[1]):
        if sys.argv[2] == 'caeser':
            if sys.argv[3] != 'automatic' and sys.argv[3] == 'encryption' or sys.argv[3] == 'decryption':
                key_ = input('Enter the key between 0-25 \n')
                number = 1
                for x in key_:
                    if not x.isdigit():
                        number = 0
                if number == 1:
                    int_key = int(key_)
                    caeser(int_key)
                else:
                    print('Key is not a number')
            else:
                caeser(0)
        if sys.argv[2] == 'vignere':
            key_ = input('Enter the alphabetical key \n')
            alpha = 0
            for x in key_:
                if not x.isalpha:
                    alpha = 1
            if alpha == 0:
                vignere(key_)
            else:
                print("Not a suitable key")
        if sys.argv[2] == 'vernam':
            vernam()
        elif sys.argv[2] != 'caeser' and sys.argv[2] != 'vignere' and sys.argv[2] != 'vernam':
            print('No such cipher available')
    else:
        print('No such file exists')
