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

int NUM_PRODUCER = 4;
int NUM_CONSUMER = 2;
int MAX_ITER = 10;
int SIZE = 3;

iso() async
{
  ReceivePort producerPort = new ReceivePort();
  ReceivePort consumerPort = new ReceivePort();
  SendPort sendProducer = producerPort.sendPort;
  SendPort sendConsumer = consumerPort.sendPort;
  for(int i = 1; i <= NUM_PRODUCER; i++)
    Isolate.spawn(produce, ProducerId(i, sendProducer));
  for(int i = 1; i <= NUM_CONSUMER; i++)
    Isolate.spawn(consume, ConsumerId(i, sendConsumer));
  
  List<String> items = [];
  int close = 0;

  producerPort.listen((message) async {
    if(message == 'close')
    {
      close ++;
      if (close == NUM_PRODUCER)
        producerPort.close();
    }
    else
    {
      // print('Message: $message');
      while(items.length >= SIZE)
      {
          await Future.delayed(Duration(milliseconds: 10));
      }
      items.add(message);
      print('Producing: $items');
    }
  });

  int closeConsume = 0;
  consumerPort.listen((message) async {
    if(message == 'close')
    {
      closeConsume ++;
      if (closeConsume == NUM_CONSUMER)
        consumerPort.close();
    }
    else
    {
      while(items.length <= 0)
      {
          await Future.delayed(Duration(milliseconds: 10));
      }
      String last = items[items.length-1];
      items.removeAt(items.length-1);
      print('Consuming: $items $last');
    }
  });

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