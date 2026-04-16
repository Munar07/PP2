import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder_name="music"):
        pygame.mixer.init()
        self.index = 0
        self.is_playing = False
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.music_folder = os.path.join(base_dir, music_folder_name)
        
        self.songs = []
        
        if os.path.exists(self.music_folder):
            for file in os.listdir(self.music_folder):
                if file.lower().endswith('.mp3'):
                    self.songs.append(file)
        else:
            print(f"Папка '{self.music_folder}' не найдена!")
            
        if not self.songs:
            print("В папке music нет MP3 файлов!")
        else:
            print(f"Найдено песен: {len(self.songs)}")

    def _get_full_path(self, filename):
        return os.path.join(self.music_folder, filename)

    def play(self):
        if not self.songs:
            return
            
        filename = self.songs[self.index]
        full_path = self._get_full_path(filename)
        
        try:
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.play()
            self.is_playing = True
            print(f"Играет: {filename}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next(self):
        if self.songs:
            self.index = (self.index + 1) % len(self.songs)
            self.play()

    def back(self):
        if self.songs:
            self.index = (self.index - 1) % len(self.songs)
            self.play()

    def name(self):
        if self.songs:
            return self.songs[self.index]
        return "No track"

    def time(self):
        if self.is_playing and pygame.mixer.music.get_busy():
            return int(pygame.mixer.music.get_pos() / 1000)
        return 0