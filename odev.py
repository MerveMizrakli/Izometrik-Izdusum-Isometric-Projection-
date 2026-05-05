import pygame
import numpy as np #burada tanımladığım nump kütüphanesini np adıyla kaydettim.

# Ekran boyutları
WIDTH, HEIGHT = 900, 700 #ekran genişiği ve yükseklik değerleri.Pygame bu değerleri baz alarak bir ekran oluşturacak.

# Pygame ayarları ; başlık , ekranda baz alınacak değerler.
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IZOMETRIK KUP CIZIM CALISMASI")

BACKGROUND_COLOR = (20, 20, 20)  # Küplerin çizileceği arkaplanın rengini siyah yaptım
AXIS_COLOR = (255, 255, 255)     # Koordinat düzlemindeki x,y,z eksenlerini ifade eden beyaz çizgi
CUBE1_COLOR = (200, 128, 128)      # Küp 1 rengi 
CUBE2_COLOR = (255, 165,0)       # Küp 2 rengi 
CUBE3_COLOR = (255, 69, 20)        # Küp 3 rengi (kırmızı)

# Küplerle ve arkaplanla ilgili renkleri belirledikten sonra küp değerlerini girip konumlarına yerleştiriyorum.
def kupyap(size, center):
    half = size / 2
    x, y, z = center
    return [
        [x - half, y - half, z - half],
        [x + half, y - half, z - half],
        [x + half, y + half, z - half],
        [x - half, y + half, z - half],
        [x - half, y - half, z + half],
        [x + half, y - half, z + half],
        [x + half, y + half, z + half],
        [x - half, y + half, z + half]
    ]

    # İzometrik projeksiyon matrisi
ISO_MATRIX = np.array([
    [np.sqrt(3) / 2, -np.sqrt(3) / 2, 0],
    [1 / 2, 1 / 2, -1]
])

# İzometrik dönüşüm yaptığımız fonksiyon.
def izometrikdonusum(points):
    transformed = []
    for point in points:
        projected = np.dot(ISO_MATRIX, point)
        transformed.append((projected[0] + WIDTH // 2, HEIGHT // 2 - projected[1])) #yaptığımız eklemeleri küpün konumuna entegre ettik.
    return transformed

# Çizgi çizme
def ciz(screen, points, edges, color):
    for edge in edges:
        start, end = points[edge[0]], points[edge[1]]
        pygame.draw.line(screen, color, start, end, 2)

EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 0),  #alt
    (4, 5), (5, 6), (6, 7), (7, 4),  #üst
    (0, 4), (1, 5), (2, 6), (3, 7)   #yan
]

cube1 = kupyap(100, (0, 0, 0))  # Orijinal küp , herhangi bir öteleme değeri girmedim.
cube2 = kupyap(100, (0, 0, 200))  # Z eksenine 2 birim öteleme yapıyorum. Z ekseni olduğu için 3. sıradaki sayı değerini değiştirmeliyiz.
cube3 = kupyap(50, (100, 100, 300))  # 100 birim x ,100 birim y , 300 birim de z ekseninde değişiklik yapılmış küpün verileri.

# İzometrik dönüşümleri gerçekleştiriyorum.
cube1_iso = izometrikdonusum(cube1)
cube2_iso = izometrikdonusum(cube2)
cube3_iso = izometrikdonusum(cube3)

running = True  #bu kısım programın çalışma süreci sırasında ekranın siyah olmasını istediğimiz için yazdığım kod.
while running:
    screen.fill(BACKGROUND_COLOR)
    
    # pygame kütüphanesi yardımıyla burada elimizdeki verileri eksenlere entegre ediyoruz.
    pygame.draw.line(screen, AXIS_COLOR, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2 + 200, HEIGHT // 2), 2)  # X Ekseni
    pygame.draw.line(screen, AXIS_COLOR, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2 - 200), 2)  # Y Ekseni
    pygame.draw.line(screen, AXIS_COLOR, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2 - 150, HEIGHT // 2 + 150), 2)  # Z Ekseni

    # Küpleri çiz
    ciz(screen, cube1_iso, EDGES, CUBE1_COLOR)
    ciz(screen, cube2_iso, EDGES, CUBE2_COLOR)
    ciz(screen, cube3_iso, EDGES, CUBE3_COLOR)

    pygame.display.flip() #yapılan tüm değişiklikler ve küplerin ekrana gelmesini sağlayan pygame fonksiyonunu çağırdık.

    #klavyeden gelen hareketlere bağlı olarak sistemdeki bilgileri getirir veya sistemden çıkış yapar.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
