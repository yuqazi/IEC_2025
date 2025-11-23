def guess_score(code, guess):
    score = {}
    score["black"] = 0
    score["white"] = 0
    for i, char in enumerate(guess):
        if char == code[i]:
            score["black"] += 1
        if char in code:
            score["white"] += 1

        score["white"] -= score["black"]

    return score