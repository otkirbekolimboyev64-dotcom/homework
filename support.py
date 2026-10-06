def greet(name):
  return f"Hello, {name}!"

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

def find_max(numbers):
  return max(numbers)

def find_min(numbers):
    return min(numbers)

def reverse_text(text):
    return text[::-1]


def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def birth_year(age, current_year=2026):
    return current_year - age

def bmi(kg, height_m):
    return round(kg / (height_m ** 2), 2)

def car_age(year, current_year=2026):
    return current_year - year
def fuel_cost (price_per_liter):
    return price_per_liter

def colour (blue, green, red):
    return f"{blue}:{green}:{red}"

def phone_number(phone_number):
    return phone_number

def university_info(name, location):
    return f"{name} — {location}"

def student(name, location):
    return f"{name} {location}"

def is_pet(type_):
    return type == "pet"

def pencil_info(brand, color):
    return f"{brand} pencil, color: {color}"
