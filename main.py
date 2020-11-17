import sys
import os


def caeser():
    file = open(sys.argv[1], 'r')
    if sys.argv[3] == 'encryption' or sys.argv[3] == 'decryption':
        key = int(input('Enter the key between 0-25 \n'))
        content = file.read()
        length = len(content)
        if sys.argv[3] == 'encryption':
            encrypted_content = ''
            for i in range(length):
                if content[i].isupper():
                    encrypted_content += chr((ord(content[i]) + key - 65) % 26 + 65)
                if content[i].islower():
                    encrypted_content += chr((ord(content[i]) + key - 97) % 26 + 97)
                elif not content[i].isupper() and not content[i].islower():
                    encrypted_content += content[i]
            print(encrypted_content)
        if sys.argv[3] == 'decryption':
            decrypted_content = ''
            for i in range(length):
                if content[i].isupper():
                    decrypted_content += chr((ord(content[i]) - key - 65) % 26 + 65)
                if content[i].islower():
                    decrypted_content += chr((ord(content[i]) - key - 97) % 26 + 97)
                elif not content[i].isupper() and not content[i].islower():
                    decrypted_content += content[i]
            print(decrypted_content)
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
                print('Would you like to continue with this or change the most frequent letter ?')
                print('Press "Y" to continue and guess other letters or "N" to change the most frequent letter or '
                      '"E"to exit')
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
    elif sys.argv[3] != 'decryption' and sys.argv[3] != 'encryption' and sys.argv[3] != 'automatic':
        print("No such function available")
    file.close()


def vignere():
    file = open(sys.argv[1], 'r')
    key = input('Enter the alphabetical key \n')
    content = file.read()
    length = len(content)
    length_with_only_letters = 0
    for x in range(length):
        if content[x].isalpha():
            length_with_only_letters += 1
    count = length_with_only_letters - len(key)
    c = 0
    for x in range(count):
        if c != length:
            key += key[c]
            c += 1
        else:
            c = 0
            key += key[c]
    print(key)
    if sys.argv[3] == 'encryption':
        encrypted_content = ''
        key_count = 0
        for i in range(length):
            if content[i].isalpha():
                encrypted_content += chr(((ord(content[i]) + ord(key[key_count])) % 26) + 65)
                key_count += 1
            else:
                encrypted_content += content[i]
        print(encrypted_content)
    if sys.argv[3] == 'decryption':
        decrypted_content = ''
        key_count = 0
        for i in range(length):
            if content[i].isalpha():
                decrypted_content += chr(((ord(content[i]) - ord(key[key_count]) + 26) % 26) + 65)
                key_count += 1
            else:
                decrypted_content += content[i]
        print(decrypted_content)
    elif sys.argv[3] != 'encryption' and sys.argv[3] != 'decryption':
        print('No such function available')
    file.close()


def vernam():
    file = open(sys.argv[1], 'r')
    content = file.read()
    count_only_letters = 0
    length = len(content)
    for x in range(length):
        if content[x].isalpha():
            count_only_letters += 1
    letters = str(count_only_letters)
    key = input('Enter the keyword. It should have ' + letters+' alphabets \n')
    if len(key) != count_only_letters:
        print('Not a suitable keyword')
        return
    if sys.argv[3] == 'encryption':
        encrypted_content = ''
        key_count = 0
        for i in range(length):
            if content[i].isalpha():
                if content[i].islower():
                    sum_of = ord(content[i]) + ord(key[key_count]) - 194
                    if sum_of > 25:
                        encrypted_content += chr(sum_of - 26 + 97)
                    else:
                        encrypted_content += chr(sum_of + 97)
                    key_count += 1
                if content[i].isupper():
                    sum_of = ord(content[i]) + ord(key[key_count]) - 130
                    if sum_of > 25:
                        encrypted_content += chr(sum_of - 26 + 65)
                    else:
                        encrypted_content += chr(sum_of + 65)
                    key_count += 1
            elif not content[i].isalpha():
                encrypted_content += content[i]
        print(encrypted_content)
    if sys.argv[3] == 'decryption':
        decrypted_content = ''
        key_count = 0
        sum_of_ = 0
        for i in range(length):
            if content[i].isalpha():
                if content[i].islower():
                    if (ord(content[i]) - 97) - (ord(key[key_count]) - 97) < 0:
                        sum_of_ = 26 + (ord(content[i]) - 97) - (ord(key[key_count]) - 97)
                    else:
                        sum_of_ = (ord(content[i]) - 97) - (ord(key[key_count]) - 97)
                    decrypted_content += chr(sum_of_ + 97)
                    key_count += 1
                if content[i].isupper():
                    if (ord(content[i]) - 65) - (ord(key[key_count]) - 65) < 0:
                        sum_of_ = 26 + (ord(content[i]) - 65) - (ord(key[key_count]) - 65)
                    else:
                        sum_of_ = (ord(content[i]) - 97) - (ord(key[key_count]) - 97)
                    decrypted_content += chr(sum_of_ + 65)
                    key_count += 1
            elif not content[i].isalpha():
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
            caeser()
        if sys.argv[2] == 'vignere':
            vignere()
        if sys.argv[2] == 'vernam':
            vernam()
    else:
        print('No such file exists')

# argv[0] - main.py
# argv[1] - .txt file path
# argv[2] - type of cipher
# argv[3] - encryption/decryption
