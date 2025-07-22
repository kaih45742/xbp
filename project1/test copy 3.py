import serial
import time

# シリアルポートとボーレートを指定
port = "COM5"  # ← 実際のArduinoのポートに合わせて変更
baudrate = 9600

try:
    ser = serial.Serial(port, baudrate, timeout=1)
    time.sleep(2)  # Arduinoのリセット待ち
    print("シリアル接続中...")

    while True:
        line = ser.readline().decode("utf-8").strip()
        if line:
            print("Received:", line)

            # 例: Strengthの値だけ取り出したい場合
            if "Strength:" in line:
                try:
                    strength_str = line.split("Strength:")[-1].strip()
                    strength = float(strength_str)
                    print("磁力の強さ:", strength)

                    # 強さがしきい値を超えたら音を鳴らす（オプション）
                    if strength > 40000:
                        print("🔔 強い磁力を検知！音を鳴らします")
                        # Windows の場合：beep音
                        import winsound
                        winsound.Beep(1000, 500)  # 周波数, 時間(ms)

                except ValueError:
                    pass

except serial.SerialException as e:
    print("シリアル接続に失敗しました:", e)
