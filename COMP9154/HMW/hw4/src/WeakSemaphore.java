public class WeakSemaphore implements Semaphore3151 {
    
    class CounterValue {
        private volatile int count;
    
        public CounterValue(int v) {
            count = v;
        }
        
        public synchronized void increment() {
            count++;
            notify();
        }

        public synchronized void decrement() {
            if (count <= 0)
            {
                try {
                    wait();
                }
                catch(InterruptedException e) {}
            }
            count--;
            notify();
        }

        public synchronized int read() {
            return count;
        }
    }

    private CounterValue c;
    public WeakSemaphore(int v) {
        c = new CounterValue(v);
    }

    @Override
    public void P() {
        c.decrement();
    }

    @Override
    public void V() {
        c.increment();
    }

}
