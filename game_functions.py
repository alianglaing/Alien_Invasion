# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:10:31 2019

@author: 靓靓
"""

import sys
import pygame


def check_keydown_events(event,ship):
    """响应按下"""
    if event.key==pygame.K_RIGHT:
         #飞船向右移动
         ship.moving_right=True
         #print(ship.rect.centerx)
    elif event.key==pygame.K_LEFT:
         ship.moving_left=True

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key==pygame.K_RIGHT:
         #飞船向右移动
         ship.moving_right=False
         #print(ship.rect.centerx)
    elif event.key==pygame.K_LEFT:
         ship.moving_left=False

def check_events(ship):
     #监视键盘和鼠标事件
     for event in pygame.event.get():
         if event.type==pygame.QUIT:
             pygame.quit()
             sys.exit()             
         elif event.type==pygame.KEYDOWN:
             check_keydown_events(event,ship)
         elif event.type==pygame.KEYUP:
             check_keyup_events(event,ship)

def update_screen(screen,ship,bg_color):
    """更新屏幕上的图像，并切换至新屏幕"""
    #重新绘制屏幕
    screen.fill(bg_color)
    ship.blitme()
    #刷新屏幕
    pygame.display.flip()