package com.checkupbot.checkupbotbackend.documents;

import jakarta.persistence.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document("ZoomData")
public class ZoomData {

    @Id
    private String id;
    private String authEndpoint;
    private String sdkKey;

    public ZoomData() {
    }

    public ZoomData(String id, String authEndpoint, String sdkKey) {
        this.id = id;
        this.authEndpoint = authEndpoint;
        this.sdkKey = sdkKey;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getAuthEndpoint() {
        return authEndpoint;
    }

    public String getSdkKey() {
        return sdkKey;
    }
}
