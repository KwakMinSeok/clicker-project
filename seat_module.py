from ast import While
import time as t
class Seat:
    # init이 뭐지?
    def __init__(self,seat_number,student_number):
        self.reserved= False
        self.reserved_minute=0
        self.reserved_hour=0
        self.now_hour=0
        self.now_minute=0
        self.left_time=0
        self.seat_number=seat_number
        self.student_number=student_number
    # 시간 지나면 함수 안불러도 자동으로 self.reserved false 되게 해야함.
    def make_reserv(self):
        self.reserved_minute=t.localtime().tm_min
        self.reserved_hour=t.localtime().tm_hour
        self.left_time= (self.reserved_hour -t.localtime().tm_hour)*60 + (self.reserved_minute+1 - t.localtime().tm_min)
        print(f"{self.student_number}님{self.reserved_hour}:{self.reserved_minute}에 {self.seat_number}번 좌석을 예약하셨습니다.")
        self.check_state()
    def quit_reserv(self):
        self.reserved=False
        print(f"{t.localtime().tm_hour}:{t.localtime().tm_min}에 좌석을 반납하셨습니다.")
    def time_remaining(self):
            now_hour=t.localtime().tm_hour
            now_minute=  t.localtime().tm_min
            self.left_time=(self.reserved_hour - now_hour)*60 + (self.reserved_minute+1 - now_minute)
            print(f"{self.left_time//60 }시간 {self.left_time%60}분 남았습니다")
    def check_state(self):
        now_hour=t.localtime().tm_hour
        now_minute=  t.localtime().tm_min
        self.left_time=(self.reserved_hour - now_hour)*60 + (self.reserved_minute+1 - now_minute)
        if (self.left_time) > 0:
            self.reserved= True
        else:
            self.reserved=False
