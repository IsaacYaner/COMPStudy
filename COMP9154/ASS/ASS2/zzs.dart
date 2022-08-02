 import 'dart:convert';
  import 'dart:io';
  import 'dart:isolate';
  
    List<Isolate> isolates = [];
  
  void start() async {
  
    isolates.add(await Isolate.spawn(runSomething, 'first'));
    isolates.add(await Isolate.spawn(runSomething, 'second'));
    isolates.add(await Isolate.spawn(runSomething, 'third'));
  }
  
  void runSomething(String arg) async {
    print('arg: $arg');
    var request = await HttpClient().getUrl(Uri.parse('https://swapi.co/api/people/1'));
    var response = await request.close();
  
    await for (var contents in response.transform(Utf8Decoder())) {
      print(contents);
    }
  }
  
  void stop() {
    for (Isolate i in isolates) {
      if (i != null) {
        i.kill(priority: Isolate.immediate);
        i = null;
        print('Killed');
      }
    }
  }
  
  void main() async {
    await start();
  
    print('Press enter to exit');
    await stdin.first;
  
    stop();
    exit(0);
  }