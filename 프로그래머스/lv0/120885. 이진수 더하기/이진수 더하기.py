def solution(bin1, bin2):
    number = int(bin1) + int(bin2)
    while True:
        # 조건
        if max(list(map(int, str(number)))) < 2:
            break
        digit = len(str(number)) - (str(number).find('2')+1)
        number -= 2 * (10**digit)
        number += 10**(digit+1)
    return str(number)