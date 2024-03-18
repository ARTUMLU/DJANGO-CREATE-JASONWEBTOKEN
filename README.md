## My Project
Welcome to My Project! This is a simple Django project that demonstrates how to implement JWT (JSON Web Tokens) authentication in a RESTful API.

## Introduction
JWT (JSON Web Token) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. JWTs can be signed using a secret (with HMAC algorithm) or a public/private key pair using RSA or ECDSA.

## Purpose of JWT
JWT is commonly used for authentication and information exchange in web applications. It allows clients to authenticate themselves and access protected resources on a server after successful login.

## How JWT Works
Authentication: When a user logs in, the server generates a JWT token and sends it back to the client.

Authorization: The client includes the JWT token in subsequent requests as a bearer token in the Authorization header.

Verification: The server validates the JWT token to ensure its authenticity and integrity. If the token is valid and not expired, the server grants access to the requested resource.

## Benefits of JWT
Stateless: JWTs are stateless, meaning server-side storage of session data is not required. This reduces the load on the server and improves scalability.

Compact: JWTs are compact and can be easily transmitted over the network as URL parameters, HTTP headers, or within the request body.

Secure: JWTs can be digitally signed to ensure data integrity and authenticity. This prevents tampering and unauthorized access to the token contents.

## Getting Started

To use JWT authentication in your Django project, you can install the djangorestframework_simplejwt package. Detailed installation and usage instructions can be found in the official documentation: 
1: 
```bash
pip3.11 install djangorestframework-simplejwt
```



<img width="1438" alt="Ekran Resmi 2024-03-18 03 43 42" src="https://github.com/ARTUMLU/DJANGO-CREATE-JASONWEBTOKEN/assets/86891887/eaf2fd6a-1db5-4360-aa05-053698a6b69d">

