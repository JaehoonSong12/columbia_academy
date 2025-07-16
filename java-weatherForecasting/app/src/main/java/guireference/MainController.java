package guireference;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainController {
    private final MessageModel model;
    private final MainView view;

    public MainController(MessageModel model, MainView view) {
        this.model = model;
        this.view = view;
        // Set initial label text from model
        view.setLabelText(model.getMessage());
        // Add button listener
        view.addButtonListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                model.setMessage("Hello, Swing world!");
                view.setLabelText(model.getMessage());
            }
        });
    }
} 