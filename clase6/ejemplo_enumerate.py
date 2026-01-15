avengers_endgame = [
    "Iron Man",
    "Captain America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Scarlet Witch",
    "Vision",
    "Falcon",
    "Winter Soldier",
    "War Machine",
    "Ant-Man",
    "Wasp",
    "Black Panther",
    "Shuri",
    "Okoye",
    "M'Baku",
    "Star-Lord",
    "Gamora",
    "Drax",
    "Rocket Raccoon",
    "Groot",
    "Nebula",
    "Wong",
    "The Ancient One",
    "Captain Marvel"
]
# print(avengers_endgame[4]) #podemos imprimir un elemento en especifico

elemento1 ,elemento2 =  (24, 'Nebula')


for indice ,avenger in enumerate(avengers_endgame, 1): #enumerate me devuelve una tupla en cada iteracion (24, 'Nebula') -> indice hara referencia al primer termino y avenger al segundo 
    
    print(f"{avenger} esta en la posicion {indice}")