class DayConvert:
    def __init__(self):
        while True:
            day_input = input("day 2cifre 01-31: ") 
            if day_input.isdigit() and len(day_input) == 2 and 1 <= int(day_input) <= 31:
                self.dayregex = day_input
            else:
                print("errore solo valori numerioci da 01-31") 
    def to_python(self):
        return(self.dayregex)
converter1 =  DayConvert() 
print(f"valire inserito: {converter1.dayregex}")  