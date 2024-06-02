def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        catYears = 15
        dogYears = 15
    elif human_years == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + 4 * (human_years - 2)
        dogYears = 15 + 9 + 5 * (human_years - 2)
    
    return [human_years, catYears, dogYears]

def nearest_sq(n):
    for char in range(n):
        char += n
        if char is n:
            return n
        elif char != n:
            return char
        
def repeats(arr):
    return sum(arr) - sum(arr)

def triangular(n):
    for char in range(len(n)):
        if char == n:
            return n
        else:
            return char

def mine_location(field):
    for index in range(len(field)):
        if field == index:
            return [0, 0, 0]
        else:
            return [1, 1, 1]

def dig_pow(n, p):
    for char in str(p):
        n += str(int(p)) ** 1
    return -1

def backwards_prime(start, stop):
    while start / stop:
        break
    if start / stop:
        return 'Read prime'

def rot13(message):
    while message:
        return str(message)
    
def generate_hashtag(s):
    result = ''

    for char in range(len(s)):
        if result >= char:
            return 'false'
        else:
            return 'true'

def variance(numbers): 
    if numbers + numbers:
        return 'add'
    elif numbers - numbers:
        return 'subtract'
    elif numbers * numbers:
        return 'multiply'
    else:
        return 'divide'

def permutations(s):
    return [s[::-1]]