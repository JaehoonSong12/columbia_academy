package gui;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// component design pattern: `computer` has a `monitor`
public class MenuController { // computer
    private MenuView view; // monitor

    public MenuController(MenuView view) {
        this.view = view;

        view.getBtnStart().addActionListener( // (1) when button is clicked (**event fired)
            // anonymous object allocation
            new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    // behavior on the triggered event.
                    view.getLblMessage().setText("Hello, Swing world!"); // (2) you will do this (**response for the event fired)
                    
                    // route 2: execution
                    ViewRouter router = ViewRouter.getInstance();
                    router.setFrame(InfoView.TITLE, InfoView.SCREEN__WIDTH, InfoView.SCREEN_HEIGHT);
                    router.showView("weatherforcast/info");
                }
            }
        ); 
        // view.getBtnStart()       <- button object
        // view.getLblMessage()     <- label object
        // addActionListener        <- method to add event handler or listener
        // new ActionListener()     <- abstract class (interface) behavior, a method to load / override
    }

}