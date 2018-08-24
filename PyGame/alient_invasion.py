import sys
import pygame
from settings import  Settings
from pygame.sprite import Group
from ship import Ship
import game_function as gf
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一艘飞船
    screen = pygame.display.set_mode([ai_settings.screen_width,ai_settings.screen_height])
    pygame.display.set_caption('Alient Invasion')
    ship = Ship(ai_settings,screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()