def solution(s: str):
    # "303213"
    # 303
    left, right = 0, 0
    count = 0
    while right < len(s):
        if s[left] == '0':
            left += 1
            continue
        num = int(s[left:right + 1])
        digit_sum = 0
        for digit in s[left:right + 1]:
            digit_sum += int(digit)
        if digit_sum % 3 == 0:
            count += 1
            right += 1
        else:
            left += 1


print(solution("303213"))
