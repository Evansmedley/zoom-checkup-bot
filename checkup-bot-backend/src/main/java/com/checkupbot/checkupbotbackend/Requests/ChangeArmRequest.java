package com.checkupbot.checkupbotbackend.Requests;

public class ChangeArmRequest {

    private String arm;

    public ChangeArmRequest() {
    }

    public String getArm() {
        return arm;
    }

    public void setArm(String arm) {
        this.arm = arm;
    }

    @Override
    public String toString() {
        return "ChangeArmRequest{" +
                "arm='" + arm + '\'' +
                '}';
    }
}
