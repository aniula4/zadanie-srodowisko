class Kwadrat():
    def __init__(self, bok): # konstruktor jak się dowiedzieliśmy jest metodą prywatną, nie można go wywołać na obiekcie klasy po kropce, ani po za klasą
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): # dziedziczymy po klasie Kwadrat aby móć skorzystać z jej funkcjonalności
    def sketchPasiasty(self, x, y, paski): # dodajemy ilość pasków, w które ma być kwadrat
        Kwadrat.sketch(self, x, y) # korzystamy z metody klasy bazowej
        space = self.bok/paski # wyliczamy przerwęmiędzy paskami
        _xLinii_ = 0 # to jest pole chronione, nie powinno się go używać w kodzie po za klaą i klasami po niej dziedziczącymi 
        for pasek in range(0, paski): # dorysowujemy paski
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space

class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self, x, y, colorR, colorG, colorB):
        fill(colorR, colorG, colorB) 
        Kwadrat.sketch(self, x, y)
        
                            
def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0) # obiekt typu kwardrat o wielkości 50
    malyKwadrat.sketch(200, 300) # rysujemy go w podanych wsółrzędnych
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyKwadrat.sketch(100, 200) # rysujemy kwadrat wielkości 50 również w innych współrzędnych
    malyPasiastyKwadrat = PasiastyKwadrat(30.0) # tu tworzymy obiekt typu pasiasty kwadrat korzystając z konstruktora klasy bazowej
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5) # umieszczamy stworzony kwadrat w 5 pasków w tych współrzędnych
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) # a teraz w 8 pasów w innych współrzędnych
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(300, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300) # na obiekcie typu klasy pochodnej można wywołać metodę klasy bazowej ( rysujemy kwadrat bez pasków )
    
    rozowyKwadrat = KolorowyKwadrat(100.0)
    rozowyKwadrat.sketchKolorowy(10, 370, 255, 204, 204)
    niebieskiKwadrat = KolorowyKwadrat(70.0)
    niebieskiKwadrat.sketchKolorowy(120, 370, 0, 0, 255)
    zielonyKwadrat = KolorowyKwadrat(50.0)
    zielonyKwadrat.sketchKolorowy(200, 370, 0, 255, 0)
    
    # 2pkt, jest ok
    
