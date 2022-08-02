#define EOF 255

int SIZE = 4;
int READERS = 3;
int ROUNDS = 70000;

byte CounterValue[SIZE];
bit Flags[SIZE];
byte Claimed[SIZE];
byte BackupValue1[SIZE];
byte BackupValue2[SIZE];
byte BackupValue3[SIZE];
byte activate = 0;
byte cry = -1;

proctype reader() {
  byte j;
  byte claim = -1;
  bit flag = false;
  byte ReadValue[SIZE];
  do
  ::true->
    claim = activate;
    Claimed[claim]++;
    for (j : 0 .. SIZE-1)
    {
      flag = Flags[j];
      if 
      ::((claim != activate) || (Flags[j] == true))->
        if
        ::claim == 1->ReadValue[j] = BackupValue1[j];
        ::claim == 2->ReadValue[j] = BackupValue2[j];
        ::claim == 3->ReadValue[j] = BackupValue3[j];
        ::else->skip;
        fi
        
      ::else->
        ReadValue[j] = CounterValue[j];
        if
        ::Flags[j] != flag->
          ReadValue[j] = BackupValue1[j];
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
  run reader();
  run reader();
  run reader();
}
