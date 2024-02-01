package com.checkupbot.checkupbotbackend.requests;

public class AuthenticationRequest {
    private String cpsoNumber;
    String password;

    public AuthenticationRequest() {
        this("", "");
    }

    public AuthenticationRequest(String cpsoNumber, String password) {
        this.cpsoNumber = cpsoNumber;
        this.password = password;
    }

    public String getCpsoNumber() {
        return cpsoNumber;
    }

    public String getPassword() {
        return password;
    }
}
