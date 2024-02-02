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
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Optional;

@RestController
public class ArmMovementController {

    private static final String CHANGE_ARM_ENDPOINT_PATH = "/changeArm";

    private static final String CHANGE_SLIDER_ENDPOINT_PATH = "/changeSlider";

    private static final Logger logger = LoggerFactory.getLogger(ArmMovementController.class);

    private final RestTemplate restTemplate;

    @Autowired
    private RoboticArmEndpointRepository roboticArmEndpointRepository;

    public ArmMovementController() {
        restTemplate = new RestTemplate();
    }


    @PostMapping(value = "/changeArm/{uuid}")
    public void changeArm(@RequestBody ChangeArmRequest changeArm, @PathVariable("uuid") String uuid) {
        logger.debug("Received Request: CHANGE ARM for endpoint '" + uuid + "'-> " + changeArm);

        Optional<RoboticArmEndpoint> endpointInfo = roboticArmEndpointRepository.findById(uuid);
        if (endpointInfo.isEmpty()) {
            logger.error("Endpoint '" + uuid + "' does not exist.");
            return;
        }

        // Define entity and send
        HttpEntity<ChangeArmRequest> request = new HttpEntity<>(changeArm);
        ResponseEntity<Void> response = restTemplate.postForEntity(
                endpointInfo.get().getUri() + CHANGE_ARM_ENDPOINT_PATH, request, Void.class);

        if (response.getStatusCode() != HttpStatus.OK) {
            logger.error("Failed to forward change arm request to endpoint");
        }
    }

    @PostMapping(value = "/changeSlider/{uuid}")
    public void changeSlider(@RequestBody ChangeSliderRequest changeSlider, @PathVariable("uuid") String uuid) {
        logger.debug("Received Request: CHANGE SLIDER for endpoint '" + uuid + "'-> " + changeSlider);

        Optional<RoboticArmEndpoint> endpointInfo = roboticArmEndpointRepository.findById(uuid);
        if (endpointInfo.isEmpty()) {
            logger.error("Endpoint '" + uuid + "' does not exist.");
            return;
        }

        // Define entity and send
        HttpEntity<ChangeSliderRequest> request = new HttpEntity<>(changeSlider);
        ResponseEntity<Void> response = restTemplate.postForEntity(
                endpointInfo.get().getUri() + CHANGE_SLIDER_ENDPOINT_PATH, request, Void.class);

        if (response.getStatusCode() != HttpStatus.OK) {
            logger.error("Failed to forward change arm request to endpoint");
        }
    }
}
