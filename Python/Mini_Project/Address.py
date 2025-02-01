class Addr:
    def __init__(self, name, phone, email, address, birth, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birth = birth
        self.group = group

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_phone(self):
        return self.phone

    def set_phone(self, value):
        self.phone = value

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address
    
    def get_birth(self):
        return self.birth
    
    def get_group(self):
        return self.group
    

    def print_info(self):
        print(f"이름 : {self.get_name()}")
        print(f"전화번호 : {self.get_phone()}")
        print(f"이메일 : {self.get_email()}")
        print(f"주소 : {self.get_address()}")
        print(f"생일 : {self.get_birth()}")
        print(f"그룹(회사/거래처) : {self.get_group()}")
        
    def showData(self):
        print(f"이름 : {self.get_name()}")
        print(f"전화번호 : {self.get_phone()}")

    