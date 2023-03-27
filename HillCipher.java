import java.io.File;
import java.io.IOException;
import java.util.Scanner;

class HillCipher {

  private static String readFile(String pathname) throws IOException {
    File file = new File(pathname);
    StringBuilder fileContents = new StringBuilder();

    try (Scanner scanner = new Scanner(file)) {
      while (scanner.hasNextLine()) {
        fileContents.append(scanner.nextLine());
      }
      return fileContents.toString().replaceAll("[^A-Za-z]+", "").toLowerCase();
    }
  }

  public static void printToConsole(String input) {
    for (int i = 0; i < input.length(); i++) {
      System.out.print(input.charAt(i));

      if ((i + 1) % 80 == 0) {
        System.out.println();
      }
    }
    System.out.println();
  }

  public static void main(String[] args) throws IOException {
    System.out.println();
    System.out.println();
    String plaintext = readFile(args[1]);
    Scanner scanner = new Scanner(new File(args[0]));

    int matrixSize = scanner.nextInt();

    int[][] matrix = new int[matrixSize][matrixSize];

    for (int i = 0; i < matrixSize; i++) {
      for (int j = 0; j < matrixSize; j++) {
        matrix[i][j] = scanner.nextInt();
      }
    }

    scanner.close();

    System.out.println("Key matrix:");
    System.out.println();

    String space = null;
    for (int[] x : matrix) {
      space = "";
      for (int y : x) {
        System.out.print(space + y);
        space = "  ";
      }
      System.out.println();
    }
    System.out.println();
    System.out.println();

    System.out.println("Plaintext:");
    System.out.println();

    StringBuilder sb = new StringBuilder(plaintext);

    while (sb.length() % matrixSize != 0) {
      sb.append('x');
    }

    plaintext = sb.toString();
    printToConsole(plaintext);

    System.out.println();
    System.out.println();

    System.out.println("Ciphertext:");
    System.out.println();

    StringBuilder cipherSB = new StringBuilder();

    for (int i = 0; i < plaintext.length(); i += matrixSize) {
      String block = plaintext.substring(i, i + matrixSize);

      for (int row = 0; row < matrixSize; row++) {
        int sum = 0;
        for (int column = 0; column < matrixSize; column++) {
          sum += (matrix[row][column] * (block.charAt(column) - 'a'));
        }
        char result = (char)((sum % 26) + 'a');
        cipherSB.append(result);
      }
    }
    printToConsole(cipherSB.toString());
  }
}
