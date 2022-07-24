import seat_module as s
import msvcrt
import time
import sys
seat_info={}
seatnum= 0
server_status= True
mini_server_status=True
a=0
student_number =0
class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04) # just to yield to other processes/threads
    raise TimeoutExpired

while server_status==True:
    if seatnum == 0 and student_number==0:
        while True:
            try:
                student_number = int(input_with_timeout('학번을 입력하세요:', 10))
                break
            except TimeoutExpired:
                print('...')
            else:
                pass            
    print("\n좌석 예약--> 1")
    print("잔여 시간 확인--> 2")
    print("좌석 반납--> 3")
    print("취소--> 4")
    while True:
        if seatnum !=0 :
            seat_info[seatnum].check_state()
            if seat_info[seatnum].reserved == False :     
                print(f"{student_number}님 {seatnum}번 자리의 시간이 모두 소요되었습니다.")
                seat_info.pop(seatnum)
                seatnum=0
                student_number=0
            else:
                try:
                    a = int(input_with_timeout('입력', 10))
                except TimeoutExpired:
                    print('...')
                else:
                   pass
                break
        else:
            try:
                a = int(input_with_timeout('입력', 10))
            except TimeoutExpired:
                print('...')
            else:
                pass
            break   
    if a==1:
        mini_server_status=True
        while mini_server_status==True:
            seatnum= int(input('원하시는 자리 번호를 입력하세요'))
            # 여기 input이 문제인듯
            if seatnum ==0 or 10<seatnum <100:
                print("좌석은 1부터 10까지 예약이 가능합니다.")
            else:
                seat_info[seatnum]=s.Seat(seatnum,student_number)
                seat_info[seatnum].make_reserv()                
                a=0
                mini_server_status=False
    elif a==2:
        if seatnum != 0:
            seat_info[seatnum].time_remaining()
        else:
            print("좌석을 먼저 예약해주세요")
        a=0
    elif a==3:
        if seatnum != 0:
            seat_info[seatnum].quit_reserv()
            seat_info.pop(seatnum)
            seatnum=0
            student_number=0
        else:
            print("좌석을 먼저 예약해주세요")
        a=0
    elif a==4:
        server_status=False
        a=0
        student_number=0
    else :
        pass

            
