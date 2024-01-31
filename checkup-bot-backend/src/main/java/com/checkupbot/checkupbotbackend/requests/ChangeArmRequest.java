package com.checkupbot.checkupbotbackend.requests;

public class ChangeArmRequest {

    private Integer arm;

  
    public ChangeArmRequest() {
    }

    public Integer getArm() {
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
