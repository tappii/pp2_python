import pygame
import clock  # Импортируем файл как модуль

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("KBTU Practice 7: Mickey Clock")
    timer = pygame.time.Clock()
    
    # Создаем объект ТУТ (внутри функции main)
    # Используем формат: модуль.Класс
    mickey_clock = clock.MickeyClock(800, 800)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        
        # Отрисовка
        mickey_clock.draw(screen)
        
        pygame.display.flip()
        timer.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()