from SmartPhone import SmartPhone

class SmartPhoneMain:

    def __init__(self):
        self.smartphone = SmartPhone()

    def menu(self):
        print("\n")
        print("1. 연락처 추가")
        print("2. 모든 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 수정")
        print("6. 종료 ")


    def start(self):
        while True:
            self.menu()
            number = input("원하시는 항목을 선택하세요 : ")
            if number == '1':
                addr = self.smartphone.input_addr()
                self.smartphone.add_info(addr)

            elif number == '2':
                self.smartphone.all_print()

            elif number == '3':
                name = input("검색할 이름을 입력하세요 : ")
                self.smartphone.search_addr(name)

            elif number == '4':
                name = input("삭제할 데이터의 이름을 입력하세요. ")
                self.smartphone.delete_addr(name)

            elif number == '5':
                name = input("수정할 데이터의 이름을 입력하세요. : ")
                new_name = self.smartphone.input_addr()
                self.smartphone.edit_addr(name, new_name)

            elif number == '6':
                print("시스템을 종료합니다.")
                break
            else:
                print("다시 선택하세요.")
                

if __name__ =='__main__':
    smartphone_main = SmartPhoneMain()
    smartphone_main.start()