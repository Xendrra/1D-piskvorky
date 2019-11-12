#!/usr/bin/env python3


class Gomoku_1D(object):
    """
    Třída obsahující implementaci piškvorek.
    """

    def __init__(
        self,
        gamester_symbol: str = 'x',
        computer_symbol: str = 'o',
        empty_symbol: str = '-',
        arena_size: int = 20
    ) -> object:
        """
        Inicializační metoda.
        """
        self._gamester_symbol = gamester_symbol
        self._computer_symbol = computer_symbol
        self._empty_symbol = empty_symbol
        self._arena_size = arena_size
        self._win_array = 3

        self.arena_init()

    def arena_init(self):
        """
        Inicializuje pole s arénou.
        """
        self._lap_counter = 0
        self._arena = [self._empty_symbol] * self._arena_size

    def is_end_game(self) -> bool:
        """
        Ujistí jestli jde provést další tah.
        """
        gamester_cnt = 0
        computer_cnt = 0
        for symbol in self._arena:
            if symbol == self._gamester_symbol:
                gamester_cnt += 1
                computer_cnt = 0
            elif symbol == self._computer_symbol:
                computer_cnt += 1
                gamester_cnt = 0
            else:
                gamester_cnt = 0
                computer_cnt = 0

            if gamester_cnt == self._win_array:
                print('Hráč vyhrál.')
                return True
            elif computer_cnt == self._win_array:
                print('Počítač vyhrál')
                return True

        if not self._empty_symbol in self._arena:
            print('Došla hrací pole')
            return True

        return False

    def game(self):
        """
        Hlavmí smyčka hry
        """
        while True:
            self._lap_counter += 1
            self.gamester_move()
            if self.is_end_game():
                self.show()
                break
            self.computer_move()
            self.show()
            if self.is_end_game():
                break

    def show(self):
        """
        Zobrazí arénu a informace o kole.
        """
        print(f'{self._lap_counter:2d} kolo: {"".join(self._arena)}')

    def gamester_move(self):
        """
        Implementace tahu hráče.
        """
        coordinates = None
        while coordinates is None:
            coordinates = input('Zadej pozici >>> ')
            if not coordinates.isdigit():
                print('Souřadnice nemá korektní formát.')
                coordinates = None
                continue
            coordinates = int(coordinates)
            if coordinates < 1 or coordinates > self._arena_size:
                print('Souřadnice se nenachází v aréně.')
                coordinates = None
                continue
            if self._arena[coordinates - 1] != self._empty_symbol:
                print('Pole je již obsazené')
                coordinates = None

        self._arena[coordinates - 1] = self._gamester_symbol

    def computer_move(self):
        """
        Implementace tahu počítače
        """

        class Rating(object):
            """
            Třída pro hodnocení políček arény.
            """

            def __init__(
                self,
                gamester_symbol: str,
                computer_symbol: str,
                empty_symbol: str,
                arena_size: int,
                arena: list
            ):
                """
                Inicializační metoda.
                """
                self._gamester_symbol = gamester_symbol
                self._computer_symbol = computer_symbol
                self._empty_symbol = empty_symbol
                self._arena_size = arena_size
                self._arena = arena

                self.rating = [0] * self._arena_size
                self.prepare_classification()

            def prepare_classification(self):
                """
                Vynulovní proměných před aplikováním metriky.
                """
                self.gamester_cnt = 0
                self.computer_cnt = 0

            def classify(self, i: int, symbol: str):

                if i > 0 and i < self._arena_size - 1:
                    if self._arena[i-1] == self._computer_symbol and self._arena[i] == self._empty_symbol and self._arena[i+1] == self._computer_symbol:
                        self.rating[i] += 100

                    if self._arena[i-1] == self._gamester_symbol and self._arena[i] == self._empty_symbol and self._arena[i+1] == self._gamester_symbol:
                        self.rating[i] += 50

                    if self._arena[i-1] == self._empty_symbol and self._arena[i] == self._gamester_symbol and self._arena[i+1] == self._empty_symbol:
                        self.rating[i-1] += 25
                        self.rating[i+1] += 25

                    if self._arena[i-1] == self._empty_symbol and self._arena[i] == self._gamester_symbol and self._arena[i+1] == self._gamester_symbol:
                        self.rating[i-1] += 50

                    if self._arena[i-1] == self._gamester_symbol and self._arena[i] == self._gamester_symbol and self._arena[i+1] == self._empty_symbol:
                        self.rating[i+1] += 50

                    if self._arena[i-1] == self._empty_symbol and self._arena[i] == self._computer_symbol and self._arena[i+1] == self._computer_symbol:
                        self.rating[i-1] += 100

                    if self._arena[i-1] == self._computer_symbol and self._arena[i] == self._computer_symbol and self._arena[i+1] == self._empty_symbol:
                        self.rating[i+1] += 100

                if symbol == self._gamester_symbol:
                    self.gamester_cnt += 1
                    self.computer_cnt = 0

                elif symbol == self._empty_symbol:
                    self.rating[i] += 1

                    self.rating[i] += self.gamester_cnt * 10
                    self.rating[i] += self.computer_cnt * 10

                    self.gamester_cnt = 0
                    self.computer_cnt = 0

                else:
                    self.gamester_cnt = 0
                    self.computer_cnt += 1

            def best_coordinates(self) -> int:
                """
                Vlátí index nejlépe hodnoceného políčka.
                """
                return self.rating.index(max(self.rating))

            def show(self):
                """
                Zobrazí ladící informace o hodnocení políček.
                """
                print(self.rating)

        rating = Rating(
            self._gamester_symbol,
            self._computer_symbol,
            self._empty_symbol,
            self._arena_size,
            self._arena
        )

        rating.prepare_classification()
        for i, symbol in enumerate(self._arena):
            rating.classify(i, symbol)
        rating.prepare_classification()
        for i, symbol in reversed(list(enumerate(self._arena))):
            rating.classify(i, symbol)

        rating.show()

        coordinates = rating.best_coordinates()
        if self._arena[coordinates] == self._empty_symbol:
            self._arena[coordinates] = self._computer_symbol


if __name__ == '__main__':
    gomoku = Gomoku_1D()
    gomoku.game()
