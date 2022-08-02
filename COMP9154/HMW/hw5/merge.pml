#define EOF 255

chan input1 = [0] of { byte };
chan input2 = [0] of { byte };
chan output = [0] of { byte };
byte sorted[10];

proctype merge() {
  bit read1 = true;
  bit read2 = true;
  byte val1 = 0;
  byte val2 = 0;

  do
  :: true->
  read: printf("New Loop!\n"); 
  // Read if readn == true
    if
    :: read1->
        printf("read1\n"); 
        input1 ? val1;
        // read1 = false;
    :: else->skip;
    fi
    if
    ::  read2->printf("read2\n"); 
        input2 ? val2;
        // read1 = false;
    :: else->skip;
    fi

  // Set readn to false once EOF is met
  // Else make readn true (because it may be
  // silented by output phase)
  if 
  :: val1 == EOF->
      read1=false;
  :: else->  read1 = true;
  fi
  if
  :: val2 == EOF->
      read2=false;
  :: else->  read2 = true;
  fi

  // Break cycle and output value
  // Only output once, so set another read to false
  // if it's not outputed
  if
  :: ((read1 == false) && (read2 == false))->
    goto finish;
  :: ((read1 == true) && (read2 == false))->
    output ! val1;
  :: ((read1 == false) && (read2 == true))->
    output ! val2;
  :: else->
    if
      :: (val1 < val2)->
        output ! val1;
        read2 = false;
      :: else->
        output ! val2;
        read1 = false;
    fi
  fi
  
  goto read;
  finish:  
  printf("Finishing!!!!!!!\n"); 
  output ! EOF;
  break;
  od;
}

proctype send1()
{
  input1 ! 1;
  input1 ! 3;
  input1 ! 5;
  input1 ! 7;
  input1 ! 9;
  input1 ! EOF;
}
proctype send2()
{
  input2 ! 2;
  input2 ! 4;
  input2 ! 6;
  input2 ! 8;
  input2 ! 10;
  input2 ! EOF;
}
proctype receive()
{
  byte i = 0;
  do
  :: true->
    output ? sorted[i];
    if 
    :: sorted[i] == EOF->break;
    :: else->skip;
    fi
    i++;
  od
}


init {
  run merge();
  run send1();
  run send2();
  run receive();
}


// proctype send1()
// {
//   do
//   :: true -> input1 ! 1;
//   :: true -> input1 ! 2;
//   :: true -> input1 ! 3;
//   :: true -> input1 ! 4;
//   :: true -> input1 ! 5;
//   :: true -> input1 ! 6;
//   :: true -> input1 ! 7;
//   :: true -> input1 ! 8;
//   :: true -> input1 ! 9;
//   :: true -> 
//     input1 ! EOF;
//     break;
//   od;
// }
// proctype send2()
// {
//   do
//   :: true -> input2 ! 1;
//   :: true -> input2 ! 2;
//   :: true -> input2 ! 3;
//   :: true -> input2 ! 4;
//   :: true -> input2 ! 5;
//   :: true -> input2 ! 6;
//   :: true -> input2 ! 7;
//   :: true -> input2 ! 8;
//   :: true -> input2 ! 9;
//   :: true -> 
//     input2 ! EOF;
//     break;
//   od;
// }