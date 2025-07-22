import serial
import time
import pygame  # pygameで音声を再生

# --- MP3ファイルの絶対パスを指定 ---
mp3_path = "C:/Users/kai23/mygit/xbp/project1/歓声　ゆうごくん.mp3"  # ←ご自身のMP3ファイルのパスに変更

# pygameの初期化
pygame.mixer.init()
pygame.mixer.music.load(mp3_path)

# シリアルポートとボーレートを指定
port = "COM5"
baudrate = 9600

try:
    ser = serial.Serial(port, baudrate, timeout=1)
    time.sleep(2)  # Arduinoのリセット待ち
    print("シリアル接続中...")

    while True:
        line = ser.readline().decode("utf-8").strip()
        if line:
            print("Received:", line)

            if "Strength:" in line:
                try:
                    strength_str = line.split("Strength:")[-1].strip()
                    strength = float(strength_str)
                    print("strength:", strength)

                    # しきい値判定でMP3再生
                    if strength < 32000 or strength > 37000:
                        print("磁力の変化を検知、音を再生")
                        pygame.mixer.music.play()

                        # 音が鳴り終わるまで待機
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)

                        print("再生完了。プログラムを終了")
                        break  # ← ここでループを終了

                except ValueError:
                    pass

    ser.close()

except serial.SerialException as e:
    print("シリアル接続に失敗しました:", e)
