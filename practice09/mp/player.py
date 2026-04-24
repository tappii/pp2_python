import pygame
import os

class MusicPlayer:
    def __init__(self):
        # Находим путь к папке music относительно этого файла
        self.base_path = os.path.dirname(__file__)
        self.music_dir = os.path.join(self.base_path, "music")
        
        # Загружаем список всех mp3 файлов
        if os.path.exists(self.music_dir):
            self.playlist = [f for f in os.listdir(self.music_dir) if f.endswith('.mp3')]
            self.playlist.sort()
        else:
            self.playlist = []
            print(f"Ошибка: Папка {self.music_dir} не найдена!")

        self.current_index = 0

    def play(self):
        if not self.playlist:
            return
        
        # Берем файл из списка и загружаем его
        track_path = os.path.join(self.music_dir, self.playlist[self.current_index])
        try:
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            print(f"Играет: {self.playlist[self.current_index]}")
        except Exception as e:
            print(f"Не удалось загрузить трек: {e}")

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()

    def prev_track(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    def get_info(self):
        # Возвращаем название трека и время для отрисовки
        if not self.playlist:
            return "Нет файлов", 0
        
        name = self.playlist[self.current_index]
        pos = pygame.mixer.music.get_pos() / 1000.0 if pygame.mixer.music.get_busy() else 0.0
        return name, pos