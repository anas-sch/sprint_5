import random
from data import domain

def generate_email():
    random_part = f"{random.randint(100,999):06d}"
    return f"Anastasia Scherbakova_20_{random_part}@{domain}".replace(" ", "")

new_email = generate_email()

def generate_password():
    return f"{random.randint(9000,88888)}{random.choice('abcdefghigklmnopqrstu')}"

new_password = generate_password()