/*
 *  Stupid little entry point for java interop playing
 */

public class Run
{
  public static void main(String[] args)
  {
      System.out.println("Look, I can fib:");
      for (int i=0; i<10; i++) {
          System.out.println(Fib.fib(i));
      }
  }
}
