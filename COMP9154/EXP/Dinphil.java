import java.util.concurrent.Semaphore;

public class Dinphil
{
    public static void main(String[] args)
    {
        Semaphore fork1 = new Semaphore(1, false);
        Semaphore fork2 = new Semaphore(1, false);
        Semaphore fork3 = new Semaphore(1, false);
        Thread t1 = new Philosopher("Hegel", fork1, fork2);
        Thread t2 = new Philosopher("Plato", fork2, fork3);
        Thread t3 = new Philosopher("Acerroes", fork1, fork3);
        t1.start();
        t2.start();
        t3.start();
    }
}