import java.util.*;

public class sorting2D {
    public static void main(String[] args) {
        int m, a[][];
        Scanner Sc = new Scanner(System.in);
        System.out.println("Enter the value of m: ");
        m = Sc.nextInt();
        a = new int[m][m];
        System.out.println("Enter the elements: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = Sc.nextInt();
            }
        }
        System.out.println("Original matrix: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(a[i][j] + "\t ");
            }
            System.out.println("");
        }
        // to change 2-D array into 1-D array
        int arr[] = new int[m * m];
        int c = 0, temp = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                arr[c++] = a[i][j];
            }
        }
        // for sorting
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < c - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        c = 0;
        System.out.println("Rearranged matrix: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = arr[c++];
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(a[i][j] + "\t");
            }
            System.out.println(" ");
        }
    }
}
