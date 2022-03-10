import pyautogui
import time 
from PIL import ImageGrab  

# 전체 화면 크기
width, height = pyautogui.size()
# 현재 마우스 위치 확인
pyautogui.position

# 60 184 4  -> 초록색
# 239 89 88 -> 빨간색
# 243 175 28 -> 노란색 

stop_flag = True # 종료 조건 
time.sleep(10)

# x, y = pyautogui.position() # 마우스 위치 얻기
# pyautogui.FAILSAFE = False
# while stop_flag: 
#     screen = ImageGrab.grab() # 화면 캡쳐
#     for h in range(height):
#         for w in range(width):
#             pyautogui.moveTo(w, h)
#             # 186,247,0
#             R, G, B = screen.getpixel(pyautogui.position()) # R,G,B 색상표 얻기 
#             if (R>= 186 and G >=  247 and B >= 0) and (R< 200 and G < 300 and B>0): 
#                 # 회색 범위 탐색 성공하면 
#                 pyautogui.click() # 클릭하기
#                 print("clicked: [" +str(R)+","+str(G)+","+str(B)+"]") 
#                 stop_flag = True # 종료 조건 충족 
out_flag = False
for i in range(1, height//2, 10):
    for j in range(1, width//2, 10):
        pyautogui.moveTo(j, i)
        screen = ImageGrab.grab() # 화면 캡쳐 
        R, G, B = screen.getpixel(pyautogui.position()) # R,G,B 색상표 얻기
        if (R>= 186 and G >=  247 and B >= 0) and (R< 200 and G < 300 and B>0): 
            pyautogui.click() # 클릭하기
            print("clicked: [" +str(R)+","+str(G)+","+str(B)+"]") 
            out_flag = True
            break
    if out_flag:
        break
print("finished")

