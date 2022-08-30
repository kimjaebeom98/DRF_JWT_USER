# DRF_JWT_USER 🚀

<br>

### ***Introduction*** ✔

<hr>

#### Summary 🔽
> - Project 소개
>   - JWT 기반 회원가입, 로그인 기능 구현
>  
> - BACKEND(Djagno Authentication Server)
>   - JWT를 이용하여 OAuth 2.0 Auth 프로토콜 기반으로 Authentication 및 Authorization 구현
> 

### Requirments 🤔
> - BACKEND(Djagno Authentication Server)
>   - Python 3.7
>   - Django 2.2.3
>   - Django REST Famework 3.10.1
>   - Django REST Framework JWT 1.11.0
>   - requirements.txt 참조 
> - DataBase
>   - db.sqlite3

### Backend End-points 1️⃣
> Resource modeling
> - 회원가입 및 로그인 관련 API
> 
>   |  HTTP |  Path |  Method |  Permission |  목적 | request data(frontend) | response data(backend) |
>   | --- | --- | --- | --- | --- | --- | --- |
>   |**POST** |/api/user/signup|CREATE| AllowAny |사용자 회원가입| JSON { "email", "nickname", "password", "address" } | { "email", "nickname", "password", "address" } |
>   |**POST** |/api/user/signin|NONE| AllowAny |사용자 로그인, access_token 생성 및 반환| JSON { "email", "password" } | { "access_token" }, HTTP_200_OK |

### DataBase Models
> schema
> ![image](https://user-images.githubusercontent.com/87630540/187402587-1ec298dd-84a1-48cb-8f8f-9eb248bd896e.png)

### Process

- 회원가입

![image](https://user-images.githubusercontent.com/87630540/187402925-82e0138f-4d86-4dc0-94ca-e225ad30eb94.png)

- 로그인

![image](https://user-images.githubusercontent.com/87630540/187403315-6ad7d020-5a44-4904-9fb7-6bbc2cd21f67.png)


