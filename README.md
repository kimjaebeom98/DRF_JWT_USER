# DRF_JWT_USER ๐

<br>

### ***Introduction*** โ

<hr>

#### Summary ๐ฝ
> - Project ์๊ฐ
>   - JWT ๊ธฐ๋ฐ ํ์๊ฐ์, ๋ก๊ทธ์ธ ๊ธฐ๋ฅ ๊ตฌํ
>  
> - BACKEND(Djagno Authentication Server)
>   - JWT๋ฅผ ์ด์ฉํ์ฌ OAuth 2.0 Auth ํ๋กํ ์ฝ ๊ธฐ๋ฐ์ผ๋ก Authentication ๋ฐ Authorization ๊ตฌํ
> 

### Requirments ๐ค
> - BACKEND(Djagno Authentication Server)
>   - Python 3.7
>   - Django 2.2.3
>   - Django REST Famework 3.10.1
>   - Django REST Framework JWT 1.11.0
>   - requirements.txt ์ฐธ์กฐ 
> - DataBase
>   - db.sqlite3

### Backend End-points 1๏ธโฃ
> Resource modeling
> - ํ์๊ฐ์ ๋ฐ ๋ก๊ทธ์ธ ๊ด๋ จ API
> 
>   |  HTTP |  Path |  Method |  Permission |  ๋ชฉ์  | request data(frontend) | response data(backend) |
>   | --- | --- | --- | --- | --- | --- | --- |
>   |**POST** |/api/user/signup|CREATE| AllowAny |์ฌ์ฉ์ ํ์๊ฐ์| JSON { "email", "nickname", "password", "address" } | { "email", "nickname", "password", "address" } |
>   |**POST** |/api/user/signin|NONE| AllowAny |์ฌ์ฉ์ ๋ก๊ทธ์ธ, access_token ์์ฑ ๋ฐ ๋ฐํ| JSON { "email", "password" } | { "access_token" }, HTTP_200_OK |

### DataBase Models
> schema
> ![image](https://user-images.githubusercontent.com/87630540/187402587-1ec298dd-84a1-48cb-8f8f-9eb248bd896e.png)

### Process

- ํ์๊ฐ์

![image](https://user-images.githubusercontent.com/87630540/187402925-82e0138f-4d86-4dc0-94ca-e225ad30eb94.png)

- ๋ก๊ทธ์ธ

![image](https://user-images.githubusercontent.com/87630540/187403315-6ad7d020-5a44-4904-9fb7-6bbc2cd21f67.png)


