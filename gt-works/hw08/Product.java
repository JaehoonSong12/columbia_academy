// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

/**
 * Represents a product in the market inventory.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Product {

    private String id;
    private int buyPrice;
    private int sellPrice;
    private int quantity;

    /**
     * Constructs a Product with the given parameters.
     *
     * @param id product ID
     * @param buyPrice cost to buy from suppliers
     * @param sellPrice price sold to customers
     * @param quantity stock quantity
     */
    public Product(String id, int buyPrice, int sellPrice, int quantity) {
        this.id = id;
        this.buyPrice = buyPrice;
        this.sellPrice = sellPrice;
        this.quantity = quantity;
    }

    /**
     * Returns product ID.
     *
     * @return product ID
     */
    public String getId() {
        return id;
    }

    /**
     * Returns buy price.
     *
     * @return buy price
     */
    public int getBuyPrice() {
        return buyPrice;
    }

    /**
     * Returns sell price.
     *
     * @return sell price
     */
    public int getSellPrice() {
        return sellPrice;
    }

    /**
     * Returns current quantity.
     *
     * @return current quantity
     */
    public int getQuantity() {
        return quantity;
    }

    /**
     * Sets the current quantity.
     *
     * @param quantity new quantity
     */
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    /**
     * Returns product info as CSV format.
     *
     * @return formatted string
     */
    @Override
    public String toString() {
        return id + "," + buyPrice + "," + sellPrice + "," + quantity;
    }
}
