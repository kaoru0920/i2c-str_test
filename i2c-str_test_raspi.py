"""
   RasPi-Arduino I2C通信(RasPi側プログラム)

   date:2022/12/09

   master:RasPi
   slave:arduino

"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus  # I2C通信するためのモジュールsmbusをインポートする
import time  # sleepするためにtimeモジュールをインポートする

# I2C受信


def readMessage(device_address):

    # 変数初期化
    loop = 0
    tmp = ""
    cha = bus.read_i2c_block_data(device_address, 0, 32)

    while 1:
        tmp = tmp+chr(cha[loop])
        if (chr(cha[loop]) == '\n'):
            break  # 改行コードが来たら抜ける
        loop = loop+1
    return str(tmp)  # 受信した文字列を返す

# I2C送信


def sendMessage(device_address, message):

    msg_list = list(map(ord, list(message)))  # 変換
    bus.write_i2c_block_data(device_address, 0x00, msg_list)  # 送信

    return


"""メイン関数"""
if __name__ == '__main__':
    bus = smbus.SMBus(1)  # I2C通信するためのモジュール、smbusのインスタンスを作成
    address = 0x13  # I2C通信したいアドレスを指定

    try:
        while True:
            # Arduinoへ文字列を送信
            sendMessage(address, "message from raspi\n")

            # Arduinoからのメッセージを表示
            data = readMessage(address)
            print(data)

            # 0.5sスリープする
            time.sleep(1)

    except KeyboardInterrupt:  # Ctl+Cが押されたら終了
        print("Ctl+C\n")
    except Exception as e:
        print(str(e))
    finally:
        print("exit program\n")
