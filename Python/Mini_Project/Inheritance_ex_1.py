class Head_store:
    def head_store(self):
        print("본점 가격표입니다.")
        print("짜장면 : 8000원")
        print("짬뽕 : 8000원")
        print("탕수육 : 12000원")
        print("군만두 : 3000원")
        print("공기밥 : 1000원")
        print("==========================")

        
class First_store(Head_store):
    def first_store(self):
        print("1호점 가격표입니다.")
        print("짜장면 : 7000원")
        print("짬뽕 : 8000원")
        print("탕수육 : 12000원")
        print("군만두 : 판매하지않음")
        print("공기밥 : 1000원")
        print("==========================")
        
class Second_store(Head_store):
    def second_store(self):
        print("2호점 가격표입니다.")
        print("짜장면 : 5000원")
        print("짬뽕 : 5000원")
        print("탕수육 : 10000원")
        print("군만두 : 3000원")
        print("공기밥 : 무료")
        print("==========================")
        
class Third_store(Head_store):
    def third_store(self):
        print("3호점 가격표입니다.")
        print("짜장면 : 7000원")
        print("짬뽕 : 7000원")
        print("탕수육 : 12000원")
        print("군만두 : 3000원")
        print("공기밥 : 1000원")
        print("==========================")
    
    
head = Head_store()
head.head_store()
first = First_store()
first.first_store()
second = Second_store()
second.second_store()
third = Third_store()
third.third_store()