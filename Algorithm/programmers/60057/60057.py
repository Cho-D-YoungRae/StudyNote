def solution(dartResult):
    sdt = {'S' : 1, 'D' : 2, 'T' : 3}
    score_list = [0]

    i_cur_score = 0
    s_cur_score = ""
    idx = 0
    while idx < len(dartResult):
        if dartResult[idx].isnumeric():
            s_cur_score += dartResult[idx]
            idx += 1
        else:
            i_cur_score = int(s_cur_score)
            s_cur_score = ""
            while idx < len(dartResult) and \
                    not dartResult[idx].isnumeric():
                if dartResult[idx] in sdt:
                    i_cur_score **= sdt[dartResult[idx]]
                elif dartResult[idx] == '*':
                    i_cur_score *= 2
                    score_list[-1] *= 2
                elif  dartResult[idx] == '#':
                    i_cur_score *= -1

                idx += 1

            score_list.append(i_cur_score)



    return sum(score_list)