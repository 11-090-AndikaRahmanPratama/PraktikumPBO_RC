import random

class Robot:
    def __init__(self, nama, attack, hp, special_attack):
        self.nama = nama
        self.attack = attack
        self.hp = hp
        self.special_attack = special_attack
        self.is_defending = False

    def attack_enemy(self, enemy, extra_damage=1, defense_reduction=0.7):
        if random.randint(0, 1) == 0:
            print(f'{self.nama} gagal menyerang {enemy.nama}!')
        else:
            damage = self.attack * extra_damage
            if enemy.is_defending:
                damage *= defense_reduction
                enemy.is_defending = False
            enemy.hp -= damage
            print(f'{self.nama} menyerang {enemy.nama} dengan {damage} serangan! {enemy.nama} sekarang memiliki {enemy.hp} HP.')

    def defend(self):
        self.is_defending = True
        print(f'{self.nama} dalam mode bertahan!')

    def giveup(self):
        self.hp = 0
        print(f'{self.nama} menyerah!')

    def use_special_attack(self, enemy):
        enemy.hp -= self.special_attack
        print(f'{self.nama} menggunakan serangan spesial dan memberikan {self.special_attack} damage pada {enemy.nama}! {enemy.nama} sekarang memiliki {enemy.hp} HP.')

def get_action(robot):
    while True:
        if robot.hp < 0.35 * robot.hp:
            print(f'{robot.nama} bisa menggunakan serangan spesial!')
        print("\n1. Attack     2. Defense     3. Giveup     4. Special Attack")
        action = int(input(f'{robot.nama}, pilih aksi: '))
        if action == 4 and robot.hp >= 0.35 * robot.hp:
            print("Tidak bisa menggunakan serangan spesial, HP masih lebih dari 35%. Silakan pilih aksi lain.")
        else:
            return action

def select_character():
    print("1. Saton [Attack: 25, HP: 350, Special Attack: 80]")
    print("2. Koneng [Attack: 20, HP: 400, Special Attack: 70]")
    print("3. Mochi [Attack: 40, HP: 380, Special Attack: 100]")
    choice = int(input("Masukkan pilihan (1/2/3): "))
    if choice == 1:
        return Robot("Saton", 25, 350, 80)
    elif choice == 2:
        return Robot("Koneng", 20, 400, 70)
    elif choice == 3:
        return Robot("Mochi", 40, 380, 100)
    else:
        print("Pilihan tidak valid, menggunakan karakter default: Saton.")
        return Robot("Saton", 25, 350, 80)

class Game:
    def __init__(self, robot1, robot2, rounds):
        self.robot1 = robot1
        self.robot2 = robot2
        self.rounds = rounds

    def start_game(self):
        print("\nSelamat datang di permainan pertarungan robot!")
        print("Dalam permainan ini terdapat 10 ronde normal. Jika pemenang belum ditemukan, akan ada 10 ronde tambahan dengan peningkatan damage 300%.")
        print("Bertahan akan mengurangi damage sebesar 30% dalam ronde normal dan 50% dalam ronde tambahan.")
        print("Serangan spesial dapat digunakan jika HP robot kurang dari 35%.")
        
        current_round = 1
        extra_damage = 1
        defense_reduction = 0.7

        while self.robot1.hp > 0 and self.robot2.hp > 0:
            if current_round == self.rounds + 1:
                print("\nTambahan 10 ronde dengan peningkatan berikut:")
                print("- Damage serangan meningkat 300%")
                print("- Pengurangan damage saat bertahan meningkat menjadi 50%")

            print(f'\nRound-{current_round} ==========================================================')
            print(f'{self.robot1.nama} [{self.robot1.hp}|{self.robot1.attack}]')
            print(f'{self.robot2.nama} [{self.robot2.hp}|{self.robot2.attack}]')

            action1 = get_action(self.robot1)
            action2 = get_action(self.robot2)

            if action1 == 1:
                self.robot1.attack_enemy(self.robot2, extra_damage, defense_reduction)
            elif action1 == 2:
                self.robot1.defend()
            elif action1 == 3:
                self.robot1.giveup()
            elif action1 == 4 and self.robot1.hp < 0.35 * 350:
                self.robot1.use_special_attack(self.robot2)

            if action2 == 1:
                self.robot2.attack_enemy(self.robot1, extra_damage, defense_reduction)
            elif action2 == 2:
                self.robot2.defend()
            elif action2 == 3:
                self.robot2.giveup()
            elif action2 == 4 and self.robot2.hp < 0.35 * 400:
                self.robot2.use_special_attack(self.robot1)

            current_round += 1

            if current_round > self.rounds:
                extra_damage = 3
                defense_reduction = 0.5

            if current_round > self.rounds + 10:
                break

        if self.robot1.hp <= 0 and self.robot2.hp <= 0:
            print("Hasil akhir: Seri!")
        elif self.robot1.hp <= 0:
            print(f'{self.robot1.nama} telah dikalahkan!')
        elif self.robot2.hp <= 0:
            print(f'{self.robot2.nama} telah dikalahkan!')
        else:
            print("Permainan berakhir. Hasil akhir: Seri!")

print("Pilih karakter pertama:")
robot1 = select_character()
print("Pilih karakter kedua:")
robot2 = select_character()

game = Game(robot1, robot2, 10)
game.start_game()
