


public class Queens {

	public static void main(String[] args){
		new Queens(Integer.parseInt(args[0])).run();
	}
    int n = 13;

    public Queens(int N) {
        
        this.n = N;
    }

    public void run() {
        enumerate(new int[this.n], 0);
    }

    private static boolean isConsistent(int[] q, int n) {
        int i = 0;
        while (i < n) {
            if (q[i] == q[n] || q[i] - q[n] == n - i || q[n] - q[i] == n - i) {
                return false;
            }
            i++;
        }
        return true;
    }

    public static void enumerate(int[] q, int n) {
        int N = q.length;
        if (n != N) {
            for (int i = 0; i < N; i++) {
                q[n] = i;
                if (isConsistent(q, n)) {
                    enumerate(q, n + 1);
                }
            }
        }
    }
}

