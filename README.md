==============================================
Micro-Manage: User Management API Microservice
==============================================

This project is a user management microservice built with Python in the Flask framework for webservers and PostgreSQL, containerized using Docker.
It provides an API for creating, reading, updating, and deleting users.

## Prerequisites

Before you begin, ensure you have the following software installed on your machine:

**Docker Desktop: This project runs entirely in docker containers. You do not need to install Python or PostgrSQL on your machine.
IMPORTANT NOTE: Docker on Windows requires the installation of WSL (Windows Subsystem for Linux) to function and may need to be installed before use of docker can begin.

All other required dependencies will be initialized by Docker in their respective containers.

## Getting started

Follow these steps to get the application running and begin managing data:

### 1. Copy or download the repository

Download or copy the project code to a folder on your machine.

### 2. Build and run the application

Open a terminal in PowerShell or CMDPrompt, navigate to the project's root directory (user-api folder) and run the following command:

docker-compose up -d --build

The --build flag builds the Python application image from the Dockerfile
The -d flag will run the containers in detached mode (in the background)

Check Docker to ensure both services are running or run the command:

docker-compose ps

This command will provide status reports on the containers so you can ensure both containers are working as intended.

### 3. Managing data

The API is available at http://localhost:5000

You can use a tool like Thunder Client in VSC, curl.exe or Invoke-WebRequest -Uri in PowerShell to interact with the endpoints.
All methods of data management will require JSON inputs.

## 1. Create new user
    Method: POST
    Endpoint: /users
    Body: JSON object with name and email
    THUNDER CLIENT EXAMPLE:
    {
        "name": "John",
        "email": "john@example.com"
    }

## 2. Get all users
    Method: GET
    Endpoint: /users
    Body: NO DATA INPUT!!

## 3. Get a single user
    Method: GET
    Endpoint: /users/<id>
    Body: NO DATA INPUT!! Only change the address to end with the relevant ID number

## 4. Update user info
    Method: PUT
    Endpoint: /users/<id>
    Body: JSON object with updated name and email (end address with relevant ID number)

## 5. Delete a user
    Method: Delete
    Endpoint: /users/<id>
    Body: NO DATA INPUT!! Only change the address to end with the relevant ID number

### 4. Managing the application

View the logs if issues arrise to troubleshoot using:

docker-compose logs -f api

Stop the application without deleting any data using:

docker-compose down

Reset the database, stopping the containers and deleting all user data using:

docker-compose down -v
