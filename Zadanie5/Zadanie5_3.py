import pygame
from random import randint

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)
SZEROKOSC_EKRANU = 700
WYSOKOSC_EKRANU = 700


class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > SZEROKOSC_EKRANU - 100:
           self.rect.x = SZEROKOSC_EKRANU - 100



class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(-8, -8), randint(4, 8)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = randint(-8,8)
        self.velocity[1] = -self.velocity[1]



# definiujemy rozmiary i otwieramy nowe okno
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietkaA = Rakietka(BIALY, 100, 10)
rakietkaA.rect.x = SZEROKOSC_EKRANU // 2
rakietkaA.rect.y = WYSOKOSC_EKRANU - 30

pileczka = Pilka(BIALY,10,10)
pileczka.rect.y = 100
pileczka.rect.x = SZEROKOSC_EKRANU // 2

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie rakietki i piłeczki do listy
all_sprites_list.add(rakietkaA)
all_sprites_list.add(pileczka)

# flaga - gramy dalej?
kontynuuj = True

koniecGry = False
najlepszy = 0

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowy wynik gracza
scoreA = 0

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    # ruchy obiektu Rakietka klawisze ->, <-
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rakietkaA.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        rakietkaA.moveRight(5)
    
    # aktualizacja listy duszków
    all_sprites_list.update()

    # sprawdzenie czy piłeczka nie uderza w którąś ścianę
    # i odpowiednie naliczenie punktu lub koniec gry
    if pileczka.rect.y<=0:
        scoreA+=1
        pileczka.velocity[1] = -pileczka.velocity[1]
    if pileczka.rect.y>=690:
        koniecGry = True
    if pileczka.rect.x>690:
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.x<0:
        pileczka.velocity[0] = -pileczka.velocity[0]

    # sprawdzenie kolizji piłeczki z rakietką
    if pygame.sprite.collide_mask(pileczka, rakietkaA):
      pileczka.bounce()

    # RYSOWANIE
    # czarny ekran
    screen.fill(CZARNY)
    
    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyników
    font = pygame.font.Font(None, 60)
    if (not koniecGry):
        text = font.render(str(scoreA), 1, BIALY)
        screen.blit(text, (330,10))
    else:
        najlepszy = max(scoreA, najlepszy)
        text = font.render('Koniec gry', 1, BIALY)
        screen.blit(text, (200, 10))
        text = font.render('Twój wynik: %d' %(scoreA), 1, BIALY)
        screen.blit(text, (200, 120))
        text = font.render('Najlepszy: %d' %(najlepszy), 1, BIALY)
        screen.blit(text, (200, 230))
        text = font.render('Enter - jeszcze raz', 1, BIALY)
        screen.blit(text, (200, 340))
        text = font.render('Esc - koniec', 1, BIALY)
        screen.blit(text, (200, 440))
        # obsługa końca gry
        if keys[pygame.K_RETURN]:
            koniecGry = False
            pileczka.rect.x = 300
            pileczka.rect.y = 100
            scoreA = 0
        elif keys[pygame.K_ESCAPE]:
            kontynuuj = False

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()