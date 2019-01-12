# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:32:17 2019

@author: 靓靓
"""

import sys
import pygame
def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    screen=pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Alien Invasion")
    bg_color=(230,230,230)
    
    #开始游戏主循环
    while True:
         #监视键盘和鼠标事件
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit()
                 sys.exit()
        #重新绘制屏幕
         screen.fill(bg_color)
        #刷新屏幕
         pygame.display.flip()

run_game()