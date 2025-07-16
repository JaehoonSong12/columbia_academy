package guireference;

public class Main {
    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(() -> {
            MessageModel model = new MessageModel();
            MainView view = new MainView();
            new MainController(model, view);
            view.setVisible(true);
        });
    }
}