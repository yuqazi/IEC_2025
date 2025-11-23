final = 97
iteration = 0
digits = [int(d) for d in str(final)]

lows = [0] * len(digits)
highs = [9] * len(digits)
guesses = [(low + high) // 2 for low, high in zip(lows, highs)]

print(guesses)

while guesses != digits:
    iteration += 1
    print(f"\n--- Iteration {iteration} ---")

    for i in range(len(digits)):
        target = digits[i]
        guess = guesses[i]

        if guess > target:
            highs[i] = guess - 1
        elif guess < target:
            lows[i] = guess + 1

        guesses[i] = (lows[i] + highs[i]) // 2

    print("Guesses so far:", guesses)


print("\nFINAL RESULT:", guesses)