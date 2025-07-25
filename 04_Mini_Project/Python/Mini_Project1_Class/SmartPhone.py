from Address import Addr

class SmartPhone:
    def __init__(self):
        self.contacts = []

    def input_addr(self):

        name = input("이름을 입력하세요 : ")
        phone = input("전화번호를 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        address = input("주소를 입력하세요 : ")
        group = input("그룹(친구/가족)을 입력하세요 :")

        return Addr(name, phone, email, address, group)


    def add_info(self, addr):  
        if len(self.contacts) < 10:
            self.contacts.append(addr)
            print("데이터가 저장되었습니다.")
        else:
            print("저장 공간이 없습니다.")

    def all_print(self):
        if not self.contacts:
            print("저장된 데이터가 없습니다.")
        else:
            for i, addr in enumerate(self.contacts):
                print(f"{i+1}")
                addr.print_info()
           

    def search_addr(self, name):
        for addr in self.contacts:
            if addr.get_name() == name:
                addr.print_info()
                return
        print(f"{name}의 데이터가 없습니다.")

    def delete_addr(self, name):
        for addr in self.contacts:
            if addr.get_name() == name:
                self.contacts.remove(addr)
                print(f"{name}의 데이터가 삭제되었습니다.")
                return
            print(f"{name}의 데이터가 존재하지 않습니다.")

    def edit_addr(self, name, new_name):
        for i, addr in enumerate(self.contacts):
            if addr.get_name() == name:
                print("저장된 연락처 :")
                addr.print_info()
                self.contacts[i] = new_name
                


                print("정보가 수정되었습니다.")
                return
        print("해당 데이터가 존재하지 않습니다.")





    
