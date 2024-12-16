# https://leetcode.com/problems/binary-watch/submissions/1410996665

def readBinaryWatch(self, turnedOn: int) -> List[str]:
    times = []
    for hour in range(12):
        for minute in range(60):
            hour_bits = bin(hour).count('1')
            minute_bits = bin(minute).count('1')
            if hour_bits + minute_bits == turnedOn:
                times.append(f"{hour}:{minute:02d}")
    return times