// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

/**
 * Represents an infirmary that treats treatable troops.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Infirmary {
    private String infirmaryName;
    private static int numberOfInfirmaries = 0;

    /**
     * Constructs an infirmary with given name.
     *
     * @param infirmaryName name of infirmary
     */
    public Infirmary(String infirmaryName) {
        this.infirmaryName = infirmaryName;
        numberOfInfirmaries++;
    }

    /**
     * Gets number of infirmaries.
     *
     * @return number of infirmaries
     */
    public static int getNumberOfInfirmaries() {
        return numberOfInfirmaries;
    }

    /**
     * Inspects a troop.
     *
     * @param t troop
     */
    public void inspectTroop(Troop t) {
        System.out.println(t.toString());
        if (t instanceof Barbarian) {
            ((Barbarian) t).scream();
        }
    }

    /**
     * Performs treatment.
     *
     * @param t treatable troop
     */
    public void doTreatment(Treatable t) {
        if (!t.needsTreatment()) {
            System.out.println("You are fine. You will not receive treatment at "
                + infirmaryName + " infirmary");
        } else {
            t.treat();
        }
    }

    @Override
    public String toString() {
        return infirmaryName + " infirmary";
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Infirmary)) {
            return false;
        }
        Infirmary other = (Infirmary) obj;
        return infirmaryName.equals(other.infirmaryName);
    }
}
