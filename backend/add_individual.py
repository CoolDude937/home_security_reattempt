import psycopg2
import face_recognition
import os

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
)

# Load the face encoding data
andy_image = face_recognition.load_image_file("andy_neutral_small.jpg")
andy_face_encoding = face_recognition.face_encodings(andy_image)[0]

# Convert the face encoding data to bytes
face_encoding_bytes = andy_face_encoding.tobytes()

# Insert the face encoding data into the database
cursor = conn.cursor()
insert_query = "INSERT INTO face_encodings (name, encoding) VALUES (%s, %s)"
cursor.execute(insert_query, ("Andy", psycopg2.Binary(face_encoding_bytes)))
conn.commit()

# Close the database connection
cursor.close()
conn.close()
