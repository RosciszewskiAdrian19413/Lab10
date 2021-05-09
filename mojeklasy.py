def testy():
    #Zadanie 1:
    p1 = Student("Adrian","Rosciszewski",19413,"IIS")
    
    print(p1.imie)
    print(p1.nazwisko)
    #print(p1.__nr_indeksu)
    print(p1.kierunek)
    
    print(p1)
    
    #Zadanie 2:
    p2 = Student("Karol","Prabucki",18452,"IIS")
    
    print(p1.__lt__(p2))
    print(p1.__eq__(p2))
    
    #Zadanie 3:
    p3 = Student("Adrian","Rosciszewski",19413,"IIS")
    
    print("Licznik wynosi %s"%(p3.getLicznik()))
    
    #Zadanie 4:
    p4 = StudentInformatyki("Adrian","Rosciszewski",19413,"IIS","Grafika Komputerowa")
    print(p4)
    
    print(p4.specjalnosc)
    
    #Zadanie 5:
    p5 = StudentInformatyki("Adrian","Rosciszewski",19413,"IIS","Grafika Komputerowa", "2")
    print(p5)
        print(p5.imie)
        print(p5.nazwisko)
        print(p5.__nr_indeksu)
        print(p5.kierunek)
        print(p5.rok)
    
        print(p5)
    
    
    print(p5.rok)
    pass

class Student():
    __licznik = 0
    
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek
        
    def getLicznik(self):
        return self.__licznik
        
    def __lt__(self,other):
    
        if self.nazwisko < other.nazwisko:
            return True
        else:
            return False
            
        
    def __eq__(self,other):
        if self.nazwisko == other.nazwisko:
            return True
        else:
            return False
    
    def __str__(self):
        return "Imie: %s\n Nazwisko: %s\n Nr ideksu: %s\n Kierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)

    def rok_drugi(self):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek
        self.rok = rok
        

class StudentInformatyki(Student):

    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki,self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "IIS"
        self.specjalnosc = specjalnosc
        self.rok = rok



if __name__ == "__main__":
    testy()
