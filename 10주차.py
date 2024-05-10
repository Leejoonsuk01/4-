import random

def lotto():
    results = []
    while len(results) < 6:
        ran_num = random.randint(1, 45)
        if ran_num not in results:
            results.append(ran_num)

    results.sort()
    return results
numbers = lotto()
print(f"생성된 로또 번호는 {numbers}입니다")





