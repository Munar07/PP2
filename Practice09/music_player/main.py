import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 250))
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

# Плеер сам найдет все mp3 в папке music/
player = MusicPlayer()

if player.songs:
    player.play()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: player.play()
            elif event.key == pygame.K_s: player.stop()
            elif event.key == pygame.K_n: player.next()
            elif event.key == pygame.K_b: player.back()
            elif event.key == pygame.K_q: run = False
            elif event.key == pygame.K_UP: 
                pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + 0.1))
            elif event.key == pygame.K_DOWN: 
                pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - 0.1))

    screen.fill((255, 255, 255))
    
    status = "Playing >>" if pygame.mixer.music.get_busy() else "Stopped"
    current_track = player.name() if player.songs else "No songs"
    
    screen.blit(font.render(f"Track: {current_track}", True, (0,0,0)), (50, 40))
    screen.blit(font.render(f"Status: {status}", True, (0,128,0)), (50, 80))
    screen.blit(font.render("Keys: P-play, S-stop, N-next, B-back, Q-quit", True, (0,0,0)), (50, 120))
    screen.blit(font.render(f"Total Songs: {len(player.songs)}", True, (0,0,0)), (50, 160))

    pygame.display.update()
    clock.tick(30)

pygame.quit()