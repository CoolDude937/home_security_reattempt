import psycopg2
import face_recognition

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="andypostgrespassword369",
    host="localhost",
    port="5432"
)

# Load the face encoding data
andy_image = face_recognition.load_image_file("andy_neutral_small.jpg")
andy_face_encoding = face_recognition.face_encodings(andy_image)[0]

# Convert the face encoding data to bytes
face_encoding_bytes = andy_face_encoding.tobytes()

# Insert the face encoding data into the database
cursor = conn.cursor()
insert_query = "INSERT INTO users (name, face_encoding) VALUES (%s, %s)"
cursor.execute(insert_query, ("Andy", psycopg2.Binary(face_encoding_bytes)))
conn.commit()

# Close the database connection
cursor.close()
conn.close()
