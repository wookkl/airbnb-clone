# Model

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

- application 폴더

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

## 다대다 필드에서 필드 추가 하는 방법!

room.amenities.add(a)

---

# View

## view는 너가 요청에 반응하는 방법이고 url은 요청에 바로 응답하는 방법임

/rooms /users 등으로 시작하는 것은 해당 앱 url에 두고 그외의 login logout들은 core에 두는게 좋음

## config urls에 app url import 하는 방법

```python
from django.urls import path, include
urlpatterns = [path("", include("core.urls"))]
```

## app_name이랑 namespace랑 같아야함

## httpResponse

httpResquest에 대한 응답으로 httpResponse object를 리턴해준다

```python
from django.http import HttpResponse

```

template(html)들을 rendering할 것임

## 장고에게 templates 위치 알려주기

config/setting.py에 TEMPLATES에 "DIRS"가 있음 여기에
Path("templates")

## templates에ㅅ 가장 장점인 부분은 context인데 context는 변수는 보내는 하나의 방법이다

context를 template에서 사용하는 방법은 {{now}}

## base.html

다른 템플릿들을 쉽게 렌더링할 수 있게 하기 위해서 골격을 짜줌

## extends

마리 만드러둔 base.html골격을 사용하기 위해서

## block

하나의 창 같은 것 임 자식 템플릿이 부모 템플릿에게 넘겨주는 창

?page=1 이런건 컨벤션 이라고 함

## url의 모든 것들은 GET request임! 브라우저에서 페이지로 가는건 GET request

request.GET은 get을 가지고 있는데 queryDictionary에서 원하는 key의 value를 가지고 올 수 있게 해줌
request.GET.get("page",0) page key가 존재하지 않을떄 기본적으로 0을 반환함

## pagingator

pagination

```python
from.django.core.paginator import Paginator
```

**room_models.Room.objects.all()** 사실 이것은 호출하는 즉시 데이터를 리턴하는 것이 아니라 쿼리셋만 생성할 뿐이다!
호출이 되는 순간에 즉시 데이터베이스로부터 불려져 올것임

## orphans: 요소의 목록인데 남겨진 요소라고 생각하면 좋을 듯

23페이지중
Paginator(room, 10) 이라면 3개의 요소가 남겨진 요소인데 여기서 orphan=5 인자를 넣어주면 5보다 작은 orphans가 나오면 그 전페이지에뿌려줌 따라서 2페이지에 13개의 요소가 뿌려짐

get_page와 page??
get_page method는 많은 것들을 허용해줘서 컨트롤하기 쉬운반면
page는 에러를 좀더 세세하게 컨트롤할 수 있음

## concept of listview

Definition : A page representing a list of objects
listview는 class based view라고 불리는 가족에게서 왔음
class based view는 함수 위에서 더 많은 abstract를 한다.
`room_views.HomeView.as_view()`
기본적으로 HomeView는 클래스인데 urlpatterns 의 path에는 view function을 넣어야함 따라서
Based view 는 as_view라는 function이 존재함 이것을 사용하면 됨

## ccbv classy class-Based Views.

https://ccbv.co.uk/
대부분의 class-based view를 보여주는 곳임

## class-Based View vs function-Based view?

CBV는 굉장히 유연하기때문에 프로그래밍할 시간을 줄일 수 있음
그러나 FBV는 하드코어하게 컨트롤을 할 수 있음

## url dispatcher

url에 변수를 가질 수 있게 함

## url tag!

{% url %}
사용 방법:
{% url namespace:name%}

## url & namespace

models.get_absolute_url() : 원하는 모델을 찾을 수 있눈 url을 리턴
`from django.urls import reverse`
reverse module: return되는 url을 namespace와 name, kwargs를 사용하여 url을 리턴 시킴

## DetailView

기본적인 detailview는 model 이름에 따라서 lowercase한다음 그것을 context로 기본적으로 제공
또한, 기본적으로 url argument로 pk를 찾음

## block Trick!

블럭을 숨기고 싶을떄 base에 block을 정의하고
block을 숨기고 싶을 경우에 빈 block을 넣어줌

## submit

form안에 button이 하나만 있다면 그것은 submit임!

## \*\*

`{**form, **choices}` 안의 요소들이 unpack됌!

## slugify

모든 것은 텍스트로 바꿔버림!!

## Field lookups

필드 필터링할때 사용!

\_\_gte: greater than equal

\_\_lte: less than equal

\_\_pk : primary key

\_\_startswith:

## Forms API

python 파일을 만들면 labels, value, placeholder, selected, checked 다 알아서 만들어줌
as_p : paragraph 형식으로 보여줌
as_ul : list 형식으로 보여줌
as_table: : 테이블 형식으로 보여줌
forms.ModelChoiceField : select option form을 생성 쿼리셋이 필요함

form field는 widget을 rendering 하는 것임 **Widget: HTML element**

## Form field attribute

help_text: 필드 밑에 도움말이 추가됨!

` form = forms.SearchForm(request.GET)` : form클래스에 보내주면 자동으로 입력된 부분을 저장해줌

## unbound form

우리가 갖고 있던 비어있는 form

## bound form

form에 정보가 입력되어 있는 상태

## if form.is_valid()

form이 알맞게 잘 설정 되었는지 확인해줌

## filtering된 객체들은 순서가 뒤섞여 있음 따라서

필터링 후에는 정렬을 해줘야 하는데
`qs = qs.order_by("created")`를 톨해 ordering 가능

## prettier ignore

django-html에서 prettier가 잘 안됨
따라서 ,prettierignore에 무시하고자 하는 파일 또는 폴더를 적으면 됌

## CSRF(Cross Site Request Forgery): 사이트간 요청 위조

웹사이트가 로그인 시켜줄떄 웹사이트는 쿠키를 준다.
브라우저가 백엔드로 쿠키를 보내는 방식은 도메인에 의해 이루어짐
만약 페이스북이 쿠키를 주면 접속할때마다 자동적으로 그 쿠키를 페이스북에 보내는 거임
문제는 너가 페이스북이 아닌 다른 웹사이트에 방문 했을 때 생김
그 웹사이트가 버튼이나 이상한 JavaScript를 가지고 있음 그버튼을 누르면 페이스북한테 요청함 maybe Ajax
그 요청은 브라우저에서 일어났기 떄문에 자동적으로 그 쿠키를 보낼건데 아까 그 웹사이트에서 페이스북 쿠키를 페이스북 백엔드쪽으로..
아마 그 웹사이트 사람은 너가 버튼 클릭할떄 너의 비밀번호를 어떻게 바꿀건지 찾아낼거임
그니까 기본적으로 다른 웹사이트에서 페이스북으로 form을 보내는거임

### Ajax란?

AJAX란, JavaScript의 라이브러리중 하나이며 Asynchronous Javascript And Xml(비동기식 자바스크립트와 xml)의 약자이다.
브라우저가 가지고있는 XMLHttpRequest 객체를 이용해서 전체 페이지를 새로 고치지 않고도
페이지의 일부만을 위한 데이터를 로드하는 기법 이며 JavaScript를 사용한 비동기 통신,
클라이언트와 서버간에 XML 데이터를 주고받는 기술이다.
즉, 쉽게 말하자면 자바스크립트를 통해서 서버에 데이터를 요청하는 것이다.

## csrf_token

이 토큰은 기본적으로 post request가 이 웹시이트에서 왔는지 확인하는 거임

## def clean_email(self):

이메일이나 비밀번호가 있는 field를 확인하고 싶으면 method 이름은 clean\_ 이어야함

에러를 넣는 것 뿐만 아니라 데이터를 정리도 해줌

form.clean_data는 모든 필드를 정리해준 거에 대한 결과
만약 clean method를 정의해줬는데 아무것도 리턴을 안한다면 그 필드를 지워버림

## clean method: 두 개의 다른 field가 서로 관련이 있을떄 확인하는 method

    무조건  cleaned_data를 리턴해야함!

## self.add_error(): 어떤 필드에서 에러가 생겼는지 나타내게 한다. clean method사용할때... field가 두개 이상이기때문에

## 로그인 시키려면 두가지 과정이 필요함

1. 인증 username,password 필요 return User oject
2. 로그인 request, User 객체를 줌
3. Redirect to a success page!

## Contrext Processor: 함수! template에 정보를 추가하는 일을 함!! 어디서든지 그 template으로 접근 할 수 있음! 그 view의 context가 아닌 어디서든지 가능

cookie를 가져와서 user을 찾고 그걸 template에 자동으로 넣어줌
파이썬 함수로 변수 하나만 가져가서 dictionary에 리턴

## Formview

인증을 해야할 떄에 정말 좋음 그리고 스스로 만들고 싶을 때도

## 암호화!!

계정을 생성하고 model에 저장할때에는 꼭 패스워드를 암호화해서 저장시켜야함!

## Modelform

장점: Modelform자체에 clean save method가 있음
unique한 field값을 validate할 수 있음
save() overiding할때에 commit=False를 넘겨줘야한다 왜냐하면 유저를 생성하고 나서
overing method 마지막에 자체적으로 commit해준다

## mailgun

이메일 서버를 따로 두지않거 WAS에서 메일을 보내게 되면 스팸으로 가기때문에
이메일 서버를 따로 둬야함 근데 그대신 인증된 mailgun API를 사용!

## dotenv

mailgun 유저 비밀번호를 git에 노출시키면 안되니까 dotenv를 사용

## email verify

email인증을 할때 랜덤숫자들을 이메일로 전송하고 그 해당 숫자들로 인증을 하는데
그 숫자들을 generate하는 모듈이 uuid임
`uuid.uuid4.hex()`

from django.utils.html import strip_tags : html문법이 포함된 스트링을 태그를 제거한후 text만 추출

from django.template.loader import render_to_string : template을 load해서 rendering

## OAuth Protocol

인터넷 사용자들이 비밀번호를 제공하지 않고 다른 웹사이트 상의 자신들의 정보에 대해 웹사이트나 애플리케이션의 접근 권한을 부여할 수 있는 공통적인 수단으로서 사용되는, 접근 위임을 위한 개방형 표준이다.이 매커니즘은 여러 기업들에 의해 사용되는데, 이를테면 아마존, 구글, 페이스북, 마이크로소프트, 트위터가 있으며 사용자들이 타사 애플리케이션이나 웹사이트의 계정에 관한 정보를 공유할 수 있게 허용한다

- 작동원리
  1. 유저랑 링크를 클릭
  2. 그 링크는 유저를 view로 이동시키는데 그 view는 github으로 redirect시킴
  3. github는 다시 유저를 웹사이트로 redirect 시킴

## 로그인할 때나 계정을 새로 만들때 Github, Kakao 인증 절차는 같음 다른점은 게정이 없다면 계쩡을 만들어준다는 것인데 결과는 같음

post.request 하기 위해서 requests 라이브러리를 사용

## .env 자료 가져올때

os.environ.get("DATA")

## Github Login 정리

    1. Github Login 버튼 클릭
    2. 그 링크는 github.com으로 redirect됨
    3. github.com 은 몇몇 데이터들을 필요로함 (client_id, redirect_uri, scope)
    4. user가 github에서 accept버튼을 누르면 다시 redirect_uri로 redirect 됨 Github_callback의 결과값
    5. github_callback에서는 url에서 code를 가져옴
    6. token을 액세스 하기 위해서 코드를가지고 request함
    7. 그럼 json data를 받을 수 있음 "Accept": "application/json" << 이 라인에 의해서 access_token이 들어있음
    8. access_token를 가지고 github api에 request할 수 있음 headers에 token을 보냄
    9. 결과적으로 user의 profile을 얻을 수 있음 json 형태로

## ImageField에 이미지 저장하는 방법

    1. image url를 얻는다.
    2. imgage url로 부터 request한다.
    3. 요청한 데이터에는 .content를 멤버변수가 있음 raw-byte 데이터임
    4. 그 데이터를 Contentfile에 넣어주면 임의의 파일이 생성됨
    5. user.imagefiled.save 메서드를 통해 저장해줌

# CSS Part

## Tailwind CSS

framework인데 utility를 우선시 하는 framework
대부분의 framework는 완제품인 (모든게 갖춰진) 다수의 class들로 제공됨
반면에 Tailwind는 오직 제공하는 것은 결과를 만들어낵 위해 같이 넣는 class name들 뿐임
간단하게 많은 CSS Property들을 class로써 가지고 있다는 것

## 작동하는 방법

styles.scss : sass file 여기에 sass code 쓸 수 있음
tailwind directive가 있음 @tailwind 라고 쓰는 건 directive를 위한 규칙
css 편집과 관련된 모든 것들은 styles.scss에 작성됨
static폴더는 건드리지 않는게 좋음
scss에서 생성하고 건드리는 모든 것들 scss파일에서 작성하는 모든 것들이 assets/scss/styles.scss에 들어있어야 함

css스크립트를 실행할 때 마다 gulp를 불러올 것 임
기본적으로 하는 일은 assets/scss/styles.scss 로 가서 css로 바꾸는 것임
결과적으로 우리가 보내는 브라우저에게 보내는 것은 statics/css파일임
assets - 프로그래머를 위한 것
static - 브라우저를 위한 것

보안문제로 인해 url만 가지고 서버의 파일을 navigate 할 수 없음
그래서 원하는 폴더에 접근할 수 없음
따라서 장고에게 어떤 파일을 expose 할 것인지 알려줘야함

gulpfile.js > 기본적으로 sass코드를 가져다가 css 코드로 바꾸는것

## static 파일 enable하는 방법

```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

## stylesheet를 링크 시킬때 일일이 절대 주소를 적을 필요 없이 태그를 사용

{% static 'css/styles.css' %}
static 태그는 잘 안쓰니까 로드해줘야 함
로드하는 방법은 맨위에 {% load statc %}

## em = = font-size

만약 font-size가 20px라면
2em은 40px 가장 가까운 font size와 관련이 있음
많은 반응형 웹 사이트들이 사용하는 측정단위

## rem = root em

rem은 가장 가까운 font size와 관련이 없음 root font size에 연관이 있음

tailwind의 root font size는 16px

## tailwind에서 확장하는 법

```javascript
//tailwind.config.js
theme: {
    extend: {
      spacing:{
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
      }
    },
  },
```

## 긴 글 자르는 밥 Tailwind

.truncate: 긴글을 자르고 축소시킴
overflow-hidden: 자신보다 길면 아예 갈라버림
block : 길어서 넘어가는 부분 ...으로 나타냄

## form에 input의 placeholder 바꾸는 방법!

```python
widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
        }
```

## general error 추가시키는 법

general 하다는 뜻은 form안에 공통적인 에러를 뜻함

## form field looping

```python
{% for field in form %}
    {{field}}
{% endfor %}
```

## 중복되는게 있으면 꼭 분할/정복 !!

```python
{% include 'partials/index.html' with object=object%}
```

## Message framework

메시지라는게 카톡같은 메시지가 아니라 문자열들을 유저들에게 준다는 것이랑 비슷
다른 HTML을 템플릿 안에 추 하기를 윈함

많은 메시지들을 유저들에게 보내줄 수 있음
메시지는 오직 한번만 보여줌!

## absolute URL concept

장고 모델들은 get_absolute_url이라는 메소드를 가지고 있음
Detail 안에 있는 모델을 보기 위해서는 url을 반환해야만 함

웹사이트에서 자세하게 무언가 보고 싶다면 get_absolute_url은 요긴하게 사용될 수 있음

## userprofileview

다른 유저의 디테일 뷰에 들어가게되면 그 다른 유저로 유저의 객체가 교체되어 자신의 profile로 들어갈 수 없는 문제 발생
->context_object_name을 사용하면 로그인 했던 유저가 아니라, 뷰에서 찾았던 객체를 가르키는 방법을 바꿀 수 있도록 해줌 **정말 중요!!**

## get_context_data

템플릿 안에 더 많은 컨텍스트를 사용할 수 있게 해줌

## UpdateView

이름 그대로 유저 모델 또는 객체를 가져와 업데이트 시켜줌. 폼을 만들어 주기도 함
모델과 필드만 넣어주면 편하게 수정이 가능함!
수정완료 버튼을 누르면 get_absolute_url로 redirect됨!!

이미지필드는 form의 인코딩 타입을 꼭 바꿔주어야함

사용하면 편리히고 좋지만 통제력이 떨어짐
최선은 UpdateView를 사용하되, 커스텀 form을 사용하는 것

디폴트로 url에 있는 pk를 받음

## get_object method

우리가 수정하기 원하는 객체를 반환

```python
def get_object(self, queryset=None):
    return self.request.user
```

## mixins class

일부 추가적인 기능을 제공
SuccessMessageMixin class: 정상적으로 form이 완료되면 완료 message를 띄울 수 있음

mixins.py

장고는 아주 강력한 퍼미션 엔진!

## pluralize

{{room.reviews.count}} review{{room.reviews.count|pluralize}}
복수일때만 s를 붙여줌

## defualt

include에서 변수 넘겨줄때 받는쪽에서 default를 지정해줄 수 있음
{{h_and_w|default:'h-20 w-20'}}

## django의 단점

드래그앤 드랍같은 인터페이스가 없음

## 사용자 인증

데코레이터(Decorator)를 이용한 구현 방법: 함수형 뷰에서 사용
믹스인(Mixin)을 이용한 구현 방법: 클래스형 뷰에서 사용

## mode

화폐 언어 또는 호스트/게스트 모드는 따로 데이터베이스에 저장하지 않아도 됨
session으로 처리할 수 있음

## save method

database에 저장할떄 many-to-many 필드는 따로 form.save_m2m() method를 호출해야함!!
대신에 모델 먼저 데이터베이스에 저장한 후에 다대다 필드를 저장!
form을 저장해야함!!

## filters and tags

{% url %} << 이게 태그
{% 'qweqwewqe'|upper} << 이게 필터

### 필터 만드는 법

1. app안에 templatetag라는 폴터를 만듬 다른 이름 x
2. 그 안에 `__init__.py`를 만듬
3. 사용자 정의 .py 파일 생성

```python
from django import template

register = template.Library() #library인스턴스를 받음

@register.filter() #extag가 필터 이름이 됨
def extag(value):
    return value.capitalize() ## 최종적인 반환값
    #{{'someting'|extag}} 쓰면 Something 반환
```

## simple_tag(func=None, takes_context=None, name=None)

takes_context=True해주면 장고가 전달해주는 유저나 다른 컨텍스트를 받을 수 있음

태그는 필터보다 더 많은 아규먼트를 보낼 수 있음!!
{% is_booked room day as is_booked_bool %} << 이렇게 하면 is_booked_bool이라는 변수를 가지게 됨!

## managers

objects.get() objects.filter 이런것들이 다 manager임
managers 상속 받는법

1. managers.py를 만듦
2.

```python
from django.db import models

class CustomReservationManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
```

3. models.py에
   ` object = managers.CustionReservationManager()`
4. 사용할땐
   `reservation = models.Reservation.objects.get_or_none(pk=pk)`

## form post

request post받으면 안에 form이 저장되어있으므로 바로 form에 넘겨주면 됨
`form = forms.CreateReviewForm(request.POST)`

## ordering

model이 list에 있는 경우에 정렬 방식을 정의

```python
class Meta:
        ordering = ("-created",)
```

## validator

MaxValueValidator, MinValueValidator form, model에 사용할 수 있음

user를 절대 믿으면 아됨 form에서도 protect해주고 model에서도 protect해주자!

## translations

1. locale 폴더 생성
2. settings.py에 locale 폴더 위치 지정
3. .html에 {% load i18n %}
4. trans태그로 태깅

## 모델을 만들떄 trans_lazy 꼭 염두 해줘야함! 나중에 하면 귀찮!
