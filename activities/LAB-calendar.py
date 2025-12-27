"""During this course, we took a brief look at the Calendar class. Your task now is to extend its functionality with a new method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

Create a class called MyCalendar that extends the Calendar class;
Create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
In your implementation, use the monthdays2calendar method of the Calendar class.
The following are the expected results:

Sample arguments
year=2019, weekday=0

Output
52"""
import calendar as c

class MyCalendar(c.Calendar):
    def __init__(self):
        c.Calendar.__init__(self)
        self.__sum = 0

    def count_weekday_in_year(self, year, weekday):
        self.__sum = 0
        for mo in range(1, 13): # todos os meses
            for week in self.monthdays2calendar(year, mo): # [(dia_do_mês, dia_da_semana), (dia_do_mês, dia_da_semana)]
                for d, wd in week:
                    # print(f"day of month = {d}, weekday = {wd}")
                    if d != 0 and wd == weekday:
                        # print("\tsum = ", self.__sum)
                        self.__sum += 1
        
        return self.__sum

my = MyCalendar()
print(my.count_weekday_in_year(2019, 0)) # 52 - ok
print(my.count_weekday_in_year(2000, 6)) # 53 - ok