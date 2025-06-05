import serial
import pygame
import time

# pygame初期化
pygame.mixer.init()

# 音声ファイル（絶対パスにする）
pygame.mixer.music.load("C:/Users/kai23/mygit/xbp/project1/tengokutojigoku.mp3")  # パスは自分のものに書き換えてください

# Arduinoと接続するCOMポート（適宜変更）
ser = serial.Serial("COM5", 9600, timeout=1)  # COM番号は環境により異なる

# 状態管理（何度も再生しないように）
playing = False

print("Arduinoからの値を監視しています...")

while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        if line.isdigit():
            light_value = int(line)
            print("センサー値:", light_value)

            if light_value >= 400 and not playing:
                print("▶ 明るさが200以上！音を再生します。")
                pygame.mixer.music.play()
                playing = True

            # 再生が終わったら playing をリセット
            if not pygame.mixer.music.get_busy() and playing:
                playing = False

        time.sleep(0.1)

    except Exception as e:
        print("エラー:", e)
