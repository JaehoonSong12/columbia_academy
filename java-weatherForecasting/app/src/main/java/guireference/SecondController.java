package guireference;

/**
 * SecondController acts as the Controller for the second view in the MVC pattern.
 * <p>
 * It handles user interaction for the second view and delegates navigation to the ViewRouter singleton.
 */
public class SecondController {
    /**
     * Constructs the SecondController, wiring up the view.
     * @param view the SecondView (MVC View)
     */
    public SecondController(SecondView view) {
        view.addButtonListener(e -> ViewRouter.getInstance().show("main"));
    }
} 