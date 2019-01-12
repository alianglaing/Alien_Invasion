# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:32:17 2019

@author: 靓靓
"""


import pygame


from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_setting = Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color=ai_setting.bg_color
    ship = Ship(screen=screen,ai_setting=ai_setting)
    
    #开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        #更新屏幕
        gf.update_screen(screen,ship,bg_color)
       # print(ship.rect.centerx)
        

run_game()