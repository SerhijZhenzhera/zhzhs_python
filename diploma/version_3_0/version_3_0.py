import random

cup_round = ['1/16', '1/8', 'quarterfinal', 'semifinal', 'final', 'CUP']
mood = ['♠', '♣', '♥', '♦']
a_formations = [['GK', 'LD', 'CD_1', 'RD', 'LM', 'DM_1', 'CM_1', 'RM', 'LF', 'CF', 'RF'],
                ['GK', 'LD', 'CD_1', 'RD', 'LM', 'DM_1',
                    'CM_1', 'AM', 'RM', 'LF', 'RF'],
                ['GK', 'LD', 'CD_1', 'RD', 'LW', 'DM_1',
                    'DM_2', 'CM_1', 'CM_2', 'RW', 'CF'],
                ['GK', 'LD', 'CD_1', 'CD_2', 'RD', 'LM',
                    'CM_1', 'RM', 'LF', 'CF', 'RF'],
                ['GK', 'LD', 'CD_1', 'CD_2', 'RD', 'LM',
                    'CM_1', 'AM', 'RM', 'LF', 'RF'],
                ['GK', 'LD', 'CD_1', 'CD_2', 'RD', 'LM',
                    'DM_1', 'CM_1', 'AM', 'RM', 'CF'],
                ['GK', 'SW', 'LD', 'CD_1', 'CD_2',
                    'RD', 'LM', 'AM', 'RM', 'LF', 'RF'],
                ['GK', 'SW', 'LD', 'CD_1', 'CD_2', 'RD', 'LM', 'CM_1', 'AM', 'RM', 'CF']]


class Player:
    number = 0

    def __init__(self):
        self.__class__.number += 1
        self.number = self.__class__.number
        self.defence = random.randint(1, 100)
        self.left = random.randint(31, 200) / 100
        self.right = random.randint(31, 200) / 100
        self.center = random.randint(31, 200) / 100
        self.mood = random.choice(mood)
        if self.number in [1, 22, 23]:  # goalkeepers
            self.attack = random.randint(1, 50)
            self.middle = random.randint(1, 75)
            self.keeper = random.randint(51, 150)
        else:
            self.attack = random.randint(1, 100)
            self.middle = random.randint(1, 100)
            self.keeper = random.randint(1, 100)

    def __repr__(self):
        return f'\n number {self.number} - attack {self.attack}, middle {self.middle}, defence {self.defence}, keeper {self.keeper}, left {self.left}, right {self.right}, center {self.center}, mood {self.mood}'


def soccer_start():
    name = input(f'Hello! What is your name? ')
    soccer_decision(name, 0)


def soccer_decision(name, current_round, base_team=None):
    if cup_round[current_round] == 'CUP':
        print(f'Congratulations, {name}! You are a CUP holder')
        return
    start_input = input(
        f'Greetings, {name}! Are you ready to play in {cup_round[current_round]} ? Y/N ').lower()
    if current_round > 0:
        if start_input == 'y':
            soccer_team(name, current_round, base_team)
        elif start_input == 'n':
            print('Thank you!')
        else:
            print('Make the right choice, please!')
            soccer_decision(name, current_round, base_team)
    else:
        if start_input == 'y':
            soccer_team(name, current_round)
        elif start_input == 'n':
            print('Thank you!')
        else:
            print('Make the right choice, please!')
            soccer_decision(name, current_round)


def soccer_team(name, current_round, base_team=None):
    b_team = [75, 100, 150, 225, 350]
    b_formations = ['5-4-1', '3-6-1', '3-4-3']
    b_team_formations = random.choice(b_formations)
    bb = b_team[current_round]
    if b_team_formations == '5-4-1':
        b_match_team = [['GK', bb], ['SW', bb], ['LD', bb], ['CD_1', bb], ['CD_2', bb], [
            'RD', bb], ['LM', bb], ['CM_1', bb], ['AM', bb], ['RM', bb], ['CF', bb]]
    elif b_team_formations == '3-6-1':
        b_match_team = [['GK', bb], ['LD', bb], ['CD_1', bb], ['RD', bb], ['LW', bb], [
            'DM_1', bb], ['DM_2', bb], ['CM_1', bb], ['CM_2', bb], ['RW', bb], ['CF', bb]]
    else:  # '3-4-3'
        b_match_team = [['GK', bb], ['LD', bb], ['CD_1', bb], ['RD', bb], ['LM', bb], [
            'DM_1', bb], ['CM_1', bb], ['RM', bb], ['LF', bb], ['CF', bb], ['RF', bb]]


    # базовая информация о противнике и наборе своих игроков
    if current_round == 0:
        base_team = [Player() for _ in range(23)]
    print(
        f"Your opponet's average strength is {b_team[current_round]} with {b_team_formations} formation")
    print(
        f"Your players (numbers 1, 22 and 23 have advanced keeper's skills): {base_team}")
    print(f'Choose formation for your team: \n    number_1 3-4-3: {a_formations[0]} \n    number_2 3-5-2: {a_formations[1]} \n\
    number_3 3-6-1: {a_formations[2]} \n    number_4 4-3-3: {a_formations[3]} \n    number_5 4-4-2: {a_formations[4]} \n\
    number_6 4-5-1: {a_formations[5]} \n    number_7 5-3-2: {a_formations[6]} \n    number_8 5-4-1: {a_formations[7]}')

    # выбор тактической схемы на матч
    while True:
        a_match_formation_number = input(
            'Choose your formation number or Q from this CUP ').lower()
        if a_match_formation_number in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print(
                f"Your team's formation {a_formations[int(a_match_formation_number) - 1]}")
            a_match_formation = a_formations[int(a_match_formation_number) - 1]
            break
        elif a_match_formation_number == 'q':
            soccer_end()
            return
        else:
            print('Make the right choice, please!')
            continue

    # выбор 11 футболистов на матч
    print("Choose 11 numbers of your players in accordance with position's list. For example: 1 2 10. Or 0 to quit from this CUP")
    while True:
        try:
            a_numbers_team = [int(x) for x in input().split()]
            if a_numbers_team == [0]:
                soccer_end()
                return
            elif len(a_numbers_team) != 11:
                print('You need 11 players!')
                continue
            elif len(a_numbers_team) == 11:
                for _ in a_numbers_team:
                    if _ not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]:
                        print('Choose the correct number, please!')
                        checked = False
                    else:
                        checked = True
                set_a_numbers_team = set(a_numbers_team)
                if len(set_a_numbers_team) != len(a_numbers_team):
                    print('All 11 players must be different!')
                    checked = False
                if checked == False:
                    continue
        except:
            print('Make the right choice, please!')
            continue
        break

    selected_team = []
    a_match_team = []
    for a_number_pl in a_numbers_team:
        for base_pl in base_team:
            if a_number_pl == base_pl.number:
                selected_team.append(base_pl)
    # print(selected_team)

    for s_pl in selected_team:
        i = selected_team.index(s_pl)
        if a_match_formation[i] == 'GK':
            a_player = ['GK', s_pl.keeper, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['SW', 'CD_1', 'CD_2']:
            a_player = [a_match_formation[i],
                        s_pl.defence * s_pl.center, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'LD':
            a_player = ['LD', s_pl.defence * s_pl.left, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'RD':
            a_player = ['RD', s_pl.defence * s_pl.right, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['DM_1', 'DM_2', 'CM_1', 'CM_2', 'AM']:
            a_player = [a_match_formation[i],
                        s_pl.middle * s_pl.center, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['LM', 'LW']:
            a_player = [a_match_formation[i],
                        s_pl.middle * s_pl.left, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['RM', 'RW']:
            a_player = [a_match_formation[i],
                        s_pl.middle * s_pl.right, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'LF':
            a_player = ['LF', s_pl.attack * s_pl.left, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'CF':
            a_player = ['CF', s_pl.attack * s_pl.center, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'RF':
            a_player = ['RF', s_pl.attack * s_pl.right, s_pl.mood]
            a_match_team.append(a_player)
    print('PLAYER team:', a_match_team)
    print('COMPUTER team:', b_match_team)
    soccer_mood(a_match_team, b_match_team, name, current_round, base_team)


def soccer_mood(a_match_team, b_match_team, name, current_round, base_team):

    a_match_team_improved = a_match_team
    for a_1 in a_match_team_improved:
        for a_2 in a_match_team_improved:
            check_1_1 = (a_1[0] != a_2[0])  # чтобы игрок не усиливал сам себя
            check_1_2 = (a_1[2] == a_2[2])  # если одинаковый настрой на сезон
            check_2 = (a_1[0] in ['GK', 'SW', 'CD_1', 'CD_2']) and (
                a_2[0] in ['GK', 'SW', 'CD_1', 'CD_2'])  # коллеги по обороне
            check_3 = (a_1[0] in ['DM_1', 'DM_2', 'CM_1', 'CM_2']) and (
                a_2[0] in ['DM_1', 'DM_2', 'CM_1', 'CM_2'])  # коллеги по опорной зоне
            check_4 = (a_1[0] in ['CM_1', 'CM_2', 'AM', 'CF']) and (
                a_2[0] in ['CM_1', 'CM_2', 'AM', 'CF'])  # коллеги по центру атаки
            check_5 = (a_1[0] in ['LD', 'LM', 'LF']) and (
                a_2[0] in ['LD', 'LM', 'LF'])  # коллеги по левому флангу
            check_6 = (a_1[0] in ['RD', 'RM', 'RF']) and (
                a_2[0] in ['RD', 'RM', 'RF'])  # коллеги по правому флангу
            if all([check_1_1, check_1_2]):
                if any([check_2, check_3, check_4, check_5, check_6]):
                    print(f'YESSS! {a_1[0]} {a_2[0]}')
                    # игрок получает +25% к силе за коллегу с таким же настроем на сезон
                    a_1[1] *= 1.25

    print(f'Improved PLAYER team: {a_match_team_improved}')
    soccer_gra(a_match_team_improved, b_match_team,
               name, current_round, base_team)


def soccer_gra(pl_match_team, cm_match_team, name, current_round, base_team):
    result_player = 0
    result_computer = 0

    for minute in range(1, 92):
        if minute >= 6:
            print(f'Match result {result_player} : {result_computer}')
            if result_player == result_computer:
                penalty_list = [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [4, 1], [
                    3, 2], [4, 2], [4, 3], [5, 3], [5, 4], [6, 5], [7, 6]]
                penalty_result = random.choice(['player', 'computer'])
                penalty_score = random.choice(penalty_list)
                if penalty_result == 'player':
                    p_p = penalty_score[0]
                    p_c = penalty_score[1]
                if penalty_result == 'computer':
                    p_p = penalty_score[1]
                    p_c = penalty_score[0]
                print(f'By penalty: {p_p} : {p_c}')
                result_player += (p_p/10)
                result_computer += (p_c/10)
            if result_player > result_computer:
                print('You won!')
                soccer_decision(name, current_round + 1, base_team)
                break
            else:
                print('You fought to the end...')
                soccer_end()
                return

            # ВЫБОР АТАКУЮЩЕЙ СТОРОНЫ
        middle_1_list = ['DM_1', 'DM_2', 'CM_1',
                         'CM_2', 'LM', 'RM', 'LW', 'RW', 'AM']
        pl_1_list = []
        cm_1_list = []
        for pl in pl_match_team:
            if pl[0] in middle_1_list:
                pl_1_list.append(pl[1])
                # выбирается один из игроков
                player_p = random.choice(pl_1_list)
                for pl in pl_match_team:
                    if player_p == pl[1]:
                        start_pl = pl
        for pl in cm_match_team:
            if pl[0] in middle_1_list:
                cm_1_list.append(pl[1])
                # выбирается один из игроков
                player_c = random.choice(cm_1_list)
        result_1 = random.choices(['player_p', 'player_c'], weights=[
                                  player_p, player_c])  # выбирается выигравшая сторона
        if result_1 == ['player_p']:  # атаковать будет человек
            team_attack = pl_match_team
            team_defence = cm_match_team
            print(f'{minute}. Player {start_pl} started the attack')
            score_flag = 'PLAYER'
        else:  # result_1 == 'player_c' атаковать будет компьютер
            team_attack = cm_match_team
            team_defence = pl_match_team
            print(f'{minute}. Your opponent started the attack')
            score_flag = 'COMPUTER'

        # БОРЬБА В ЦЕНТРЕ ПОЛЯ
        result_3 = False  # переменная следующего этапа борьбы, который можно обойти дальним пасом
        attack_2_list = ['CM_1', 'CM_2', 'LM', 'RM', 'LW', 'RW', 'AM']
        defence_2_list = ['DM_1', 'DM_2', 'CM_1', 'CM_2', 'LM', 'RM']
        att_2_list = []
        att_2_sum = 0
        def_2_list = []
        def_2_sum = 0
        def_gk = team_defence[0]
        for pl in team_attack:
            if pl[0] in attack_2_list:
                att_2_list.append(pl[1])
                att_2_sum += pl[1]
        for pl in team_defence:
            if pl[0] in defence_2_list:
                def_2_list.append(pl[1])
                def_2_sum += pl[1]
        distant_strike = 10
        distant_pass = 20
        attack_distant = 70
        # берётся вратарь обороняющейся стороны (его сила может возрасти втрое и вдвое)
        player_gk = def_gk[1]
        # выбирается действие атакующей стороной в центре поля
        result_2 = random.choices(['distant_strike', 'distant_pass', 'attack_distant'], weights=[
                                  distant_strike, distant_pass, attack_distant])
        if result_2 == ['distant_strike']:
            # выбирается бьющий игрок (от его силы будет взята треть)
            player_att = random.choice(att_2_list)
            if score_flag == 'PLAYER':
                for pl in team_attack:
                    if player_att == pl[1]:
                        distant_strike_player = pl
            # выбирается мешающий ему игрок
            player_def = random.choice(def_2_list)
            result_2 = random.choices(['player_att', 'player_def', 'gk'], weights=[
                                      player_att/3, player_def, player_gk*3])  # попытка дальнего удара
            if result_2 == ['player_att']:
                if score_flag == 'PLAYER':
                    print(
                        f'---GOAL! Long distant strike by {distant_strike_player}')
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    print('---GOAL! Long distant strike by your opponent')
                    result_computer += 1
                    continue
            elif result_2 == ['player_def']:
                print('Long distant strike was blocked')
                continue
            else:
                print('Long distant strike was saved by keeper')
                continue
        # попытка дальнего голевого паса за спины защитников
        if result_2 == ['distant_pass']:
            result_2 = random.randint(1, 100)
            if result_2 <= 5:
                print('Distant pass!')
                result_3 = True  # следующий этап борьбы пропускается
            else:
                print('Distant pass failed')
                continue
        # попытка пройти центр поля, переиграв полузащиту
        if result_2 == ['attack_distant']:
            result_2 = random.choices(['att_2_sum', 'def_2_sum'], weights=[
                                      att_2_sum, def_2_sum])
            if result_2 == ['att_2_sum']:
                print('Attack passed middle zone!')
            else:
                print('The ball is intercepted in the center')
                continue

        # БОРЬБА НА ПОЛОВИНЕ ПОЛЯ ПРОТИВНИКА
        if not result_3:  # если полузащита не была переброшена дальним пасом
            defence_3_list = ['DM_1', 'DM_2', 'CD_1', 'CD_2', 'LD', 'RD']
            att_3_list = att_2_list
            att_3_sum = att_2_sum
            def_3_list = []
            def_3_sum = 0
            for pl in team_defence:
                if pl[0] in defence_3_list:
                    def_3_list.append(pl[1])
                    def_3_sum += pl[1]
            middle_strike = 30
            attack_middle = 70
            # выбирается действие атакующей стороной на половине поля противника
            result_3 = random.choices(['middle_strike', 'attack_middle'], weights=[
                                      middle_strike, attack_middle])
            if result_3 == ['middle_strike']:
                # выбирается бьющий игрок (от его силы будет взята половина)
                player_att = random.choice(att_3_list)
                if score_flag == 'PLAYER':
                    for pl in team_attack:
                        if player_att == pl[1]:
                            middle_strike_player = pl
                # выбирается мешающий ему игрок
                player_def = random.choice(def_3_list)
                result_3 = random.choices(['player_att', 'player_def', 'gk'], weights=[
                                          player_att/2, player_def, player_gk*2])  # попытка дальнего удара
                if result_3 == ['player_att']:
                    if score_flag == 'PLAYER':
                        print(
                            f'---GOAL! Middle distant strike by {middle_strike_player}')
                        result_player += 1
                        continue
                    if score_flag == 'COMPUTER':
                        print('---GOAL! Middle distant strike by your opponent')
                        result_computer += 1
                        continue
                elif result_3 == ['player_def']:
                    print('Middle distant strike was blocked')
                    continue
                else:
                    print('Middle distant strike was saved by keeper')
                    continue
            if result_3 == ['attack_middle']:  # попытка прорваться в штрафную площадь
                result_3 = random.choices(['att_3_sum', 'def_3_sum'], weights=[
                                          att_3_sum, def_3_sum])
                if result_3 == ['att_3_sum']:
                    print('Attack reached penalty area!')
                else:
                    print('The ball is intercepted near penalty area')
                    continue

        # БОРЬБА В ШТРАФНОЙ ПЛОЩАДИ
        attack_4_list = ['LW', 'RW', 'AM', 'LF', 'RF', 'CF']
        defence_4_list = ['DM_1', 'DM_2', 'CD_1', 'CD_2',
                          'LD', 'RD', 'SW']  # обычная группа защиты
        defence_4_1_list = ['SW', 'GK']  # на случай провала обороны
        att_4_list = []
        att_4_sum = 0
        def_4_list = []
        def_4_sum = 0
        def_4_1_list = []
        def_4_1_sum = 0
        for pl in team_attack:
            if pl[0] in attack_4_list:
                att_4_list.append(pl[1])
                att_4_sum += pl[1]
        for pl in team_defence:
            if pl[0] in defence_4_list:
                def_4_list.append(pl[1])
                def_4_sum += pl[1]
        for pl in team_defence:
            if pl[0] in defence_4_1_list:
                def_4_1_list.append(pl[1])
                def_4_1_sum += pl[1]
        defence_crush = 5*(att_4_sum / def_4_sum)
        face_to_face = 10
        close_strike = 85
        # выбирается результат борьбы у ворот
        result_4 = random.choices(['defence_crush', 'face_to_face', 'close_strike'], weights=[
                                  defence_crush, face_to_face, close_strike])
        if result_4 == ['defence_crush']:  # провал обороны с выходом группы атаки на ворота
            result_4 = random.choices(['att_4_sum', 'def_4_1_sum'], weights=[
                                      att_4_sum, def_4_1_sum])
            if result_4 == 'att_4_sum':
                if score_flag == 'PLAYER':  # случайный выбор автора голевого удара
                    player_goal = random.choice(attack_4_list)
                    for pl in team_attack:
                        if player_goal == pl[1]:
                            close_attack_player = pl
                    print(
                        f'---GOAL! After defence crush by {close_attack_player}')
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    print('---GOAL! After defence crush by your opponent')
                    result_computer += 1
                    continue
            else:
                print('Brilliant save after defence crush!')
                continue
        if result_4 == ['face_to_face']:  # выбирается игрок, вышедший на вратаря
            player_att = random.choice(att_4_list)
            if score_flag == 'PLAYER':
                for pl in team_attack:
                    if player_att == pl[1]:
                        close_attack_player = pl
            result_4 = random.choices(['player_att', 'gk'], weights=[
                                      player_att, player_gk])  # поединок с вратарём
            if result_4 == ['player_att']:
                if score_flag == 'PLAYER':
                    print(
                        f'---GOAL! After face-to-face by {close_attack_player}')
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    print('---GOAL! After face-to-face by your opponent')
                    result_computer += 1
                    continue
            else:
                print('Brilliant save after face-to-face!')
                continue
        if result_4 == ['close_strike']:  # выбирается бьющий игрок
            player_att = random.choice(att_4_list)
            if score_flag == 'PLAYER':
                for pl in team_attack:
                    if player_att == pl[1]:
                        close_attack_player = pl
            # выбирается мешающий ему игрок (свипер страхует либо его сила удваивается)
            player_def = random.choice(def_4_list)
            result_4 = random.choices(['player_att', 'player_def', 'def_4_1_sum'], weights=[
                                      player_att, player_def, def_4_1_sum])  # попытка ударить в упор
            if result_4 == ['player_att']:
                if score_flag == 'PLAYER':
                    print(f'---GOAL! Close strike by {close_attack_player}')
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    print('---GOAL! Close strike by your opponent')
                    result_computer += 1
                    continue
            elif result_4 == ['player_def']:
                print('Close strike was blocked')
                continue
            else:
                print('Close strike was saved')
                continue


def soccer_end():
    print("Let's have a rest...")
    return


if __name__ == '__main__':

    soccer_start()
