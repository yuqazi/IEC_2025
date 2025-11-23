def guess_score(code, guess):
    guess = list(guess)
    if len(code) != len(guess):
        raise ValueError(f"code of len {len(code)} is not equal to guess of len {len(guess)}")
    else:
         length = len(code)

    score = {"black": 0, "white": 0}
  
    for i in range(length):
        if code[i] == guess[i]:
            score["black"] += 1
        elif code[i] in guess:
                guess[guess.index(code[i])] = "-1"
                score["white"] += 1
    
    return score