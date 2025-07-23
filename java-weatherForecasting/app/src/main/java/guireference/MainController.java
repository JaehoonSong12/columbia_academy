package guireference;

/**
 * MainController acts as the Controller for the main view in the MVC pattern.
 * <p>
 * It handles user interaction for the main view and delegates navigation to the ViewRouter singleton.
 */
public class MainController {
    /**
     * Constructs the MainController, wiring up the view and model.
     * @param model the MessageModel (MVC Model)
     * @param view the MainView (MVC View)
     */
    public MainController(MessageModel model, MainView view) {
        view.setLabelText(model.getMessage());
        view.addButtonListener(e -> ViewRouter.getInstance().show("second"));
    }
} 