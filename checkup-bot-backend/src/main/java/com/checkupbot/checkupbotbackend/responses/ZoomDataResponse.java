package com.checkupbot.checkupbotbackend.responses;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class ZoomDataResponse {
    private String sdkKey;
    private String authEndpoint;
}
