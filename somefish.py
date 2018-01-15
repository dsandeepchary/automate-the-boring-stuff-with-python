while True:
    print('Who are you?');
    name = input();
    if name != 'Sandeep':
        continue;
    print('Heylo Sandeep, been a while since I saw you, What is the password?');
    password = input();
    if password == 'somefish':
        break;
print('Yay! Access Granted');
