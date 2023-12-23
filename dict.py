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

weight = team['players']['LeBron James']['weight']
team['players']['Anthony Davis']['number'] = 23
team_Anthony = list(team['players'].keys())[1]
position_Anthony = team['players']['Anthony Davis']['position']
number_Anthony = team['players']['Anthony Davis']['number']

print(f"LeBron James weighs {weight} kg.")
print(f"Team: {team['name']} - {team_Anthony} ({position_Anthony}, #{number_Anthony})")

print('---')

# 
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

"""
Do podanego słownika dodaj nowego gracza o kluczu 'Kobe Bryant' i poniższej wartości:
    {
        'position': 'Guard',
        'number': 24,
        'height': 198,
        'weight': 96,
    }
W odpowiedzi wydrukuj poniższe informacje:
    liczbę zawodników w słowniku team
    numer dla zawodnika 'Kobe Bryant'
"""
team['players']['Kobe Bryant'] = {
        'position': 'Guard',
        'number': 24,
        'height': 198,
        'weight': 96,
    }

print(len(team['players']))
print(team['players']['Kobe Bryant']['number'])

print('---')

flight = {
'airline': 'Delta',
'flight_number': 'DL215',
'origin': {
    'airport': 'JFK',
    'city': 'New York',
    'state': 'NY',
    'country': 'USA',
},
'destination': {
    'airport': 'LHR',
    'city': 'London',
    'country': 'UK',
},
'departure_time': '2023-05-01T08:00:00Z',
'arrival_time': '2023-05-01T20:00:00Z',
'passengers': [
    {'name': 'John Smith', 'seat': '17A', 'meal': 'Vegetarian'},
    {'name': 'Jane Doe', 'seat': '17B', 'meal': 'Kosher'},
],
}

"""
Wykonaj poniższe kroki:
    wyodrębnij nazwę linii lotniczej i przypisz do zmiennej airline
    wyodrębnij nazwę lotniska wylotu i przypisz do zmiennej origin_airport
    wyznacz liczbę pasażerów i przypisz do zmiennej num_passengers
    wyodrębnij numer lotu i przypisz do zmiennej flight_number
"""
airline = flight['airline']
origin_airport = flight['origin']['airport']
num_passengers = len(flight['passengers'])
flight_number = flight['flight_number']

print(f"Airline: {airline}")
print(f"Origin airport code: {origin_airport}")
print(f"Flight: {flight_number}")
print(f"Number of passengers: {num_passengers}")

print('---')

flight = {
    'airline': 'Delta',
    'flight_number': 'DL215',
    'origin': {
        'airport': 'JFK',
        'city': 'New York',
        'state': 'NY',
        'country': 'USA',
    },
    'destination': {
        'airport': 'LHR',
        'city': 'London',
        'country': 'UK',
    },
    'departure_time': '2023-05-01T08:00:00Z',
    'arrival_time': '2023-05-01T20:00:00Z',
    'passengers': [
        {'name': 'John Smith', 'seat': '17A', 'meal': 'Vegetarian'},
        {'name': 'Jane Doe', 'seat': '17B', 'meal': 'Kosher'},
    ],
}

"""
Wykonaj poniższe kroki:
    zaktualizuj wartość miejsca - 'seat' dla drugiego pasażera na numer '18B'
    dodaj kolejnego pasażera o podanych danych
    {'name': 'Bob Johnson', 'seat': '19C', 'meal': 'Halal'}
    wyznacz liczbę pasażerów i przypisz do zmiennej num_passengers
"""
flight ['passengers'] = [
        {'name': 'John Smith', 'seat': '17A', 'meal': 'Vegetarian'},
        {'name': 'Jane Doe', 'seat': '18B', 'meal': 'Kosher'},
        {'name': 'Bob Johnson', 'seat': '19C', 'meal': 'Halal'}
    ]

num_passengers = len(flight ['passengers'])
arrival_time = flight['arrival_time']
departure_time = flight['departure_time']
origin_city = flight['origin']['city']
state_origin_city = flight['origin']['state']
airport_origin_city = flight['origin']['airport']
destination_city = flight['destination']['city']
airport_destination_city = flight['destination']['airport']
country_destination_city = flight['destination']['country']


print(f"From {origin_city}, {state_origin_city} ({airport_origin_city})")
print(f"To {destination_city}, {country_destination_city} ({airport_destination_city})")
print(f"Departure time: {departure_time}")
print(f"Arrival time: {arrival_time}")
print(f"Number of passengers: {num_passengers}")
