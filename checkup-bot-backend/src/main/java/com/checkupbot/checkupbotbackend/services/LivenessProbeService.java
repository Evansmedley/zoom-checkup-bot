package com.checkupbot.checkupbotbackend.services;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import com.checkupbot.checkupbotbackend.repositories.RoboticArmEndpointRepository;
import com.checkupbot.checkupbotbackend.responses.ProbeRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.client.ResourceAccessException;
import org.springframework.web.client.RestTemplate;

import java.util.Objects;

@Service
public class LivenessProbeService {

    private static final Logger logger = LoggerFactory.getLogger(LivenessProbeService.class);

    @Autowired
    private RoboticArmEndpointRepository roboticArmEndpointRepository;

    @Scheduled(fixedRate = 15000)
    public void sendLivenessProbeToAllEndpoints() {
        logger.debug("Sending liveness probes to endpoints");
        RestTemplate restTemplate = new RestTemplate();

        for (RoboticArmEndpoint roboticArmEndpoint : roboticArmEndpointRepository.findAll()) {

            try {
                ResponseEntity<ProbeRequest> response = restTemplate.getForEntity(roboticArmEndpoint.getUri() + "/liveness", ProbeRequest.class);

                if (response.getStatusCode() == HttpStatus.OK && Objects.equals(Objects.requireNonNull(response.getBody()).getUuid(), roboticArmEndpoint.getUuid())) {
                    logger.debug("Probe of endpoint '" + roboticArmEndpoint.getUuid() + "' successful");
                    successfulLivenessProbe(roboticArmEndpoint);
                } else {
                    failedLivenessProbe(roboticArmEndpoint);
                }
            } catch (ResourceAccessException e) {
                logger.debug(e.toString());
                failedLivenessProbe(roboticArmEndpoint);
            }
        }
    }

    private void successfulLivenessProbe(RoboticArmEndpoint roboticArmEndpoint) {
        if (!roboticArmEndpoint.isActive()) {
            logger.info("Endpoint '" + roboticArmEndpoint.getUuid() + "' set to active.");
            roboticArmEndpoint.setActive(true);
            roboticArmEndpointRepository.save(roboticArmEndpoint);
        }
    }

    private void failedLivenessProbe(RoboticArmEndpoint roboticArmEndpoint) {
        if (roboticArmEndpoint.isActive()) {
            logger.info("Endpoint '" + roboticArmEndpoint.getUuid() + "' set to inactive.");
            roboticArmEndpoint.setActive(false);
            roboticArmEndpointRepository.save(roboticArmEndpoint);
        }
    }
}
