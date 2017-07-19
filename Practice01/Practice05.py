class TrollMonster:
    count = 0

    def __init__(self):
        TrollMonster.count += 1

tm1 = TrollMonster()
tm2 = TrollMonster()
tm3 = TrollMonster()

if TrollMonster.count > 1:
    print "Attack like there's no tomorrow"
else:
    print "Wait for others."