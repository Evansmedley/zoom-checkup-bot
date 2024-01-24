package com.checkupbot.checkupbotbackend.Requests;

public class ChangeSliderRequest {

    private int move;

    public ChangeSliderRequest() {
    }

    public int getMove() {
        return move;
    }

    public void setMove(int move) {
        this.move = move;
    }

    @Override
    public String toString() {
        return "ChangeSliderRequest{" +
                "move=" + move +
                '}';
    }
}
