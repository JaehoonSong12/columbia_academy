// Collaboration Statement: I worked on the homework assignment alone,

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

/**
 * The StarterUpper class builds the JavaFX interface for collecting problem
 * ideation information and saving StartUpIdea objects to a file.
 *
 * @author Tai Park
 * @version 1.0
 */
public class StarterUpper extends Application {

    private static final String USER_INITIALS = "T.P.";
    private static final String USER_GTID = "904070882";
    private final ArrayList<StartUpIdea> ideas = new ArrayList<>();
    private TextField problemField;
    private TextField customerField;
    private TextField needField;
    private TextField knownPeopleField;
    private TextField marketSizeField;
    private TextField competitorsField;

    /**
     * Starts the JavaFX application and constructs the UI components.
     *
     * @param primaryStage the main stage for the application
     */
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Problem Ideation Form.");

        Label initialsLabel = new Label(USER_INITIALS);
        initialsLabel.setPadding(new Insets(8));

        Button gtidButton = new Button(USER_GTID);

        gtidButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                Alert info = new Alert(AlertType.INFORMATION);
                info.setHeaderText("GTID");
                info.setContentText("GTID: " + USER_GTID);
                info.showAndWait();
            }
        });

        HBox topBar = new HBox(10, initialsLabel, gtidButton);
        topBar.setPadding(new Insets(10));

        GridPane form = new GridPane();
        form.setHgap(10);
        form.setVgap(12);
        form.setPadding(new Insets(10));

        problemField = new TextField();
        customerField = new TextField();
        needField = new TextField();
        knownPeopleField = new TextField();
        marketSizeField = new TextField();
        competitorsField = new TextField();

        problemField.setPromptText("What is the problem?");
        customerField.setPromptText("Who is the target customer?");
        needField.setPromptText(
                "How badly does the customer NEED this problem fixed (1–10)?");
        knownPeopleField.setPromptText(
                "How many people do you know who might experience this problem?");
        marketSizeField.setPromptText("How big is the target market?");
        competitorsField.setPromptText("Who are the competitors/existing solutions?");

        form.add(new Label("What is the problem?"), 0, 0);
        form.add(problemField, 1, 0);

        form.add(new Label("Who is the target customer?"), 0, 1);
        form.add(customerField, 1, 1);

        form.add(new Label(
                "How badly does the customer NEED this problem fixed (1–10)?"),
                0, 2);
        form.add(needField, 1, 2);

        form.add(new Label(
                "How many people do you know who might experience this problem?"),
                0, 3);
        form.add(knownPeopleField, 1, 3);

        form.add(new Label("How big is the target market?"), 0, 4);
        form.add(marketSizeField, 1, 4);

        form.add(new Label("Who are the competitors/existing solutions?"), 0, 5);
        form.add(competitorsField, 1, 5);

        Button addButton = new Button("Add Idea");
        Button sortButton = new Button("Sort Ideas");
        Button resetButton = new Button("Reset Form");
        Button saveButton = new Button("Save Ideas");

        addButton.setOnAction(event -> {
            if (!inputsValid()) {
                showError("Please fill all fields. "
                        + "Need must be 1–10. Numeric fields must be integers.");
                return;
            }
            ideas.add(buildIdea());
            clearForm();
        });

        sortButton.setOnAction(event -> {
            Collections.sort(ideas);
            showInfo("Sorted", "Ideas sorted successfully.");
        });

        resetButton.setOnAction(event -> {
            Alert confirm = new Alert(AlertType.CONFIRMATION);
            confirm.setHeaderText("Reset form?");
            confirm.setContentText(
                    "This will clear all fields and delete ideas.txt if it exists.");
            confirm.showAndWait().ifPresent(response -> {
                if (response == ButtonType.OK) {
                    File file = new File("ideas.txt");
                    if (file.exists()) {
                        file.delete();
                    }
                    clearForm();
                }
            });
        });

        saveButton.setOnAction(event -> {
            File file = new File("ideas.txt");
            boolean ok = FileUtil.saveIdeasToFile(ideas, file);
            if (ok) {
                showInfo("Saved", "Ideas saved to ideas.txt");
            } else {
                showError("Unable to save ideas to file.");
            }
        });

        HBox buttonBar = new HBox(12, addButton, sortButton, resetButton, saveButton);
        buttonBar.setPadding(new Insets(12));

        // ---------------- MAIN LAYOUT ----------------
        VBox root = new VBox(10, topBar, form, buttonBar);
        Scene scene = new Scene(root, 750, 500);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * Builds a StartUpIdea from the current form entries.
     *
     * @return a populated StartUpIdea instance
     */
    private StartUpIdea buildIdea() {
        String problem = problemField.getText().trim();
        String customer = customerField.getText().trim();
        int need = Integer.parseInt(needField.getText().trim());
        int known = Integer.parseInt(knownPeopleField.getText().trim());
        int market = Integer.parseInt(marketSizeField.getText().trim());
        String competitors = competitorsField.getText().trim();

        return new StartUpIdea(problem, customer, need, known, market, competitors);
    }

    /**
     * Validates whether user input fields contain usable values.
     *
     * @return true if all fields have valid and consistent values
     */
    private boolean inputsValid() {
        if (isEmpty(problemField)
                || isEmpty(customerField)
                || isEmpty(needField)
                || isEmpty(knownPeopleField)
                || isEmpty(marketSizeField)
                || isEmpty(competitorsField)) {
            return false;
        }

        try {
            int need = Integer.parseInt(needField.getText().trim());
            if (need < 1 || need > 10) {
                return false;
            }
            Integer.parseInt(knownPeopleField.getText().trim());
            Integer.parseInt(marketSizeField.getText().trim());
        } catch (NumberFormatException exc) {
            return false;
        }

        return true;
    }

    /**
     * Checks whether a TextField is empty or whitespace.
     *
     * @param tf the TextField to check
     * @return true if empty, false otherwise
     */
    private boolean isEmpty(TextField tf) {
        return tf.getText() == null || tf.getText().trim().isEmpty();
    }

    /** Clears all form text fields. */
    private void clearForm() {
        problemField.clear();
        customerField.clear();
        needField.clear();
        knownPeopleField.clear();
        marketSizeField.clear();
        competitorsField.clear();
    }

    /**
     * Displays an error dialog.
     *
     * @param message the error message to show
     */
    private void showError(String message) {
        Alert alert = new Alert(AlertType.ERROR);
        alert.setHeaderText("Error");
        alert.setContentText(message);
        alert.showAndWait();
    }

    /**
     * Displays an informational dialog.
     *
     * @param title the dialog title
     * @param message the message text
     */
    private void showInfo(String title, String message) {
        Alert alert = new Alert(AlertType.INFORMATION);
        alert.setHeaderText(title);
        alert.setContentText(message);
        alert.showAndWait();
    }

    /**
     * Launches the JavaFX application.
     *
     * @param args standard command-line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
}
