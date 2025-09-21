import time


def generate_fake_email() -> str:
    return f"user{time.time()}@example.com"

