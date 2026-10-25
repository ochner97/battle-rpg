#FAZER SISTEMA DE STATUS
#FAZER SISTEMA DE TENDÊNCIA

import random

def main():
    username = ''

    user = {'hp': 100, 'attacks': 100, 'heal_hp': 1, 'name': username, 'shield': [2, False]}
    pc = {'hp': 100, 'attacks': 100, 'heal_hp': 1, 'name': 'PC', 'shield': [1, False]}

    while True:
        print('Bem-vindo, nobre aventureiro! Qual o seu nome?')
        user['name'] = input('->  ')
        print('*** Seja bem-vindo {}! ***'.format(user['name']))
        print('É sua vez de jogar e você tem algumas escolhas...\nO seu oponente é o {}.'.format(pc['name'])) 
        print('O que deseja fazer? Digite: ATACAR para ataque;\nCURAR para curar o HP;\nESCUDO para ativar o escudo')

        while user['hp'] > 0 and pc['hp'] > 0: #enquanto os dois tiverem hp, segue o duelo
            cmd = input('->  ')
            if cmd == 'atacar':
                attack(user, pc)
            elif cmd == 'escudo':
                if user['shield'][0] > 0 and user['shield'][1] == False:
                    user['shield'][0] -= 1
                    user['shield'][1] = True
                    print('Escudo ativo!')
                elif user['shield'][1] == True:
                    print('Escudo já ativo.')
                else:
                    print('Não tem mais escudos.')
                continue
            elif cmd == 'curar':
                heal(user)
                user['heal_hp'] -= 1
                continue

            #JOGADAS ALEATÓRIAS DO PC
            if random.random() < 0.5 and pc['hp'] > 0: #contra ataque aleatório
                attack(pc, user)
                continue
            elif random.random() < 0.7 and pc['shield'][0] > 0 and pc['shield'][1] == False and pc['hp'] > 0: #ativação escudo do pc aleatória
                pc['shield'][0] -= 1
                pc['shield'][1] = True
                print('{} ativou o escudo.'.format(pc['name']))
            elif random.random() < 0.7 and pc['heal_hp'] > 0: #cura hp aleatória
                heal(pc)

        if user['hp'] - pc['hp'] > 0: 
            print('{} vence!'.format(user['name']))
        else:
            print('{} vence!'.format(pc['name']))

        break

def attack(attacker, defender): #SISTEMA DE ATAQUE
    if attacker['attacks'] > 0:
        print('-----')
        print('{} ataca!'.format(attacker['name']))
        attacker['attacks'] -= 1 
        #tendency = [random.choice(['y', 'n']) for i in range(10)] #TENDENCIA ** FAZER TENDENCIA FRACA, MEDIA, AGRESSIVA ???
        #if random.choice(tendency) == 'y':
        defense(defender)

        print('{} tem {} ataques restando'.format(attacker['name'], attacker['attacks']))
        defender['hp'] = clamp(0, 100, defender['hp'])
        print('*** HP restante {}: {} ***'.format(defender['name'], defender['hp']))
    else:
        print('{} não tem mais ataques'.format(attacker['name']))

def defense(defender): #SISTEMA DE DEFESA
    ranges = {'lower': random.randrange(1, 10), 
              'medium': random.randrange(11, 20), 
              'higher': random.randrange(20, 30)}

    opponents = ['Fantasma', 'Vampiro', 'Lobisomem', 'PC']


    print('{} se defendeu!'.format(defender['name']))

    if random.random() < 0.2: #20% de chance hit crítico
        defender['hp'] -= ranges['higher']
        print('Hit crítico! Dano causado: {}'.format(ranges['higher']))
        defender['shield'][1] = False #futuramente verificar se o escudo já está inativo e não desativar
    elif defender['shield'][1] == False:
        defender['hp'] -= ranges['medium']
    else:
        defender['hp'] -= ranges['lower']

def heal(attacker): #SISTEMA DE CURA HP
    if attacker['heal_hp'] > 0:
        attacker['hp'] += 10
        attacker['hp'] = clamp(0, 100, attacker['hp'])
        print('Curando {}... HP restaurada para {}'.format(attacker['name'], attacker['hp']))
        attacker['heal_hp'] -= 1
    else:
        print('{} não tem mais poção de cura.'.format(attacker['name']))


def clamp(floor, ceiling, quant): #clamping
    return max(floor, min(quant, ceiling))

main()