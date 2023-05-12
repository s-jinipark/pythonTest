def solution(cards1, cards2, goal):
    answer = ''
    c1_idx = 0
    c2_idx = 0

    for i in range(len(goal)):
        print(goal[i])
        if c1_idx < len(cards1) and cards1[c1_idx] == goal[i] :
            c1_idx += 1
        elif c2_idx < len(cards2) and cards2[c2_idx] == goal[i] :
            c2_idx += 1
        else:
            #print("No")
            return "No"

        answer = "Yes"
    return answer


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

# cards1 = ["i", "water", "drink"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]

re = solution(cards1, cards2, goal)

print(re)

print("====================")

