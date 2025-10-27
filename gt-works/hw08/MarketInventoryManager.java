import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;

/**
 * Manages the market's inventory, including products and money.
 * This class can load inventory from a file, perform buy/sell transactions,
 * and save the inventory back to a file. It also serves as the main
 * program executable.
 *
 * @author Tayion Park
 * @version 1.0
 */
public class MarketInventoryManager {

    /**
     * An array holding all the products in the inventory.
     */
    private Product[] products;

    /**
     * The amount of money the market currently has.
     */
    private int money;

    /**
     * Private constructor to create a MarketInventoryManager instance.
     *
     * @param products An array of Product objects.
     * @param money The initial amount of money for the market.
     */
    private MarketInventoryManager(Product[] products, int money) {
        this.products = products;
        this.money = money;
    }

    /**
     * Creates and returns a MarketInventoryManager instance by reading
     * inventory data from a file.
     *
     * @param file The file to read the inventory from.
     * @return A new MarketInventoryManager instance.
     * @throws IOException If the file cannot be read.
     * @throws MalformedInventoryFileException If the file format is invalid.
     */
    public static MarketInventoryManager fromFile(File file) throws IOException, MalformedInventoryFileException {
        Scanner fileScanner = null;
        try {
            fileScanner = new Scanner(file);
            // 1. Read Header
            if (!fileScanner.hasNextLine()) {
                throw new MalformedInventoryFileException("Invalid inventory header");
            }
            String headerLine = fileScanner.nextLine();
            Scanner headerScanner = new Scanner(headerLine);

            int productCount;
            int money;

            try {
                productCount = headerScanner.nextInt();
                money = headerScanner.nextInt();
            } catch (InputMismatchException | NoSuchElementException e) {
                throw new MalformedInventoryFileException("Invalid inventory header");
            }

            // Check for negative values or extra data
            if (productCount < 0 || money < 0 || headerScanner.hasNext()) {
                throw new MalformedInventoryFileException("Invalid inventory header");
            }
            headerScanner.close();

            // 2. Read Products
            Product[] products = new Product[productCount];
            for (int i = 0; i < productCount; i++) {
                int productNumber = i + 1;

                if (!fileScanner.hasNextLine()) {
                    throw new MalformedInventoryFileException("Product information incomplete");
                }
                String productLine = fileScanner.nextLine();
                String[] parts = productLine.split(",");

                if (parts.length != 4) {
                    throw new MalformedInventoryFileException("Product information invalid for product " + productNumber);
                }

                String id = parts[0];
                if (id.isEmpty() || id.contains(" ")) {
                    throw new MalformedInventoryFileException("Product information invalid for product " + productNumber);
                }

                // Check for duplicate ID
                for (int j = 0; j < i; j++) {
                    if (products[j].getId().equals(id)) {
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
                    throw new MalformedInventoryFileException("Product information invalid for product " + productNumber);
                }

                if (buyPrice < 0 || sellPrice < 0 || quantity < 0) {
                    throw new MalformedInventoryFileException("Product information invalid for product " + productNumber);
                }

                // All checks passed for this product
                products[i] = new Product(id, buyPrice, sellPrice, quantity);
            }

            // All products loaded successfully
            return new MarketInventoryManager(products, money);

        } finally {
            if (fileScanner != null) {
                fileScanner.close();
            }
        }
    }

    /**
     * Helper method to find a product by its ID.
     *
     * @param id The ID of the product to find.
     * @return The Product object if found, or null otherwise.
     */
    private Product findProductById(String id) {
        for (Product p : this.products) {
            if (p.getId().equals(id)) {
                return p;
            }
        }
        return null;
    }

    /**
     * Buys a specified quantity of a product from a supplier.
     *
     * @param id The ID of the product to buy.
     * @param quantity The non-negative quantity to buy.
     * @throws CannotFulfillTransactionException If the transaction cannot be completed.
     */
    public void buy(String id, int quantity) throws CannotFulfillTransactionException {
        if (quantity < 0) {
            throw new CannotFulfillTransactionException("Quantity is negative");
        }

        Product product = findProductById(id);
        if (product == null) {
            throw new CannotFulfillTransactionException("Product ID not found");
        }

        // Use long to prevent overflow during calculation
        long totalCost = (long) product.getBuyPrice() * quantity;
        if (this.money < totalCost) {
            throw new CannotFulfillTransactionException("Not enough money to buy");
        }

        // Transaction is valid
        this.money -= totalCost;
        product.setQuantity(product.getQuantity() + quantity);
    }

    /**
     * Sells a specified quantity of a product to a customer.
     *
     * @param id The ID of the product to sell.
     * @param quantity The non-negative quantity to sell.
     * @throws CannotFulfillTransactionException If the transaction cannot be completed.
     */
    public void sell(String id, int quantity) throws CannotFulfillTransactionException {
        if (quantity < 0) {
            throw new CannotFulfillTransactionException("Quantity is negative");
        }

        Product product = findProductById(id);
        if (product == null) {
            throw new CannotFulfillTransactionException("Product ID not found");
        }

        if (product.getQuantity() < quantity) {
            throw new CannotFulfillTransactionException("Not enough quantity to sell");
        }

        // Transaction is valid
        // Use long to prevent overflow during calculation
        this.money += (long) product.getSellPrice() * quantity;
        product.setQuantity(product.getQuantity() - quantity);
    }

    /**
     * Returns an array of all product IDs in the inventory.
     *
     * @return A String array of product IDs.
     */
    public String[] marketProducts() {
        String[] ids = new String[this.products.length];
        for (int i = 0; i < this.products.length; i++) {
            ids[i] = this.products[i].getId();
        }
        return ids;
    }

    /**
     * Saves the current state of the market inventory (money and products)
     * to the specified file.
     *
     * @param file The file to write the inventory data to.
     * @throws IOException If an error occurs during writing.
     */
    public void saveToFile(File file) throws IOException {
        PrintWriter writer = null;
        try {
            writer = new PrintWriter(file);

            // Write header
            writer.println(this.products.length + " " + this.money);

            // Write each product
            for (Product p : this.products) {
                writer.println(p.toString());
            }
        } finally {
            if (writer != null) {
                writer.close();
            }
        }
    }

    /**
     * The main entry point for the Market Inventory Manager program.
     *
     * @param args Command-line arguments, expecting one: the filename.
     */
    public static void main(String[] args) {
        // 1. Check arguments
        if (args.length != 1) {
            System.out.println("Usage: java MarketInventoryManager <inventory-file>");
            return;
        }

        // 2. Load inventory from file
        String filename = args[0];
        File file = new File(filename);
        MarketInventoryManager manager;

        try {
            manager = MarketInventoryManager.fromFile(file);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return;
        }

        // 3. Command loop
        Scanner consoleScanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.print("> ");
            String line = consoleScanner.nextLine();
            String[] parts = line.split(" ");
            String command = parts.length > 0 ? parts[0] : "";

            switch (command) {
            case "quit":
                if (parts.length == 1) {
                    running = false;
                } else {
                    System.out.println("Error: Invalid command");
                }
                break;
            case "products":
                if (parts.length == 1) {
                    String[] ids = manager.marketProducts();
                    // Manually join to avoid importing java.lang.String
                    for (int i = 0; i < ids.length; i++) {
                        System.out.print(ids[i]);
                        if (i < ids.length - 1) {
                            System.out.print(", ");
                        }
                    }
                    System.out.println();
                } else {
                    System.out.println("Error: Invalid command");
                }
                break;
            case "buy":
            case "sell":
                if (parts.length == 3) {
                    try {
                        String id = parts[1];
                        int quantity = Integer.parseInt(parts[2]);
                        if (command.equals("buy")) {
                            manager.buy(id, quantity);
                        } else {
                            manager.sell(id, quantity);
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Error: Invalid command");
                    } catch (CannotFulfillTransactionException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                } else {
                    System.out.println("Error: Invalid command");
                }
                break;
            default:
                System.out.println("Error: Invalid command");
                break;
            }
        }
        consoleScanner.close();

        // 4. Save inventory back to file
        try {
            manager.saveToFile(file);
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}