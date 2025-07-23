package guireference;

import javax.swing.*;
import java.awt.*;
import java.util.HashMap;
import java.util.Map;

/**
 * ViewRouter is a Singleton responsible for centralized navigation between views (JPanels) in the application.
 * <p>
 * <b>Design Pattern:</b> Singleton, Router (Controller in MVC for navigation)
 * <br>
 * It owns the main JFrame and CardLayout container, allowing controllers and views to switch screens and manage the window.
 */
public class ViewRouter {
    /** Singleton instance of the ViewRouter. */
    private static ViewRouter instance;

    /** The main application window. */
    private final JFrame frame;
    /** The CardLayout container holding all views. */
    private final JPanel container = new JPanel(new CardLayout());
    /** The CardLayout used for switching views. */
    private final CardLayout layout = (CardLayout) container.getLayout();
    /** Map of view names to their JPanel instances. */
    private final Map<String, JPanel> views = new HashMap<>();

    /**
     * Private constructor for Singleton pattern. Initializes the JFrame and layout.
     */
    private ViewRouter() {
        frame = new JFrame("MVC with Singleton Navigation");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setContentPane(container);
        frame.setLocationRelativeTo(null);
    }

    /**
     * Returns the singleton instance of the ViewRouter.
     * @return the ViewRouter instance
     */
    public static ViewRouter getInstance() {
        if (instance == null) {
            instance = new ViewRouter();
        }
        return instance;
    }

    /**
     * Registers a view (JPanel) with a unique name for navigation.
     * @param name the unique name for the view
     * @param view the JPanel instance
     */
    public void addView(String name, JPanel view) {
        views.put(name, view);
        container.add(view, name);
    }

    /**
     * Switches to the view registered with the given name and ensures the window is visible.
     * @param name the name of the view to show
     */
    public void show(String name) {
        layout.show(container, name);
        if (!frame.isVisible()) frame.setVisible(true);
    }

    /**
     * Returns the main application JFrame for window management.
     * @return the JFrame
     */
    public JFrame getFrame() {
        return frame;
    }
} 