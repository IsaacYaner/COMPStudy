import 'dart:async';
void main() async
{
  print('main function');
  
  await new Future((() => print('Event executing')));

  scheduleMicrotask(() {
    print('micro task executing');
  });

  print('main ends');
}
