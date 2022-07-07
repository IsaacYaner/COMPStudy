public class BusyWaitSemaphore implements Semaphore3151 {

    class CounterValue {
        private volatile int count;
    
        public CounterValue(int v) {
            count = v;
        }
        
        public synchronized void increment() {
            count++;
        }

        public synchronized Boolean decrement() {
            if (count <= 0)
                return false;
            count--;
            return true;
        }

        public synchronized int read() {
            return count;
        }
    }
    
    private CounterValue c;
    public BusyWaitSemaphore(int v) {
        c = new CounterValue(v);
    }
    @Override
    public void P() {
        while (!c.decrement())
        {
            Thread.yield();
        }
    }

    @Override
    public void V() {
        c.increment();
    }
}
