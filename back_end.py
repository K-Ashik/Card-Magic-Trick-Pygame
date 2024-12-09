def lists_formation(complete_list):
    row_A = []
    row_B = []
    row_C = []

    partial_list = complete_list

    for i in range(0, 21, 3):
        row_A.append(partial_list[i])
    for j in range(1, 21, 3):
        row_B.append(partial_list[j])
    for k in range(2, 21, 3):
        row_C.append(partial_list[k])

    return row_A, row_B, row_C

def positioning(row_A, row_B, row_C, correct_column):
    choice = correct_column
    deck_of_cards = []

    if choice == "A":
        for i in row_B:
            deck_of_cards.append(i)
        for j in row_A:
            deck_of_cards.append(j)
        for k in row_C:
            deck_of_cards.append(k)
    if choice == "B":
        for i in row_A:
            deck_of_cards.append(i)
        for j in row_B:
            deck_of_cards.append(j)
        for k in row_C:
            deck_of_cards.append(k)
    if choice == "C":
        for i in row_B:
            deck_of_cards.append(i)
        for j in row_C:
            deck_of_cards.append(j)
        for k in row_A:
            deck_of_cards.append(k)

    return deck_of_cards

def colors():
    return {"white": (255, 255, 255),
            "dark_orange": (201, 90, 10),
            "light_orange": (245, 127, 10),
            "dark_purple": (110, 60, 128),
            "light_purple": (145, 17, 171),
            }

def cards(): 
    return {'JH': 'JH.png',
            'QD': 'QD.png',
            '3C': '3C.png',
            '6C': '6C.png',
            '9H': '9H.png',
            '7H': '7H.png',
            '8H': '8H.png',
            '3D': '3D.png',
            '5C': '5C.png',
            '8D': '8D.png',
            'AD': 'AD.png',
            'AC': 'AC.png',
            '5D': '5D.png',
            '10H': '10H.png',
            '3H': '3H.png',
            '9C': '9C.png',
            '9S': '9S.png',
            '4H': '4H.png',
            '9D': '9D.png',
            'JS': 'JS.png',
            '4D': '4D.png',
            '7S': '7S.png',
            '8C': '8C.png',
            '10D': '10D.png',
            '4S': '4S.png',
            '10C': '10C.png',
            'AH': 'AH.png',
            '2H': '2H.png',
            '10S': '10S.png',
            '3S': '3S.png',
            '5H': '5H.png',
            'JD': 'JD.png',
            '6D': '6D.png',
            'KH': 'KH.png',
            '7D': '7D.png',
            '6H': '6H.png',
            'JC': 'JC.png',
            '2C': '2C.png',
            '8S': '8S.png',
            'AS': 'AS.png',
            'KD': 'KD.png',
            '5S': '5S.png',
            'QC': 'QC.png',
            '6S': '6S.png',
            'KC': 'KC.png',
            '4C': '4C.png',
            'KS': 'KS.png',
            'QS': 'QS.png',
            '7C': '7C.png',
            '2S': '2S.png',
            'QH': 'QH.png',
            '2D': '2D.png',
            'purple_back': 'purple_back.png',
            }



     