camp = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
repeated = []

print('These are the positions in this tic-tac-toe game:')
print('1|2|3')
print('4|5|6') 
print('7|8|9')

while True:
    p1 = int(input('Which position do you want to mark? [1-9] '))
    while p1 in repeated:
        p1 = int(input('This number has already been used, try another [1-9]: '))
    while p1 > 9 or p1 < 1:
        p1 = int(input('Invalid option, type again [1-9]: '))
    repeated.append(p1)
    camp[p1-1] = 'X'

    print(f'{camp[0]}|{camp[1]}|{camp[2]}')
    print(f'{camp[3]}|{camp[4]}|{camp[5]}') 
    print(f'{camp[6]}|{camp[7]}|{camp[8]}')

    if camp[0] == 'X' and camp[1] == 'X' and camp[2] == 'X':
        print('Player 1 is the winner!')
        break
    if camp[3] == 'X' and camp[4] == 'X' and camp[5] == 'X':
        print('Player 1 is the winner!')
        break
    if camp[6] == 'X' and camp[7] == 'X' and camp[8] == 'X':
        print('Player 1 is the winner!')
        break
    if camp[0] == 'X' and camp[3] == 'X' and camp[6] == 'X':
        print('Player 1 is the winner!')
        break
    if camp[1] == 'X' and camp[4] == 'X' and camp[7] == 'X':
        print('Player 1 is the winner!')
        break
    if camp[2] == 'X' and camp[5] == 'X' and camp[8] == 'X':
        print('Player 1 is the winner!')
        break
    if camp[0] == 'X' and camp[4] == 'X' and camp[8] == 'X':
        print('Player 1 is the winner!')
        break
    if camp[6] == 'X' and camp[4] == 'X' and camp[2] == 'X':
        print('Player 1 is the winner!')
        break
    if '_' not in camp:
        print('All the positions were filled and nobody won!')
        break

    p2 = int(input('Which position do you want to mark? [1-9] '))
    while p2 in repeated:
        p2 = int(input('This number has already been used, try another [1-9]: '))
    while p2 > 9 or p2 < 1:
        p2 = int(input('Invalid option, type again [1-9]: '))
    repeated.append(p2)
    camp[p2-1] = 'O'

    print(f'{camp[0]}|{camp[1]}|{camp[2]}')
    print(f'{camp[3]}|{camp[4]}|{camp[5]}') 
    print(f'{camp[6]}|{camp[7]}|{camp[8]}')

    if camp[0] == 'O' and camp[1] == 'O' and camp[2] == 'O':
        print('Player 2 is the winner!')
        break
    if camp[3] == 'O' and camp[4] == 'O' and camp[5] == 'O':
        print('Player 2 is the winner!')
        break
    if camp[6] == 'O' and camp[7] == 'O' and camp[8] == 'O':
        print('Player 2 is the winner!')
        break
    if camp[0] == 'O' and camp[3] == 'O' and camp[6] == 'O':
        print('Player 2 is the winner!')
        break
    if camp[1] == 'O' and camp[4] == 'O' and camp[7] == 'O':
        print('Player 2 is the winner!')
        break
    if camp[2] == 'O' and camp[5] == 'O' and camp[8] == 'O':
        print('Player 2 is the winner!')
        break
    if camp[0] == 'O' and camp[4] == 'O' and camp[8] == 'O':
        print('Player 2 is the winner!')
        break
    if camp[6] == 'O' and camp[4] == 'O' and camp[2] == 'O':
        print('Player 2 is the winner!')
        break
    if '_' not in camp:
        print('All the positions were filled and nobody won!')
        break
