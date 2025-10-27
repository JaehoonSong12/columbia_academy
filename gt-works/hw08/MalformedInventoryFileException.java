/**
 * A checked exception describing a reason why the file containing the
 * information of the market is not valid or is formatted incorrectly.
 *
 * @author Tayion Park
 * @version 1.0
 */
public class MalformedInventoryFileException extends Exception {

    /**
     * Creates a new MalformedInventoryFileException with a specific message.
     *
     * @param message A String describing the reason for the exception.
     */
    public MalformedInventoryFileException(String message) {
        super(message);
    }
}