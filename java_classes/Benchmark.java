import java.lang.reflect.Array;
import org.antlr.runtime.ANTLRReaderStream;



public class Benchmark {

	public static void main(String[] args){
		System.out.print(new Benchmark().run());
	}
    private static final double MIN_TIME = 2.0d;
    private static final int RANDOM_SEED = 101010;

    public Benchmark() {
        
    }

    public double run() {
        Random R = new Random(RANDOM_SEED);
        double fftResult = this.measureFFT(ANTLRReaderStream.READ_BUFFER_SIZE, R);
        double sorResult = measureSOR(100, R);
        double montecarloResult = measureMonteCarlo(R);
        return ((((fftResult + sorResult) + montecarloResult) + measureSparseMat(100, 2.47E-321d, R)) + measureLU(100, R)) / 5.0d;
    }

    private double measureFFT(int N, Random R) {
        double[] x = RandomVector(N * 2, R);
        long cycles = 1;
        Stopwatch Q = new Stopwatch();
        while (true) {
            Q.start();
            for (int i = 0; ((long) i) < cycles; i++) {
                FFT.transform(x);
                FFT.inverse(x);
            }
            Q.stop();
            if (Q.read() >= MIN_TIME) {
                break;
            }
            cycles *= 2;
        }
        if (FFT.test(x) / ((double) N) > 1.0E-10d) {
            return 0.0d;
        }
        return ((FFT.num_flops(N) * ((double) cycles)) / Q.read()) * 1.0E-6d;
    }

    private static double measureSOR(int N, Random R) {
        double[][] G = RandomMatrix(N, N, R);
        Stopwatch Q = new Stopwatch();
        int cycles = 1;
        while (true) {
            Q.start();
            SOR.execute(1.25d, G, cycles);
            Q.stop();
            if (Q.read() >= MIN_TIME) {
                return (SOR.num_flops(N, N, cycles) / Q.read()) * 1.0E-6d;
            }
            cycles *= 2;
        }
    }

    private static double measureMonteCarlo(Random R) {
        Stopwatch Q = new Stopwatch();
        int cycles = 1;
        while (true) {
            Q.start();
            MonteCarlo.integrate(cycles);
            Q.stop();
            if (Q.read() >= MIN_TIME) {
                return (MonteCarlo.num_flops(cycles) / Q.read()) * 1.0E-6d;
            }
            cycles *= 2;
        }
    }

    private static double measureSparseMat(int N, int nz, Random R) {
        int i;
        int i2 = N;
        int i3 = nz;
        Random random = R;
        double[] x = RandomVector(i2, random);
        double[] y = new double[i2];
        int nr = i3 / i2;
        int anz = nr * i2;
        double[] val = RandomVector(anz, random);
        int[] col = new int[anz];
        int[] row = new int[(i2 + 1)];
        row[0] = 0;
        for (int r = 0; r < i2; r++) {
            int rowr = row[r];
            row[r + 1] = rowr + nr;
            int step = r / nr;
            if (step < 1) {
                step = 1;
            }
            for (i = 0; i < nr; i++) {
                col[rowr + i] = i * step;
            }
        }
        Stopwatch Q = new Stopwatch();
        i = 1;
        while (true) {
            Stopwatch Q2 = Q;
            Q2.start();
            Stopwatch Q3 = Q2;
            int cycles = i;
            SparseCompRow.matmult(y, val, row, col, x, i);
            Q3.stop();
            if (Q3.read() >= MIN_TIME) {
                return (SparseCompRow.num_flops(i2, i3, cycles) / Q3.read()) * 1.0E-6d;
            }
            i = cycles * 2;
            Q = Q3;
            random = R;
        }
    }

    private static double measureLU(int N, Random R) {
        double[][] A = RandomMatrix(N, N, R);
        double[][] lu = (double[][]) Array.newInstance(double.class, new int[]{N, N});
        int[] pivot = new int[N];
        Stopwatch Q = new Stopwatch();
        int cycles = 1;
        while (true) {
            Q.start();
            for (int i = 0; i < cycles; i++) {
                CopyMatrix(lu, A);
                LU.factor(lu, pivot);
            }
            Q.stop();
            if (Q.read() >= MIN_TIME) {
                break;
            }
            cycles *= 2;
        }
        double[] b = RandomVector(N, R);
        double[] x = NewVectorCopy(b);
        LU.solve(lu, pivot, x);
        if (normabs(b, matvec(A, x)) / ((double) N) > 1.0E-12d) {
            return 0.0d;
        }
        return ((LU.num_flops(N) * ((double) cycles)) / Q.read()) * 1.0E-6d;
    }

    private static double[] NewVectorCopy(double[] x) {
        int N = x.length;
        double[] y = new double[N];
        for (int i = 0; i < N; i++) {
            y[i] = x[i];
        }
        return y;
    }

    private static void CopyVector(double[] B, double[] A) {
        int N = A.length;
        for (int i = 0; i < N; i++) {
            B[i] = A[i];
        }
    }

    private static double normabs(double[] x, double[] y) {
        double sum = 0.0d;
        for (int i = 0; i < x.length; i++) {
            sum += Math.abs(x[i] - y[i]);
        }
        return sum;
    }

    private static void CopyMatrix(double[][] B, double[][] A) {
        int M = A.length;
        int N = A[0].length;
        int remainder = N & 3;
        for (int i = 0; i < M; i++) {
            int j;
            double[] Bi = B[i];
            double[] Ai = A[i];
            for (j = 0; j < remainder; j++) {
                Bi[j] = Ai[j];
            }
            for (j = remainder; j < N; j += 4) {
                Bi[j] = Ai[j];
                Bi[j + 1] = Ai[j + 1];
                Bi[j + 2] = Ai[j + 2];
                Bi[j + 3] = Ai[j + 3];
            }
        }
    }

    private static double[][] RandomMatrix(int M, int N, Random R) {
        double[][] A = (double[][]) Array.newInstance(double.class, new int[]{M, N});
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] = R.nextDouble();
            }
        }
        return A;
    }

    private static double[] RandomVector(int N, Random R) {
        double[] A = new double[N];
        for (int i = 0; i < N; i++) {
            A[i] = R.nextDouble();
        }
        return A;
    }

    private static double[] matvec(double[][] A, double[] x) {
        double[] y = new double[x.length];
        matvec(A, x, y);
        return y;
    }

    private static void matvec(double[][] A, double[] x, double[] y) {
        int M = A.length;
        int N = A[0].length;
        for (int i = 0; i < M; i++) {
            double[] Ai = A[i];
            double sum = 0.0d;
            for (int j = 0; j < N; j++) {
                sum += Ai[j] * x[j];
            }
            y[i] = sum;
        }
    }
}

