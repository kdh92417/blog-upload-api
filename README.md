# 🚀 Posting Upload API Service

- 게시글을 비밀번호 설정하여 업로드하는 API 서비스

# 📆 개발 기간
- 2022.09.06 ~ 2022.09.07

# 기능
- 유저가 포스팅 업로드
  - 비밀번호 설정 가능
  - 이모지 포함 기능

- 유저가 올린 포스팅을 비밀번호 입력후 수정/삭제 가능
- Pagination(20개의 포스팅 단위)

# 기술 스택
- Backend: `Django Rest Framework`
- DB: `MySQL`
- Etc: `Docker`
- Tool : `Git`

# API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /api/posting/v1/  | GET   | 게시글 리스트 조회 |  -  | 게시글 리스트|
| /api/posting/v1/  | POST     | 게시글 생성  | title: string <br/>content: string <br/> password: string   | 생성된 게시글 인스턴스   |
| /api/posting/v1/id/  | PATCH     | 게시글 수정  | password: string   | 수정된 게시글 인스턴스  |
| /api/posting/v1/id/  | DELETE   | 게시글 삭제|  password: string  | 성공여부 |

# ERD
![스크린샷 2022-09-07 오후 2 19 41](https://user-images.githubusercontent.com/58774316/188794790-3a4a3e45-b3e1-4658-a09c-348f0f6ee886.png)

# 참조 문서
- [Postman API 문서](https://documenter.getpostman.com/view/11682851/VVBQXUTd)
