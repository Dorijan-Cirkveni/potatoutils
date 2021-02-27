class RangeList:
    def __init__(self, ranges: list[tuple]):
        self.beginnings = list()
        self.ends = list()
        if len(ranges) == 0:
            return
        self.beginnings.append(ranges[0][0])
        current = ranges[0][1]
        ranges.append((float("inf"), float("inf")))
        ranges.sort()
        for e in ranges[1:]:
            a = e[0]
            b = e[1]
            if a <= current:
                if b > current:
                    current = b
            else:
                self.ends.append(current)
                self.beginnings.append(a)
        return
