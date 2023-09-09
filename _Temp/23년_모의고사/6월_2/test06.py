
def solution(id):
    success_count = 0
    existing_ids = set()

    for i in range(len(id)):
        print(id[i])
        if id[i] not in existing_ids:
            existing_ids.add(id[i])
            success_count += 1

    return success_count



id = ["sky123", "Jason", "sky123", "99kate"]

an = solution(id)
print(an)