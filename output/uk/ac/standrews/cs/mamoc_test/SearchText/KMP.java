package uk.ac.standrews.cs.mamoc_test.SearchText;
public class KMP {

    public KMP()
    {
        return;
    }

    private void computeLPSArray(String p5, int p6, int[] p7)
    {
        int v0 = 0;
        int v1 = 1;
        p7[0] = 0;
        while (v1 < p6) {
            if (p5.charAt(v1) != p5.charAt(v0)) {
                if (v0 == 0) {
                    p7[v1] = v0;
                    v1++;
                } else {
                    v0 = p7[(v0 - 1)];
                }
            } else {
                v0++;
                p7[v1] = v0;
                v1++;
            }
        }
        return;
    }

    public int searchKMP(String p9, String p10)
    {
        int v0 = 0;
        int v1 = p10.length();
        int v2 = p9.length();
        int[] v3 = new int[v1];
        int v4 = 0;
        this.computeLPSArray(p10, v1, v3);
        int v5 = 0;
        while (v5 < v2) {
            if (p10.charAt(v4) == p9.charAt(v5)) {
                v4++;
                v5++;
            }
            if (v4 != v1) {
                if ((v5 < v2) && (p10.charAt(v4) != p9.charAt(v5))) {
                    if (v4 == 0) {
                        v5++;
                    } else {
                        v4 = v3[(v4 - 1)];
                    }
                }
            } else {
                v0++;
                v4 = v3[(v4 - 1)];
            }
        }
        return v0;
    }
}
