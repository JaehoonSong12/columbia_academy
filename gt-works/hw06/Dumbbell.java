// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Concrete Dumbbell class extending FreeWeight.
 *
 * @author Tai Park
 * @version 1.0.0
 */
public class Dumbbell extends FreeWeight {
    private final String gripType;

    /**
     * Constructs a Dumbbell with the given ID, weight, and grip type.
     *
     * @param freeWeightID the dumbbell's ID
     * @param weight the dumbbell's weight
     * @param gripType the grip type
     */
    public Dumbbell(String freeWeightID, int weight, String gripType) {
        super(freeWeightID, 2, weight);
        this.gripType = gripType;
    }

    /**
     * Compares this Dumbbell to another FreeWeight.
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

        Dumbbell d = (Dumbbell) other;
        int result = this.gripType.compareTo(d.gripType);
        if (result != 0) {
            return result;
        }

        return this.getFreeWeightID().compareTo(d.getFreeWeightID());
    }

    /**
     * Returns a string representation of this dumbbell.
     *
     * @return formatted string including grip type
     */
    @Override
    public String toString() {
        return super.toString() + " dumbbell with " + this.gripType + " grip";
    }

    /**
     * Returns this dumbbell's grip type.
     *
     * @return the grip type
     */
    public String getGripType() {
        return this.gripType;
    }
}
