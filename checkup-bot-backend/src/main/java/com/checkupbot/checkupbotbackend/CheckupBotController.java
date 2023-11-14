package com.checkupbot.checkupbotbackend;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CheckupBotController {

    @GetMapping
    public String root() {
        return "hi";
    }
}
