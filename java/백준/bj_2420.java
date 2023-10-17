import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_2420 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");

        long n = Integer.parseInt(st.nextToken());
        long m = Integer.parseInt(st.nextToken());

        System.out.println(Math.abs(n-m));
    }
}
