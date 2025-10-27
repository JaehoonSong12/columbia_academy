// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

// java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw07/*.java

/**
 * Interface representing a treatable troop.
 *
 * @author Tai Park
 * @version 1.0
 */
public interface Treatable {
    /**
     * Checks if this troop needs treatment.
     *
     * @return true if the troop needs treatment
     */
    boolean needsTreatment();

    /**
     * Treats this troop.
     */
    void treat();
}
