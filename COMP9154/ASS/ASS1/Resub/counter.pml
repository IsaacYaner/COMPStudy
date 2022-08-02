#define EOF 255

int SIZE = 4;
int READERS = 3;
int ROUNDS = 7000;

byte CounterValue[SIZE];
bit Flags[SIZE];
byte Claimed[SIZE];
byte BackupValue1[SIZE];
byte BackupValue2[SIZE];
byte BackupValue3[SIZE];
byte ReadValue1[SIZE];
byte ReadValue2[SIZE];
byte ReadValue3[SIZE];
byte activate = 0;
byte cry = -1;
byte Saved[SIZE];
byte Saved1[SIZE];
byte Saved2[SIZE];
byte Saved3[SIZE];
bit done1=false;
bit done2=false;
bit done3=false;

proctype reader1() {
  byte j;
  byte claim = -1;
  bit flag = false;
  int k = 0;

  do
  ::k<ROUNDS->
    newround:
    claim = activate;
    Claimed[claim]++;
    byte i = 0;
    atomic
    {
      done1 = false;
      for (i : 0 .. SIZE-1)
      {
        Saved1[i] = Saved[i];
      }
    }
    for (j : 0 .. SIZE-1)
    {
      flag = Flags[j];
      if 
      ::((claim != activate) || (Flags[j] == true))->
        if
        ::claim == 1->ReadValue1[j] = BackupValue1[j];
        ::claim == 2->ReadValue1[j] = BackupValue2[j];
        ::claim == 3->ReadValue1[j] = BackupValue3[j];
        ::else->skip;
        fi
        
      ::else->
        ReadValue1[j] = CounterValue[j];
        if
        ::Flags[j] != flag->
          ReadValue1[j] = BackupValue1[j];
        ::else->
          skip;
        fi
      fi
    }
    done1 = true;
    Claimed[claim]--;
    claim = -1;
    k++;
  ::else->break;
  od
}
proctype reader2() {
  byte j;
  byte claim = -1;
  bit flag = false;
  int k = 0;

  do
  ::k<ROUNDS->
    newround:
    claim = activate;
    Claimed[claim]++;
    byte i = 0;
    atomic
    {
      done2 = false;
      for (i : 0 .. SIZE-1)
      {
        Saved2[i] = Saved[i];
      }
    }
    for (j : 0 .. SIZE-1)
    {
      flag = Flags[j];
      if 
      ::((claim != activate) || (Flags[j] == true))->
        if
        ::claim == 1->ReadValue2[j] = BackupValue1[j];
        ::claim == 2->ReadValue2[j] = BackupValue2[j];
        ::claim == 3->ReadValue2[j] = BackupValue3[j];
        ::else->skip;
        fi
        
      ::else->
        ReadValue2[j] = CounterValue[j];
        if
        ::Flags[j] != flag->
          ReadValue2[j] = BackupValue1[j];
        ::else->
          skip;
        fi
      fi
    }
    done2 = true;
    Claimed[claim]--;
    claim = -1;
    k++;
  ::else->break;
  od
}
proctype reader3() {
  byte j;
  byte claim = -1;
  bit flag = false;
  int k = 0;

  do
  ::k<ROUNDS->
    newround:
    claim = activate;
    Claimed[claim]++;
    byte i = 0;
    atomic
    {
      done3 = false;
      for (i : 0 .. SIZE-1)
      {
        Saved3[i] = Saved[i];
      }
    }
    for (j : 0 .. SIZE-1)
    {
      flag = Flags[j];
      if 
      ::((claim != activate) || (Flags[j] == true))->
        if
        ::claim == 1->ReadValue3[j] = BackupValue1[j];
        ::claim == 2->ReadValue3[j] = BackupValue2[j];
        ::claim == 3->ReadValue3[j] = BackupValue3[j];
        ::else->skip;
        fi
        
      ::else->
        ReadValue3[j] = CounterValue[j];
        if
        ::Flags[j] != flag->
          ReadValue3[j] = BackupValue1[j];
        ::else->
          skip;
        fi
      fi
    }
    done2 = true;
    Claimed[claim]--;
    claim = -1;
    k++;
  ::else->break;
  od
}

inline carry()
{
  byte i = cry;//%SIZE?
  if
  ::activate == 1->BackupValue1[i] = CounterValue[i];
  ::activate == 2->BackupValue2[i] = CounterValue[i];
  ::activate == 3->BackupValue3[i] = CounterValue[i];
  ::else->skip;
  fi
  Flags[i] = true;
  CounterValue[i]++;
  if
  ::(CounterValue[i] == 0 && i<SIZE)->cry = i+1;
  ::else->cry = -1;
  fi
}

proctype writer() {
  int k = 0;

  do
  ::k<ROUNDS->
  newround:
    if
    ::CounterValue[0] == 255->
      cry = 1;
      do
      ::(cry != 255)->carry();
      ::else->break;
      od
      byte i = 0;
      for (i : 0 .. SIZE-1)
      {
        if
        ::activate == 1->BackupValue1[i] = CounterValue[i];
        ::activate == 2->BackupValue2[i] = CounterValue[i];
        ::activate == 3->BackupValue3[i] = CounterValue[i];
        ::else->skip;
        fi
      }

      do
      ::Claimed[activate] != 0->activate = (activate+1)%READERS;
      ::else->break;
      od
      for (i : 0 .. SIZE-1)
      {
        Flags[i] = false;
      }
    :: else->CounterValue[0]++;
    fi
    atomic
    {
      for (i : 0 .. SIZE-1)
      {
        Saved[i] = CounterValue[i];
      }
    }
    k++;
  ::else->break;
  od
}


init {
  run writer();
  run reader1();
  run reader2();
  run reader3();
}

// Please enforce weak fairness contraint
// Please add evrdn for more readers
#define evrd1 ([]<>reader1@newround)
#define evrd2 ([]<>reader2@newround)
#define evrd3 ([]<>reader3@newround)
#define evwt ([]<>writer@newround)
ltl eventual_reader {evrd1&&evrd2&&evrd3&&evwt}

// For each reader, cvn, low[B][n], hi[B][n] are required in the same format
// Set low[highest byte] in the format below
#define low31 (CounterValue[3]>=ReadValue1[3])
// set low[0..highest] in the format below
#define low21 (CounterValue[3]==ReadValue1[3] implies CounterValue[2]>=ReadValue1[2])
#define low11 (CounterValue[2]==ReadValue1[2] implies CounterValue[1]>=ReadValue1[1])
#define low01 (CounterValue[1]==ReadValue1[1] implies CounterValue[0]>=ReadValue1[0])

// Set hi[highest byte] in the format below
#define hi31 (Saved1[3]<=ReadValue1[3])
// set hi[0..highest] in the format below
#define hi21 (Saved1[3]==ReadValue1[3] implies Saved1[2]<=ReadValue1[2])
#define hi11 (Saved1[2]==ReadValue1[2] implies Saved1[1]<=ReadValue1[1])
#define hi01 (Saved1[1]==ReadValue1[1] implies Saved1[0]<=ReadValue1[0])
#define high1 (done1 implies hi01&&hi11&&hi21&&hi31)
#define cv1 (low01&&low11&&low21&&low31&&high1)


// Set low[highest byte] in the format below
#define low32 (CounterValue[3]>=ReadValue2[3])
// set low[0..highest] in the format below
#define low22 (CounterValue[3]==ReadValue2[3] implies CounterValue[2]>=ReadValue2[2])
#define low12 (CounterValue[2]==ReadValue2[2] implies CounterValue[1]>=ReadValue2[1])
#define low02 (CounterValue[1]==ReadValue2[1] implies CounterValue[0]>=ReadValue2[0])

// Set hi[highest byte] in the format below
#define hi32 (Saved2[3]<=ReadValue2[3])
// set hi[0..highest] in the format below
#define hi22 (Saved2[3]==ReadValue2[3] implies Saved2[2]<=ReadValue2[2])
#define hi12 (Saved2[2]==ReadValue2[2] implies Saved2[1]<=ReadValue2[1])
#define hi02 (Saved2[1]==ReadValue2[1] implies Saved2[0]<=ReadValue2[0])
#define high2 (done2 implies hi02&&hi12&&hi22&&hi32)
#define cv2 (low02&&low12&&low22&&low32&&high2)


// Set low[highest byte] in the format below
#define low33 (CounterValue[3]>=ReadValue3[3])
// set low[0..highest] in the format below
#define low23 (CounterValue[3]==ReadValue3[3] implies CounterValue[2]>=ReadValue3[2])
#define low13 (CounterValue[2]==ReadValue3[2] implies CounterValue[1]>=ReadValue3[1])
#define low03 (CounterValue[1]==ReadValue3[1] implies CounterValue[0]>=ReadValue3[0])

// Set hi[highest byte] in the format below
#define hi33 (Saved3[3]<=ReadValue3[3])
// set hi[0..highest] in the format below
#define hi23 (Saved3[3]==ReadValue3[3] implies Saved3[2]<=ReadValue3[2])
#define hi13 (Saved3[2]==ReadValue3[2] implies Saved3[1]<=ReadValue3[1])
#define hi03 (Saved3[1]==ReadValue3[1] implies Saved3[0]<=ReadValue3[0])
#define high3 (done3 implies hi03&&hi13&&hi23&&hi33)
#define cv3 (low03&&low13&&low23&&low33&&high3)

// Please add &&cvn for more readers
ltl correct_value {cv1&&cv2&&cv3}
