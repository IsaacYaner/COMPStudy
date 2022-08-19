import 'dart:isolate';
import 'dart:math';

int NUM_TRAITORS = 1;
int NUM_GENERALS = 4 * NUM_TRAITORS + 1;
List<GeneralPort> GEN = [];
// var GEN = <GeneralPort>{};

class GeneralPort {
  int id;
  SendPort port;
  GeneralPort(this.id, this.port);
}

class Plan {
  int id;
  bool plan;
  Plan(this.id, this.plan);
}

void main() async {
  ReceivePort mainport = new ReceivePort();
  List<GeneralPort> GEN = [];
  int k = 0;

  for (int i = 0; i < NUM_GENERALS; i++) {
    await Isolate.spawn(general, GeneralPort(i, mainport.sendPort));
  }

  mainport.listen((msg) async {
    if (msg is GeneralPort) {
      GEN.add(msg);
    } else if (msg is Plan) {
      if (GEN.length != NUM_GENERALS) {
        mainport.sendPort.send(
            msg); // add msg to the queue when the ports has not been all received
      } else {
        for (GeneralPort G in GEN) {
          if (G.id != msg.id) {
            G.port.send(msg);
            // var id1 = msg.id;
            // var id2 = G.id;
            //print("$id1 message to $id2 sent");
          }
        }
      }
    } else if (msg is bool) {
      if (msg == true) {
        k++;
      }
      if (k == NUM_GENERALS) {
        for (GeneralPort G in GEN) {
          G.port.send(true);
        }
        k = 0;
      }
    }
    // int gid = msg.id;
    // bool plan = msg.plan;
    // print("Report: $gid, $plan");
  });
}

void general(GeneralPort main) async {
  ReceivePort me = new ReceivePort();
  int id = main.id;
  main.port.send(GeneralPort(id, me.sendPort));
  bool next = false;

  int votesMajority;
  int King = 0;
  bool kingPlan;
  List<bool> plan = [];

  int k = 0;

  // deciede my plan
  bool myplan = Random().nextBool();
  print("General $id initial plan: $myplan");

  //init planlist
  for (int i = 0; i < NUM_GENERALS; i++) {
    plan.add(myplan);
  }

  me.listen((msg) async {
    if (msg is Plan) {
      plan[msg.id] = msg.plan;
      k++;
    } else if (msg is bool) {
      print("$id: $plan");
      next = true;
    }
    if (k == NUM_GENERALS - 1) {
      //next ronund
      main.port.send(true);
      k = 0;
    }
  });

  for (int r = 1; r <= NUM_TRAITORS + 1; r++) {
    // send plans to all other generals
    main.port.send(Plan(id, myplan));

    // receive plans from all other generals

    next = false;

    // await for (var msg in me) {
    //   if (msg is Plan) {
    //     int gid = msg.id;
    //     bool plan = msg.plan;
    //     print("I am general $id. Report: $gid, $plan");
    //     k++;
    //   }
    //   if (k >= NUM_GENERALS - 1) {
    //     me.drain();
    //     main.port.send(true);
    //     break;
    //   }
    // }

    // for (int i = 0; i < NUM_GENERALS; i++) {
    //   await for (var msg in me) {
    //     int gid = msg.id;
    //     bool plan = msg.plan;
    //     print("I am general $id. Report: $gid, $plan");
    //   }
    // }

    // find majority

    // votes Majority

    // check if my turn to be king

    // send my Majority as King

    // or receive King's plan

  }
  // making final decision

  return;
}
