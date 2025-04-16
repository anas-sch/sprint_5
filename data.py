import random

name = "Anastasiya"
my_email = "a.m.scherbakova@yandex.ru"
correct_password = "98765!"
incorrect_password = "12345"
domain = "yandex.ru"

def generate_email():
    random_part = f"{random.randint(100,999):06d}"
    return f"Anastasia Scherbakova_20_{random_part}@{domain}".replace(" ", "")

new_email = generate_email()

def generate_password():
    return f"{random.randint(9000,88888)}{random.choice('abcdefghigklmnopqrstu')}"

new_password = generate_password()