package member;

public class MemberMain {

	public static void main(String[] args) {
		MemberService memberService = new MemberService();	// MemberService에 접근하는 주소
		memberService.menu();
		System.out.println("프로그램을 종료합니다.");
		

	}

}
/*
[문제] 회원관리

* 조건
- 회원을 입력받아서 파일에 저장하거나 파일의 내용을 읽어온다.
- MemberService 클래스에 메뉴 메소드 작성한다.
  메뉴에 따라 각각의 클래스를 작성한다.
- 회원의 정보는 이름, 나이, 핸드폰, 주소로 한다.

1. 클래스 작성
MemberMain.java

MemberService.java
- 메뉴 작성

MemberDTO.java
- 필드, 생성자, setter, getter

MemberInsert.java
MemberPrint.java
MemberPhoneSearch.java
MemberNameAsc.java
MemberFileInput.java
MemberFileOutput.java

2. 인터페이스 작성
Member.java
- 추상메소드 public void execute();
=> member 패키지에 인터페이스 Member 생성 후 추상메소드 public void execute(); 입력


menu()
********************
  1. 등록
  2. 출력
  3. 핸드폰 검색
  4. 이름으로 오름차순
  5. 파일 저장
  6. 파일 읽기
  7. 끝
********************
  번호 : 

=============================================================================

MemberInsert aa = new MemberInsert(); -> 1:1 관계, 결합도가 높다
MemberPrint bb =  new MemberPrint(); -> 1:1 관계, 결합도가 높다
MemberPhoneSearch cc = new MemberPhoneSearch(); -> 1:1 관계, 결합도가 높다

결합도 낮추기, 다형성(부모 = 자식)
interface 

Member member
member = new MemberInsert();
member.insert(); => member.execute();

member =  new MemberPrint();
member.print(); => member.execute();

member = new MemberPhoneSearch();
member.search(); => member.execute();

*/