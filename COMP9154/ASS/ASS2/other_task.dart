import 'dart:isolate';
import  'dart:io';


void main(args, SendPort port1) {
  print("isolate_1 start");
  print("isolate_1 args: $args");

  ReceivePort receivePort = new ReceivePort();
  SendPort port2 = receivePort.sendPort;

  receivePort.listen((message){
    print("isolate_1 message: $message");
  });

  // 将当前 isolate 中创建的SendPort发送到主 isolate中用于通信
  port1.send([0, port2]);
  // 模拟耗时5秒
  sleep(Duration(seconds:5));
  port1.send([1, "isolate_1 任务完成"]);

  print("isolate_1 stop");
}