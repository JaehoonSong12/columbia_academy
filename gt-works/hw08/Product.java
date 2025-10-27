/**
 * Represents a product in the market's inventory.
 * Stores information about the product's ID, pricing, and quantity.
 *
 * @author [Your Name]
 * @version 1.0
 */
public class Product {

    /**
     * The unique identifier for the product.
     */
    private String id;

    /**
     * The price the market pays to buy this product from a supplier.
     */
    private int buyPrice;

    /**
     * The price the market charges to sell this product to a customer.
     */
    private int sellPrice;

    /**
     * The current quantity of this product in the inventory.
     */
    private int quantity;

    /**
     * Creates a new Product instance.
     *
     * @param id The product's unique ID.
     * @param buyPrice The price the market pays for this product.
     * @param sellPrice The price the market sells this product for.
     * @param quantity The initial quantity of this product.
     */
    public Product(String id, int buyPrice, int sellPrice, int quantity) {
        this.id = id;
        this.buyPrice = buyPrice;
        this.sellPrice = sellPrice;
        this.quantity = quantity;
    }

    /**
     * Gets the product's ID.
     *
     * @return The String ID.
     */
    public String getId() {
        return this.id;
    }

    /**
     * Gets the product's buy price.
     *
     * @return The integer buy price.
     */
    public int getBuyPrice() {
        return this.buyPrice;
    }

    /**
     * Gets the product's sell price.
     *
     * @return The integer sell price.
     */
    public int getSellPrice() {
        return this.sellPrice;
    }

    /**
     * Gets the current quantity of the product.
     *
     * @return The integer quantity.
     */
    public int getQuantity() {
        return this.quantity;
    }

    /**
     * Sets the quantity of the product.
     *
     * @param quantity The new quantity.
     */
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    /**
     * Returns a string representation of the product, with all instance
     * variables comma-separated.
     *
     * @return A String in the format "id,buyPrice,sellPrice,quantity".
     */
    @Override
    public String toString() {
        return this.id + "," + this.buyPrice + "," + this.sellPrice + "," + this.quantity;
    }
}