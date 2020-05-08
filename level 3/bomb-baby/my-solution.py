def solution(MACH, FACH):
    mach, fach = int(MACH), int(FACH)
    total = 0
    while not (mach == 1 and mach == 1):
        if fach <= 0 or mach <= 0:
            return "impossible"
        if fach == 1:
            return str(total + mach - 1)
        else:
            total += int(mach/fach)
            mach,fach = fach, mach % fach
    return str(total)

solution("4","7")