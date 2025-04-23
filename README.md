# pyQT001
pyQT를 이용한 고객 관리 프로그램 제작 
1. Python 파일을 package 포함해서 APP.exe    1 File 로 만들기    
   준비물 - best.pt(이것은 좀 아껴 두기로 한다.)

   GUI APP을 만들기 위해서    
   1.1 QTDesigner를 설치 한다.    
         https://build-system.fman.io/qt-designer-download

   1.2 간단한 GUI APP을 만들어 보자    
<img width="642" alt="image" src="https://github.com/user-attachments/assets/ae9d1d69-8805-467f-8c73-edbd57abca8f" />
   1.3 각각의 object는 이름을 갖고 있고  그 이름을 이용해서 GUI를 코드로 구현한다.
   <img width="960" alt="image" src="https://github.com/user-attachments/assets/cdc72647-53fc-4693-9078-3002f4e81f4b" />

2. UI가 완성 되었으면
   2.1 메소드 구현을 한다.   
   저장, 수정, 삭제, 조회(기본틀이다)   
   2.2 DataBase연동을 한다.   
   dbConnect와 SQL 문으로 데이터 연동   
   2.3 그림 파일은 항상 내 로컬에 있는 것으로 한다.   
   만약 수정이 필요하면 FTP를 이용하고 경로만 DB에 저장하는 방식이다.   
   
3. Finnaly   
   3.1 웹카메라와 먼저 만들어 놓은 best.pt를 이용해서    
   3.2 특정 이벤트 예를 들어거 고양이를 발견 햇을때만 필요한 내용을 저장하는 것으로 발전 시킨다.    

      
