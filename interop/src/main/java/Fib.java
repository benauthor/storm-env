/*
 * Stupid little java class to import.
 */

public class Fib {

    public static int fib(int n) {

        if (n < 2) {
            return n;
        } else {
            return fib(n - 1) + fib(n - 2);
        }

    }

}
