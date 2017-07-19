class Time:
    """Time abstract data type (ADT) definition"""

    def __init__(self):
        """Initializes hour, minute and second to zero"""

        self.hour = 0   # 0~23
        self.minute = 0 # 0~59
        self.second = 0 # 0~59

    def printMilitary(self):
        """Prints object of class Time in military format"""

        print "%.2d:%.2d:%.2d" % \
              (self.hour, self.minute, self.second),