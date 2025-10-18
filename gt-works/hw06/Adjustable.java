// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents an object whose weight can be adjusted.
 *
 * @author Tai Park
 * @version 1.0.0
 */
public interface Adjustable {

    /**
     * Adjusts the weight of this object by a given amount.
     *
     * @param adjustment the change in weight (can be positive or negative)
     * @return true if the adjustment was successful, false otherwise
     */
    boolean adjustWeight(int adjustment);
}
