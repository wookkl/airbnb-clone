# pipenv: 파이썬 패키지 관리 툴 프로젝트

패키지가 전역으로 설치되는 것을 없애기 위해 만들어짐
패키지를 프로젝트 단위로 설치하고 관리할 수 있게 해준다

## 가상환경에 장고 설치하기

```sh
pipenv --three #독립된 프로젝트 환경에서 python3를 설치
pipenv shell  #독립된 프로젝트 내로 작업할 수 있게 가상 환경을 활성화함
pipenv install Django # 가상 환경에 장고를 설치
```

## 장고 프로젝트 생성하기

```
django-admin startproject config

```

# Linter : 에러가 생길 부분을 미리 감지해주는 툴 "flake8"

# PEP(python Enhancement Proposals): 파이썬 쓸 때의 코딩 권장사항

# Formatter: 코드를 Formatting 해준다. "black"

pipfile에서

- [dev-packages]: 개발자가 개발할 떄만 쓰이는 패키지
- [packages]: 웹 에플리케이션이 동작할때 사용하는 패키지

Linter-flake8과 formatter-black은 최고의 조합이다!!

## 파일들의 각각의 목적들

**init**.py : 장고와 관련된 파일이 아니라 파이썬에게 필요한 파일
settings.py : 애플리케이션을 만드는데 필요한 모든것이 담겨 있음

# Django document site!

장고에 필요한 모든 내용이 다 들어있음!

# db.sqlite3

최종 데이터베이스가 아니라 개발용 데이터베이스

# admin page 접속을 위한 슈퍼유저 게정 생성

```sh
python manage.py createsuperuser
```

# 장고 프로젝트는 여러 애플리케이션을 포함하고 있음!

## 프로젝트를 만들기전에 몇가지 애플리케이션을 만들어야하는지 생각해본다.

주의할 점!

- 절대로 에플리케이션 폴더를 크게 만드면 안됨!! 많은 기능들을 한 폴더에 넣지 말자(Divide and Conquor!!)

TIP! 한문장으로 애플리케이션을 표현할 수 있어야함

## Creating apps!

```sh
django-admin startapps examples  #애플리케이션 이름은 복수형이어야함
```

## authentification application

지금까지 할 수 있게 해준 애플리케이션임

## application을 만들고 만들어진 파일들의 이름을 절대 바꾸면 안됨!! 라이브러리가 아니라 프레임워크를 사용하는 것임!

만약 admin.py에 코드를 짜면 admin 패널에 반영됨

- application폴더

* models.py : 원하는 데이터베이스가 어떻게 생걌는지에 대해서 설명하는 곳, 데이터가 보여지는 곳

- Project 폴더
  urls.py: 웹사이트의 url들을 컨트롤함 여기에 모든 url들을 넣으면 안되고 분할 정복을 하자
  각각의 application안에 urls.py를 만들어주자

# 객체 상속 _매우중요_

## makemigrations 모델의 변경사항을 기반으로 새 마이그레이션을 생성

```sh
python manage.py makemigration
```

## migrate

```sh
python manage.py migrate # 변경사항을 마이그레이트
```

## Model Fields

- 데이터베이스 아규먼트를 추가하며 디폴트 값을 넣어 줘야함 2가지 방법이 있다

```python3
    * ex = models.TextFields(null=True)
    * ex = models.TextFields(default=False)
```

from . import models : 같은 폴더에 있는 models.py를 import 한다

## CharField는 옵션이 있음

choices는 튜플로된 데이터를 넣어주면 그 항목들만 고를 수 있게 해줌
ex) CharField(choices=GENDER_CHOICES, max_length=10, null=True)
이러한 변화들을 직접적으로 데이터베이스에 영향을 주지 않지 때문에 마이그레이션 할 필요 **x**!!

@admin.site.register(models.User,UserAdmin) > admin 패널에서 컨트롤할 수 있는 유저 클래스

Admin 패널 에서

```python

@admin.register(models.User)
class CustionUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost") #어드민패널에 리스트를 보여줌
    """ 어드민패널에 필터 기능 추가 """
    list_filter = (
        "language",
        "currency",
        "superhost",
    )
```

## recap

config folder : 마스터 폴터같은 개념

application folder : function 의 그룹

Django는 데이터베이스와 통신함
Django는 장고 ORM(Object Relational Mapping)을 탑재
ORM : 파이썬 코드를 SQL 문으로 바꿔서 데이터베이스가 알아 들을 수 있게 만듦
models.py : 넣는 것들 모두 데이터베이스 테이블로 만들어준다
Model은 필드로 구성되어 있다.
CharField TextField DataField BooleanField등등

admin.py: admin에 Model을 가져오려면 register을 해줘야 함

migrations는 적게 유지하는 것이 좋음 한번하는게 좋음

application을 만들땐 꼭 settings.py에 등록을 해주자

## CORE APP

다른 application의 재사용을 위한 common file을 만들어준다

## import 할때 TIP

처음엔 django와 관련된 패키지를 import
그다음 서드파티 패키지 import
그다음 프로젝트 패키지를 import

## 모델에 다른 모델 넣기 (Foreign Key)

```python
from users import models as user_models
ex) host = models.ForeignKey(user_models.User, on_delete= models.CASCADE)
```

### DateTimeField Option

auto_now_add: 이 모델이 생성되면 그 날짜와 시간을 자동으로 넣어줌
auto_add: 이 모델을 저장할때마다 자동으로 그 날짜와 시간을 업데이트해줌

### Foreign Key

on-delete=models.CASCADE : FOREIGN KEY가 데이터베이스에서 삭제되면 해당 데이터열도 삭제딤
many-to-one relationship

## Meta Class: 모든 모델내에 있는 class

    verbose_name: 어드민 애플리케이션에서 해당 모델이 보여질때 s를 붙이는 대신 모델 이름을 바꿔줄 수 있음
    verbose_name_plural: s를 안붙이고 모델 이름 자체적으로 바꿀 수 있음

## 모델을 만들때

필드 -> 외래키,주요키 ->메타클래스 또는 함수 정의

## model.py에서

**str** 는 해당 클래스로 만들어진 인스턴트를 자체를 출력할 때, 문자열로 설명해주기 위한 메서드임

## search_field

search_box가 생성되고 icontain이라는 디폴트 값을 가지고 일치하는 값을 검색해준다.
icontain: insensitiv를 포함한다는 말인데, 그말인 즉슨 대문자 소문자를 구별하지 않음
Foreign key의 필드의 필드에 접근하려면 언더바 \_\_ 를 써주고 접근한다.

## filter_horizontal

manytomany field만 적용 가능!
admin site에서 많은 속성중에 원하는 찾을수 이쓴 필터 기능이 있음

## fieldsets Options

'classes': 'collapse' ->필드를 접거나 펼 수 있음

## ordering

정렬되는 우선순위대로 정렬함

## admin 함수

같은 admin에서 사용할 수 있고, 원하는 이름을 지을 수 있음
admin함수는 두가지를 가짐

1. self는 Admin클래스임
2. object는 현재 row임
   따라서 `def __functionname__(self, obj)`

## short_description

`__functionname__.short_description = 'potato'` 이면 속성값이 potato로 바뀜

## Managers

장고 설정과 장고 모델들을 사용해서 프로젝트와 소통하고 싶다면

```shell
python manage.py shell #프로젝트 shell로 이동
```

vars(): **dict**, dictionary 또는 클래스 리스트안을 나타내는 것을 리턴한다.

dir(): 클래스 안의 names 리스트들을 리턴

Users.objects 하면 manager을 볼 수 있음
이 manager는 데이터베이트로부터 elements를 가져올 수 있음 sql문을 쓰지 안하도 됨! 장고의 특별한 부분중 하나!

데이터 모델을 생성하기만 하면, 장고가 자동으로 database-abstraction API(Ojects 를 CRUD할 수 있게 해주는)을 자동으로 제공.

## QuerySets

QuerySet이란?? 쉽게 Object 리스트, 데이터베이스로 부터 온 장고 Objects
Foreign key를 element로 가리치면
element 또한 foreign key에 접근할 수 있다
set은 foreign key의 대상이 element를 얻는 방법

related_name : 장고의 ORM기능을 활용하기 위함, 참조하는 객체 입장에서 related_name을 설정해줘야 함

many to many field는 바로 접근 가능

## models.py 에서의 function

사용자들에게도 웹페이지에 보여줄 수 있게끔 하기 위함

## from django.utils import timezone

파이썬 모듈 말고 장고의 모듈을 사용하는 이유는 다른 나라에서 서버에 접근 했을때 그 시간대로 바꿔주기 떄문
timezone.now().date(): 현재시간을 리턴
function_name.boolean = True : 리턴되는 값을 불리언으로 바꿔줌

## photo!!

photo url을 살펴보면 이상한 경로임 그 이유는 아직 URL이 없기 떄문!
장고에게 url을 부여하고 /media/로 가야 우리가 업로드한 photo들을 볼거라고 설정해줘야함

## media_root

장고에게 어디에다 우리가 업도르한 파일들을 써야 할 지 말해주는 변수임
config foledr에 setting.py에
MEDIA_ROOT = BASE_DIR / "uploads" 이런식으로 경로지정

## image field argument

upload_to : 여기에 MEDIA_ROOT안의 어떤 폴더에 업로드 할 것 인지

## media_url

media_url은 media_root에서온 media를 다룬다
MEDIA_URL = "/media/" -> 마지만엔 slash를 붙여줘야함
그담음엔 꼭 config.urls에 설정을 해줘야 사진을 볼 수 있음

## 어떻게 장고에게 폴더안에 파일들을 제공하나?

사용자 파일들을 저장할때 서버자체에 저장하는 것 보단 amazon s3같은 클라우드 컴퓨팅 서비스를 사용해야함
그러나, 지금 개발하기 위해서 서버에 저장함

## setting.py를 impor하고 싶을떄??

from django.conf import settings

## 서버가 개발모드인지 프로덕션 모드인지 아는 방법

setting.py 에 DEBUG를 확인

## 개발모드일때 폴더에 있는 파일들을 장고에게 알려주는 방법

if setting.DEBUG:
urlpatterns += static()
여가서 static은
from django.conf.urls.static import static

## static

static은 기본적으로 static 파일들을 제공함

static("URL",document_root="")

## f'<img src = "{obj.file.url}"/>'

admin에서 사진을 띄우려면 위에 처럼 html을 사용해야하는데 장고는 그러한 스크립트에 대해 보안을 기본적으로 하기 떄문에
그것을 장고에게 알려줘야함
`from django.utils.html import mark_safe`

## raw_id_field

예를들어 수천개의 user가 있을때 일일히 스크롤 하기 힘드니 raw_id_field를 사용하면 작은 유저 어드민 패널에 들어가서 검색해서 선택할 수 있음

## InlineAdmins

!! 이게 admin 안에 admin을 넣는 방법!

```python
class PhotoInline(admin.TabularInline):
    """ Definition PhotoInline """

    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Romm Admin Definition """

    inlines = (PhotoInline,)
```

어드민 패널을 보면 해당 Room의 foreign key를 가지고 있는 사진들을 나타내줌
\*\*왜냐하면 relationship name이 room이고 class name이 room 이기때문에 장고가 자동으로 뭘 말하는지 앎

## model이 저장되는 것을 가로채는 방법??

부모클래스를 참조한다! super()

## save()와 admin_save()

save()는 models.py에서 직접 데이터가 저장되는 메서드이고
admin_save()는 admin 패널에서 저장될때의 메서드임

호출 순서는 admin_save() -> save()임
따라서 admin_save()만 참조하여 오버라이딩 한다면 admin패널에서 일어나는 부분만 수정이 가능

## Custom command!

1. 아무 애플리케이션 폴더에 등어간다.
2. management 폴더를 생성
3. 그 안에 `__init__.py` 생성
4. commands 폴더 생성, `__init__.py` 생성
5. commands에 파이썬 파일 생성
6. `python manage.py loveyou --times 50 // loveyou를 50번 한다 `
7. Command class 생성

```python
def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that i love you",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0,int(times)):
            self.stdout.write.(self.style.SUCCESS("I love you"))
```

## Django seed

가짜 데이터를 빠르게 만들 수 있게 해줌

## from django.contrib.admin.utils import flatten

2차원 배열을 평평하게!
