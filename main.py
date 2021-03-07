import pygame, sys, os
from pygame._sdl2 import Window, Texture, Image, Renderer, get_drivers, messagebox
#import dosyalar.kutuphaneler.bolumMaster

pygame.init()
pygame.display.init
pygame.display.set_caption("Star of Dreams")
#os.chdir("StarOfDreams_V10")

print("|------------------------------|")
print("|Kütüphane dosyaları yükleniyor|")

import dosyalar.kutuphaneler.bolumMaster as bolumMaster
import dosyalar.kutuphaneler.ekranMaster as ekranMaster
import dosyalar.kutuphaneler.mekanikMaster as mekanikMaster
import dosyalar.bolumler.menu as menu

bolumMaster.test()
mekanikMaster.test()
ekranMaster.test()

print("|Tüm sistemler hazır, ==>menü  |")
print("|------------------------------|")

bolumMaster.yuklenmeEkrani()
pygame.time.wait(500)
menu.menuA()
