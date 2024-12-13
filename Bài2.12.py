import re
passwords = input("Nhập mật khẩu: ").split(',')

valid_passwords = []

for password in passwords:
    if (6 <= len(password) <= 12 and
            re.search("[a-z]", password) and
            re.search("[0-9]", password) and
            re.search("[A-Z]", password) and
            re.search("[$#@]", password) and
            not re.search("\s", password)):
        valid_passwords.append(password)

print(",".join(valid_passwords))
