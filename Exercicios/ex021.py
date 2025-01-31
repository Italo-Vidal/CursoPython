import pygame # Aqui tem que instalar o pygame no seu VSCode ou pycharm

# Inicializa todos os módulos do pygame
pygame.init()

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('ex021.mp3')

# Reproduz o arquivo MP3
pygame.mixer.music.play()

parar = str(input('Aperta [ P ] para desligar: '))
