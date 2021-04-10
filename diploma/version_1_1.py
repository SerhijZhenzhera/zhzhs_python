import random

cup_round = ['1/16', '1/8', 'quarterfinal', 'semifinal', 'final', 'CUP']
mood = ['♠', '♣', '♥', '♦']
b_team = [75, 100, 150, 225, 350]
b_formations = ['5-4-1', '3-6-1', '3-4-3']
gk, sw, ld, cd_1, cd_2, rd, dm_1, dm_2, lm, cm_1, cm_2, rm, lw, am, rw, lf, cf, rf = \
    'GK', 'SW', 'LD', 'CD_1', 'CD_2', 'RD', 'DM_1', 'DM_2', 'LM', 'CM_1', 'CM_2', 'RM', 'LW', 'AM', 'RW', 'LF', 'CF', 'RF'
a_formations = [[gk, ld, cd_1, rd, lm, dm_1, cm_1, rm, lf, cf, rf],
                [gk, ld, cd_1, rd, lm, dm_1, cm_1, am, rm, lf, rf],
                [gk, ld, cd_1, rd, lw, dm_1, dm_2, cm_1, cm_2, rw, cf],
                [gk, ld, cd_1, cd_2, rd, lm, cm_1, rm, lf, cf, rf],
                [gk, ld, cd_1, cd_2, rd, lm, cm_1, am, rm, lf, rf],
                [gk, ld, cd_1, cd_2, rd, lm, dm_1, cm_1, am, rm, cf],
                [gk, sw, ld, cd_1, cd_2, rd, lm, am, rm, lf, rf],
                [gk, sw, ld, cd_1, cd_2, rd, lm, cm_1, am, rm, cf]]


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
    print(base_team)
    b_team_formations = random.choice(b_formations)
    if b_team_formations == '5-4-1':
        bb = b_sw = b_ld = b_cd_1 = b_cd_2 = b_rd = b_lm = b_cm_1 = b_am = b_rm = b_cf = b_team[
            current_round]
        b_match_team = [['GK', bb], ['SW', bb], ['LD', bb], ['CD_1', bb], ['CD_2', bb], [
            'RD', bb], ['LM', bb], ['CM_1', bb], ['AM', bb], ['RM', bb], ['CF', bb]]
    elif b_team_formations == '3-6-1':
        bb = b_ld = b_cd_1 = b_rd = b_lw = b_dm_1 = b_dm_2 = b_cm_1 = b_cm_2 = b_rw = b_cf = b_team[
            current_round]
        b_match_team = [['GK', bb], ['LD', bb], ['CD_1', bb], ['RD', bb], ['LW', bb], [
            'DM_1', bb], ['DM_2', bb], ['CM_1', bb], ['CM_2', bb], ['RW', bb], ['CF', bb]]
    else:  # '3-4-3'
        bb = b_ld = b_cd_1 = b_rd = b_lm = b_dm_1 = b_cm_1 = b_rm = b_lf = b_cf_1 = b_rf = b_team[
            current_round]
        b_match_team = [['GK', bb], ['LD', bb], ['CD_1', bb], ['RD', bb], ['LM', bb], [
            'DM_1', bb], ['CM_1', bb], ['RM', bb], ['LF', bb], ['CF', bb], ['RF', bb]]

    if current_round == 0:
        # goalkeepers:
        a_pl_1 = [1, random.randint(1, 51), random.randint(1, 76), random.randint(1, 101), random.randint(51, 151), random.randint(
        31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_22 = [22, random.randint(1, 51), random.randint(1, 76), random.randint(1, 101), random.randint(
        51, 151), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_23 = [23, random.randint(1, 51), random.randint(1, 76), random.randint(1, 101), random.randint(
        51, 151), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        # outfield players:
        a_pl_2 = [2, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_3 = [3, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_4 = [4, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_5 = [5, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_6 = [6, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_7 = [7, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_8 = [8, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_9 = [9, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_10 = [10, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_11 = [11, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_12 = [12, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_13 = [13, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_14 = [14, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_15 = [15, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_16 = [16, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_17 = [17, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_18 = [18, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_19 = [19, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_20 = [20, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        a_pl_21 = [21, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(
        1, 101), random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.randint(31, 201) / 100, random.choice(mood)]
        base_team = [a_pl_1, a_pl_2, a_pl_3, a_pl_4, a_pl_5, a_pl_6, a_pl_7, a_pl_8, a_pl_9, a_pl_10, a_pl_11,
                 a_pl_12, a_pl_13, a_pl_14, a_pl_15, a_pl_16, a_pl_17, a_pl_18, a_pl_19, a_pl_20, a_pl_21, a_pl_22, a_pl_23]

    if current_round > 0:
        # goalkeepers:
        a_pl_1, a_pl_22, a_pl_23 = base_team[0], base_team[21], base_team[22]
        # outfield players:
        a_pl_2 = base_team[1]
        a_pl_3 = base_team[2]
        a_pl_4 = base_team[3]
        a_pl_5 = base_team[4]
        a_pl_6 = base_team[5]
        a_pl_7 = base_team[6]
        a_pl_8 = base_team[7]
        a_pl_9 = base_team[8]
        a_pl_10 = base_team[9]
        a_pl_11 = base_team[10]
        a_pl_12 = base_team[11]
        a_pl_13 = base_team[12]
        a_pl_14 = base_team[13]
        a_pl_15 = base_team[14]
        a_pl_16 = base_team[15]
        a_pl_17 = base_team[16]
        a_pl_18 = base_team[17]
        a_pl_19 = base_team[18]
        a_pl_20 = base_team[19]
        a_pl_21 = base_team[20]

    print(f'Your keepers: \n\
        number {a_pl_1[0]} - attack {a_pl_1[1]}, middle {a_pl_1[2]}, defence {a_pl_1[3]}, keeper {a_pl_1[4]}, left {a_pl_1[5]}, right {a_pl_1[6]}, center {a_pl_1[7]}, mood {a_pl_1[8]} \n\
        number {a_pl_22[0]} - attack {a_pl_22[1]}, middle {a_pl_22[2]}, defence {a_pl_22[3]}, keeper {a_pl_22[4]}, left {a_pl_22[5]}, right {a_pl_22[6]}, center {a_pl_22[7]}, mood {a_pl_22[8]} \n\
        number {a_pl_23[0]} - attack {a_pl_23[1]}, middle {a_pl_23[2]}, defence {a_pl_23[3]}, keeper {a_pl_23[4]}, left {a_pl_23[5]}, right {a_pl_23[6]}, center {a_pl_23[7]}, mood {a_pl_23[8]}')

    print(f'Your players: \n\
        number {a_pl_2[0]} - attack {a_pl_2[1]}, middle {a_pl_2[2]}, defence {a_pl_2[3]}, keeper {a_pl_2[4]}, left {a_pl_2[5]}, right {a_pl_2[6]}, center {a_pl_2[7]}, mood {a_pl_2[8]} \n\
        number {a_pl_3[0]} - attack {a_pl_3[1]}, middle {a_pl_3[2]}, defence {a_pl_3[3]}, keeper {a_pl_3[4]}, left {a_pl_3[5]}, right {a_pl_3[6]}, center {a_pl_3[7]}, mood {a_pl_3[8]} \n\
        number {a_pl_4[0]} - attack {a_pl_4[1]}, middle {a_pl_4[2]}, defence {a_pl_4[3]}, keeper {a_pl_4[4]}, left {a_pl_4[5]}, right {a_pl_4[6]}, center {a_pl_4[7]}, mood {a_pl_4[8]} \n\
        number {a_pl_5[0]} - attack {a_pl_5[1]}, middle {a_pl_5[2]}, defence {a_pl_5[3]}, keeper {a_pl_5[4]}, left {a_pl_5[5]}, right {a_pl_5[6]}, center {a_pl_5[7]}, mood {a_pl_5[8]} \n\
        number {a_pl_6[0]} - attack {a_pl_6[1]}, middle {a_pl_6[2]}, defence {a_pl_6[3]}, keeper {a_pl_6[4]}, left {a_pl_6[5]}, right {a_pl_6[6]}, center {a_pl_6[7]}, mood {a_pl_6[8]} \n\
        number {a_pl_7[0]} - attack {a_pl_7[1]}, middle {a_pl_7[2]}, defence {a_pl_7[3]}, keeper {a_pl_7[4]}, left {a_pl_7[5]}, right {a_pl_7[6]}, center {a_pl_7[7]}, mood {a_pl_7[8]} \n\
        number {a_pl_8[0]} - attack {a_pl_8[1]}, middle {a_pl_8[2]}, defence {a_pl_8[3]}, keeper {a_pl_8[4]}, left {a_pl_8[5]}, right {a_pl_8[6]}, center {a_pl_8[7]}, mood {a_pl_8[8]} \n\
        number {a_pl_9[0]} - attack {a_pl_9[1]}, middle {a_pl_9[2]}, defence {a_pl_9[3]}, keeper {a_pl_9[4]}, left {a_pl_9[5]}, right {a_pl_9[6]}, center {a_pl_9[7]}, mood {a_pl_9[8]} \n\
        number {a_pl_10[0]} - attack {a_pl_10[1]}, middle {a_pl_10[2]}, defence {a_pl_10[3]}, keeper {a_pl_10[4]}, left {a_pl_10[5]}, right {a_pl_10[6]}, center {a_pl_10[7]}, mood {a_pl_10[8]} \n\
        number {a_pl_11[0]} - attack {a_pl_11[1]}, middle {a_pl_11[2]}, defence {a_pl_11[3]}, keeper {a_pl_11[4]}, left {a_pl_11[5]}, right {a_pl_11[6]}, center {a_pl_11[7]}, mood {a_pl_11[8]} \n\
        number {a_pl_12[0]} - attack {a_pl_12[1]}, middle {a_pl_12[2]}, defence {a_pl_12[3]}, keeper {a_pl_12[4]}, left {a_pl_12[5]}, right {a_pl_12[6]}, center {a_pl_12[7]}, mood {a_pl_12[8]} \n\
        number {a_pl_13[0]} - attack {a_pl_13[1]}, middle {a_pl_13[2]}, defence {a_pl_13[3]}, keeper {a_pl_13[4]}, left {a_pl_13[5]}, right {a_pl_13[6]}, center {a_pl_13[7]}, mood {a_pl_13[8]} \n\
        number {a_pl_14[0]} - attack {a_pl_14[1]}, middle {a_pl_14[2]}, defence {a_pl_14[3]}, keeper {a_pl_14[4]}, left {a_pl_14[5]}, right {a_pl_14[6]}, center {a_pl_14[7]}, mood {a_pl_14[8]} \n\
        number {a_pl_15[0]} - attack {a_pl_15[1]}, middle {a_pl_15[2]}, defence {a_pl_15[3]}, keeper {a_pl_15[4]}, left {a_pl_15[5]}, right {a_pl_15[6]}, center {a_pl_15[7]}, mood {a_pl_15[8]} \n\
        number {a_pl_16[0]} - attack {a_pl_16[1]}, middle {a_pl_16[2]}, defence {a_pl_16[3]}, keeper {a_pl_16[4]}, left {a_pl_16[5]}, right {a_pl_16[6]}, center {a_pl_16[7]}, mood {a_pl_16[8]} \n\
        number {a_pl_17[0]} - attack {a_pl_17[1]}, middle {a_pl_17[2]}, defence {a_pl_17[3]}, keeper {a_pl_17[4]}, left {a_pl_17[5]}, right {a_pl_17[6]}, center {a_pl_17[7]}, mood {a_pl_17[8]} \n\
        number {a_pl_18[0]} - attack {a_pl_18[1]}, middle {a_pl_18[2]}, defence {a_pl_18[3]}, keeper {a_pl_18[4]}, left {a_pl_18[5]}, right {a_pl_18[6]}, center {a_pl_18[7]}, mood {a_pl_18[8]} \n\
        number {a_pl_19[0]} - attack {a_pl_19[1]}, middle {a_pl_19[2]}, defence {a_pl_19[3]}, keeper {a_pl_19[4]}, left {a_pl_19[5]}, right {a_pl_19[6]}, center {a_pl_19[7]}, mood {a_pl_19[8]} \n\
        number {a_pl_20[0]} - attack {a_pl_20[1]}, middle {a_pl_20[2]}, defence {a_pl_20[3]}, keeper {a_pl_20[4]}, left {a_pl_20[5]}, right {a_pl_20[6]}, center {a_pl_20[7]}, mood {a_pl_20[8]} \n\
        number {a_pl_21[0]} - attack {a_pl_21[1]}, middle {a_pl_21[2]}, defence {a_pl_21[3]}, keeper {a_pl_21[4]}, left {a_pl_21[5]}, right {a_pl_21[6]}, center {a_pl_21[7]}, mood {a_pl_21[8]}')

    print(
        f"Your opponet's average strength is {b_team[current_round]} with {b_team_formations} formation")
    print(f'Choose formation for your team: \n    number_1 3-4-3: {a_formations[0]} \n    number_2 3-5-2: {a_formations[1]} \n\
    number_3 3-6-1: {a_formations[2]} \n    number_4 4-3-3: {a_formations[3]} \n    number_5 4-4-2: {a_formations[4]} \n\
    number_6 4-5-1: {a_formations[5]} \n    number_7 5-3-2: {a_formations[6]} \n    number_8 5-4-1: {a_formations[7]}')
    a_match_formation_number = int(input('Choose your formation number '))
    print(
        f"Your team's formation {a_formations[a_match_formation_number - 1]}")
    a_match_formation = a_formations[a_match_formation_number - 1]

    '''
    https://overcoder.net/q/получить-список-чисел-в-качестве-ввода-от-пользователя
    a = [int(x) for x in input().split()]
    -----
    s = input()
    numbers = list(map(int, s.split()))
    '''

    print("Choose 11 numbers of your players in accordance with position's list. For example: 1 2 10")
    a_numbers_team = [int(x) for x in input().split()]

    ch_team = []
    a_match_team = []

    for a_n_pl in a_numbers_team:
        for base_pl in base_team:
            if a_n_pl == base_pl[0]:
                ch_team.append(base_pl)
    # print(ch_team)

    for ch_pl in ch_team:
        i = ch_team.index(ch_pl)
        if a_match_formation[i] == gk:
            a_player = ['GK', base_pl[4], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == sw:
            a_player = ['SW', base_pl[3] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == ld:
            a_player = ['LD', base_pl[3] * base_pl[5], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == cd_1:
            a_player = ['CD_1', base_pl[3] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == cd_2:
            a_player = ['CD_2', base_pl[3] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == rd:
            a_player = ['RD', base_pl[3] * base_pl[6], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == dm_1:
            a_player = ['DM_1', base_pl[2] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == dm_2:
            a_player = ['DM_2', base_pl[2] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == lm:
            a_player = ['LM', base_pl[2] * base_pl[5], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == cm_1:
            a_player = ['CM_1', base_pl[2] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == cm_2:
            a_player = ['CM_2', base_pl[2] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == rm:
            a_player = ['RM', base_pl[2] * base_pl[6], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == lw:
            a_player = ['LW', base_pl[2] * base_pl[5], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == am:
            a_player = ['AM', base_pl[2] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == rw:
            a_player = ['RW', base_pl[2] * base_pl[6], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == lf:
            a_player = ['LF', base_pl[1] * base_pl[5], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == cf:
            a_player = ['CF', base_pl[1] * base_pl[7], base_pl[8]]
            a_match_team.append(a_player)
        if a_match_formation[i] == rf:
            a_player = ['RF', base_pl[1] * base_pl[6], base_pl[8]]
            a_match_team.append(a_player)
    print('PLAYER team:', a_match_team)
    print('COMPUTER team:', b_match_team)
    soccer_mood(a_match_team, b_match_team, name, current_round, base_team)


def soccer_mood(a_match_team, b_match_team, name, current_round, base_team):
    a_match_team_improved = a_match_team
    for a_1 in a_match_team_improved:
        if a_1[0] == 'GK':
            for a_2 in a_match_team:
                if a_2[0] == 'SW' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CD_1' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CD_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'SW':
            for a_2 in a_match_team:
                if a_2[0] == 'CD_1' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CD_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'CD_1':
            for a_2 in a_match_team:
                if a_2[0] == 'CD_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'DM_1':
            for a_2 in a_match_team:
                if a_2[0] == 'DM_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CM_1' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CM_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'DM_2':
            for a_2 in a_match_team:
                if a_2[0] == 'CM_1' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CM_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'CM_1':
            for a_2 in a_match_team:
                if a_2[0] == 'CM_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'CF':
            for a_2 in a_match_team:
                if a_2[0] == 'AM' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CM_1' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CM_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'AM':
            for a_2 in a_match_team:
                if a_2[0] == 'CM_1' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'CM_2' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'LD':
            for a_2 in a_match_team:
                if a_2[0] == 'LM' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'LW' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'LF' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'LM':
            for a_2 in a_match_team:
                if a_2[0] == 'LW' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'LF' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'LW':
            for a_2 in a_match_team:
                if a_2[0] == 'LF' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'RD':
            for a_2 in a_match_team:
                if a_2[0] == 'RM' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'RW' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'RF' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'RM':
            for a_2 in a_match_team:
                if a_2[0] == 'RW' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
                if a_2[0] == 'RF' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
        if a_1[0] == 'RW':
            for a_2 in a_match_team:
                if a_2[0] == 'RF' and a_1[2] == a_2[2]:
                    print('YESSS!')
                    a_1[1] *= 1.25
                    a_2[1] *= 1.25
    print(f'Improved PLAYER team: {a_match_team_improved}')
    soccer_gra(a_match_team_improved, b_match_team, name, current_round, base_team)


def soccer_gra(pl_match_team, cm_match_team, name, current_round, base_team):
    result_player = 0
    result_computer = 0

    for minute in range(1, 5):
        if minute >= 5:
            print(f'Match result {result_player} : {result_computer}')
            if result_player == result_computer:
                penalty_list = [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [4, 1], [
                    3, 2], [4, 2], [4, 3], [5, 3], [5, 4], [6, 5], [7, 6]]
                penalty_result = random.choice(['player', 'computer'])
                penalty_score = random.choice(penalty_list)
                if penalty_result == 'player':
                    p_p = penalty_score[0]
                    p_c = penalty_score[1]
                elif penalty_result == 'computer':
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
                    break
            elif result_player > result_computer:
                print('You won!')
                soccer_decision(name, current_round + 1, base_team)
                break
            else:
                print('You fought to the end...')
                soccer_end()
                break

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
