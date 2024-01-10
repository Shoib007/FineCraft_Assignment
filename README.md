# MACHINE SETUP
---
### Step 1
##### Install Docker
- Mac [Docker](https://docs.docker.com/desktop/install/mac-install/)
- Win [Docker](https://docs.docker.com/desktop/install/windows-install/)
### Step 2
#### Clone the Repo 
```
git clone https://github.com/Shoib007/FineCraft_Assignment
```
```
cd FineCraft_Assignment
```
### Step 3
#### Run the Docker Compose file using following command
```
docker compose up -d
```
### Step 4
#### Create Super User for Django Admin
```
docker exec -it django-container bash
python3 manage.py createsuperuser
```
Provide an email and password in order to register as an Admin

# API DOCUMENTATION
---
|  Path|Description  | Method |
|--|--|--|
| token/ |To get Refresh and Access Token  |POST  |
|token/refresh/  | To get the new Token | POST |
|accounts/register/  |For New User Registration (first_name, last_name, email, password  |POST |
|accounts/auth/  |For User Login  | GET|
|accounts/auth/  |For User Logout (User should pass the refresh_token in the body  | POST|
|products/  |To get all the listed products  |GET  |
|products/id  |Get,Update, Delete the product by its id  |GET, PUT, DELETE |
