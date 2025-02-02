from Address import Addr

class CustomerAddr(Addr):
    def __init__(self, name, phone, email, address, birth, group, client, item, client_position):
        super().__init__(name, phone, email, address, birth, group)
        self.client = client
        self.item = item
        self.client_position = client_position

    
    def get_client(self):
        return self.client
    
    def get_item(self):
        return self.item
    
    def get_client_position(self):
        return self.client_position
    
    def print_info(self):
        super().print_info()
        print(f"거래처이름 : {self.get_client()}")
        print(f"품목이름 : {self.get_item()}")
        print(f"직급 : {self.get_client_position()}")
