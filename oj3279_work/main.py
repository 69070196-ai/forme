"""PM Watch"""
def main():
    """PM over peak streak start"""
    N = int(input())
    PM = 0
    over = 0
    peak = 0
    streak = 0
    streak2 = 0
    start = 0
    start2 = 0
    for i in range(1,N+1):
        PM = int(input())
        if PM > 50:
            over += 1
            streak += 1
            if streak == 1:
                start = i
        else:
            streak = 0
        if streak >= streak2:
            streak2 = streak
            start2 = start
        if PM > peak:
            peak = PM
    print(f"OVER = {over}")
    print(f"PEAK = {peak}")
    print(f"STREAK = {streak2}")
    print(f"START = {start2}")
main()
