# Vue

#### I. 개요

  1. Front - end

     ​	Web App / Web Site의 UI / UX를 제작, 관리

     ​	UI (user interface) -> **시각적**

     ​	UX (user experience) -> **사용자 경험**

​			

​	2. MPA vs SPA

![img](https://blog.kakaocdn.net/dn/kB6Ji/btrlxFH9Aus/GEDwtXPGVw4iCQGL2SKW4k/img.png)

​			MPA

​				장 ) SEO 유리 (크롤러가 보기 쉬움)

​				단 ) 새로고침 -> **초기 이후** **속도 **↓, **서버 부하 많음**

​			**SPA**

​				장 ) 최초 1장의 HTML (CSR 방식) -> 새로고침 필요X -> **트래픽 감소, 속도 ↑**

​				단 ) **초기 로딩 시간 ↑**, SEO 불리 (빈 HTML)



​	3. CSR vs SSR

​			**CSR**

​				i ) AJAX 요청

​				ii ) 서버 -> JSON 데이터 -> JS로 처리, 렌더링 (데이터는 줄테니까 니네가 알아서 그려라)

​			SSR

​				i ) 요청 -> 그에 맞는 HTML 렌더링 (ㅇㅋ 내가 다 떠먹여줌)

​				ii ) 응답할 때마다 새로고침

​			=>  적절히 둘을 잘 활용할 것



#### II. Vue : JavaScript Framework

![](C:\Users\SSAFY\Desktop\수업자료\캡처2.PNG)

​		1. new -> Vue 인스턴스 생성

​		2. el : [Vue 객체 & DOM] 연결

​		3. data : 인스턴스 속성 -> {{ }}를 통해 view에 렌더링

​				- Observer : Vue data를 감시

​		4. methods : 해당 Vue 인스턴스 메서드 정의



![](C:\Users\SSAFY\Desktop\수업자료\캡처3.PNG)

 