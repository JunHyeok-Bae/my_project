from Address import Addr

class CompanyAddr(Addr):
    def __init__(self, name, phone, email, address, birth, group, company_name, department, company_position):
        super().__init__(name, phone, email, address, birth, group)
        self.company_name = company_name
        self.department = department
        self.company_position = company_position


    def get_company_name(self):
        return self.company_name
    
    def get_department(self):
        return self.department
    
    def get_company_position(self):
        return self.company_position
    
    def print_info(self):
        super().print_info()
        print(f"회사이름 : {self.get_company_name()}")
        print(f"부서이름 : {self.get_department()}")
        print(f"직급 : {self.get_company_position()}")
