def solution(p):
    if not p:
        return ''

    brackets_count = [0, 0]

    #i = None
    for i in range(len(p)):
        if p[i] == '(':
            brackets_count[0] += 1
        else:
            brackets_count[1] += 1

        if brackets_count[0] == brackets_count[1]:
            break

    u, v = p[:i+1], p[i+1:]

    if u[0] == '(':
        v = solution(v)
        return u + v
    else:
        result = "(" + solution(v) + ")"
        for i in range(1, len(u)-1):
            if u[i] == '(':
                result += ')'
            else:
                result += '('

        return result