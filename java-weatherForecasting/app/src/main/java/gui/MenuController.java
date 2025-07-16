package gui;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// component design pattern: `computer` has a `monitor`
public class MenuController { // computer
    private MenuView view; // monitor

    public MenuController(MenuView view) {
        this.view = view;
        view.setVisible(true);
        view.setLocationRelativeTo(null);

        view.getBtnStart().addActionListener(
            new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    view.getLblMessage().setText("Hello, Swing world!");
                }
            }
        ); 
        // view.getBtnStart()       <- button object
        // view.getLblMessage()     <- label object
        // addActionListener        <- method to add event handler or listener
        // new ActionListener()     <- abstract class (interface) behavior, a method to load / override
    }

}