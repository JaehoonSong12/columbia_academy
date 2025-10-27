/**
 * Collaboration Statement:
 * I worked on the homework assignment alone, using only course materials.
 */

/**
 * A checked exception describing a reason why the market is unable to
 * fulfill a transaction (buy or sell).
 *
 * @author Tayion Park
 * @version 1.0
 */
public class CannotFulfillTransactionException extends Exception {

    /**
     * Creates a new CannotFulfillTransactionException with a specific message.
     *
     * @param message A String describing the reason for the exception.
     */
    public CannotFulfillTransactionException(String message) {
        super(message);
    }
}