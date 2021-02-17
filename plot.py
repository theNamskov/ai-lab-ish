from tkinter import *

from payload import payload

INTERVAL = 20
UPPER_BOUNDARY = 200
ORIGIN_Y = 560
ORIGIN_X = 140
TERMINAL_Y = 140
TERMINAL_X = 560
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600
POINT_WIDTH = 6
COORDINATES_RANGE = 11


def point_mapper(x, y):
    return ((ORIGIN_X + ((x/UPPER_BOUNDARY)*(TERMINAL_X-ORIGIN_X)-2), ORIGIN_Y - ((y/UPPER_BOUNDARY)*(ORIGIN_Y-TERMINAL_Y-20))))


def drawPlot(dataList, app, payload=None):
    canvas = Canvas(app, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
    canvas.pack()

    canvas.create_line(ORIGIN_X, ORIGIN_Y, TERMINAL_X, ORIGIN_Y, width=1)
    canvas.create_line(ORIGIN_X, ORIGIN_Y, ORIGIN_X, TERMINAL_Y,  width=1)

    # markings on x axis
    for i in range(COORDINATES_RANGE):
        x = ORIGIN_X + (i * INTERVAL*2)
        canvas.create_line(x,ORIGIN_Y+10,x,TERMINAL_Y, width=1)
        canvas.create_text(x,ORIGIN_Y+20, text='%d'% (INTERVAL*i), anchor=N)

    # markings on y axis
    for i in range(COORDINATES_RANGE):
        y = ORIGIN_Y - (i * INTERVAL*2)
        canvas.create_line(ORIGIN_X-20, y, TERMINAL_X, y, width=1)
        canvas.create_text(ORIGIN_X-34, y, text='%5.1f'% (INTERVAL*i), anchor=E)

    for (xs,ys) in dataList:
        canvas.create_oval(xs-POINT_WIDTH,ys-POINT_WIDTH,xs+POINT_WIDTH,ys+POINT_WIDTH, width=1,
                           outline='black', fill='SkyBlue2')
    
    if payload is not None:
        for data in payload:
            start_x, start_y = point_mapper(data.get('x'), data.get('y'))
            end_x, end_y = point_mapper(data.get('to_x'), data.get('to_y'))
            canvas.create_line(start_x, start_y, end_x, end_y, width=3)

    
    app.mainloop()
    

def main():

    if __name__ != '__main__':
        return
     
    scaledDataList = []
    for data in payload:
        scaledDataList.append(point_mapper(data.get('x'), data.get('y')))
    
    app = Tk()
    app.title('AI Lab')

    drawPlot(scaledDataList, app, payload)

main()