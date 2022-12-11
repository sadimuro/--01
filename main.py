class SuperHero:
    def __init__(self, name, nickname, superpower, health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def __str__(self):
        return  f'name is {self.name} \n' \
                f'nickname is {self.nickname}\n'\
                f'superpower is {self.superpower}\n'\
                f'health_points are {self.health_points}\n'\
                f'catchphrase is {self.catchphrase}\n'
    def __len__(self):
        return len(self)
    def Hero(self):
        print(self.name, self.nickname, self.catchphrase, self.health_points, self.catchphrase)

s = SuperHero('Superman', 'super', 'power','never dead', 'cathing')

# print(s.name)
# print()
# print(s.health_points *2)
# print(len(s.catchphrase))
# print(s)

# h = SuperHero('Spiderman', 'spider', 'power','jumping', 'cathing')
# h.Hero()


class SuperHero_1(SuperHero):
    h = 1
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False):
        SuperHero.__init__(self,name, nickname, superpower, health_points,catchphrase)

        self.fly = fly
    def print_name_hero(self):
        print(f'{self.health_points ** 2 }')
        self.fly = True

    def fly_true(self):
        print('fly in the True_phrase')

    # def fly(self):
    #     print(self.name, 'is fly in False')

s1 = SuperHero_1('hero1', 'heeroo','power', 'never', 'catch')
print(s1)
# s1.fly()

class SuperHero_2(SuperHero):

    k = 1
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False):
        SuperHero.__init__(self,name, nickname, superpower, health_points,catchphrase)

        self.fly = fly
    def print_name_hero(self):
        print(f'{self.health_points ** 2}')
        self.fly = True

    def fly_true(self):
        print('fly in the True_phrase')

class SuperHero_3(SuperHero):

        z = 1
        def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False):

            SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)

            self.fly = fly


        def print_name_hero(self):
            print(f'{self.health_points ** 2}')
            self.fly = True


        def fly_true(self):
            print('fly in the True_phrase')

f=SuperHero_1('hero1', 'heeroo','power', 'never', 'catch')
f.fly_true()
f.print_name_hero()