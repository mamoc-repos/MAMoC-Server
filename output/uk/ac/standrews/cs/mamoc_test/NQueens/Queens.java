package uk.ac.standrews.cs.mamoc_test.NQueens;
public class Queens {

    public Queens()
    {
        return;
    }

    private static void enumerate(int[] p3, int p4)
    {
        int v0 = p3.length;
        if (p4 != v0) {
            int v1 = 0;
            while (v1 < v0) {
                p3[p4] = v1;
                if (uk.ac.standrews.cs.mamoc_test.NQueens.Queens.isConsistent(p3, p4)) {
                    uk.ac.standrews.cs.mamoc_test.NQueens.Queens.enumerate(p3, (p4 + 1));
                }
                v1++;
            }
        }
        return;
    }

    private static boolean isConsistent(int[] p4, int p5)
    {
        int v1 = 0;
        while (v1 < p5) {
            if (p4[v1] != p4[p5]) {
                if ((p4[v1] - p4[p5]) != (p5 - v1)) {
                    if ((p4[p5] - p4[v1]) != (p5 - v1)) {
                        v1++;
                    } else {
                        return 0;
                    }
                } else {
                    return 0;
                }
            } else {
                return 0;
            }
        }
        return 1;
    }

    public static void run(int p2)
    {
        int[] v0 = new int[p2];
        uk.ac.standrews.cs.mamoc_test.NQueens.Queens.enumerate(v0, 0);
        return;
    }
}
