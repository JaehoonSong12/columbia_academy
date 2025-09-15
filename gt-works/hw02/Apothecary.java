/*
INSTRUCTIONS:
    This class is homework 2.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw02/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw02/Apothecary.java    # compile (.java to .class)
     java           -cp "./out"     Apothecary              # execute (.class to run)
     rm -rf out/                                            # clean up .class files

 */

import java.util.Scanner;

/**
 * This class is used to ask potential buyers of potions can query the
 * cost of your potion-making services.
 * <ul>
 *     <li>Item 1</li>
 *     <li>Item 2</li>
 *     <li>Item 3</li>
 * </ul>
 *
 * @author Taiyun Park
 * @version 0.0.1
 */
public class Apothecary {
    /**
     * Main method.
     *
     * @param args argument from user input
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Welcome to my apothecary! Please enter your name here: ");
        String nameInput = sc.nextLine().trim();
        String formattedName;
        if (nameInput.isEmpty()) {
            formattedName = "Apprentice";
        } else {
            formattedName = nameInput.substring(0, 1).toUpperCase()
            + nameInput.substring(1).toLowerCase();
        }
        System.out.print("Hello " + formattedName + ", which potion do you want me to brew? ");
        String potionInput = sc.nextLine().trim();
        String ing1Sing = "", ing1Plur = "";
        String ing2Sing = "", ing2Plur = "";
        String ing3Sing = "", ing3Plur = "";
        int ing1Qty = 0, ing2Qty = 0, ing3Qty = 0;
        int ing1Cost = 0, ing2Cost = 0, ing3Cost = 0;
        int numIngredients = 0;
        String potionName = "";
        boolean isAdvanced = false;
        switch (potionInput.toLowerCase()) {
            case "potion of clarity":
                potionName = "Potion of Clarity";
                ing1Sing = "Vial of Crystal Dew"; ing1Plur = "Vials of Crystal Dew";
                ing1Qty = 2; ing1Cost = 10;
                numIngredients = 1;
                isAdvanced = false;
                break;
            case "elixir of agility":
                potionName = "Elixir of Agility";
                ing1Sing = "Swift Feather"; ing1Plur = "Swift Feathers";
                ing1Qty = 3; ing1Cost = 20;
                numIngredients = 1;
                isAdvanced = false;
                break;
            case "healing draught":
                potionName = "Healing Draught";
                ing1Sing = "Phoenix Feather"; ing1Plur = "Phoenix Feathers";
                ing1Qty = 1; ing1Cost = 50;
                ing2Sing = "Vial of Moonlit Dew"; ing2Plur = "Vials of Moonlit Dew";
                ing2Qty = 2; ing2Cost = 15;
                numIngredients = 2;
                isAdvanced = true;
                break;
            case "elixir of elemental power":
                potionName = "Elixir of Elemental Power";
                ing1Sing = "Vial of Moonlit Dew"; ing1Plur = "Vials of Moonlit Dew";
                ing1Qty = 1; ing1Cost = 15;
                ing2Sing = "Lava Stone"; ing2Plur = "Lava Stones";
                ing2Qty = 3; ing2Cost = 30;
                ing3Sing = "Phoenix Feather"; ing3Plur = "Phoenix Feathers";
                ing3Qty = 2; ing3Cost = 50;
                numIngredients = 3;
                isAdvanced = true;
                break;
            case "death poison":
                System.out.println("GUARDS!");
                sc.close();
                return;
            default:
                System.out.println("I am sorry, I cannot brew that potion.");
                sc.close();
                return;
        }
        String requires = "";
        if (numIngredients == 1) {
            String name = (ing1Qty == 1) ? ing1Sing : ing1Plur;
            requires = ing1Qty + " " + name;
        } else if (numIngredients == 2) {
            String name1 = (ing1Qty == 1) ? ing1Sing : ing1Plur;
            String name2 = (ing2Qty == 1) ? ing2Sing : ing2Plur;
            requires = ing1Qty + " " + name1 + " and " + ing2Qty + " " + name2;
        } else if (numIngredients == 3) {
            String name1 = (ing1Qty == 1) ? ing1Sing : ing1Plur;
            String name2 = (ing2Qty == 1) ? ing2Sing : ing2Plur;
            String name3 = (ing3Qty == 1) ? ing3Sing : ing3Plur;
            requires = ing1Qty + " " + name1 + ", " + ing2Qty + " " + name2 + ", and " + ing3Qty + " " + name3;
        }
        System.out.print("The " + potionName + " requires " + requires + ". How many would you like? ");
        String qtyInput = sc.nextLine().trim();
        int amount;
        try {
            amount = Integer.parseInt(qtyInput);
            if (amount < 1) amount = 1;
        } catch (NumberFormatException e) {
            amount = 1;
        }
        int missingCost = 0;
        if (numIngredients >= 1) {
            System.out.print("How many " + ing1Plur + " will you provide? ");
            int provided = Integer.parseInt(sc.nextLine().trim());
            int required = ing1Qty * amount;
            int missing = (provided < required) ? (required - provided) : 0; // ternary operator
            missingCost += missing * ing1Cost;
        }
        if (numIngredients >= 2) {
            System.out.print("How many " + ing2Plur + " will you provide? ");
            int provided = Integer.parseInt(sc.nextLine().trim());
            int required = ing2Qty * amount;
            int missing = (provided < required) ? (required - provided) : 0;
            missingCost += missing * ing2Cost;
        }
        if (numIngredients == 3) {
            System.out.print("How many " + ing3Plur + " will you provide? ");
            int provided = Integer.parseInt(sc.nextLine().trim());
            int required = ing3Qty * amount;
            int missing = (provided < required) ? (required - provided) : 0;
            missingCost += missing * ing3Cost;
        }
        System.out.print("Is there anything I should know? ");
        String extra = sc.nextLine().trim();
        boolean discount = extra.equals("The order is for the King");
        int serviceFee = isAdvanced ? 20 : 10;
        int potionCost = (isAdvanced ? 25 : 15) * amount;
        double totalCost = serviceFee + potionCost + missingCost;
        if (discount) {
            totalCost /= 2.0;
        }
        String finalPotionName;
        if (amount > 1) {
            if (potionName.equals("Potion of Clarity")) {
                finalPotionName = "Potions of Clarity";
            } else if (potionName.equals("Elixir of Agility")) {
                finalPotionName = "Elixirs of Agility";
            } else if (potionName.equals("Healing Draught")) {
                finalPotionName = "Healing Draughts";
            } else if (potionName.equals("Elixir of Elemental Power")) {
                finalPotionName = "Elixirs of Elemental Power";
            } else {
                finalPotionName = potionName;
            }
        } else {
            finalPotionName = potionName;
        }
        System.out.printf("%s, thank you for requesting the %s. The cost is $%.2f.%n",
                formattedName, finalPotionName, totalCost);
        sc.close();
    }
}
