L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

d1 = dict(zip(L1, L2))

print(d1)

num = int(input("Enter a number: "))

def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

fact = factorial(num)

print(f"The factorial of {num} is {fact}")

L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for x in L:
    if x.startswith('B'):
        print(x)
d2 = {i: i+1 for i in range(11)}
print(d2)


def binary_to_decimal(binary_str):
    
    try:
        for digit in binary_str:
            if digit not in ['1', '0']:
                raise ValueError("Input must be only 1s or 0s.")
        
        dec = int(binary_str, 2)
        return dec
    
    except ValueError as s:
        print(s)
        return None

binary_number = input("Enter a binary number: ")

decimal_number = binary_to_decimal(binary_number)

if decimal_number is not None:
    print(f"The decimal number is: {decimal_number}")


import json
import csv

def calculate_score(user_answers, correct_answers):
    score = 0
    for question, answer in user_answers.items():
        if answer == correct_answers.get(question):
            score += 1
    return score

def save_results(user_name, user_answers, score, file_format):
    file_name = f'{user_name}_quiz_results.{file_format}'
    if file_format == 'json':
        with open(file_name, 'w') as json_file:
            json.dump({'name': user_name, 'resu': f'{score}/20', 'ans': user_answers}, json_file)
        print('save is done as .json')
    elif file_format == 'csv':
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Question', 'User Answer'])
            for question, answer in user_answers.items():
                csv_writer.writerow([question, answer])
            csv_writer.writerow(['Score', f'{score}/20'])
        print('result save as csv.')
    else:
        print('not save the file dosnt support.')

user_name = input('your name: ')

file_name = input('file ques and ans: ')

with open(file_name, 'r') as file:
    w = file.read()

questions_and_answers = json.loads(w)

user_answers = {}
for question in questions_and_answers.keys():
    user_answer = input(f'Your answer for "{question}": ')
    user_answers[question] = user_answer

score = calculate_score(user_answers, questions_and_answers)
print(f'Your score is: {score}/20')

file_format = input('Choose the file format to save the results (JSON or CSV): ')
save_results(user_name, user_answers, score, file_format)

class BankAccount:
    def __init__(s, acc_num, acc_hol):
        s.acc_num = acc_num
        s.acc_hol = acc_hol
        s.balance = 0.0

    def deposit(s, amount):
        s.balance += amount

    def withdraw(s, amount):
        if s.balance >= amount:
            s.balance -= amount
        else:
            print("Insu funds.")

    def get_balance(s):
        return s.balance

class SavingsAccount(BankAccount):
    def __init__(s, acc_num, acc_hol, interest_rate):
        super().__init__(acc_num, acc_hol)
        s.interest_rate = interest_rate

    def apply_interest(s):
        s.balance += s.balance * s.interest_rate

    def __str__(s):
        return f"Account Holder: {s.acc_hol}\nAccount Balance: ${s.balance:.2f}\nInterest Rate: {s.interest_rate*100:.2f}%"

bank_account = BankAccount("123456789", "had s")


bank_account.deposit(1000)
print(f"Current Balance: ${bank_account.get_balance():.2f}")


bank_account.withdraw(500)
print(f"Current Balance: ${bank_account.get_balance():.2f}")

savings_account = SavingsAccount("0000000", "haedara s ", 0.05)

savings_account.apply_interest()
print(savings_account)



