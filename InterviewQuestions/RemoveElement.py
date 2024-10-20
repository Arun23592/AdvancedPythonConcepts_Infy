def RemoveElement(self, num, value):
    i = 0
    for x in num:
        if x != value:
            num[i] = x
            i += 1
        return i

RemoveElement()