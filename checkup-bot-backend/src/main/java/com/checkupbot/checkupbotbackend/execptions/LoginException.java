package com.checkupbot.checkupbotbackend.execptions;

import org.springframework.http.HttpStatus;

public class LoginException extends RuntimeException {
    private final HttpStatus status;

    public LoginException(String message, HttpStatus status) {
        super(message);
        this.status = status;
    }

    public HttpStatus getStatus() {
        return status;
    }
}
