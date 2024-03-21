package com.checkupbot.checkupbotbackend.repositories;

import com.checkupbot.checkupbotbackend.documents.ZoomData;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ZoomDataRepository extends MongoRepository<ZoomData, String> {
}
