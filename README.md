# ๐ Posting Upload API Service

- ๊ฒ์๊ธ์ ๋น๋ฐ๋ฒํธ ์ค์ ํ์ฌ ์๋ก๋ํ๋ API ์๋น์ค

# ๐ ๊ฐ๋ฐ ๊ธฐ๊ฐ
- 2022.09.06 ~ 2022.09.07

# ๊ธฐ๋ฅ
- ์ ์ ๊ฐ ํฌ์คํ ์๋ก๋
  - ๋น๋ฐ๋ฒํธ ์ค์  ๊ฐ๋ฅ
  - ์ด๋ชจ์ง ํฌํจ ๊ธฐ๋ฅ

- ์ ์ ๊ฐ ์ฌ๋ฆฐ ํฌ์คํ์ ๋น๋ฐ๋ฒํธ ์๋ ฅํ ์์ /์ญ์  ๊ฐ๋ฅ
- Pagination(20๊ฐ์ ํฌ์คํ ๋จ์)

# ๊ธฐ์  ์คํ
- Backend: `Django Rest Framework`
- DB: `MySQL`
- Etc: `Docker`
- Tool : `Git`

# API Endpoints
| endpoint | HTTP Method | ๊ธฐ๋ฅ   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /api/posting/v1/  | GET   | ๊ฒ์๊ธ ๋ฆฌ์คํธ ์กฐํ |  -  | ๊ฒ์๊ธ ๋ฆฌ์คํธ|
| /api/posting/v1/  | POST     | ๊ฒ์๊ธ ์์ฑ  | title: string <br/>content: string <br/> password: string   | ์์ฑ๋ ๊ฒ์๊ธ ์ธ์คํด์ค   |
| /api/posting/v1/id/  | PATCH     | ๊ฒ์๊ธ ์์   | password: string   | ์์ ๋ ๊ฒ์๊ธ ์ธ์คํด์ค  |
| /api/posting/v1/id/  | DELETE   | ๊ฒ์๊ธ ์ญ์ |  password: string  | ์ฑ๊ณต์ฌ๋ถ |

# ERD
![แแณแแณแแตแซแแฃแบ 2022-09-07 แแฉแแฎ 2 19 41](https://user-images.githubusercontent.com/58774316/188794790-3a4a3e45-b3e1-4658-a09c-348f0f6ee886.png)

# ์ฐธ์กฐ ๋ฌธ์
- [Postman API ๋ฌธ์](https://documenter.getpostman.com/view/11682851/VVBQXUTd)
