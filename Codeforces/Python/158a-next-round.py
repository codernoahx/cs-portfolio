def main():
    # N is no. of contestants and K is the index of the finishers place, both 1-indexed. Any contestant with score >= k will advance.
    # Except if the score is 0 and contestant with score greater than 0 will advance
    n, k = map(int, input().split())  # extract k and n
    scores = input().split()  # split the list of scores by space
    # Find the k-th contestants score and -1 because it's 1 indexed
    k_score = int(scores[k - 1])
    contestants = 0
    # If score of k-th contestant is greater than 0, we add k to total contestants who will advance because the places before k have
    # score greater than k. We won't sub because it's not about palces it's about contestants
    if k_score > 0:
        contestants += k
        for i in range(k, n):  # We'll iterate from k because it's 1-indexed
            # If a contestant's score with ith place has score less than k-th place score, we can ignore the places after the ith place
            # because the places ahead of ith place will also have scores equal or lower to ith contestant's score.
            if int(scores[i]) < k_score:
                break
            contestants += 1  # Else we add +1
    else:
        # Else if score is == 0 then we start from 0th index and go till k, because k is 0, so we don't need it.
        for i in range(0, k):
            # If at any point any contestant score is 0, that means the scores of the contestants that will come after him will also
            # have score == 0, and thus we prematurely exit the loop.
            if int(scores[i]) == 0:
                break
            contestants += 1  # Else we add +1
    print(contestants)  # Print the results


if __name__ == "__main__":
    main()
