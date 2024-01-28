package com.checkupbot.checkupbotbackend.controllers;

import com.checkupbot.checkupbotbackend.requests.ChangeArmRequest;
import com.checkupbot.checkupbotbackend.requests.ChangeSliderRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ArmMovementController {

    private static final Logger logger = LoggerFactory.getLogger(ArmMovementController.class);

    @GetMapping
    public String root() {
        return "hi";
    }

    @PostMapping(value = "/changeArm")
    public void changeArm(@RequestBody ChangeArmRequest changeArm) {
        logger.debug("Received Request: CHANGE ARM\n" + changeArm);

        // TODO forward to robot endpoint
    }

    @PostMapping(value = "/changeSlider")
    public void changeSlider(@RequestBody ChangeSliderRequest changeSlider) {
        logger.debug("Received Request: CHANGE SLIDER\n" + changeSlider);

        // TODO forward to robot endpoint
    }
}
