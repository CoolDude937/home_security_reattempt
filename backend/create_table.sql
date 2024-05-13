CREATE TABLE face_encodings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    encoding BYTEA NOT NULL
);