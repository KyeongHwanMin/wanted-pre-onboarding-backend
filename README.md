# 원티드 프리 온보딩 백엔드 과제 - 민경환
[1.개발환경 세팅](#개발-환경-세팅)
[2.API 명세](#API-Specifications)
[3.테스트](#테스트)

## pre requirements
- Pyenv(https://github.com/pyenv/pyenv)

## 프로젝트 스펙 정보
- Python 3.12.x
- Django 4.2.x
- djangorestframework 3.14.x

## 개발 환경 세팅
```bash
# python 설치
pyenv install 3.12.x
# 가상환경 설치
python -m venv venv
# 가상환경 활성화
venv/Scripts/activate
# 의존성 설치
pip install -r requirements.txt
# 데이터베이스 마이그레이션
python manage.py migrate
```

## 서버 정상 실행 확인
```bash
python manage.py runserver
```
위 명령 실행 결과로 아래와 같은 콘솔 출력이 뜨고, http://127.0.0.1:8000/ 접속이 되면 정상이다.
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2023 - 13:40:31
Django version 4.0.10, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
## API Specifications

### 회사등록
[요청]
- URL : POST /api/v1/company
- Body
```json
{
  "name" : "원티드랩",
  "nation" : "한국",
  "area": "서울"
}
```
[응답]
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 201
```json
{
  "id" : 1,
  "name" : "원티드랩",
  "nation" : "한국",
  "area": "서울"
}
```
- Error

|에러코드| 설명        |
|------|-----------|
|400| 잘못된 요청 구문 |

### 채용공고 등록
[요청]
- URL: POST /api/v1/recruitment-notice
- Body
```json
{
    "회사_id":1,
    "채용포지션":"백엔드 주니어 개발자",
    "채용보상금":1000000,
    "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은...",
    "사용기술":"Python"
}
```
- Body 파라미터 설명
  - 회사_id : 등록된 회사의 id 입력
  - 채용포지션 : 문자열 입력
  - 채용보상금 : 0 이상의 정수 입력
  - 채용내용 : 채용상세 내용. 문자열 입력  
  - 사용기술 : 사용할 수 있는 기술. 문자열 입력
  
[응답]
- Body
```json
{
    "회사_id": 1,
    "채용포지션": "백엔드 주니어 개발자",
    "채용보상금": 1000000,
    "채용내용": "원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은...",
    "사용기술": "Python"
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 201
  - 응답 Body 설명 : 수정된 결과가 반환 됩니다.
  

- Error

|에러코드| 설명        |
|------|-----------|
|400| 잘못된 요청 구문 |

### 채용공고 수정
[요청]
- URL: PATCH /api/v1/recruitment-notice/:pk
  - Patch 파라미터 설명 : pk는 RecruitmentNotice의 식별 아이디를 입력.
- Body
```json
{
    "채용포지션":"백엔드 개발자",
    "채용보상금":1500000,
    "채용내용":"원티드랩에서 백엔드 주니어 개발자를 '적극' 채용합니다. 자격요건은...",
    "사용기술":"Python"
}
```
- Body 파라미터 설명
  - 채용포지션 : 문자열 입력
  - 채용보상금 : 0 이상의 정수 입력
  - 채용내용 : 채용상세 내용. 문자열 입력  
  - 사용기술 : 사용할 수 있는 기술. 문자열 입력
  
[응답]
- Body
```json
{
    "채용포지션": "백엔드 개발자",
    "채용보상금": 1500000,
    "채용내용": "원티드랩에서 백엔드 주니어 개발자를 '적극' 채용합니다. 자격요건은...",
    "사용기술": "Python"
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 수정된 결과가 반환 됩니다.
  

- Error

|에러코드| 설명        |
|------|-----------|
|400| 잘못된 요청 구문 |

### 채용공고 삭제
[요청]
- URL: DELETE /api/v1/recruitment-notice/:pk
  - Delete 파라미터 설명 : pk는 RecruitmentNotice의 식별 아이디를 입력.

[응답]
- Body
```json
{
    HTTP 204 No Content
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 204
  - 응답 Body 설명 : 내역이 삭제 됩니다.

### 채용공고 조회
[요청]
- URL: GET /api/v1/recruitment-notice
  
[응답]
- Body
```json
[
    {
        "채용공고_id": "1",
        "회사명": "원티드랩",
        "국가": "한국",
        "지역": "서울",
        "채용포지션": "백엔드 주니어 개발자",
        "채용보상금": 1500000,
        "사용기술": "Python"
    },
    {
        "채용공고_id": "2",
        "회사명": "네이버",
        "국가": "한국",
        "지역": "판교",
        "채용포지션": "Django 백엔드 개발자",
        "채용보상금": 1000000,
        "사용기술": "Django"
    }
]
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 모든 채용공고의 결과가 반환 됩니다.

### 채용공고 검색 조회
[요청]
- URL: GET /api/v1/recruitment-notice?search="검색어"
  - 예시 :(/api/v1/recruitment-notice?search="원티드")
  
[응답]
- Body
```json
[
    {
        "채용공고_id": "8",
        "회사명": "원티드랩",
        "국가": "한국",
        "지역": "서울",
        "채용포지션": "백엔드 주니어 개발자",
        "채용보상금": 1500000,
        "사용기술": "Python"
    },
    {
        "채용공고_id": "10",
        "회사명": "원티드코리아",
        "국가": "한국",
        "지역": "부산",
        "채용포지션": "프론트엔드 개발자",
        "채용보상금": 5000000,
        "사용기술": "javascript"
    }
]

```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 검색어가 포함된 채용공고의 결과가 반환 됩니다.

### 채용공고 상세 조회
[요청]
- URL: GET /api/v1/recruitment-notice/:pk
  - Get 파라미터 설명 : pk는 RecruitmentNotice의 식별 아이디를 입력.
  

[응답]
- Body
```json
{
    "채용공고_id": "1",
    "회사명": "원티드랩",
    "국가": "한국",
    "지역": "서울",
    "채용포지션": "백엔드 주니어 개발자",
    "채용보상금": 1500000,
    "사용기술": "Python",
    "채용내용": "원티드랩에서 백엔드 개발자를 채용합니다. 자격요건은...",
    "회사가올린다른채용공고": [
        11,
        12
    ]
}

```
- Body 파라미터 설명
  - 회사가올린다른채용공고 : 채용공고 식별 id가 리스트 형태로 반환.
  
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 채용공고 상세 조회된 결과가 반환 됩니다.

- Error

| 에러코드 | 설명          |
|------|-------------|
| 404  | 채용공고가 없는 경우 |

### 회원가입
[요청]
- URL : POST /api/v1/user
- Body
```json
{
    "email":"user@naver.com",
    "name":"user",
    "password":"123"
}
```
- Body 파라미터 설명
  - email : 이메일 형태로 입력. 문자열
  - name : 이름 입력. 문자열
  - password : 비밀번호 입력  
  
[응답]
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 201
```json
{
    "email": "user@naver.com",
    "name": "user",
    "password": "pbkdf2_sha256$320000$StVvPqtGcsRKcZm6FhKNFV$yAKrRLj0agMey4lZrT7isfJvOXJrJG/dn3bfueEMeEM="
}
```
- Error

|에러코드| 설명             |
|------|----------------|
|400| 중복된 이메일이 있을 경우 |

### 채용공고 지원
[요청]
- URL: POST /api/v1/recruitment-support
- Body
```json
{
    "recruitment_notice":8
}
```
- Body 파라미터 설명
  - recruitment_notice_id : 등록된 채용공고 식별 id 입력
  
[응답]
- Body
```json
{
    "recruitment_notice": 1,
    "user": 1
}
```
- Body 파라미터 설명
  - recruitment_notice_id : 등록된 채용공고 식별 id
  - user : 등록된 유저 식별 id
  - 
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 201
  - 응답 Body 설명 : 채용공고에 지원된 결과 반환.
  

- Error

|에러코드| 설명             |
|------|----------------|
|400| 중복요청이 있을 경우 |


## 테스트

### 채용
[채용공고 등록]
 ``` bash
python manage.py test recruitment_notice.tests.test_views.RecruitmentNoticeTest.test_create_recruitmentnotice
```
[채용공고 수정]
 ``` bash
python manage.py test recruitment_notice.tests.test_views.RecruitmentNoticeTest.test_update_recruitmentnotice
```
[채용공고 삭제]
 ``` bash
python manage.py test recruitment_notice.tests.test_views.RecruitmentNoticeTest.test_delete_recruitmentnotice
```
[채용공고 조회]
 ``` bash
python manage.py test recruitment_notice.tests.test_views.RecruitmentNoticeTest.test_list_recruitmentnotice
```

### 회사
[회사 등록]
```bash
python manage.py test company.tests.test_views.CompanyTest.test_create_company
```

### 유저
[유저 등록]
```bash
python manage.py test account.tests.test_views.AccountTest
```
