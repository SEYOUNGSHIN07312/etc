# JavaScript

I. 개요
	웹 페이지에서 이벤트 발생 시 어떻게 작동하는지 프로그래밍
	웹 페이지 동작을 제어

​	세미콜론 : 회사, 팀에 맞춰서 쓰기



II. 기초문법

1) 변수
   let 재할당O, 재선언X
   const 재할당X, 재선언X
   var (default) 재할당O, 재선언O -> 함수 스코프, 변수 호이스팅 발생

   블럭 : if for 함수의 중괄호 내부

   일단 const로 하고 에러나면 let으로 바꾸자
   var는 쓰지말자(에러 가능성, 메모리)

2) 호이스팅
   런타임 이전에 선언문들이 끌어올려지는 것 -> 자수성가라서(?)

3) 연산자
   다른건 다 비슷함
   동등 연산자 (==) : 암묵적 형변환
   일치 연산자 (===) : 값과 타입이 모두 같아야 true

4) 함수
   선언식 : 함수 호이스팅
   표현식 : 변수 호이스팅
   자수성가 언어라서 너그러움 -> 매개변수랑 인자 개수 달라도 알아서 허용해줌

   화살표함수 : 함수를 간결하게 정의, 귀찮아서 탄생

5) 배열
   키와 속성들을 가지는 객체
   0과 자연수 인덱스로 접근 가능

   helper methods
       i) forEach : 반환값 없음
       ii) map : 반환값을 요소로 하는 배열 반환
       iii) filter : 반환이 참인 것만 모아서 배열 반환
       iv) reduce : 값들을 누적해서 반환
       v) find, some, every
   
   

III. DOM
	선택 + 조작



IV. Event
	addEventListener -> 이벤트 전파 capturing / bubbling / target



V. 동기 / 비동기
	call back - (콜백지옥, 실패보장X) - promise - (then chaining) - async, await - axios

​	비동기 시작은 사용자 경험 보완을 위함 -> 이후 코드 가독성까지 개선



VI. 비동기 웹 통신
	DOM + Event + promise, axios