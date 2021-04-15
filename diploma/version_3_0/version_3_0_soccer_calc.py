import random
import traceback
from tkinter import *

root = Tk()
root.title('SOCCER Calculator')

buttons_1 = (('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'),
             )

buttons_2 = (('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
              '13', '14', '15', '16'),
             )

buttons_3 = (('♥', '♦', '♣', '♠'),
             )


buttons_4 = (('f 3-4-3', 'f 3-5-2', 'f 3-6-1', 'f 4-3-3', 'f 4-4-2', 'f 4-5-1', 'f 5-3-2', 'f 5-4-1'),
             )

f_input_list = ['f 3-4-3', 'f 3-5-2', 'f 3-6-1',
                'f 4-3-3', 'f 4-4-2', 'f 4-5-1', 'f 5-3-2', 'f 5-4-1']

activeStr = ''
name = ''
info = ''
check_flag = 0
a_match_formation = 10
match_stat = []
a_numbers_team = []
base_team = []
b_match_team = []


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


def tree(n):
    tr = '♠' + '\n'
    for i in range(n):
        tr += i*'*' + '*' + '\n'
    return tr


def soccer_info():
    add_info = "    В зависимости от ВЫБРАННОЙ НА МАТЧ ПОЗИЦИИ, игрок будет показывать силу, помноженную на модификатор флага/центра \n\
    Дополнительный фактор - НАСТРОЙ НА СЕЗОН. Условно обозначен в виде одной из мастей: ['♠', '♣', '♥', '♦'] \n\
    Основной смысл масти раскрывается на стратегическом уровне, а в данном примере моделируется тактика на один сезон \n\
    Если в линии (оборона, полузащита, атака по центру, левый фланг, правый фланг) несколько игроков одной масти, \n\
    то сила каждого из них возрастает на 50% за каждого - т.е. если червовых игроков трое, то каждый играет сильнее на 75%. \n\
    CM может получить бонусы и от полузащиты, и от атаки по центру \n\
            -------СОКРАЩЕНИЯ------- \n\
    GK голкипер, вратарь \n\
    LD левый защитник \n\
    SW свипер, последний защитник (всегда за спинами центральных, 'подчищает', с ним нельзя делать искусственный оффсайд) \n\
    CD центральный защитник \n\
    RD правый защитник \n\
    DM (CD+CM) опорный полузащитник (оттягивается в оборону из центра поля, часто начинает свои атаки точными передачами) \n\
    LM левый полузащитник \n\
    CM центральный полузащитник \n\
    RM правый полузащитник \n\
    LW (LM+LF) левый вингер (по левой бровке подключается к атакам, навешивает с фланга) \n\
    AM (CM+CF) центральный атакующий полузащитник, диспетчер (подключается к атакам из центра поля, отдаёт голевые передачи) \n\
    RW (RM+RF) правый вингер (по правой бровке подключается к атакам, навешивает с фланга) \n\
    LF левый форвард (врывается в штрафную с левого фланга) \n\
    CF центрфорвард (атакует ворота по центру, замыкает навесы с флангов) \n\
    RF правый форвард (врывается в штрафную с правого фланга) \n\
    ST страйкер (действует только в атаке, завершает ударами в упор, назад почти не отходит, часто попадает в оффсайд) \n\
    FR свободный художник (очень опытный игрок, которому позволено играть на своё усмотрение, обычно следует за мячом)"
    label.configure(text=add_info, font='Arial 14', justify=LEFT)


def click(text):
    global activeStr
    global a_match_formation
    global check_flag
    stack = []

    if text == 'ENTER':
        stack.append(label['text'])
        global name
        name = ''.join(stack)
        result = "Greetings, " + name + "! \n\n Choose ♥ to see your team, \n\n choose ♦ for game's tutorial, \n\n choose ♣ for last match's statistics, \n\n or choose ♠ to smile... \n\n or try to GOAL yourself!"
        label.configure(text=result, font='Arial 14')
        activeStr = ''
    elif text == '♦':
        soccer_info()
    elif text == '♠':
        label.configure(text=str(tree(13)), justify=CENTER)
    elif text == '♣':
        label_stat = ''
        for el in match_stat:
            if match_stat.index(el)%2 != 0:
                el += '\n'
            else:
                el += '       '
            label_stat += el
        label.configure(text=label_stat)
    elif text == '♥':
        global check_flag
        check_flag = 2
        b_team = [75, 100, 150, 225, 350]
        b_formations = ['5-4-1', '3-6-1', '3-4-3']
        b_team_formations = random.choice(b_formations)
        bb = random.choice(b_team)
        global b_match_team
        if b_team_formations == '5-4-1':
            b_match_team = [['GK', bb], ['SW', bb], ['LD', bb], ['CD_1', bb], ['CD_2', bb], [
                'RD', bb], ['LM', bb], ['CM_1', bb], ['AM', bb], ['RM', bb], ['CF', bb]]
        elif b_team_formations == '3-6-1':
            b_match_team = [['GK', bb], ['LD', bb], ['CD_1', bb], ['RD', bb], ['LW', bb], [
                'DM_1', bb], ['DM_2', bb], ['CM_1', bb], ['CM_2', bb], ['RW', bb], ['CF', bb]]
        else:  # '3-4-3'
            b_match_team = [['GK', bb], ['LD', bb], ['CD_1', bb], ['RD', bb], ['LM', bb], [
                'DM_1', bb], ['CM_1', bb], ['RM', bb], ['LF', bb], ['CF', bb], ['RF', bb]]

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
                if self.number in [1, 12]:  # goalkeepers
                    self.attack = random.randint(1, 50)
                    self.middle = random.randint(1, 75)
                    self.keeper = random.randint(51, 250)
                else:
                    self.attack = random.randint(1, 100)
                    self.middle = random.randint(1, 100)
                    self.keeper = random.randint(1, 100)

            def __repr__(self):
                return f'\n number {self.number} - attack {self.attack}, middle {self.middle}, defence {self.defence}, keeper {self.keeper}, left {self.left}, right {self.right}, center {self.center}, mood {self.mood}'

        global base_team
        base_team = [Player() for _ in range(16)]
        global str_base_team
        str_base_team = str(base_team)
        result = "Your opponet's average strength is " + \
            str(bb) + " with " + str(b_team_formations) + \
            " formation \n" + "\n Your team: \n" + \
            str_base_team[2:len(str_base_team)-1] + \
            "\n \n \n Choose formation for your team using special buttons..."
        label.configure(text=result, justify=LEFT)

    elif text in f_input_list:
        if check_flag == 2:
            check_flag = 3
            a_match_formation_number = f_input_list.index(text)
            global a_match_formation
            a_match_formation = a_formations[a_match_formation_number]
            str_a_match_formation = str(a_match_formation)
            result = "Your team formation is " + str_a_match_formation[1:len(str_a_match_formation)-1] + "\n \n Your team: \n" + \
                str_base_team[2:len(
                    str_base_team)-1] + "\n \n \n Choose 11 numbers of your players in accordance with position's list. For example: 1 2 10 ..."
            global info
            info = result
            label.configure(text=result, justify=LEFT)
        else:
            label.configure(text='Start the game first, please!')
            return

    elif check_flag == 3:    
        activeStr += (' ' + text)
        label.configure(text=info + '\n \n' + activeStr, justify=LEFT)
        global a_numbers_team
        try:
            a_numbers_team.append(int(text))
            if len(a_numbers_team) == 11:
                check_flag = 0
                activeStr = ''
                set_a_numbers_team = set(a_numbers_team)
                if len(set_a_numbers_team) != len(a_numbers_team):
                            label.configure(
                                text='All 11 players must be different! Technical defeat 0:3...')
                            return
                soccer_mood(a_numbers_team)
        except:
            # print(traceback.format_exc())
            label.configure(text='Choose only numbers!')

    elif text in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        activeStr += text
        label.configure(text=activeStr)
        if activeStr == 'GOAL':
            label.configure(text=match_stat, height=575, width=1200, image=photo)


def soccer_mood(a_numbers_team):
    selected_team = []
    a_match_team = []
    for a_number_pl in a_numbers_team:
        for base_pl in base_team:
            if a_number_pl == base_pl.number:
                selected_team.append(base_pl)

    for s_pl in selected_team:
        i = selected_team.index(s_pl)
        if a_match_formation[i] == 'GK':
            a_player = ['GK', s_pl.keeper, s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['SW', 'CD_1', 'CD_2']:
            a_player = [a_match_formation[i],
                        int(s_pl.defence * s_pl.center), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'LD':
            a_player = ['LD', int(s_pl.defence * s_pl.left), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'RD':
            a_player = ['RD', int(s_pl.defence * s_pl.right), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['DM_1', 'DM_2', 'CM_1', 'CM_2', 'AM']:
            a_player = [a_match_formation[i],
                        int(s_pl.middle * s_pl.center), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['LM', 'LW']:
            a_player = [a_match_formation[i],
                        int(s_pl.middle * s_pl.left), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] in ['RM', 'RW']:
            a_player = [a_match_formation[i],
                        int(s_pl.middle * s_pl.right), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'LF':
            a_player = ['LF', int(s_pl.attack * s_pl.left), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'CF':
            a_player = ['CF', int(s_pl.attack * s_pl.center), s_pl.mood]
            a_match_team.append(a_player)
        if a_match_formation[i] == 'RF':
            a_player = ['RF', int(s_pl.attack * s_pl.right), s_pl.mood]
            a_match_team.append(a_player)

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
                    # print(f'YESSS! {a_1[0]} {a_2[0]}')
                    # игрок получает +50% к силе за коллегу с таким же настроем на сезон
                    temp_a_1 = a_1[1] * 1.5
                    a_1[1] = int(temp_a_1)
    # print(a_match_team_improved)
    # print(b_match_team)
    soccer_gra(a_match_team_improved, b_match_team)


def soccer_gra(pl_match_team, cm_match_team):
    result_player = 0
    result_computer = 0
    global match_stat

    for minute in range(1, 92):
        if minute >= 91:
            print(match_stat)
            print(result_computer, result_player)
            if result_player > result_computer:
                result = 'You won! \n\n\n' + str(result_player) + ' : ' + str(result_computer)
                label.configure(text=result, justify=CENTER)
                soccer_end()
                return
            elif result_player < result_computer:
                result = 'You fought to the end... \n\n\n' + str(result_player) + ' : ' + str(result_computer)
                label.configure(text=result, justify=CENTER) 
                soccer_end()
                return
            elif result_player == result_computer:
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
                result_player += (p_p/10)
                result_computer += (p_c/10)
                if result_player > result_computer:
                    result = 'You won! \n \n' + str(int(result_player)) + ' : ' + str(int(result_computer)) + '\n \n by penalty \n \n' + str(p_p) + ' : ' + str(p_c)
                    label.configure(text=result, justify=CENTER)
                    soccer_end()
                    return
                elif result_player < result_computer:
                    result = 'You fought to the end... \n \n' + str(int(result_player)) + ' : ' + str(int(result_computer)) + '\n \n by penalty \n \n' + str(p_p) + ' : ' + str(p_c)
                    label.configure(text=result, justify=CENTER) 
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
            score_flag = 'PLAYER'
        else:  # result_1 == 'player_c' атаковать будет компьютер
            team_attack = cm_match_team
            team_defence = pl_match_team
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
                    match_stat.append(str(minute) + '. ---GOAL! Long distant strike by ' + str(distant_strike_player))
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + '. ---GOAL! Long distant strike by your opponent')
                    result_computer += 1
                    continue
            elif result_2 == ['player_def']:
                continue
            else:
                if score_flag == 'PLAYER':
                    match_stat.append(str(minute) + '. Long distant strike was saved by your keeper')
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + ". Long distant strike was saved by opponent's keeper")
                continue
        # попытка дальнего голевого паса за спины защитников
        if result_2 == ['distant_pass']:
            result_2 = random.randint(1, 100)
            if result_2 <= 5:
                result_3 = True  # следующий этап борьбы пропускается
            else:
                continue
        # попытка пройти центр поля, переиграв полузащиту
        if result_2 == ['attack_distant']:
            result_2 = random.choices(['att_2_sum', 'def_2_sum'], weights=[
                                      att_2_sum, def_2_sum])
            if result_2 == ['att_2_sum']:
                pass
            else:
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
                        match_stat.append(str(minute) + '. ---GOAL! Middle distant strike by' + str(middle_strike_player))
                        result_player += 1
                        continue
                    if score_flag == 'COMPUTER':
                        match_stat.append(str(minute) + '. ---GOAL! Middle distant strike by your opponent')
                        result_computer += 1
                        continue
                elif result_3 == ['player_def']:
                    continue
                else:
                    if score_flag == 'PLAYER':
                        match_stat.append(str(minute) + '. Middle distant strike was saved by your keeper')
                    if score_flag == 'COMPUTER':
                        match_stat.append(str(minute) + ". Middle distant strike was saved by opponent's keeper")
                    continue
            if result_3 == ['attack_middle']:  # попытка прорваться в штрафную площадь
                result_3 = random.choices(['att_3_sum', 'def_3_sum'], weights=[
                                          att_3_sum, def_3_sum])
                if result_3 == ['att_3_sum']:
                    pass
                else:
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
                    match_stat.append(str(minute) + '.---GOAL! After defence crush by' + str(close_attack_player))
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + '.---GOAL! After defence crush by your opponent')
                    result_computer += 1
                    continue
            else:
                if score_flag == 'PLAYER':
                    match_stat.append(str(minute) + '. Brilliant save after defence crush by your keeper!')
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + ". Save after defence crush by opponent's keeper")
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
                    match_stat.append(str(minute) + '. ---GOAL! After face-to-face by' + str(close_attack_player))
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + '. ---GOAL! After face-to-face by your opponent')
                    result_computer += 1
                    continue
            else:
                if score_flag == 'PLAYER':
                    match_stat.append(str(minute) + '. Brilliant save after face-to-face by your keeper!')
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + ". Save after face-to-face by opponent's keeper")
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
                    match_stat.append(str(minute) + '. ---GOAL! Close strike by' + str(close_attack_player))
                    result_player += 1
                    continue
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + '. ---GOAL! Close strike by your opponent')
                    result_computer += 1
                    continue
            elif result_4 == ['player_def']:
                continue
            else:
                if score_flag == 'PLAYER':
                    match_stat.append(str(minute) + '. Close strike was saved by your keeper!')
                if score_flag == 'COMPUTER':
                    match_stat.append(str(minute) + ". Close strike was saved by opponent's keeper")
                continue


def soccer_end():
    return


photo = PhotoImage(file = 'R:\\Daily\\results_13_14\\_version_3_0\\_verion_3_1\\football_PNG52764.png')
root['bg'] = 'grey'
label = Label(root, text='Enter your name or START SOCCER GAME witn ♥',
              font='Arial 14', height=26, width=109, bg='grey')
label.grid(row=0, column=0, columnspan=26, sticky="nsew")

button = Button(root, text='ENTER', bg='orange', relief='raised', font='Arial 9', height=2,
                command=lambda text='ENTER': click(text))
button.grid(row=1, column=14, columnspan=26, sticky="nsew")
for col in range(26):
    button = Button(root, height=2, font='Arial 9', text=buttons_1[0][col],
                        command=lambda row=2, col=col: click(buttons_1[0][col]))
    button.grid(row=2, column=col, sticky="nsew")
for col in range(16):
    button = Button(root, height=2, font='Arial 9', text=buttons_2[0][col],
                        command=lambda row=3, col=col: click(buttons_2[0][col]))
    button.grid(row=3, column=1+col, sticky="nsew")
for col in range(4):
    button = Button(root, height=2,  bg='orange', font='Arial 9', text=buttons_3[0][col],
                        command=lambda row=3, col=col: click(buttons_3[0][col]))
    button.grid(row=3, column=19+(col-1)*2, columnspan=2, sticky="nsew")
for col in range(8):
    button = Button(root, height=2, font='Arial 9',
                        text=buttons_4[0][col], bg='black', fg='white', relief='raised', command=lambda row=4, col=col: click(buttons_4[0][col]))
    button.grid(row=4, column=4+(col-1) *
                    3, columnspan=3, sticky="nsew")


root.mainloop()
