package com.checkupbot.checkupbotbackend.entities;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import javax.annotation.processing.Generated;

@AllArgsConstructor
@NoArgsConstructor
@Builder
@Data
@Document
public class Doctor {
    @Id
    private Long id;
    private String cpsoId;
    private String password;
}
