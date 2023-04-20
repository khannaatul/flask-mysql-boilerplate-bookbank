# MySQL + Flask Boilerplate Project

# Project Description

This is a book swap application. This application allows book readers to register their user information, location, and book they currently have (physical or eBook). Allows book readers to request book swaps with other book readers/receive book swap requests so the two users can meet up in person or virtually and swap books. Allows book readers to perform book swaps with the book bank and add and remove with their library. Authors can submit books to the book bank.

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

# Video Demo
https://youtu.be/Xfq4R-L_KJE
## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




