public class CigaretteSmokers {
    static Semaphore3151 agent    = new JavaSemaphore(1);
    static Semaphore3151 tobacco  = new JavaSemaphore(0);
    static Semaphore3151 paper    = new JavaSemaphore(0);
    static Semaphore3151 match    = new JavaSemaphore(0);
    static Semaphore3151 readyA   = new JavaSemaphore(0);
    static Semaphore3151 readyB   = new JavaSemaphore(0);
    static Semaphore3151 readyC   = new JavaSemaphore(0);
    static Semaphore3151 pusher   = new JavaSemaphore(1);
    
    static int sleeptime = 10;
    static Boolean readyMatch = false;
    static Boolean readyTobacco = false;
    static Boolean readyPaper = false;
    public static void main(String[] args) {
        AgentA a = new AgentA();
        AgentB b = new AgentB();
        AgentC c = new AgentC();
        SmokerA sa = new SmokerA();
        SmokerB sb = new SmokerB();
        SmokerC sc = new SmokerC();
        pusherMatch pm = new pusherMatch();
        pusherTobacco pt = new pusherTobacco();
        pusherPaper pp = new pusherPaper();

        a.start();
        b.start();
        c.start();
        sa.start();
        sb.start();
        sc.start();
        pm.start();
        pt.start();
        pp.start();
    }

    // Smoker with Tobacco
    public static class SmokerA extends Thread {

        private void smoke() {
            System.out.println("SMOKEA: Got a paper and matches. Puff Puff.");
        }
        @Override
        public void run() {
            while (true) {
                readyA.P();
                smoke();
                try {
                    Thread.sleep(sleeptime);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                agent.V();
            }
        }
    }

    // Smoker with Paper
    public static class SmokerB extends Thread {

        private void smoke() {
            System.out.println("SMOKEB: Got tobacco and matches. Puff Puff.");
        }
        @Override
        public void run() {
            while (true) {
                readyB.P();
                smoke();
                try {
                    Thread.sleep(sleeptime);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                agent.V();
            }
        }
    }
    // Smoker with Matches
    public static class SmokerC extends Thread {

        private void smoke() {
            System.out.println("SMOKEC: Got tobacco and paper. Puff Puff.");
        }
        @Override
        public void run() {
            while (true) {
                readyC.P();
                smoke();
                try {
                    Thread.sleep(sleeptime);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                agent.V();
            }
        }
    }

    /* Do not change anything below this line */
    public static class AgentA extends Thread {
        @Override
        public void run() {
            while (true) {
                agent.P();
                System.out.println("AGENTA: Supplying tobacco and paper");
                tobacco.V();
                paper.V();
                try {
                    Thread.sleep(sleeptime);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    public static class AgentB extends Thread {
        @Override
        public void run() {
            while (true) {
                agent.P();
                System.out.println("AGENTB: Supplying paper and match");
                paper.V();
                match.V();
                try {
                    Thread.sleep(sleeptime);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    public static class AgentC extends Thread {
        @Override
        public void run() {
            while (true) {
                agent.P();
                System.out.println("AGENTC: Supplying tobacco and match");
                tobacco.V();
                match.V();
                try {
                    Thread.sleep(sleeptime);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    public static class pusherMatch extends Thread {
        @Override
        public void run() {
            while (true) {
                match.P();
                pusher.P();
                readyMatch = true;
                if (readyPaper)
                {
                    //Consume
                    readyPaper = false;
                    readyMatch = false;
                    readyA.V();
                    pusher.V();
                    continue;
                }
                if (readyTobacco)
                {
                    //Consume
                    readyPaper = false;
                    readyMatch = false;
                    readyB.V();
                    pusher.V();
                    continue;
                }
                pusher.V();
            }
        }
    }
    public static class pusherTobacco extends Thread {
        @Override
        public void run() {
            while (true) {
                tobacco.P();
                pusher.P();
                readyTobacco = true;
                if (readyMatch)
                {
                    //Consume
                    readyMatch = false;
                    readyTobacco = false;
                    readyB.V();
                    pusher.V();
                    continue;
                }
                if (readyPaper)
                {
                    //Consume
                    readyPaper = false;
                    readyTobacco = false;
                    readyC.V();
                    pusher.V();
                    continue;
                }
                pusher.V();
            }
        }
    }
    public static class pusherPaper extends Thread {
        @Override
        public void run() {
            while (true) {
                paper.P();
                pusher.P();
                readyPaper = true;
                if (readyTobacco)
                {
                    //Consume
                    readyTobacco = false;
                    readyPaper = false;
                    readyC.V();
                    pusher.V();
                    continue;
                }
                if (readyMatch)
                {
                    //Consume
                    readyMatch = false;
                    readyPaper = false;
                    readyA.V();
                    pusher.V();
                    continue;
                }
                pusher.V();
            }
        }
    }


}
