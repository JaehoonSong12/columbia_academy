// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

// java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw08/*.java

/**
 * Exception thrown when a transaction cannot be fulfilled by the market.
 *
 * @author Tai Park
 * @version 1.0
 */
public class CannotFulfillTransactionException extends Exception {

    /**
     * Constructs a CannotFulfillTransactionException with a message.
     *
     * @param message explanation of the failure
     */
    public CannotFulfillTransactionException(String message) {
        super(message);
    }
}
