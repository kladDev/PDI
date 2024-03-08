import cv2
from random import randint

capture = cv2.VideoCapture("video.mp4")

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv2.CAP_PROP_FPS))

pos_x = -1
pos_y = -1
circle_positions = [] 

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS = [BLUE, GREEN, RED, BLACK, GRAY]
c = 0

def draw_circle(event, x, y, flags, param):
    global pos_x 
    global pos_y
    global c

    if event == cv2.EVENT_LBUTTONDOWN:
        pos_x = x 
        pos_y = y
        circle_positions.append((x, y, c))

def draw_circle_onscreen(frame):
    for x, y, c in circle_positions:
        cv2.circle(frame,(x,y),3,COLORS[c],-1)

cv2.namedWindow('Vídeo com Círculos')
cv2.setMouseCallback('Vídeo com Círculos', draw_circle)

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("video_cinza.avi", fourcc, int(fps), (int(frame_width), int(frame_height)), False)
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            output.write(frame)
            draw_circle_onscreen(frame)
            cv2.imshow('Vídeo com Círculos', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            if cv2.waitKey(20) & 0xFF == ord('c'):
                c = randint(0,len(COLORS)-1)
        else:
            break

capture.release()   
output.release()
cv2.destroyAllWindows()