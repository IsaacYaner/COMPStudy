import 'dart:isolate';
import 'dart:math';

enum AorR {
  A,
  R,
  T;
}

class GeneralPort {
  int id;
  SendPort port;
  bool traitor;
  int num_traitors;
  int num_generals;
  GeneralPort(
      this.id, this.port, this.traitor, this.num_traitors, this.num_generals);
}

class Plan {
  int id;
  AorR plan;
  Plan(this.id, this.plan);
}

class KingsPlan {
  int id;
  AorR plan;
  KingsPlan(this.id, this.plan);
}

class TraitorsPlan {
  int id;
  TraitorsPlan(this.id);
}

class KingTraitorsPlan {
  int id;
  KingTraitorsPlan(this.id);
}

class PlanTable {
  int id;
  List<AorR> plans;
  PlanTable(this.id, this.plans);
}

class FinalPlan {
  int id;
  AorR plan;
  FinalPlan(this.id, this.plan);
}

void main(List<String> arguments) async {
  // init default number of traitors & generals
  int NUM_TRAITORS = 1;
  int NUM_GENERALS = 4 * NUM_TRAITORS + 1;
  if (arguments.length == 2) {
    var arg0 = int.parse(arguments[0]);
    var arg1 = int.parse(arguments[1]);
    if (arg0 > 0 && arg1 >= 0) {
      NUM_GENERALS = arg0;
      NUM_TRAITORS = arg1;
      if (NUM_TRAITORS >= NUM_GENERALS) {
        print(
            "Invalid NUM_TRAITORS, it should at least be smaller than NUM_GENERALS");
        return;
      }
    } else {
      print("Invalid NUM_GENERALS or NUM_TRAITORS");
      return;
    }
  }

  // init plan table
  List<AorR> finalplans = <AorR>[];
  var table = <List<String>>[];
  for (int i = 0; i < NUM_GENERALS; i++) {
    table.add(<String>[]);
    finalplans.add(AorR.T);
  }

  // create the main port and init varibles
  ReceivePort mainport = new ReceivePort();
  List<GeneralPort> GEN = [];
  int k = 0;
  int j = 0;
  int r = 0;
  AorR kingPlan = AorR.R;

  // randomly select traitors
  var traitors = <int>{};
  bool isTraitor;
  while (traitors.length < NUM_TRAITORS) {
    int traitor = Random().nextInt(NUM_GENERALS);
    traitors.add(traitor);
  }
  print("traitors: $traitors");

  // spawn generals
  for (int i = 0; i < NUM_GENERALS; i++) {
    if (traitors.contains(i)) {
      isTraitor = true;
    } else {
      isTraitor = false;
    }
    await Isolate.spawn(
        general,
        GeneralPort(
            i, mainport.sendPort, isTraitor, NUM_TRAITORS, NUM_GENERALS));
  }

  mainport.listen((msg) async {
    if (msg is GeneralPort) {
      // save general's port for future communication
      GEN.add(msg);
    } else if (msg is Plan || msg is TraitorsPlan) {
      // add msg back to the queue when the ports has not been all received
      if (GEN.length != NUM_GENERALS) {
        mainport.sendPort.send(msg);
      } else {
        // send plan or traitor's plan
        if (msg is TraitorsPlan) {
          for (GeneralPort G in GEN) {
            if (G.id != msg.id) {
              bool random = Random().nextBool();
              if (random) {
                G.port.send(Plan(msg.id, AorR.A));
              } else {
                G.port.send(Plan(msg.id, AorR.R));
              }
            }
          }
        } else {
          for (GeneralPort G in GEN) {
            if (G.id != msg.id) {
              G.port.send(msg);
            }
          }
        }
      }
      // check if every general is finished then send signal to general's to let them pass
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
      // send King's plan
    } else if (msg is KingsPlan) {
      kingPlan = msg.plan;
      for (GeneralPort G in GEN) {
        if (G.id != msg.id) {
          G.port.send(msg);
        }
      }
      // close the port
    } else if (msg == 'close') {
      for (GeneralPort G in GEN) {
        G.port.send('close');
      }
      mainport.close();
      // send traitor's plan as King's plan
    } else if (msg is KingTraitorsPlan) {
      kingPlan = AorR.T;
      for (GeneralPort G in GEN) {
        if (G.id != msg.id) {
          bool random = Random().nextBool();
          if (random) {
            G.port.send(KingsPlan(msg.id, AorR.A));
          } else {
            G.port.send(KingsPlan(msg.id, AorR.R));
          }
        }
      }
      // print table's for each generals every rounds
    } else if (msg is PlanTable) {
      for (int i = 0; i < NUM_GENERALS; i++) {
        table[msg.id].add(msg.plans[i].name);
      }
      j++;
      if (j == NUM_GENERALS) {
        j = 0;
        //print tables
        print("Round: $r");
        String k = kingPlan.name;
        print("King's plan: $k");
        for (int i = 0; i < NUM_GENERALS; i++) {
          List<String> p = table[i];
          print("General $i: $p");
        }
        print("=======================");
        // increment round
        r++;
        // clear the table
        table = <List<String>>[];
        for (int i = 0; i < NUM_GENERALS; i++) {
          table.add(<String>[]);
        }
        // awake generals
        for (GeneralPort G in GEN) {
          G.port.send(true);
        }
      }
      // print every general's final plan
    } else if (msg is FinalPlan) {
      k++;
      finalplans[msg.id] = msg.plan;
      if (k == NUM_GENERALS) {
        for (int i = 0; i < NUM_GENERALS; i++) {
          String p = finalplans[i].name;
          print("General $i's final plan: $p");
        }
        // test the if the consensus is reached
        bool consensus = true;
        AorR a = finalplans[0];
        AorR b = AorR.A;
        if (a == AorR.A) {
          b = AorR.R;
        }
        if (finalplans.contains(b)) {
          consensus = false;
        }
        print("Conensus test: $consensus");

        for (GeneralPort G in GEN) {
          G.port.send('close');
        }
        mainport.close();
      }
    }
  });
}

void general(GeneralPort main) async {
  ReceivePort me = new ReceivePort();
  int id = main.id;
  main.port.send(GeneralPort(id, me.sendPort, false, 0, 0));
  bool next1 = false;
  bool next2 = false;
  int count = 0;
  int NUM_GENERALS = main.num_generals;
  int NUM_TRAITORS = main.num_traitors;

  int votesMajority = 0;
  AorR kingPlan = AorR.R;
  AorR myMojority = AorR.R;
  List<AorR> plan = [];
  AorR finalPlan = AorR.R;
  bool isTraitor = false;

  if (main.traitor == true) {
    isTraitor = true;
  }

  int k = 0;

  // deciede my plan
  bool random = Random().nextBool();
  AorR myplan;
  if (random) {
    myplan = AorR.A;
  } else {
    myplan = AorR.R;
  }

  // init planlist
  for (int i = 0; i < NUM_GENERALS; i++) {
    plan.add(myplan);
  }

  me.listen((msg) async {
    // recieve plan and count the number
    if (msg is Plan) {
      plan[msg.id] = msg.plan;
      k++;
      // receive passing signal's
    } else if (msg is bool) {
      next1 = true;
    }
    // sending finish signal when all plans are received
    if (k == NUM_GENERALS - 1) {
      //go next
      main.port.send(true);
      k = 0;
      // receive the king's plan then let the general pass
    } else if (msg is KingsPlan) {
      next2 = true;
      kingPlan = msg.plan;
      // close the port
    } else if (msg == 'close') {
      me.close();
    }
  });

  for (int r = 0; r < NUM_TRAITORS + 1; r++) {
    // send plans to all other generals
    if (isTraitor == true) {
      main.port.send(TraitorsPlan(id));
    } else {
      main.port.send(Plan(id, myplan));
    }

    // wait until receive plans from all other generals
    while (next1 == false) {
      await Future.delayed(Duration(milliseconds: 10));
    }
    next1 = false;

    // find majority
    count = 0;
    for (AorR p in plan) {
      if (p == AorR.A) {
        count++;
      }
    }
    if (count >= (NUM_GENERALS + 1) / 2) {
      myMojority = AorR.A;
    } else {
      myMojority = AorR.R;
      count = NUM_GENERALS - count;
    }

    // votes Majority
    votesMajority = count;

    // check if my turn to be king
    if (r == id) {
      // send my Majority as King
      if (isTraitor == true) {
        main.port.send(KingTraitorsPlan(id));
      } else {
        main.port.send(KingsPlan(id, myMojority));
      }
      plan[id] = myMojority;
    } else {
      // wait to recive king's plan
      while (next2 == false) {
        await Future.delayed(Duration(milliseconds: 10));
      }
      next2 = false;

      if (votesMajority > (NUM_GENERALS / 2 + NUM_TRAITORS)) {
        plan[id] = myMojority;
      } else {
        plan[id] = kingPlan;
      }
    }
    myplan = plan[id];

    // send my table and wait for others and audit before next round
    main.port.send(PlanTable(id, plan));
    while (next1 == false) {
      await Future.delayed(Duration(milliseconds: 10));
    }
    next1 = false;
  }

  // making final decision
  finalPlan = plan[id];
  main.port.send(FinalPlan(id, finalPlan));

  return;
}
