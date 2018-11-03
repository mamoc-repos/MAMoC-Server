package uk.ac.standrews.cs.mamoc_test.Sorting;
public class MergeSort {

    public MergeSort()
    {
        return;
    }

    public static void merge(String[] p5, String[] p6, String[] p7)
    {
        int v0 = 0;
        int v1 = 0;
        int v2 = 0;
        while (v2 < p5.length) {
            if ((v1 < p7.length) && ((v0 >= p6.length) || (p6[v0].compareToIgnoreCase(p7[v1]) >= 0))) {
                p5[v2] = p7[v1];
                v1++;
            } else {
                p5[v2] = p6[v0];
                v0++;
            }
            v2++;
        }
        return;
    }

    public static void mergeSort(String[] p6)
    {
        if (p6.length >= 2) {
            String[] v0_3 = new String[(p6.length / 2)];
            String[] v2_0 = new String[(p6.length - (p6.length / 2))];
            int v3_0 = 0;
            String v4_0 = 0;
            while (v4_0 < v0_3.length) {
                v0_3[v4_0] = p6[v4_0];
                v4_0++;
            }
            while (v3_0 < v2_0.length) {
                v2_0[v3_0] = p6[((p6.length / 2) + v3_0)];
                v3_0++;
            }
            uk.ac.standrews.cs.mamoc_test.Sorting.MergeSort.mergeSort(v0_3);
            uk.ac.standrews.cs.mamoc_test.Sorting.MergeSort.mergeSort(v2_0);
            uk.ac.standrews.cs.mamoc_test.Sorting.MergeSort.merge(p6, v0_3, v2_0);
        }
        return;
    }
}
