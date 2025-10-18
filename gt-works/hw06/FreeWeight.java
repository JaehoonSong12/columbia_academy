// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Abstract FreeWeight class that implements Comparable for FreeWeight items.
 *
 * @author Tai Park
 * @version 1.0.0
 */
public abstract class FreeWeight implements Comparable<FreeWeight> {
    private final String freeWeightID;
    private final int category;
    private final int weight;

    /**
     * Constructs a FreeWeight object with the given values.
     *
     * @param freeWeightID the ID of this free weight
     * @param category the category of this free weight
     * @param weight the weight in pounds
     */
    public FreeWeight(String freeWeightID, int category, int weight) {
        this.freeWeightID = freeWeightID;
        this.category = category;
        this.weight = weight;
    }

    /**
     * Compares this FreeWeight to another FreeWeight.
     *
     * @param other the other FreeWeight to compare to
     * @return a negative integer, zero, or a positive integer as this object
     *         is less than, equal to, or greater than the specified object
     */
    @Override
    public int compareTo(FreeWeight other) {
        if (other == null) {
            throw new NullPointerException("Cannot compare to null");
        }
        int result = Integer.compare(this.category, other.category);
        if (result != 0) {
            return result;
        }
        return Integer.compare(this.weight, other.weight);
    }

    /**
     * Returns a string representation of this FreeWeight.
     *
     * @return the string in format "[id]: [weight] lb."
     */
    @Override
    public String toString() {
        return this.freeWeightID + ": " + this.weight + " lb.";
    }

    /**
     * Returns this free weight's ID.
     *
     * @return the ID
     */
    public String getFreeWeightID() {
        return this.freeWeightID;
    }

    /**
     * Returns this free weight's weight.
     *
     * @return the weight
     */
    public int getWeight() {
        return this.weight;
    }
}
