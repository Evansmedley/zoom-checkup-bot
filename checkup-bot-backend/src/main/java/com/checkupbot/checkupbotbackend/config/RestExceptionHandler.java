package com.checkupbot.checkupbotbackend.config;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

import com.checkupbot.checkupbotbackend.dtos.ErrorDto;
import com.checkupbot.checkupbotbackend.execptions.LoginException;

@ControllerAdvice
public class RestExceptionHandler {

    @ExceptionHandler(value = { LoginException.class })
    @ResponseBody
    public ResponseEntity<ErrorDto> handleException(LoginException ex) {
        return ResponseEntity
                .status(ex.getStatus())
                .body(ErrorDto.builder().message(ex.getMessage()).build());
    }
}
