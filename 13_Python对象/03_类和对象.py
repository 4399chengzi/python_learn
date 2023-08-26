"""
演示类和对象
"""


class Clock:
    id = None
    price = None

    def ring(self):
        # import winsound
        # winsound.Beep(2000, 3000)
        print('1')


clock1 = Clock()
clock1.id = '1'
clock1.price = '1.0'
print(f'{clock1.id}{clock1.price}')
clock1.ring()

clock2 = Clock()
clock2.id = '2'
clock2.price = '2.0'
print(f'{clock2.id}{clock2.price}')
clock2.ring()
