package com.checkupbot.checkupbotbackend.documents;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Collection;
import java.util.List;

@Document("DoctorDB")
public class Doctor implements UserDetails {
    @Id
    private String id;
    private String cpsoNumber;
    private String password;

    public Doctor() {
        this("", "", "");
    }

    public Doctor(String id, String cpsoNumber, String password) {
        this.id = id;
        this.cpsoNumber = cpsoNumber;
        this.password = password;
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return List.of(new SimpleGrantedAuthority(Role.USER.name()));
    }

    @Override
    public String getUsername() {
        return cpsoNumber;
    }

    @Override
    public String getPassword() {
        return password;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}
