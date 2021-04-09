mood = ['♠', '♣', '♥', '♦']
a_match_team = [['GK', 87, '♥'], ['LD', 73.87, '♥'], ['CD_1', 88.74, '♥'], ['RD', 33.839999999999996, '♥'], ['LM', 125.73, '♠'], ['DM_1', 180.48, '♦'], ['CM_1', 134.64000000000001, '♦'], ['RM', 73.53, '♥'], ['LF', 98.53, '♣'], ['CF', 34.4, '♦'], ['RF', 32.64, '♥']]

def soccer_mood(a_match_team, b_match_team=None, name='_', current_round=0):
    
    a_match_team_improved = a_match_team
    for a_1 in a_match_team_improved:
        for a_2 in a_match_team_improved:
            check_1_1 = (a_1[0] != a_2[0]) # чтобы игрок не усиливал сам себя
            check_1_2 = (a_1[2] == a_2[2]) # если одинаковый настрой на сезон
            check_2 = (a_1[0] in ['GK', 'SW', 'CD_1', 'CD_2']) and (a_2[0] in ['GK', 'SW', 'CD_1', 'CD_2']) # коллеги по обороне
            check_3 = (a_1[0] in ['DM_1', 'DM_2', 'CM_1', 'CM_2']) and (a_2[0] in ['DM_1', 'DM_2', 'CM_1', 'CM_2']) # коллеги по опорной зоне
            check_4 = (a_1[0] in ['CM_1', 'CM_2', 'AM', 'CF']) and (a_2[0] in ['CM_1', 'CM_2', 'AM', 'CF']) # коллеги по центру атаки
            check_5 = (a_1[0] in ['LD', 'LM', 'LF']) and (a_2[0] in ['LD', 'LM', 'LF']) # коллеги по левому флангу
            check_6 = (a_1[0] in ['RD', 'RM', 'RF']) and (a_2[0] in ['RD', 'RM', 'RF']) # коллеги по правому флангу
            if all([check_1_1, check_1_2]): 
                if any([check_2, check_3, check_4, check_5, check_6]):
                    print(f'YESSS! {a_1[0]} {a_2[0]}')
                    a_1[1] *= 1.25 # игрок получает +25% к силе за коллегу с таким же настроем на сезон

    print(f'Improved PLAYER team: {a_match_team_improved}')
    # soccer_gra(a_match_team_improved, b_match_team, name, current_round)


if __name__ == '__main__':

    soccer_mood(a_match_team)
