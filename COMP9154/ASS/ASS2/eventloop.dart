import 'dart:async';
void main()
{
  print('main function');
  
  new Future((() => print('Event executing')));

  scheduleMicrotask(() {
    print('micro task executing');
  });

  print('main ends');
}
