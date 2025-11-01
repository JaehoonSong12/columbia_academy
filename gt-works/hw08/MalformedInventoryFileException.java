// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

/**
 * Exception thrown when an inventory file is malformed or invalid.
 *
 * @author Tai Park
 * @version 1.0
 */
public class MalformedInventoryFileException extends Exception {

    /**
     * Constructs a MalformedInventoryFileException with a message.
     *
     * @param message explanation of the invalid file
     */
    public MalformedInventoryFileException(String message) {
        super(message);
    }
}
