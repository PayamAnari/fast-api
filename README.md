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

### Post Management

- **Create Post:** Authenticated users can create new posts with a title, content, location, and specify if the post is published or not.
- **Read Post:** Users can view posts, which include details like the title, content, author, creation date, number of likes, and comments.
- **Update Post:** Users can update their own posts, including modifying the title, content, and published status.
- **Delete Post:** Users can delete their own posts.

### Like and Favorite
- **Like Post:** Users can like posts they find interesting. They can only like a post once.
- **Favorite Post:** Users can add posts to their favorites list for quick access. They can also remove posts from their favorites.

### Search
- **Search Posts:** Users can search for posts by title.

---

## Technologies Used

- **FastAPI:** A modern Python web framework for building APIs with Python type hints.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL:** A powerful, open-source relational database system.
- **Pydantic:** Data validation and settings management using Python type annotations.
JWT (JSON Web Tokens): Authentication mechanism for securing API endpoints.
Passlib: Password hashing library for securely storing passwords.
