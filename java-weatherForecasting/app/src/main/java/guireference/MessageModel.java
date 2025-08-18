package guireference;

/**
 * MessageModel is the Model in the MVC pattern.
 * <p>
 * It holds the message state for the application.
 */
public class MessageModel {
    private String message = "Main Panel";

    /**
     * Gets the current message.
     * @return the message
     */
    public String getMessage() { return message; }

    /**
     * Sets the message.
     * @param message the new message
     */
    public void setMessage(String message) { this.message = message; }
} 