package gui;

/// JDK already has the following as library (JRE)
import javax.swing.JFrame;      // (1) Window Screen
import javax.swing.JPanel;      // (2) Scene Layout
import java.awt.BorderLayout;       // styling of layouts!
import javax.swing.JButton;     // (3) UI component - control
import javax.swing.JLabel;      // (3) UI component - visual

/**
 * Logic (Coding Part) of the app, not visual compoenents on your Monitor
 */
import javax.swing.SwingUtilities;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;







/**
 * Main.java
 * 
 * this is the entry point of the application.
 */








/**
 * A simple Swing GUI application with a button and label.
 */
public class Main {
    public static void main(String[] args) {
        // Schedule GUI creation on the Event Dispatch Thread
        // SwingUtilities.invokeLater(Main::createAndShowGUI);
        // SwingUtilities.invokeLater(Main::createAndShowGUI2);

        SwingUtilities.invokeLater(Main::start);

        // SwingUtilities.invokeLater(CardLayoutExample::createAndShowGUI);
    }



    /**
     * Create and display the GUI.
     */
    private static void start() {

        ViewRouter router = ViewRouter.getInstance();


        // route 1: menu
        JPanel view1 = new MenuView();
        new MenuController((MenuView) view1);
        router.routeView("weatherforcast/menu", view1);

        // route 2: info (weather-forcasting page)
        JPanel view2 = new InfoView();
        new InfoController((InfoView) view2);
        router.routeView("weatherforcast/info", view2);




        // route 1: execution
        router.setFrame(MenuView.TITLE, MenuView.SCREEN__WIDTH, MenuView.SCREEN_HEIGHT);
        router.showView("weatherforcast/menu");


        
        // // route 2: execution
        // router.setFrame(InfoView.TITLE, InfoView.SCREEN__WIDTH, InfoView.SCREEN_HEIGHT);
        // router.showView("weatherforcast/info");
    }







    /**
     * Create and display the GUI.
     */
    private static void createAndShowGUI() {
        // Main frame (Window Screen)
        // JFrame frame = new JFrame("Simple GUI App");
        JPanel view = new MenuView();
        new MenuController((MenuView) view);
    }


    
    private static void createAndShowGUI2() {
        // Main frame (Window Screen)
        // JFrame frame = new JFrame("Simple GUI App");
        JPanel view = new InfoView();
        new InfoController((InfoView) view);
    }







    
}