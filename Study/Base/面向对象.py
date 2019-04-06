class Cat:
    """这是一个猫类"""

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

tom = Cat()
tom.drink()
tom.eat()

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

# 提问：tom 和 lazy_cat 是同一个对象吗？
print("%x",tom)
print("%x",lazy_cat)
print(id(tom))
print(id(lazy_cat))