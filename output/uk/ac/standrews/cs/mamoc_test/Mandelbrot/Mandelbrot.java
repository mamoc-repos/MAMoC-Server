package uk.ac.standrews.cs.mamoc_test.Mandelbrot;
public class Mandelbrot {
    private static double[] Cib;
    private static double[] Crb;
    private static byte[][] out;
    private static java.util.concurrent.atomic.AtomicInteger yCt;

    public Mandelbrot()
    {
        return;
    }

    static synthetic java.util.concurrent.atomic.AtomicInteger access$000()
    {
        return uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.yCt;
    }

    static synthetic byte[][] access$100()
    {
        return uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.out;
    }

    static synthetic void access$200(int p0, byte[] p1)
    {
        uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.putLine(p0, p1);
        return;
    }

    private static int getByte(int p28, int p29)
    {
        int v1 = 0;
        int v2 = 0;
        while (v2 < 8) {
            double v4_0 = uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Crb[(p28 + v2)];
            double v6 = uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Cib[p29];
            double v8_2 = uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Crb[((p28 + v2) + 1)];
            double v10 = uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Cib[p29];
            int v3_2 = 0;
            int v12 = 49;
            do {
                double v15_4 = (((v4_0 * v6) + (v4_0 * v6)) + uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Cib[p29]);
                v4_0 = (((v4_0 * v4_0) - (v6 * v6)) + uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Crb[(p28 + v2)]);
                v6 = v15_4;
                double v19_4 = (((v8_2 * v10) + (v8_2 * v10)) + uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Cib[p29]);
                v8_2 = (((v8_2 * v8_2) - (v10 * v10)) + uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Crb[((p28 + v2) + 1)]);
                v10 = v19_4;
                if (((v4_0 * v4_0) + (v6 * v6)) <= 4.0) {
                    if (((v8_2 * v8_2) + (v10 * v10)) > 4.0) {
                        v3_2 |= 1;
                        if (v3_2 == 3) {
                            break;
                        }
                    }
                    v12--;
                } else {
                    v3_2 |= 2;
                    if (v3_2 == 3) {
                        break;
                    }
                }
            } while(v12 > 0);
            v1 = ((v1 << 2) + v3_2);
            v2 += 2;
        }
        return (~ v1);
    }

    private static void putLine(int p2, byte[] p3)
    {
        int v0 = 0;
        while (v0 < p3.length) {
            p3[v0] = ((byte) uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.getByte((v0 * 8), p2));
            v0++;
        }
        return;
    }

    public static void run(int p9)
    {
        int v0_1 = new double[(p9 + 7)];
        uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Crb = v0_1;
        int v0_3 = new double[(p9 + 7)];
        uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Cib = v0_3;
        double v2_1 = (2.0 / ((double) p9));
        int v0_4 = 0;
        Thread[] v1_0 = 0;
        while (v1_0 < p9) {
            uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Cib[v1_0] = ((((double) v1_0) * v2_1) - 1.0);
            uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.Crb[v1_0] = ((((double) v1_0) * v2_1) - 1.5);
            v1_0++;
        }
        uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.yCt = new java.util.concurrent.atomic.AtomicInteger();
        uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot.out = ((byte[][]) reflect.Array.newInstance(byte, new int[] {p9, ((p9 + 7) / 8)})));
        Thread[] v1_11 = new Thread[(Runtime.getRuntime().availableProcessors() * 2)];
        int v4_1 = 0;
        while (v4_1 < v1_11.length) {
            v1_11[v4_1] = new uk.ac.standrews.cs.mamoc_test.Mandelbrot.Mandelbrot$1();
            v4_1++;
        }
        int v4_2 = v1_11.length;
        Thread v5_1 = 0;
        while (v5_1 < v4_2) {
            v1_11[v5_1].start();
            v5_1++;
        }
        int v4_3 = v1_11.length;
        while (v0_4 < v4_3) {
            v1_11[v0_4].join();
            v0_4++;
        }
        return;
    }
}
