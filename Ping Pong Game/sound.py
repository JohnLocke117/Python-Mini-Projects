from pygame import mixer
mixer.init()

class Sound:
    def __init__(self):
        pass

    def bg_music(self):
        mixer.music.load(r"stuff\music.mp3")
        mixer.music.set_volume(1.0)
        mixer.music.play(-1)

    def collision(self):
        ball_collision = mixer.Sound(r"stuff\collide.wav")
        ball_collision.play()

    def game_lose(self):
        lose = mixer.Sound(r"stuff\lose.wav")
        lose.play()

    def wall_collision(self):
        wall_collide = mixer.Sound(r"stuff\wall.wav")
        wall_collide.play()

    def paddle_sound(self):
        paddle = mixer.Sound(r"stuff\paddle.wav")
        paddle.set_volume(0.3)
        paddle.play()

    def game_over(self):
        over = mixer.Sound(r"stuff\game over.wav")
        over.play()
