import random

def generate_token():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])  # ⚠️ Predictable Token
