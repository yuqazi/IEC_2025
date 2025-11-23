from typing import Counter

rounds = 0

def guess_score(code, guess):
    if len(code) != len(guess):
        raise ValueError(f"code of len {len(code)} is not equal to guess of len {len(guess)}")

    score = {"black": 0, "white": 0}
  
    for i, char in enumerate(guess):
        if char == code[i]:
            score["black"] += 1

    code_counter  = Counter(code)
    guess_counter = Counter(guess)

    overlap = sum((code_counter & guess_counter).values()) # sums only the counts where the number of each element is the same in both dictionaries
    score["white"] = overlap - score["black"]
    
    return score

def guess_score_easy(code, guess):
    if len(code) != len(guess):
        raise ValueError(f"code of len {len(code)} is not equal to guess of len {len(guess)}")
    else:
        length = len(code)

    score = ["0"] * length
    used_code = [False] * length
    used_guess = [False] * length

    for i in range(length):
        if guess[i] == code[i]:
            score[i] = "2"
            used_code[i] = True
            used_guess[i] = True 

    for i in range(length):
        if matched := used_guess[i]:
            for j in range(length):
                if not matched and not used_code[j] and guess[i] == code[j]:
                    score[i] = "1"
                    used_code[j] = True
                    matched = True

    return score