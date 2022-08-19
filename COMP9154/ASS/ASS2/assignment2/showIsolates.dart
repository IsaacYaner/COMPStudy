import 'dart:isolate';

void main() {
  print("main isolate start");
  create_isolate();
  print("main isolate end");
}

// Create an isolate
create_isolate() {
  ReceivePort rp = new ReceivePort();
  SendPort port1 = rp.sendPort;

  Isolate.spawn(doWork, port1);

  rp.listen((message){
    print("Received message: $message");
    rp.close();
  });
}

// Isolated job
void doWork(SendPort port1){
  print("new isolate start");
  port1.send("doWork Finished!");
  print("new isolate end");
}