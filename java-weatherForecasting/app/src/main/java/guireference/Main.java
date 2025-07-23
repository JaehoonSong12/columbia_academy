package guireference;

/**
 * Main application entry point.
 * <p>
 * Sets up the MVC structure and initializes the ViewRouter singleton for navigation.
 */
public class Main {
    /**
     * Launches the application.
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(() -> {
            ViewRouter viewRouter = ViewRouter.getInstance();

            MessageModel model = new MessageModel();
            MainView mainView = new MainView();
            new MainController(model, mainView);

            SecondView secondView = new SecondView();
            new SecondController(secondView);

            viewRouter.addView("main", mainView);
            viewRouter.addView("second", secondView);


            viewRouter.show("main");
        });
    }
}