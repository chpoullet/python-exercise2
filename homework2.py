from random import randint

# I want you to use operators
# equate something
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

secret_num = randint(1, 10)

print('Hello there, please choose a number between 1-10!')
user_num = int(input().strip())

if user_num == secret_num:
    print('Well done, you won!')
else:
    print('Unlucky, maybe next time!')
    print(f'The number was actually {secret_num}.')