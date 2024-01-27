package com.checkupbot.checkupbotbackend.controllers;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import com.checkupbot.checkupbotbackend.repositories.RoboticArmEndpointRepository;
import com.checkupbot.checkupbotbackend.requests.ChangeArmRequest;
import com.checkupbot.checkupbotbackend.requests.ChangeSliderRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class ArmMovementController {

    private static final String CHANGE_ARM_ENDPOINT_PATH = "/changeArm";

    private static final String CHANGE_SLIDER_ENDPOINT_PATH = "/changeSlider";

    private static final Logger logger = LoggerFactory.getLogger(ArmMovementController.class);

    private final RestTemplate restTemplate;


    // TODO REMOVE THIS AND USE COOKIES TO SELECT ACTIVE ARM
    @Autowired
    private RoboticArmEndpointRepository roboticArmEndpointRepository;

    public ArmMovementController() {
        restTemplate = new RestTemplate();
    }

    // TODO REMOVE THIS AND USE COOKIES TO SELECT ACTIVE ARM
    private String getFirstActiveEndpointUri() {
        // Select first active endpoint to send to
        String activeEndpointUri = "";
        for (RoboticArmEndpoint roboticArmEndpoint : roboticArmEndpointRepository.findAll()) {
            if (roboticArmEndpoint.isActive()) {
                activeEndpointUri = roboticArmEndpoint.getUri();
            }
        }

        return activeEndpointUri;
    }

    @GetMapping
    public String root() {
        return "hi";
    }

    @PostMapping(value = "/changeArm")
    public void changeArm(@RequestBody ChangeArmRequest changeArm) {
        logger.debug("Received Request: CHANGE ARM -> " + changeArm);

        // TODO REMOVE THIS AND USE COOKIES TO SELECT ACTIVE ARM
        String activeEndpointUri = getFirstActiveEndpointUri();
        if (activeEndpointUri.isEmpty()) {
            logger.debug("No active endpoints to forward to");
            return;
        }

        // Define entity and send
        HttpEntity<ChangeArmRequest> request = new HttpEntity<>(changeArm);
        ResponseEntity<Void> response = restTemplate.postForEntity(
                activeEndpointUri + CHANGE_ARM_ENDPOINT_PATH, request, Void.class);

        if (response.getStatusCode() != HttpStatus.OK) {
            logger.info("Failed to forward change arm request to endpoint");
        }
    }

    @PostMapping(value = "/changeSlider")
    public void changeSlider(@RequestBody ChangeSliderRequest changeSlider) {
        logger.debug("Received Request: CHANGE SLIDER -> " + changeSlider);

        // TODO REMOVE THIS AND USE COOKIES TO SELECT ACTIVE ARM
        String activeEndpointUri = getFirstActiveEndpointUri();
        if (activeEndpointUri.isEmpty()) {
            logger.debug("No active endpoints to forward to");
            return;
        }

        // Define entity and send
        HttpEntity<ChangeSliderRequest> request = new HttpEntity<>(changeSlider);
        ResponseEntity<Void> response = restTemplate.postForEntity(
                activeEndpointUri + CHANGE_SLIDER_ENDPOINT_PATH, request, Void.class);

        if (response.getStatusCode() != HttpStatus.OK) {
            logger.info("Failed to forward change slider request to endpoint");
        }
    }
}
