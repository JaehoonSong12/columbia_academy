// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
// import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;

/**
 * Manages the market inventory, buying and selling products,
 * reading/writing from/to file, and interacting with the employee.
 *
 * @author Tai Park
 * @version 1.0
 */
public class MarketInventoryManager {

    private Product[] products;
    private int money;

    /**
     * Constructs a manager with given products and money.
     *
     * @param products array of products
     * @param money available market money
     */
    private MarketInventoryManager(Product[] products, int money) {
        this.products = products;
        this.money = money;
    }

    /**
     * Loads market data from file.
     *
     * @param file file containing inventory info
     * @return MarketInventoryManager instance
     * @throws IOException if file cannot be read
     * @throws MalformedInventoryFileException if file is invalid
     */
    public static MarketInventoryManager fromFile(File file)
            throws IOException, MalformedInventoryFileException {
        try (Scanner sc = new Scanner(file)) {
            if (!sc.hasNextLine()) {
                throw new MalformedInventoryFileException("Invalid inventory header");
            }

            String[] header = sc.nextLine().trim().split(" ");
            if (header.length != 2) {
                throw new MalformedInventoryFileException("Invalid inventory header");
            }

            int numProducts;
            int money;
            try {
                numProducts = Integer.parseInt(header[0]);
                money = Integer.parseInt(header[1]);
            } catch (NumberFormatException e) {
                throw new MalformedInventoryFileException("Invalid inventory header");
            }

            if (numProducts < 0 || money < 0) {
                throw new MalformedInventoryFileException("Invalid inventory header");
            }

            Product[] products = new Product[numProducts];
            for (int i = 0; i < numProducts; i++) {
                if (!sc.hasNextLine()) {
                    throw new MalformedInventoryFileException("Product information incomplete");
                }
                String line = sc.nextLine().trim();
                String[] parts = line.split(",");

                if (parts.length != 4) {
                    throw new MalformedInventoryFileException(
                        "Product information invalid for product " + (i + 1));
                }

                String id = parts[0];
                if (id.isEmpty() || id.contains(" ")) {
                    throw new MalformedInventoryFileException(
                        "Product information invalid for product " + (i + 1));
                }

                for (Product p : products) {
                    if (p != null && p.getId().equals(id)) {
                        throw new MalformedInventoryFileException("Duplicate product ID: " + id);
                    }
                }

                int buyPrice;
                int sellPrice;
                int quantity;
                try {
                    buyPrice = Integer.parseInt(parts[1]);
                    sellPrice = Integer.parseInt(parts[2]);
                    quantity = Integer.parseInt(parts[3]);
                } catch (NumberFormatException e) {
                    throw new MalformedInventoryFileException(
                        "Product information invalid for product " + (i + 1));
                }

                if (buyPrice < 0 || sellPrice < 0 || quantity < 0) {
                    throw new MalformedInventoryFileException(
                        "Product information invalid for product " + (i + 1));
                }

                products[i] = new Product(id, buyPrice, sellPrice, quantity);
            }
            return new MarketInventoryManager(products, money);
        } catch (NoSuchElementException e) {
            throw new MalformedInventoryFileException("Invalid inventory header");
        }
    }

    /**
     * Buys a product from supplier.
     *
     * @param id product ID
     * @param quantity quantity to buy
     * @throws CannotFulfillTransactionException if transaction fails
     */
    public void buy(String id, int quantity)
            throws CannotFulfillTransactionException {
        if (quantity < 0) {
            throw new CannotFulfillTransactionException("Quantity is negative");
        }

        Product p = findProduct(id);
        if (p == null) {
            throw new CannotFulfillTransactionException("Product ID not found");
        }

        int cost = p.getBuyPrice() * quantity;
        if (cost > money) {
            throw new CannotFulfillTransactionException("Not enough money to buy");
        }

        p.setQuantity(p.getQuantity() + quantity);
        money -= cost;
    }

    /**
     * Sells a product to customer.
     *
     * @param id product ID
     * @param quantity quantity to sell
     * @throws CannotFulfillTransactionException if transaction fails
     */
    public void sell(String id, int quantity)
            throws CannotFulfillTransactionException {
        if (quantity < 0) {
            throw new CannotFulfillTransactionException("Quantity is negative");
        }

        Product p = findProduct(id);
        if (p == null) {
            throw new CannotFulfillTransactionException("Product ID not found");
        }

        if (p.getQuantity() < quantity) {
            throw new CannotFulfillTransactionException("Not enough quantity to sell");
        }

        p.setQuantity(p.getQuantity() - quantity);
        money += p.getSellPrice() * quantity;
    }

    /**
     * Returns array of product IDs in market order.
     *
     * @return array of product IDs in market order
     */
    public String[] marketProducts() {
        String[] ids = new String[products.length];
        for (int i = 0; i < products.length; i++) {
            ids[i] = products[i].getId();
        }
        return ids;
    }

    /**
     * Saves inventory data to file.
     *
     * @param file output file
     * @throws IOException if writing fails
     */
    public void saveToFile(File file) throws IOException {
        try (PrintWriter pw = new PrintWriter(file)) {
            pw.println(products.length + " " + money);
            for (Product p : products) {
                pw.println(p.toString());
            }
        }
    }

    /**
     * Helper to find a product by ID.
     *
     * @param id product ID
     * @return Product or null
     */
    private Product findProduct(String id) {
        for (Product p : products) {
            if (p.getId().equals(id)) {
                return p;
            }
        }
        return null;
    }

    /**
     * Program entry point for interactive use.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java MarketInventoryManager <inventory-file>");
            return;
        }

        File file = new File(args[0]);
        MarketInventoryManager manager;

        try {
            manager = MarketInventoryManager.fromFile(file);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return;
        }

        Scanner input = new Scanner(System.in);
        while (true) {
            System.out.print("> ");
            if (!input.hasNextLine()) {
                break;
            }
            String command = input.nextLine().trim();

            if (command.equals("quit")) {
                break;
            } else if (command.equals("products")) {
                String[] ids = manager.marketProducts();
                if (ids.length > 0) {
                    System.out.println(String.join(", ", ids));
                }
            } else if (command.startsWith("buy ") || command.startsWith("sell ")) {
                String[] parts = command.split(" ");
                if (parts.length != 3) {
                    System.out.println("Error: Invalid command");
                    continue;
                }

                String id = parts[1];
                int quantity;
                try {
                    quantity = Integer.parseInt(parts[2]);
                } catch (NumberFormatException e) {
                    System.out.println("Error: Invalid command");
                    continue;
                }

                try {
                    if (parts[0].equals("buy")) {
                        manager.buy(id, quantity);
                    } else {
                        manager.sell(id, quantity);
                    }
                } catch (CannotFulfillTransactionException e) {
                    System.out.println("Error: " + e.getMessage());
                }
            } else {
                System.out.println("Error: Invalid command");
            }
        }

        try {
            manager.saveToFile(file);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
