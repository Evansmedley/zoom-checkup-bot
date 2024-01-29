package com.checkupbot.checkupbotbackend.repositories;

import com.checkupbot.checkupbotbackend.documents.Doctor;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface DoctorRepository extends MongoRepository<Doctor, String> {
    Optional<Doctor> findByCpsoNumber(String cpsoNumber);
}
