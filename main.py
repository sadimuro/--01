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


superhero_1 = SuperHero('Superman', 'super', 'power','never dead', 'cathing')
print(superhero_1)
print()