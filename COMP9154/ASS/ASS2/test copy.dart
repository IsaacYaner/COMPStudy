import 'dart:isolate';
void main() async
{
  await iso();
}

class ProducerId
{
  int id;
  SendPort sendPort;
  ProducerId(this.id, this.sendPort);
}
class ConsumerId
{
  int id;
  SendPort sendPort;
  ConsumerId(this.id, this.sendPort);
}

int NUM_PRODUCER = 2;
int NUM_CONSUMER = 2;
int MAX_ITER = 5;
int SIZE = 3;
int TOTAL_GENERALS = 3;

iso() async
{
  ReceivePort consumerPort = new ReceivePort();
  SendPort sendConsumer = consumerPort.sendPort;
  for(int i = 1; i <= NUM_CONSUMER; i++)
    Isolate.spawn(consume, ConsumerId(i, sendConsumer));
  
  List<int> plan = [];

  int received = 0;
  consumerPort.listen((message) {
    received++;
      plan[message.G] = message.plan;
  });
  while(received <= TOTAL_GENERALS)
  {
    await Future.delayed(Duration(milliseconds: 100));
  }
  print('do next step');
  return;
}

void produce(ProducerId id) async
{
  int idd = id.id;
  for(int i = 0; i < MAX_ITER; i++)
  {
    id.sendPort.send('$idd');
    await Future.delayed(Duration(milliseconds: 100));
  }
  id.sendPort.send('close');
}

void consume(ConsumerId id) async
{
  int idd = id.id;
  for(int i = 0; i < MAX_ITER*NUM_PRODUCER/NUM_CONSUMER; i++)
  {
    id.sendPort.send('con $idd');
    await Future.delayed(Duration(milliseconds: 100));
  }
  id.sendPort.send('close');
}