/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw05/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw05/Archer.java     # compile (.java to .class)
     java           -cp "./out"     Archer               # execute (.class to run)
     rm -rf out/                                        # clean up .class files

DEPENDENCIES:
 */
import java.util.Scanner;

/**
 * This class is homework 3.
 *
 * @author CS 1331 TAs
 * @version 1.0.0
 */
public class Archer {
    /**
     * Calculates the total payment from all guests currently checked in.
     *
     * @param guests 2D array of guest names
     * @param costs  2D array of room costs
     * @return total payment from all guests
     */
    public static int calculatePayment(String[][] guests, int[][] costs) {
        int total = 0;
        for (int i = 0; i < guests.length; i++) {
            for (int j = 0; j < guests[i].length; j++) {
                if (guests[i][j] != null) {
                    total += costs[i][j];
                }
            }
        }
        return total;
    }

    /**
     * Main method.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Invalid number of floors or rooms.");
            return;
        }

        int floors = Integer.parseInt(args[0]);
        int rooms = Integer.parseInt(args[1]);
        if (floors < 1 || rooms < 1) {
            System.out.println("Invalid number of floors or rooms.");
            return;
        }

        Scanner sc = new Scanner(System.in);
        int[][] costs = new int[floors][rooms];
        String[][] guests = new String[floors][rooms];
        int[][] daysLeft = new int[floors][rooms];

        for (int f = 0; f < floors; f++) {
            boolean ok;
            do {
                ok = true;
                System.out.print("Costs for floor " + (f + 1) + ": ");
                for (int r = 0; r < rooms; r++) {
                    costs[f][r] = sc.nextInt();
                    if (costs[f][r] <= 0) {
                        ok = false;
                    }
                }
                sc.nextLine(); // consume line end
                if (!ok) {
                    System.out.println("Room costs must be positive.");
                }
            } while (!ok);
        }

        System.out.println();

        boolean running = true;
        while (running) {
            System.out.print("> ");
            String cmd = sc.next();

            if (cmd.equals("in")) {
                String name = sc.next();
                int stay = sc.nextInt();
                int fl = sc.nextInt();
                int rm = sc.nextInt();
                sc.nextLine();

                if (findGuest(guests, name)) {
                    System.out.println(name + " already checked in.");
                } else if (fl < 1 || fl > floors || rm < 1 || rm > rooms) {
                    System.out.println("Invalid floor or room.");
                } else if (stay < 1) {
                    System.out.println("Guests must stay at least one day.");
                } else if (guests[fl - 1][rm - 1] != null) {
                    System.out.println("Room is already occupied.");
                } else {
                    guests[fl - 1][rm - 1] = name;
                    daysLeft[fl - 1][rm - 1] = stay;
                    System.out.println("Checking in " + name + " to floor " + fl
                                        + ", room " + rm + ", for " + stay
                                        + (stay == 1 ? " day." : " days."));
                }

            } else if (cmd.equals("nd")) {
                int total = calculatePayment(guests, costs);
                int gcount = countGuests(guests);
                System.out.println("Total payment from " + gcount + " "
                        + (gcount == 1 ? "guest" : "guests") + ": "
                        + formatMoney(total) + ".");

                for (int f = 0; f < floors; f++) {
                    for (int r = 0; r < rooms; r++) {
                        if (guests[f][r] != null) {
                            daysLeft[f][r]--;
                            if (daysLeft[f][r] == 0) {
                                System.out.println(
                                    "Checking out " + guests[f][r] + " from floor "
                                    + (f + 1) + ", room " + (r + 1) + "."
                                );
                                guests[f][r] = null;
                            }
                        }
                    }
                }

            } else if (cmd.equals("price")) {
                int fl = sc.nextInt();
                int rm = sc.nextInt();
                sc.nextLine();
                if (fl < 1 || fl > floors || rm < 1 || rm > rooms) {
                    System.out.println("Invalid floor or room.");
                } else {
                    System.out.println(
                        "The price for floor " + fl
                        + ", room " + rm + " is "
                        + formatMoney(costs[fl - 1][rm - 1]) + " per day."
                    );
                }

            } else if (cmd.equals("print")) {
                sc.nextLine();
                for (int f = floors - 1; f >= 0; f--) {
                    StringBuilder sb = new StringBuilder("|");
                    for (int r = 0; r < rooms; r++) {
                        sb.append(guests[f][r] == null ? " " : guests[f][r]);
                        sb.append("|");
                    }
                    System.out.println(sb);
                }

            } else if (cmd.equals("quit")) {
                running = false;
            } else {
                sc.nextLine();
            }
        }
        sc.close();
    }


    private static boolean findGuest(String[][] guests, String name) {
        for (String[] row : guests) {
            for (String g : row) {
                if (name.equals(g)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static int countGuests(String[][] guests) {
        int c = 0;
        for (int i = 0; i < guests.length; i++) {
            for (int j = 0; j < guests[i].length; j++) {
                if (guests[i][j] != null) {
                    c++;
                }
            }
        }
        return c;
    }

    private static String formatMoney(int dollars) {
        return "$" + dollars + ".00";
    }
}
