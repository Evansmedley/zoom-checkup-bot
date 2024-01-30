package com.checkupbot.checkupbotbackend.requests;

public class ChangeArmRequest {

    private int arm;

    public ChangeArmRequest() {
    }

    public int getArm() {
        return arm;
    }

    public void setArm(int arm) {
        this.arm = arm;
    }

    @Override
    public String toString() {
        return "ChangeArmRequest{" +
                "arm='" + arm + '\'' +
                '}';
    }
}
