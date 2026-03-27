def my_function():
    print('새로운')
    print('함수를')
    print('만들었어요.')  #-> 호출안됌

my_function()

#-----------------------
def show_price(customer):
    print(f'{customer} 고객님')
    print('커트 가격은 15000원 입니다.')

customer1 = '나장발'
show_price(customer1)

customer2 = '나수염'
show_price(customer2)