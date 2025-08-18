# access modifier
class player:
    # atribut : informasi
    # bertipe publik, bisa diakses oleh outer class, karena atribut name bisa diakses
    name = 'rasridho'
    health_point = 1000
    __private_HP = 1500  # jika ingin atribut tidak dapat diakses di luar class maka bisa ditambahkan __hp

    # methods atau perintah
    def get_hp(self):
        return self.__private_HP


run = player()

print(f'player {run.name} berhasil dibuat')
print(f'HP awal {run.name} sebesar {run.health_point} points')
player.health_point = 3000  # atribut HP bisa diakses di luar class karena bersifat publik
run.health_point  # karena bisa diakses sehingga mudah untuk diubah-ubah
# run.__private_HP # output error player' object has no attribute '__private_HP'

print(run.get_hp())  # bisa dipanggil karena method masih di dalam class
print(run.health_point)

# __private_HP tidak bisa diubah seperti health_point
#
#
class Player:
    def __init__(self, name: str, health: int): # menambahkan hint setelah variabel
        self.name = name
        self.health = health
        print(f'player {self.name} memiliki HP {self.health}')

p1 = Player('rasridho', 1000)
p2 = Player(1000, 'rasridho') # akan muncul notif bahwa data yg diinput tidak sesuai dengan class

