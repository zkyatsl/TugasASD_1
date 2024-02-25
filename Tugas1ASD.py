from prettytable import PrettyTable

class Game:
    def __init__(self, id, judul, genre, harga, jumlah):
        self.id = id
        self.judul = judul
        self.genre = genre
        self.harga = harga
        self.jumlah = jumlah

class GameStore:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game_id):
        for game in self.games:
            if game.id == game_id:
                self.games.remove(game)
                return True
        return False

    def update_game_stock(self, game_id, new_stock):
        for game in self.games:
            if game.id == game_id:
                game.jumlah = new_stock
                return True
        return False

    def display_games(self):
        table = PrettyTable()
        table.field_names = ["NO", "Judul", "Genre", "Harga", "Jumlah"]
        for game in self.games:
            table.add_row([game.id, game.judul, game.genre, game.harga, game.jumlah])
        print(table)

# Menu Utama sekaligus sama CRUD nya
def main():
    game_store = GameStore()
    game1 = Game(1, "The Last of Us Part II", "Action-Adventure", 630000, 10)
    game2 = Game(2, "God of War", "Action-Adventure", 729000, 5)
    game3 = Game(3, "Uncharted 4: A Thief's End", "Action-Adventure", 250000, 3)
    game4 = Game(4, "Sekiro™: Shadows Die Twice - GOTY Edition", "Action-Adventure", 891000, 7)
    game_store.add_game(game1)
    game_store.add_game(game2)
    game_store.add_game(game3)
    game_store.add_game(game4)
    print("="*71)
    print ("|                  SELAMAT DATANG DI MAMANK GAMESHOP                   |")
    print("="*71)
    game_store.display_games()


    while True:
        print("="*71)
        print("|                         WELCOME, ADMIN Mamanks                      |")
        print("="*71)
        print("Menu:")
        print("1. Tambah Game")
        print("2. Hapus Game")
        print("3. Update Stok Game")
        print("4. Tampilkan Semua Game")
        print("5. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            id = int(input("Masukkan ID Game: "))
            judul = input("Masukkan Judul Game: ")
            genre = input("Masukkan Genre Game: ")
            harga = float(input("Masukkan Harga Game: "))
            jumlah = int(input("Masukkan Stok Game: "))
            game = Game(id, judul, genre, harga, jumlah)
            game_store.add_game(game)
            print("Game berhasil ditambahkan!.")

        elif choice == "2":
            game_id = int(input("Masukkan ID Game yang ingin dihapus: "))
            if game_store.remove_game(game_id):
                print("Game berhasil dihapus!.")
            else:
                print("Game yang kamu cari ga ada!.")

        elif choice == "3":
            game_id = int(input("Masukkan ID Game yang ingin diupdate stoknya: "))
            new_stock = int(input("Masukkan Stok Baru: "))
            if game_store.update_game_stock(game_id, new_stock):
                print("Stok game berhasil diupdate!.")
            else:
                print("Game yang kamu cari ga ada!.")

        elif choice == "4":
            game_store.display_games()

        elif choice == "5":
            print("Terima kasih! Balik ya!")
            break

        else:
            print("Opsi tidak valid. Silakan pilih opsi yang benar.")

if __name__ == "__main__":
    main()

