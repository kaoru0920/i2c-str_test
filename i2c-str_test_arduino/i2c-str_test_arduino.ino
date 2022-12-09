/*
   RasPi-Arduino I2C通信(Arduino側プログラム)

   date:2022/12/09

   master:RasPi
   slave:arduino
*/

#include <Wire.h>

//グローバル変数初期化
const int SLAVE_ADDRESS = 0x13;  //I2Cのアドレスを設定
char recv_msg[32];               //受信メッセージ保管場所

/*初期化*/
void setup() {
  Serial.begin(9600);             //シリアル通信開始
  Wire.begin(SLAVE_ADDRESS);      //I2C接続開始
  Wire.onReceive(ReceiveMessage); //I2C受信時に実行される関数を登録
  Wire.onRequest(RequestMessage); //I2C送信時に実行される関数を登録
}

/*メインループ*/
void loop() {

}

/*受信時処理*/
void ReceiveMessage(int n) {

  //変数初期化
  char tmp;
  int loop = 0;

  //受信処理
  while (Wire.available()) {            // 要求より短いデータが来る可能性あり
    tmp = Wire.read();                  // 1バイトずつ受信
    recv_msg[loop] = tmp;
    if (recv_msg[loop] == '\n') {
      break;                            //改行コードが来たら抜ける
    }
    loop++;
  }
  Serial.println(recv_msg);             //受信したメッセージを表示
}

/*送信時処理*/
void RequestMessage() {
  /*※改行コードで終端を判別しているため、メッセージの最後には改行コードをつけること*/
  Wire.write("message from arduino\n"); //メッセージをi2c経由で送信
}
