<h1 align="center">
  <img
    width="400"
    alt="fastapi"
    src="https://live.staticflickr.com/65535/53630455037_dcf1107361_z.jpg">
</h1>

---

<h3 align="center">
  <strong>
🛠 FastAPI Social Media App 🛠

  </strong>
</h3>

---
<p align="center">
  <img 
    width="1000"
    alt="home"
    src="https://live.staticflickr.com/65535/53631352156_f878f151f9.jpg"/>
</p>
<p align="center">
  <img 
    width="1000"
    alt="home"
    src="https://live.staticflickr.com/65535/53631795820_30a3f555fd_w.jpg"/>
</p>

---

## FastAPI Social Media App
### Description

This repository contains the code for a social media application built with FastAPI, a modern Python web framework. The application provides functionalities for users to create, read, update, and delete posts, as well as like and favorite posts. Users can also register, login, and manage their profiles.

## Features

### User Management(Dockerized)

- **Registration:** Users can register by providing a unique username, email, password, age, and gender.
- **Authentication:** Authentication is handled using JWT tokens. Upon successful login, users receive an access token which they can use to authenticate subsequent requests.
- **Profile Management:** Users can update their profile information, such as username, email, password, age, and gender.
- **User Deletion:** Users can delete their accounts.

### Post Management(Dockerized)

- **Create Post:** Authenticated users can create new posts with a title, content, location, and specify if the post is published or not.
- **Read Post:** Users can view posts, which include details like the title, content, author, creation date, number of likes, and comments.
- **Update Post:** Users can update their own posts, including modifying the title, content, and published status.
- **Delete Post:** Users can delete their own posts.

### Like and Favorite(Dockerized)
- **Like Post:** Users can like posts they find interesting. They can only like a post once.
- **Favorite Post:** Users can add posts to their favorites list for quick access. They can also remove posts from their favorites.

### Search(Dockerized)
- **Search Posts:** Users can search for posts by title.

---

## Technologies Used

- **FastAPI:** A modern Python web framework for building APIs with Python type hints.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL:** A powerful, open-source relational database system.
- **Pydantic:** Data validation and settings management using Python type annotations.
- **JWT (JSON Web Tokens):** Authentication mechanism for securing API endpoints.
- **Passlib:** Password hashing library for securely storing passwords.
- **Docker:** A platform for developing, shipping, and running applications in containers, providing a consistent environment across different systems.
- **Docker Compose:** A tool for defining and running multi-container Docker applications, simplifying the process of managing complex containerized environments.

  <p align="left">
  <img src="https://img.shields.io/badge/fastapi-00008B?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/sqlalchemy-acace6?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
  <img src="https://img.shields.io/badge/postgresql-800000?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/pydantic-85EA2D?style=for-the-badge&logo=pydantic&logoColor=white"/>
  <img src="https://img.shields.io/badge/jwt-ffa500?style=for-the-badge&logo=wt&logoColor=white"/>
  <img src="https://img.shields.io/badge/passlib-FF0000?style=for-the-badge&logo=passlib&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker-0000FF?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker compose-4682B4?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

---

## API Endpoints

### Post

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/posts``` | _Get_All_Posts_|_All users_|
| *POST* | ```/posts``` | _Create Post_|_All users_|
| *GET* | ```/posts/{id}``` | _Get Post By Id_|_All users_|
| *PUT*  | ```/posts/{id}``` | Update Post |_All users_|
| *DELETE*  | ```/posts/{id}``` | Delete Post |_All users_|


### User

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/users``` | _Get_All_Users_|_All users_|
| *POST* | ```/users``` | _Create User_|_All users_|
| *GET* | ```/users/{id}``` | _Get User By Id_|_All users_|
| *PUT*  | ```/users/{id}``` | Update User |_All users_|
| *DELETE*  | ```/users/{id}``` | Delete User |_All users_|

### Authentications

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/login``` | _Login user(jwt)_|_All users_|

### Likes

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/likes``` | _Like Post_|_All users_|


### Favorites

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/favorite``` | _Favorite Post_|_All users_|

---

## Installation

1- **Clone the repository:**
```
git clone https://github.com/yourusername/fast-api.git

```

2- **Install dependencies:**
```
pip install -r requirements.txt

```
3- **Configure environment variables:**
Create a .env file and set the following variables:

```
DATABASE_HOSTNAME=your_database_hostname
DATABASE_PORT=your_database_port
DATABASE_NAME=your_database_name
DATABASE_USERNAME=your_database_username
DATABASE_PASSWORD=your_database_password
SECRET_KEY=your_secret_key
ALGORITHM=your_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=your_access_token_expire_minutes

```
4- **Run the application:**
```
uvicorn app.main:app --reload

```

