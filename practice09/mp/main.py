import pygame
from player import MusicPlayer

def main():
    pygame.init()
    pygame.mixer.init()

    # Создаем окно
    screen = pygame.display.set_mode((600, 250))
    pygame.display.set_caption("KBTU Music Player")
    
    font = pygame.font.SysFont("Arial", 22)
    clock = pygame.time.Clock()
    
    # Создаем объект плеера
    player = MusicPlayer()

    running = True
    while running:
        # 1. ОБЯЗАТЕЛЬНО: Очищаем экран в начале каждого кадра
        screen.fill((40, 40, 40)) 
        
        # 2. Обработка нажатий клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: player.play()
                if event.key == pygame.K_s: player.stop()
                if event.key == pygame.K_n: player.next_track()
                if event.key == pygame.K_b: player.prev_track()
                if event.key == pygame.K_q: running = False

        # 3. Получаем данные о треке
        track_name, position = player.get_info()
        
        # 4. Рисуем текст на экране (внутри цикла!)
        title_surf = font.render(f"Трек: {track_name}", True, (255, 255, 255))
        pos_surf = font.render(f"Время: {position:.1f} сек", True, (0, 255, 0))
        hint_surf = font.render("P: Play | S: Stop | N: Next | B: Back | Q: Quit", True, (150, 150, 150))

        screen.blit(title_surf, (30, 50))
        screen.blit(pos_surf, (30, 100))
        screen.blit(hint_surf, (30, 180))

        # 5. ОБЯЗАТЕЛЬНО: Обновляем экран
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()