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

print(s.name)
print()
print(s.health_points *2)
print(len(s.catchphrase))
print(s)

h = SuperHero('Spiderman', 'spider', 'power','jumping', 'cathing')
h.Hero()