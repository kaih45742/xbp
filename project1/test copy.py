import serial
import time
import pygame  # pygameで音声を再生

# --- MP3ファイルの絶対パスを指定 ---
mp3_path = "C:/Users/kai23/mygit/xbp/project1/ahiru2.mp3"  # ←ご自身のMP3ファイルのパスに変更

# pygameの初期化
pygame.mixer.init()
pygame.mixer.music.load(mp3_path)

# シリアルポートとボーレートを指定
port = "COM7"
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
                    print("磁力の強さ:", strength)

                    # しきい値判定でMP3再生
                    if strength < 20000 or strength > 70000:
                        print("🔔 異常な磁力を検知！音を再生します")
                        pygame.mixer.music.play()

                        # 音が鳴り終わるまで待機（必要なら）
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)

                except ValueError:
                    pass

except serial.SerialException as e:
    print("シリアル接続に失敗しました:", e)
