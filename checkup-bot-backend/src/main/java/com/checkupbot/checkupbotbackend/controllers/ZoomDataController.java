package com.checkupbot.checkupbotbackend.controllers;

import com.checkupbot.checkupbotbackend.documents.ZoomData;
import com.checkupbot.checkupbotbackend.repositories.ZoomDataRepository;
import com.checkupbot.checkupbotbackend.responses.ZoomDataResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ZoomDataController {
    @Autowired
    private ZoomDataRepository zoomDataRepository;

    private ZoomData fetchZoomData() {
        System.out.println(zoomDataRepository.findAll());
        return zoomDataRepository.findAll().get(0);
    }

    @GetMapping("/zoom")
    public ZoomDataResponse getZoomData() {
        ZoomData data = fetchZoomData();
        return ZoomDataResponse.builder().sdkKey(data.getSdkKey()).authEndpoint(data.getAuthEndpoint()).build();
    }
}
