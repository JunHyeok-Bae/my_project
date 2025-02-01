from CompanyAddr import CompanyAddr
from CustomerAddr import CustomerAddr

class SmartPhone(CompanyAddr, CustomerAddr):
    def __init__(self):
        self.contacts = []

    def input_addr(self):

        name = input("이름을 입력하세요 : ")
        phone = input("전화번호를 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        address = input("주소를 입력하세요 : ")
        birth = input("생일을 입력하세요. ")
        group = input("그룹(회사/거래처)을 입력하세요 : ")
        company_name = input("회사이름을 입력하세요 : ")
        department = input("부서이름을 입력하세요 : ")
        company_position = input("직급을 입력하세요 : ")
        print("데이터가 저장되었습니다. (1)")

        return CompanyAddr(name, phone, email, address, birth, group, company_name, department, company_position)
    
    def input_addr2(self):

        name = input("이름을 입력하세요 : ")
        phone = input("전화번호를 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        address = input("주소를 입력하세요 : ")
        group = input("그룹(회사/거래처)을 입력하세요 : ")
        birth = input("생일을 입력하세요. ")
        client = input("거래처이름을 입력하세요 : ")
        item = input("품목이름을 입력하세요 : ")
        client_position = input("직급을 입력하세요 : ")
        print("데이터가 저장되었습니다. (2)")

        return CustomerAddr(name, phone, email, address, birth, group, client, item, client_position)

    def add_info(self, addr):  
        if len(self.contacts) < 10:
            self.contacts.append(addr)
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








    