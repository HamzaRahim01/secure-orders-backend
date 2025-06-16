# secure-orders-backend
A secure backend service built with Django Rest Framework for managing user and order data. 


INSTALLATIOM:
Clone the repository from https://github.com/HamzaRahim01/secure-orders-backend.git



USAGE:
To make the application up and running, execute the following command on the terminal 
"docker-compose up --build"



API DOCUMENTATION:
The API is accessible at http://localhost:8000/ and requires JWT authentication for protected endpoints. Below are the key endpoints:

1.User Registration: POST http://localhost:8000/api/register/ 
- Create a new user(No authentication needed).

2.Endpoint to obtain auth token: POST http://localhost:8000/api/token/ 
-Returns Access and Refresh token(Provide username and password of registered user in the Body)

3.User Detail: GET/PATCH/DELETE http://localhost:8000/users/<int:pk>/
-Retrieve, update, or delete a specific user by ID.
-Requires authentication and appropriate permissions.

4.Admin Email List: GET http://localhost:8000/admin/emails/
-Retrieve a list of all emails of all users.
-An authenticaticated api which only superuser can execute.

5.Order Create/List: GET/POST http://localhost:8000/orders/
-Retrieve a list of all orders or create a new order.
-Requires authentication.

6.Order Detail: GET/PUT/DELETE http://localhost:8000/orders/<int:pk>/
-Retrieve, update, or delete a specific order by ID.
-Requires authentication and appropriate permissions.

7.Admin Orders by Email: GET http://localhost:8000/admin/orders-by-email/
-Provided a list of emails in the body all orders owned by users of those emails will be fetched.
-An authenticaticated api which only superuser can execute.