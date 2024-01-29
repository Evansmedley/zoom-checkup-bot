package com.checkupbot.checkupbotbackend.documents;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.net.URL;
import java.util.Objects;
import java.util.UUID;

@Document
public class RoboticArmEndpoint {

    @Id
    private String uuid;
    private String name;
    private String ip;
    private int port;
    private boolean active;

    public RoboticArmEndpoint() {
    }

    public RoboticArmEndpoint(String name, String ip, int port) {
        this.uuid = UUID.randomUUID().toString();
        this.name = name;
        this.ip = ip;
        this.port = port;
        this.active = true;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public String getUri() {
        return "http://" + this.ip + ":" + this.port;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        RoboticArmEndpoint that = (RoboticArmEndpoint) o;
        return port == that.port && active == that.active && Objects.equals(uuid, that.uuid) && Objects.equals(name, that.name) && Objects.equals(ip, that.ip);
    }

    @Override
    public int hashCode() {
        return Objects.hash(uuid, name, ip, port, active);
    }

    @Override
    public String toString() {
        return "RoboticArmEndpoint{" +
                "uuid='" + uuid + '\'' +
                ", name='" + name + '\'' +
                ", ip='" + ip + '\'' +
                ", port=" + port +
                ", active=" + active +
                '}';
    }
}
