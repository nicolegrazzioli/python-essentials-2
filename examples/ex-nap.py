import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds) #espera 5s
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)