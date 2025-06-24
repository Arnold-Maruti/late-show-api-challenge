
LATE SHOW API 


This is a backend flask appliction for a late Night Tv show system.Its entails user registration and JWT-based authentication.It uses PostgresSQL for persistent storage



SETUP INSTRUCTIONS

Run the following commands in the terminal to install dependencies:
      1) Pipenv install flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary 


      2)sudo apt install postgresql postgresql-contrib


PostgreSQL DB setup 
The database has already been setup so no need to create it


To run server use flask run command

MIGRATIONS
Run the following commands:

flask db init     
flask db migrate
flask db upgrade


Auth Flow




🔸 Register
POST /auth/register

Request:


{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secret123"
}



Response:


{
  "message": "User registered successfully."
}




🔸 Login
POST /auth/login

Request:

{
  "email": "john@example.com",
  "password": "secret123"
}



Response:


{
  "token": "your-jwt-token"
}




🔸 Using the token
Include it in the header for protected routes:
          Authorization: Bearer your-jwt-token

Routes list


| Method | Endpoint       | Auth Required | Description              |
| ------ | -------------- | ------------- | -------------------      |
| POST   | /appearances   | Required      | Shows all users          |
| POST   | /register      | None          | Adds a new user          |
| POST   | /login         | None          | Adds an account          |
| GET    | /guests        | None          | List all guest           |
| GET    | /episodes/<id> | None          | Get episode by ID        |
| DELETE | /episodes/<id> | Required      | Delete episode           |


POST /appearances (Requires Auth)


Headers:


Authorization: Bearer your-jwt-token



Request:


{
  "episode_id": 1,
  "guest_id": 2
}



Response:


{
  "id": 5,
  "episode_id": 1,
  "guest_id": 2,
  "created_at": "2025-06-24T10:00:00"
}


Postman Usage


1)Import the included Postman collection: postman_collection.json



2)Set an environment variable token after login.



3)All protected routes will automatically use {{token}} in the Authorization header.