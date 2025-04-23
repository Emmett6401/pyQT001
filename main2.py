# -*- coding: utf-8 -*-
# 한글 처리를 위해서 맨 윗줄에 추가 한 내용

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
import cv2
import os

Form, Window = uic.loadUiType("res/mainWin.ui")

class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.form = Form()
        self.form.setupUi(self)
        
        # 웹캠 초기화
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30ms 간격으로 프레임 업데이트
        
        # 버튼 클릭 이벤트 연결
        self.form.btnSave.clicked.connect(self.save_data)
        self.form.btnPhoto.clicked.connect(self.capture_photo)
    
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # OpenCV BGR -> RGB 변환
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            # QImage로 변환
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            # label_4에 영상 표시
            self.form.label_4.setPixmap(QPixmap.fromImage(qt_image))
    
    def capture_photo(self):
        try:
            ret, frame = self.cap.read()
            if ret:
                # 파일명 생성
                name = self.form.lineEditName.text()
                phone= self.form.lineEditPhone.text()
                if not phone:
                    phone = "photo"
                filename = f"photos/{phone}.jpg"
                
                # photos 디렉토리가 없으면 생성
                os.makedirs("photos", exist_ok=True)
                
                # BGR 이미지 직접 저장 (RGB로 변환하지 않음)
                success = cv2.imwrite(filename, frame)
                
                if success:
                    # lineEditPhoto에 파일 경로 설정
                    self.form.lineEditPhoto.setText(filename)
                    print(f"사진이 성공적으로 저장되었습니다: {filename}")
                else:
                    print("사진 저장 실패")
                
        except Exception as e:
            print(f"사진 저장 중 오류 발생: {str(e)}")
            import traceback
            traceback.print_exc()  # 상세 에러 메시지 출력
    
    def save_data(self):
        try:
            # CSV 모듈 임포트
            import csv
            
            # UI에서 데이터 가져오기
            name = self.form.lineEditName.text()
            phone = self.form.lineEditPhone.text()
            recommend = self.form.textEditRecommand.toPlainText()
            photo = self.form.lineEditPhoto.text()
            
            # UTF-8-SIG로 저장 (BOM 포함)
            with open('data.csv', 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                # 파일이 비어있다면 헤더 추가
                if f.tell() == 0:
                    writer.writerow(['이름', '전화번호', '추천사항', '사진'])
                # 데이터 추가
                writer.writerow([name, phone, recommend, photo])
                
            print("데이터가 성공적으로 저장되었습니다.")
        except Exception as e:
            print(f"저장 중 오류 발생: {str(e)}")
    
    def closeEvent(self, event):
        # 창이 닫힐 때 웹캠 해제
        self.cap.release()
        event.accept()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()