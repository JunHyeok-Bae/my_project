import numpy as np

seat = np.array([["*", "*", "*", "*", "*", "*", "*"],
                ["*", "*", "*", "*", "*", "*", "*"]])

print("공연 예약 프로그램 - 공연일: 12월 24일")
reservation_date = input("예약일을 입력해주세요(월-일): ")
total_seat = np.count_nonzero(seat == "*")

def reservation():
    reservation_number = int(input("예약할 총 좌석 수를 입력해주세요: "))
    print(f"{reservation_number}개 좌석의 총 결제 금액은{reservation_number * 25000}원입니다.")
    if total_seat - reservation_number < 0 :
        print("예약 가능한 좌석 수를 초과했습니다.")
    else:
        pass
    if total_seat - reservation_number !=0:
        while reservation_number>0:
            reservation_number-= 1
            reservation_seat_number = input("예약할 좌석 번호를 입력해주세요: ")
            if reservation_seat_number == "A1":
                if seat[0, 0] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[0, 0] = "-" 
            elif reservation_seat_number =="A2":
                if seat[0, 1] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[0, 1] = "-"
            elif reservation_seat_number =="A3":
                if seat[0, 2] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[0, 2] = "-"
            elif reservation_seat_number =="A4":
                if seat[0, 3] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[0, 3] = "-"
            elif reservation_seat_number =="A5":
                if seat[0, 4] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[0, 4] = "-"
            elif reservation_seat_number =="A6":
                if seat[0, 5] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[0, 5] = "-"
            elif reservation_seat_number =="A7":
                if seat[0, 6] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[0, 6] = "-"
            elif reservation_seat_number =="B1":
                if seat[1, 0] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[1, 0] = "-"
            elif reservation_seat_number =="B2":
                if seat[1, 1] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[1, 1] = "-"
            elif reservation_seat_number =="B3":
                if seat[1, 2] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[1, 2] = "-"
            elif reservation_seat_number =="B4":
                if seat[1, 3] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[1, 3] = "-"
            elif reservation_seat_number =="B5":
                if seat[1, 4] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[1, 4] = "-"
            elif reservation_seat_number =="B6":
                if seat[1, 5] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[1, 5] = "-"
            elif reservation_seat_number =="B7":
                if seat[1, 6] == "-":
                    print("이미 예약된 좌석입니다.")
                    reservation()
                else:
                    seat[1, 6] = "-"
            else:
                print("좌석 번호를 잘못 입력했습니다.")
                return 

reservation()

while True:
    reservation_seat = np.count_nonzero(seat =="-")
    if reservation_seat !=14:
        print("--------현재 좌석 현황--------")
        print(seat)
        print(f"예약된 좌석 수: {reservation_seat}\n남은 좌석 수:{14 - reservation_seat}")
        answer = input("계속 예약하시겠습니까?(y 또는 n): ")
        if answer == "n":
            print("공연 예약 프로그램을 종료합니다.")
            break
        elif answer =="y": 
                reservation()

    elif reservation_seat >=14:
        print("현재 빈 좌석이 없어서 예약이 불가능합니다.")
        print("공연 예약 프로그램을 종료합니다.")
        break
    else:
        print("다시 입력하십시오.")
        answer = input("계속 예약하시겠습니까?(y 또는 n): ")
print(seat)

         










