"""We need a class able to count seconds. Easy? Not as easy as you may think, as we're going to have some specific requirements.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from the range [0..23] – we will be using military time), minutes (from the range [0..59]) and seconds (from the range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside the objects by +1/-1 second respectively.
Use the following hints:

all object properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Expected output
Output
23:59:59
00:00:00
23:59:59"""

class Timer:
    def __init__(self, h = 0, m = 0, s = 0):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def __format_time(self, val):
        if val < 10:
            return '0' + str(val)
        return str(val)

    def __str__(self): #formata para imprimir
        s_hour = self.__format_time(self.__hours)
        s_min = self.__format_time(self.__minutes)
        s_sec = self.__format_time(self.__seconds)
            
        #hh:mm:ss
        return f"{s_hour}:{s_min}:{s_sec}"
    
    def __format_tosec(self):
        return int(self.__hours * 3600) + int(self.__minutes * 60) + self.__seconds

    def __format_tohour(self, total):
        setattr(self, '_Timer__hours', (total // 3600) % 24)

        total = total % 3600
        setattr(self, '_Timer__minutes', total // 60)

        total = total % 60
        setattr(self, '_Timer__seconds', total)

    def next_second(self):
        new_self = self.__format_tosec()
        new_self += 1 
        self.__format_tohour(new_self)
    

    def prev_second(self):
        new_self = self.__format_tosec()
        new_self -= 1 
        self.__format_tohour(new_self)
       

timer = Timer(23, 59, 59)
print(timer) #chama timer.__str__()
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    