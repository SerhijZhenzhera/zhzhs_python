def chess_knight(position, goal):
    result_list = []
    result_archive = []
    result_check_1 = result_check_2 = result_check_3 = result_check_4 = result_check_5 = result_check_6 = 0
    temp_p = list(position)
    temp_g = list(goal)

    def numb(pair_list):  # зашифратор
        num_pair_list = ''
        if pair_list[0] == 'a':
            num_pair_list = 10
        elif pair_list[0] == 'b':
            num_pair_list = 20
        elif pair_list[0] == 'c':
            num_pair_list = 30
        elif pair_list[0] == 'd':
            num_pair_list = 40
        elif pair_list[0] == 'e':
            num_pair_list = 50
        elif pair_list[0] == 'f':
            num_pair_list = 60
        elif pair_list[0] == 'g':
            num_pair_list = 70
        elif pair_list[0] == 'h':
            num_pair_list = 80
        else:
            return 00
        return num_pair_list + int(pair_list[1])

    def posit(step_position: int):  # расшифратор
        posit_result = step_position // 10
        if posit_result == 1:
            lett = 'a'
        elif posit_result == 2:
            lett = 'b'
        elif posit_result == 3:
            lett = 'c'
        elif posit_result == 4:
            lett = 'd'
        elif posit_result == 5:
            lett = 'e'
        elif posit_result == 6:
            lett = 'f'
        elif posit_result == 7:
            lett = 'g'
        elif posit_result == 8:
            lett = 'h'
        else:
            return 'Out of the desk!'
        return lett + str(step_position % 10)

    position_n = numb(temp_p)
    goal_n = numb(temp_g)
    desk = [11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38,
            41, 42, 43, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 65, 66, 67, 68,
            71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88]
    if not position_n in desk:
        return 'Missed the desk!'
    if not goal_n in desk:
        return 'Out of the desk!'
    step_list = [12, 21, 19, 8, -12, -21, -19, -8]
    for el_1 in step_list:
        result_check_1 = position_n + el_1
        if not result_check_1 in desk:
            continue
        if result_check_1 == goal_n and result_check_1 in desk:
            result_archive.append((posit(result_check_1),))
            result_list = [posit(result_check_1)]
        for el_2 in step_list:
            result_check_2 = position_n + el_1 + el_2
            if not result_check_2 in desk:
                continue
            if result_check_2 == goal_n and result_check_2 in desk:
                result_archive.append((posit(position_n + el_1),
                                       posit(result_check_2)))
                if not 0 < len(result_list) < 2:
                    result_list = [posit(position_n + el_1),
                                   posit(result_check_2)]
            for el_3 in step_list:
                result_check_3 = position_n + el_1 + el_2 + el_3
                if not result_check_3 in desk:
                    continue
                if result_check_3 == goal_n and result_check_3 in desk:
                    result_archive.append(
                        (posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(result_check_3)))
                    if not 0 < len(result_list) < 3:
                        result_list = [
                            posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(result_check_3)]
                for el_4 in step_list:
                    result_check_4 = position_n + el_1 + el_2 + el_3 + el_4
                    if not result_check_4 in desk:
                        continue
                    if result_check_4 == goal_n and result_check_4 in desk:
                        result_archive.append((posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(
                            position_n + el_1 + el_2 + el_3), posit(result_check_4)))
                        if not 0 < len(result_list) < 4:
                            result_list = [posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(
                                position_n + el_1 + el_2 + el_3), posit(result_check_4)]
                    for el_5 in step_list:
                        result_check_5 = position_n + el_1 + el_2 + el_3 + el_4 + el_5
                        if not result_check_5 in desk:
                            continue
                        if result_check_5 == goal_n and result_check_5 in desk:
                            result_archive.append(
                                (posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(position_n + el_1 + el_2 + el_3), posit(position_n + el_1 + el_2 + el_3 + el_4), posit(result_check_5)))
                            if not 0 < len(result_list) < 5:
                                result_list = [posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(
                                    position_n + el_1 + el_2 + el_3), posit(position_n + el_1 + el_2 + el_3 + el_4), posit(result_check_5)]
                        for el_6 in step_list:
                            result_check_6 = position_n + el_1 + el_2 + el_3 + el_4 + el_5 + el_6
                            if not result_check_6 in desk:
                                continue
                            if result_check_6 == goal_n and result_check_6 in desk:
                                result_archive.append(
                                    (posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(position_n + el_1 + el_2 + el_3), posit(position_n + el_1 + el_2 + el_3 + el_4), posit(position_n + el_1 + el_2 + el_3 + el_4 + el_5), posit(result_check_6)))
                                if not 0 < len(result_list) < 6:
                                    result_list = [posit(position_n + el_1), posit(position_n + el_1 + el_2), posit(position_n + el_1 + el_2 + el_3), posit(
                                        position_n + el_1 + el_2 + el_3 + el_4), posit(position_n + el_1 + el_2 + el_3 + el_4 + el_5), posit(result_check_6)]

    result_archive.sort(key=len)
    return 'From:', position, 'Short:', result_list, 'All:', result_archive
    # return f'Start: {position} - Short root: {result_list}. All roots: {result_archive} - by Python Beetroot'


print(chess_knight('a1', 'b3'))
print(chess_knight('a1', 'c5'))
print(chess_knight('a1', 'd7'))
print(chess_knight('a1', 'e5'))
print(chess_knight('a1', 'g8'))
print(chess_knight('a1', 'h8'))
print(chess_knight('h8', 'g6'))
print(chess_knight('h8', 'a1'))
