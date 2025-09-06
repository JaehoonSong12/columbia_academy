package gui;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InfoController {
    private InfoView view;

    public InfoController(InfoView view) {
        this.view = view;


        view.getBtnSubmit().addActionListener( // (1) when button is clicked (**event fired)
            new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String temp = view.getTxaAskTemp().getText();
                    view.getLblTemp().setText(String.format("Temperture: %s", temp));
                }
            }
        );
        view.getBtnBack().addActionListener(
            new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    System.out.println("Going Back to Main Menu");

                    ViewRouter.getInstance().showView(MenuView.getUrl());
                }
            }
        );
    }
}