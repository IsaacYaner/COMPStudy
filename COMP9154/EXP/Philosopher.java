import java.util.concurrent.Semaphore;

public class Philosopher extends Thread
{
    String name;
    Semaphore left_fork;
    Semaphore right_fork;

    public Philosopher(String string, Semaphore fork1, Semaphore fork2) {
        this.name = string;
        this.left_fork = fork1;
        this.right_fork = fork2;
    }

    public void run()
    {
        while(true)
        {
            System.out.println(name + " thinks...");
            try {
                Thread.sleep(150);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            left_fork.acquireUninterruptibly();
                
            System.out.println(name + " grab a fork...");
            try {
                Thread.sleep(150);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(name + " grab another fork...");
            right_fork.acquireUninterruptibly();
            System.out.println(name + "eating...");
            try {
                Thread.sleep(150);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(name + " releases forks...");
            left_fork.release();
            right_fork.release();
        }
    }
}

