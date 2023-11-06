class Time:
    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = s

    # Read-only field accessors
    @property
    def hours(self):
        return self._h

    @property
    def minutes(self):
        return self._m

    @property
    def seconds(self):
        return self._s

    def __lt__(self, other):
        if self._h < other._h:
            return True
        elif self._h > other._h:
            return False
        else:
            if self._m < other._m:
                return True
            elif self._m > other._m:
                return False
            else:
                return self._s < other._s

    def __eq__(self, other):
        return self._h == other._h and self._m == other._m and self._s == other._s

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


# instanciation
t1 = Time(13, 10, 5)
t2 = Time(5, 15, 30)
t3 = Time(5, 15, 30)
print(t1 < t2)
print(t1 > t2)
print(t1 == t2)
print(t2 == t3)