import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;


public class KMP {

	public static String readResourceContent(String filePath){
		try {
			return new String(Files.readAllBytes(Paths.get(filePath)));
		} catch (IOException e) {
			e.printStackTrace();
			return null;		
		}
	}

	public static void main(String[] args){
		System.out.print(new KMP(readResourceContent("../data/medium.txt"), args[0]).run());
	}
    String content;
    String pattern;

    public KMP(String content, String pattern) {
        
        this.content = content;
        this.pattern = pattern;
    }

    public int run() {
        int matches = 0;
        int M = this.pattern.length();
        int N = this.content.length();
        int[] lps = new int[M];
        int j = 0;
        this.computeLPSArray(this.pattern, M, lps);
        int i = 0;
        while (i < N) {
            if (this.pattern.charAt(j) == this.content.charAt(i)) {
                j++;
                i++;
            }
            if (j == M) {
                matches++;
                j = lps[j - 1];
            } else if (i < N && this.pattern.charAt(j) != this.content.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return matches;
    }

    private void computeLPSArray(String pat, int M, int[] lps) {
        int len = 0;
        int i = 1;
        lps[0] = 0;
        while (i < M) {
            if (pat.charAt(i) == pat.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = len;
                i++;
            }
        }
    }
}

