import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;



public class QuickSort {

	public static String readResourceContent(String filePath){
		File file = new File(filePath);
		StringBuilder fileContents = new StringBuilder((int)file.length());
		try (Scanner scanner = new Scanner(file)) {
			while(scanner.hasNextLine()) {
				fileContents.append(scanner.nextLine() + System.lineSeparator());
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return fileContents.toString();
	}

	public static void main(String[] args){
		new QuickSort(readResourceContent("../data/large.txt")).run();
	}
    private static final String BLANK_SPACE = " ";
    String content;
    String[] strArr;

    public QuickSort(String words) {
        
        this.content = words;
        this.strArr = this.content.split(BLANK_SPACE);
    }

    public void run() {
        this.quickSort(this.strArr, 0, this.strArr.length - 1);
    }

    private String[] quickSort(String[] strArr, int p, int r) {
        if (p < r) {
            int q = partition(strArr, p, r);
            this.quickSort(strArr, p, q);
            this.quickSort(strArr, q + 1, r);
        }
        return strArr;
    }

    private static int partition(String[] strArr, int p, int r) {
        String x = strArr[p];
        int i = p - 1;
        int j = r + 1;
        while (true) {
            i++;
            while (i < r && strArr[i].compareTo(x) < 0) {
                i++;
            }
            j--;
            while (j > p && strArr[j].compareTo(x) > 0) {
                j--;
            }
            if (i >= j) {
                return j;
            }
            swap(strArr, i, j);
        }
    }

    private static void swap(String[] strArr, int i, int j) {
        String temp = strArr[i];
        strArr[i] = strArr[j];
        strArr[j] = temp;
    }
}

