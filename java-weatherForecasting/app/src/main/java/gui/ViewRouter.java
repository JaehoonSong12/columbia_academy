package gui;

import javax.swing.*;
import java.awt.*;
import java.util.HashMap;       // child class (concrete class)
import java.util.Map;           // parent class (abstract class)

/**
 * ViewRouter is a Singleton responsible for centralized navigation 
 * between views (JPanels) in the application.
 * <p>
 * <b>Design Pattern:</b> Singleton, Router (Controller in MVC for navigation)
 * <br>
 * 
 * 
 * 
 * - Singleton design pattern   (Memory Space Complexity Purpose)
 * The Singleton design pattern allocates only one unique instance of a class
 * for the entire runtime of your program.
 * 
 * - Router design pattern      (Memory Space Complexity Purpose)
 * The Router design pattern centralizes the decision of "which handler should 
 * process this request" by mapping incoming requests 
 * (messages, UI events, HTTP calls, etc.) to the appropriate 
 * processing component. It's widely used in web frameworks 
 * (Express, Spring MVC), in UI navigation (React Router), and 
 * in message-driven systems.
 * 
 * 
 * It owns the main JFrame and CardLayout container, allowing controllers 
 * and views to switch screens and manage the window.
 */

public class ViewRouter {
    // Router Desgin Pattern
    private final JFrame frame;                 // (1) Window of the Program            (Stage)
    private final JPanel container;             // (2) Session of the Program           (Scene)
    private final CardLayout layout;            // (3) Screen Layout with Transition    (Pane)
    //routing purpose data structure
    // private final Map<String, JPanel> viewRoutes;    // routing purpose data structure to save your memory (DSA)



    
    public void setFrame(String windowTitle, int width, int height) {
        frame.setTitle(windowTitle);
        frame.setSize(width, height);
    }

    /**
     * Registers a view (JPanel) with a unique name for navigation.
     * @param key the unique key (URL) for the view     e.g. https://www.google.com/account
     * @param view the JPanel instance                    e.g. new InfoView()
     */
    public void routeView(String key, JPanel value) {
        container.add(value, key);
    }
    /**
     * Switches to the view registered with the given name and ensures the window is visible.
     * @param key the unique key (URL) for the view
     */
    public void showView(String key) {

                    ///////////////////////// HW 2: Just like container(key), you should get value, and do ////////////////////////////////
                    //// frame.setTitle(windowTitle);
                    ///frame.setSize(width, height);
                    ///based on the value (View object / JPanel object)


        layout.show(container, key);
        if (!frame.isVisible()) frame.setVisible(true);
        return;
    }







    // Singleton Desgin Pattern
    private static ViewRouter instance = null; 
    // private constructor (intended) to initialize when it is called for the first time.
    private ViewRouter() {
        this.container = new JPanel(new CardLayout());
        this.layout = (CardLayout) container.getLayout();
        // this.viewRoutes = new HashMap<>();
        this.frame = new JFrame();
        this.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.frame.setContentPane(container);
        this.frame.setLocationRelativeTo(null);
        this.setFrame("Initial Title (For Testing)", 600, 400);
    }
    // returns singlton and make sure it is created only one object.
    public static ViewRouter getInstance() {
        if (instance == null) ViewRouter.instance = new ViewRouter(); // detection of the 1st call
        return ViewRouter.instance; // ViewRouter.instance == "ViewRouter class's instance static variable"
    }
    /**
     * dynmaic vs static
     * static (need to type): In CS, static means "compile-time" (or "before running"). So, if you make your 
     * variable or function static, they will be concretely defined (memory space actually took place 
     * within .class file by javac command) as soon as you run your program.
     * 
     * dynamic (no need to type): In CS, dynamic means "run-time" (or "after running"). So, if you make your
     * attribute or method dynamic, they will be defined only after you call "new" keyword. Moreover, 
     * "new" keyword calls the class's constructor to build up the memory space and return the completed 
     * object's address.
     */
}