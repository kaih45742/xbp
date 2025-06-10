import serial
import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/kai23/mygit/xbp/project1/tengokutojigoku.mp3")

#HC-06が割り当てられているCOMポートに変更
ser = serial.Serial("COM7", 9600, timeout=1)
playing = False
print("Arduinoからの値を監視しています...")

while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        if line.isdigit():
            light_value = int(line)
            print("センサー値:", light_value)

            if light_value >= 200:
                if not playing:
                    print("▶ 明るさが200以上。ループ再生開始")
                    pygame.mixer.music.play(-1)
                    playing = True
            else:
                if playing:
                    print("▶ 明るさが200未満。再生停止")
                    pygame.mixer.music.stop()
                    playing = False

        time.sleep(0.1)

    except Exception as e:
        print("エラー:", e)
