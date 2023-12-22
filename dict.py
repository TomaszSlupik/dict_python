# Słowniki - najważniejsze metody
# Copy - kopiowanie słowników
word = {"dog": "pies", "cat": "kot", "cow": "krowa"}
word_copy = word.copy()

print(word_copy)

print('---')

# clear - usuwanie całości
phone = {"Iphone": 15, "Samsung": "galaxy"}
phone.clear()

print(phone)

print('---')
# fromkeys - literowanie po każej literze
gym = {"pierwsza": "grafit", "druga": "xtreme"}

print(gym.fromkeys("druga", "test"))
print(gym)

print('---')
# keys - wyodrebnienie tylko kluczy
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}

print(capitals.keys())

print('---')

# values - wyodrebnienie tylko wartości
print(capitals.values())

print('---')

# items - wyodrebnienie pary klucz-wartość
print(capitals.items())

print('---')

# get - dostanie wartośći dla podanego klucza
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}

print(capitals.get('Austria'))

print('---')

# Korzystając z operatora wycinania wyodrębnij wartość dla klucza 'PLW
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

plw = stocks['PLW']
print(plw)

print('---')

# Wyodrębnij cenę dla spółki 'Ten Square Games' (wartość dla klucza 'Ten Square Games')

stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

ten_stocks = stocks.get('TEN')

print(ten_stocks['Ten Square Games'])
print('---')

# Update - Aktualizacja ceny
# Zaktualizuj cenę spółki CD Projekt na wartość 310. Wartość dla klucza 'CDR' wydrukuj do konsoli.
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

stocks.get('CDR').update({"CD Projekt": 310})

print(stocks)

print('---')

# ADD - dodawanie
# Dodaj do słownika stocks czwartą parę o kluczu: 'BBT' oraz wartości: {'Boombit': 23}.
# Wartości słownika stocks wydrukuj do konsoli.stocks
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}


stocks['BBT'] = {"Boombit": 2}

print(stocks.values())

print('---')

# enumerate - numerowanie indeksów
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

print(list(enumerate(ticker)))

print('---')

# Przekształcenie listy w słownik + ponumerowanie => enumerate
# Przekształć tę listę w słownik (indeks, ticker).
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

dict_ticker = dict(enumerate(ticker))

print(dict_ticker)

print('---')

# Sortowanie
project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

sorted_project_ids = sorted(project_ids.values())

sorted_project_ids.pop(1)

print(sorted_project_ids)

print('---')

# Usuwanie klucz-wartość ze słownika
# 1 metoda del  - usuwanie
stats = {'website': 'python.org', 'traffic': 100, 'type': 'organic'}

del stats['traffic']

print(stats)

print('---')
# 2 metdoa pop - usuwanie
statsTwo = {'website': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
statsTwo.pop('traffic')
print(statsTwo)

print('---')
# w momencie próby odczytu wartości dla klucza, który nie występuje w słowniku
# nie podnosi błędu KeyError tylko zwraca wartość domyślną 'undefined'

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}


def userCheck(value):
    if value in users.keys():
        print(f"Klucz: {value}, Wartość: {users[value]}")
    else:
        print('undefined')


userCheck('004')

print('---')

# zaktualizuj wartość dla klucza 'location' na 'Los Angeles'
# do listy dla klucza 'interests' dodaj wartość 'travel'

profile = {
    'name': 'John Doe',
    'age': 25,
    'location': 'New York',
    'interests': ['photography', 'music', 'hiking'],
}

profile['location'] = 'Los Angeles'
profile['interests'] = ['photography', 'music', 'hiking', 'travel']

print(profile)

print('---')

"""
Następnie wykonaj poniższe kroki:
    dla klucza num_guests ustaw nową wartość 3
    dodaj nową parę 'price': 200
    usuń parę dla klucza 'room_type'
    wydrukuj liczbę elementów słownika hotel_booking
    wydrukuj posortowaną alfabetycznie listę kluczy słownika hotel_booking 
"""

hotel_booking = {
    'hotel_name': 'Sheraton',
    'check_in_date': '2024-06-10',
    'check_out_date': '2023-06-13',
    'room_type': 'Deluxe',
    'num_guests': 2
}

hotel_booking['num_guests'] = 3
hotel_booking['price'] = 200
del hotel_booking['room_type']
print(len(hotel_booking))
print(sorted(hotel_booking.keys()))


print('---')
"""
Wykonaj poniższe kroki:
    dla klucza 'duration' ustaw nową wartość 10
    do listy dla klucza 'activities' dodaj 'Visit the Palace of Versailles'
    dodaj nową parę 'accommodation': 'Hotel'
"""
itinerary = {
    'destination': 'Paris, France',
    'duration': 7,
    'budget': 1500,
    'activities': [
        'Visit the Eiffel Tower',
        'Explore the Louvre',
        'Take a Seine River Cruise',
    ],
}
itinerary['duration'] = 10
itinerary['activities'] = ['Visit the Eiffel Tower', 'Explore the Louvre',
                           'Take a Seine River Cruise', 'Visit the Palace of Versailles']
itinerary['accommodation'] = 'Hotel'

print(f"Destination: {itinerary['destination']}")
print(f"Duration: {itinerary['duration']} days")
print(f"Budget: ${itinerary['budget']}")
print(f"Number of activities: {len(itinerary['activities'])}")

print('---')

"""
Wykonaj poniższe operacje:
    odczytaj wagę dla zawodnika 'LeBron James' i wydrukuj do konsoli tak jak pokazano poniżej
    zaktualizuj numer dla zawodnika 'Anthony Davis' na 23
    wydrukuj informacje o zawodniku 'Anthony Davis' tak jak pokazano poniżej
"""
team = {
    'name': 'Lakers',
    'city': 'Los Angeles',
    'players': {
        'LeBron James': {
            'position': 'Forward',
            'number': 23,
            'height': 203,
            'weight': 113,
        },
        'Anthony Davis': {
            'position': 'Center',
            'number': 3,
            'height': 208,
            'weight': 115,
        },
        'Russell Westbrook': {
            'position': 'Guard',
            'number': 0,
            'height': 190,
            'weight': 91,
        },
    },
}

