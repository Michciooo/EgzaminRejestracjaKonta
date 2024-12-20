class Sortowanie:
    def __init__(self):
        self.array = []

    def wypelnij_tablice(self):
        print("Wypełnij tablicę:")
        for x in range(1, 11):
            nowa_liczba = int(input(f"Podaj {x} element tablicy do dodania: "))
            self.array.append(nowa_liczba)

        '''
        /******************************************************** 
        * nazwa funkcji: wypelnij_tablice
        * parametry wejściowe: brak
        * wartość zwracana: brak , wypelnia tablice liczbami podanymi przez uzytkownika
        * autor: 2137
        * ****************************************************/ 
        '''

    def _znajdz_indeks_najwiekszej_wartosci(self, start):
        max_index = start
        for x in range(start + 1, len(self.array)):
            if self.array[x] > self.array[max_index]:
                max_index = x
        return max_index

        '''
        /******************************************************** 
        * nazwa funkcji: znajdz_indeks_najwiekszej_wartosci
        * parametry wejściowe: start - int
        * wartość zwracana: int , zwraca indeks najwiekszej liczby z danej tablicy
        * autor: 2137
        * ****************************************************/ 
        '''

    def sortowanie_malejaco(self):
        for i in range(len(self.array)):
            max_index = self._znajdz_indeks_najwiekszej_wartosci(i)
            self.array[i], self.array[max_index] = self.array[max_index], self.array[i]
        print(self.array)

        '''
        /******************************************************** 
        * nazwa funkcji: sortowanie_malejaco
        * parametry wejściowe: brak
        * wartość zwracana: brak , sortuje malejaco i wyswietla posortowana tablice
        * autor: 2137
        * ****************************************************/ 
        '''


if __name__ == "__main__":
    sort = Sortowanie()
    sort.wypelnij_tablice()
    print("Tablica po sortowaniu malejąco:")
    sort.sortowanie_malejaco()
