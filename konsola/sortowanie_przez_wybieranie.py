class Sortowanie:
    def __init__(self):
        self.array = []

    def wypelnij_tablice(self):
        print("Wypełnij tablicę:")
        for x in range(1, 11):
            nowa_liczba = int(input(f"Podaj {x} element tablicy do dodania: "))
            self.array.append(nowa_liczba)

    def _znajdz_indeks_najwiekszej_wartosci(self, start):
        max_index = start
        for x in range(start + 1, len(self.array)):
            if self.array[x] > self.array[max_index]:
                max_index = x
        return max_index

    def sortowanie_malejaco(self):
        for i in range(len(self.array)):
            max_index = self._znajdz_indeks_najwiekszej_wartosci(i)
            self.array[i], self.array[max_index] = self.array[max_index], self.array[i]
        print(self.array)


if __name__ == "__main__":
    sort = Sortowanie()
    sort.wypelnij_tablice()
    print("Tablica po sortowaniu malejąco:")
    sort.sortowanie_malejaco()
