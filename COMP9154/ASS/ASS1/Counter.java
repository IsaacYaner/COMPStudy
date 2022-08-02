public class Counter {

    public static int SIZE;
    public static int READERS;
    public static int ROUNDS;

    public static volatile Byte[] CounterValue;     // the main array to store the counter value
    public static volatile Boolean[] Flags;         // indicate the byte was carried
    public static volatile Byte[][] BackupValue;    // the backups of the counter value
    public static volatile int[] Claimed;           // how many current claims for a backup array
    public static int active = 0;                   // current active backup array for writer to write
    public static void main(String[] args) {
        try {
            READERS = Integer.parseInt(args[0]);
            SIZE = Integer.parseInt(args[1]);
            ROUNDS = Integer.parseInt(args[2]);
        } catch (Exception e) {
            System.out.println("Usage: java Ass1 [READERS] [SIZE] [ROUNDS]");
            System.exit(255);
        }

        System.out.println("Readers: " + READERS);
        System.out.println("Counter size: " + SIZE);
        System.out.println("Rounds: " + ROUNDS);

        // init
        CounterValue = new Byte[SIZE];
        Flags = new Boolean[SIZE];
        BackupValue = new Byte[READERS][SIZE];
        Claimed = new int[READERS];
        
        for (int i=0;i<SIZE;i++) {
            CounterValue[i] = 0;
            Flags[i] = false;
        }
        
        for (int i=0;i<READERS;i++) {
            for (int j=0;j<SIZE;j++) {
                BackupValue[i][j] = 0;
            }
            Claimed[i] = 0;
        }


        Writer coun = new Writer();

        coun.start();


        for (int i=0;i<READERS;i++) {
            Reader r = new Reader();
            r.start();
            System.out.println("Reader: " + i + " started");
        }


    }

    public static class Writer extends Thread {

        private int i = 0;
        private String s = "";

        @Override
        public void run() {
            while (true) {
                // increase Value
                CounterValue[0]++;
                // manage carry
                if (CounterVal(0) == 0) {
                    carry(1);
                    //seal the value
                    if (Claimed[active] != 0) {
                        for (int j=0;j<SIZE;j++) {
                            BackupValue[active][j] = CounterValue[j];
                        }
                    } 
                    // active next
                    while (Claimed[active] != 0) {
                        active = (active+1)%READERS;
                    }
                    // reset flags
                    for (int j=0;j<SIZE;j++) {
                        Flags[j] = false;
                    }
                }

                // print value
                s = "  Write value:";
                for (int j=SIZE-1;j>=0;j--) {
                    s+=" ";
                    s+=Integer.toHexString(CounterVal(j));
                }
                System.out.println(s);
                i++;
                if (i == ROUNDS) {
                    break;
                }
                if (ROUNDS == 0) {
                    i--;
                }
            }
            System.out.println("Finished counting");
        }
    }

    public static class Reader extends Thread {

        private int i = 0;
        private int claim = -1;
        private String s = "";
        private Boolean flag = false;
        private Byte[] ReadValue = new Byte[SIZE];


        @Override
        public void run() {
            while (true) {
                // claim backup
                claim = active;
                Claimed[claim]++;
                // read value
                for (int j=0;j<SIZE;j++) {
                    //check backup
                    flag = Flags[j];
                    if (claim != active || Flags[j] == true) {
                        ReadValue[j] = BackupValue[claim][j];
                    } else {
                        ReadValue[j] = CounterValue[j];
                        // recheck
                        if (Flags[j] != flag) {
                            ReadValue[j] = BackupValue[claim][j];
                        }
                    }
                }
                // reset claim
                Claimed[claim]--;
                claim = -1;

                // print value
                s = getId() + " Read value:";
                for (int j=SIZE-1;j>=0;j--) {
                    s+=" ";
                    s+=Integer.toHexString((int)ReadValue[j] & 0xff);
                }
                System.out.println(s);
                i++;
                if (i == ROUNDS) {
                    break;
                }
                if (ROUNDS == 0) {
                    i--;
                }
            }
        }
    }


    public static void carry(int i)  {
        i = i%SIZE;
        // backup
        BackupValue[active][i] = CounterValue[i];
        Flags[i] = true;
        // increament
        CounterValue[i]++;
        if (CounterVal(i) == 0) {
            carry(i+1);
        }
    }




    public static int CounterVal(int i) {
        return ((int)CounterValue[i] & 0xff);
    }

}