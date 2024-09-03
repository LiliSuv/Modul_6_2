class Vehicle:
    def __init__(self, __model, __engine_power, __color, owner):
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.owner = owner

    def get_model(self, __model):
        __model.__str__ ()
        return f'Модель: {self.__model}'

    def get_horsepower(self, __engine_power):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self, __color):
        return f'Цвет машины: {self.__color}'

    def get_owner(self, owner):
        return f"Владелец: {self.owner}"

    def cet_color(self, new_color):
        __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
        a = []
        a = [new_color for i in range (len (__COLOR_VARIANTS)) if new_color.lower () == __COLOR_VARIANTS[i].lower ()]

        if a != []:
            self.__color = new_color
        else:
            print (f"Нельзя сменить цвет на: {new_color.upper ()}"
                   f'\n{'-' * 40}')
        return self.__color

    def print_info(self):
        print (f"Модель: {self.__model}"
               f"\nМощность двигателя: {self.__engine_power}"
               f"\nЦвет машины: {self.__color}"
               f"\nВладелец: {self.owner} "
               f'\n{'-' * 40}')


class Sedan (Vehicle):
    def __init__(self, __model, __engine_power, __color, owner, __PASSENGERS_LIMIT):
        super ().__init__ (__model, __engine_power, __color, owner)
        self.__PASSENGERS_LIMIT = __PASSENGERS_LIMIT
        print (f'Седан {__PASSENGERS_LIMIT} мест')


car = Vehicle ('Жигуль', '50000', 'голубой', 'Лили')
car.print_info ()
car.owner = 'Фируз'
car.print_info ()
car.cet_color ("red")
car.print_info ()
car.cet_color ("re")
car.print_info ()
car.cet_color ("rekk")
car.print_info ()
car.cet_color ("white")
car.print_info ()
sedan = Sedan ('Жигуль', '50000', 'голубой', 'Лили', 5)
car.print_info ()
sedan.owner = 'Тошка картошка'
sedan.print_info ()
sedan.cet_color ("MMM")
sedan.cet_color ('BLue')
sedan.print_info ()