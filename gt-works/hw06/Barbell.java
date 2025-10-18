// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Concrete Barbell class extending FreeWeight and implementing Adjustable.
 *
 * @author Tai Park
 * @version 1.0.0
 */
public class Barbell extends FreeWeight implements Adjustable {
    private final int loadCapacity;
    private int loadedWeight;

    /**
     * Constructs a Barbell object with the given ID, base weight,
     * and load capacity.
     *
     * @param freeWeightID the barbell's ID
     * @param weight the barbell's base weight
     * @param loadCapacity the maximum load capacity
     */
    public Barbell(String freeWeightID, int weight, int loadCapacity) {
        super(freeWeightID, 1, weight);
        this.loadCapacity = loadCapacity;
        this.loadedWeight = 0;
    }

    /**
     * Compares this Barbell to another FreeWeight.
     * Adds additional ordering after FreeWeight's comparison.
     *
     * @param other the other FreeWeight to compare to
     * @return comparison integer
     */
    @Override
    public int compareTo(FreeWeight other) {
        int superResult = super.compareTo(other);
        if (superResult != 0) {
            return superResult;
        }

        Barbell b = (Barbell) other;
        int result = Integer.compare(this.loadCapacity, b.loadCapacity);
        if (result != 0) {
            return result;
        }

        result = Integer.compare(b.loadedWeight, this.loadedWeight);
        if (result != 0) {
            return result;
        }

        return this.getFreeWeightID().compareTo(b.getFreeWeightID());
    }

    /**
     * Adjusts this barbell's loaded weight.
     *
     * @param adjustment the amount to add or remove
     * @return true if successful, false otherwise
     */
    @Override
    public boolean adjustWeight(int adjustment) {
        int newLoaded = this.loadedWeight + adjustment;
        if (newLoaded < 0 || newLoaded > this.loadCapacity) {
            return false;
        }
        this.loadedWeight = newLoaded;
        return true;
    }

    /**
     * Returns a string representation of this barbell.
     *
     * @return formatted string including "barbell"
     */
    @Override
    public String toString() {
        return super.toString() + " barbell";
    }

    /**
     * Returns this barbell's load capacity.
     *
     * @return load capacity
     */
    public int getLoadCapacity() {
        return this.loadCapacity;
    }

    /**
     * Returns this barbell's loaded weight.
     *
     * @return loaded weight
     */
    public int getLoadedWeight() {
        return this.loadedWeight;
    }
}
