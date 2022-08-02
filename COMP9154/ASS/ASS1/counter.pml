#define EOF 255

int SIZE = 4;
int READERS = 3;

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

proctype reader1() {
  byte j;
  byte claim = -1;
  bit flag = false;
  do
  ::true->
    newround:
    claim = activate;
    Claimed[claim]++;
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
    Claimed[claim]--;
    claim = -1;
  od
}
proctype reader2() {
  byte j;
  byte claim = -1;
  bit flag = false;
  do
  ::true->
    newround:
    claim = activate;
    Claimed[claim]++;
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
    Claimed[claim]--;
    claim = -1;
  od
}
proctype reader3() {
  byte j;
  byte claim = -1;
  bit flag = false;
  do
  ::true->
    newround:
    claim = activate;
    Claimed[claim]++;
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
    Claimed[claim]--;
    claim = -1;
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
  do
  ::true->
  newround:
    CounterValue[0]++;
    if
    ::CounterValue[0] == 0->
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
    :: else->skip;
    fi
  od
}


init {
  run writer();
  run reader1();
  run reader2();
  run reader3();
}

// Please enforce weak fairness contraint
#define evrd1 ([]<>reader1@newround)
#define evrd2 ([]<>reader2@newround)
#define evrd3 ([]<>reader3@newround)
#define evwt ([]<>writer@newround)
ltl eventual_reader {evrd1&&evrd2&&evrd3&&evwt}

// Set corr[highest byte] in the format below
#define corr3 (CounterValue[3]>=ReadValue1[3])
// set corr[0..highest] in the format below
#define corr2 (CounterValue[3]==ReadValue1[3] implies CounterValue[2]>=ReadValue1[2])
#define corr1 (CounterValue[2]==ReadValue1[2] implies CounterValue[1]>=ReadValue1[1])
#define corr0 (CounterValue[1]==ReadValue1[1] implies CounterValue[0]>=ReadValue1[0])
ltl correct_value {corr0&&corr1&&corr2&&corr3}
