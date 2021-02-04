# Single comment-out are for the first program, second comment-out is for second program, and third comment-out is for third program
#4th comment-out is for the last program
from guizero import App, Text, Picture, Box, PushButton
from gpiozero import LED, Button

# def mainfunc():
#     app = App(title="Command & Conquer Tiberian Sun",
#             width=800, 
#             height=600,)
#     app.display()
#     return

# # def secondfunc():
# #     app.bg = "#000000" #light gray, you may set the colour you want
# #     app.width = 1280
# #     app.height= 740
# #     wanted_text = Text(app, "Welcome back Commander...")
# #     wanted_text.text_size = 12
# #     wanted_text.font = "Times New Roman"
# #     wanted_text.text_color = "#ff0000"
# #     cat = Picture(app, image="Lighting1.png")
# #     app.when_closed = close_app
# #     #app.on_close(close_input = app.yesno("Close","Do you want to quit?"))
# #     return app
# # 
# # def close_app():
# #     if app.yesno("Close","Do you want to quit?"):
# #         app.destroy()
# #     return

# # # def do_nothing():
# # #     return 0

# # # # led26 = LED(26)
# # # # def GPIO_26():
# # # #     if button1.text == "GPIO26_ON ":
# # # #         button1.text ="GPIO26_OFF"
# # # #         led26.on()
# # # #     else:
# # # #         button1.text="GPIO26_ON "
# # # #         led26.off()

button = Button(20)
led = LED(26)

def scanInput():
    if button.is_pressed:
        text.value = 1 #"GPIO2 ON "
        led.on()
    else:
        text.value = 0 #"GPIO2 OFF"
        led.off()
def exitGUI():
    text.destroy()
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        print("Adios")
    return

if __name__ == '__main__': 
#     mainfunc()
    
# #     app = App("Command & Conquer Tiberian Sun")
# #     app2 = secondfunc()
# #     app.display(app2)

# # #     app = App(title="My app", height=300, width=300, layout="grid")
# # #     text = Text(app, text="Some text here", grid=[0,0])
# # #     box = Box(app, layout="grid", grid=[1,0])
# # #     
# # #     button1 = PushButton(box, command=do_nothing, text="1", grid=[0,0])
# # #     button2 = PushButton(box, command=do_nothing, text="2", grid=[1,0])
# # #     button3 = PushButton(box, command=do_nothing, text="3", grid=[2,0])
# # #     button4 = PushButton(box, command=do_nothing, text="4", grid=[0,1])
# # #     button5 = PushButton(box, command=do_nothing, text="5", grid=[1,1])
# # #     button6 = PushButton(box, command=do_nothing, text="6", grid=[2,1])
# # #     app.display()

# # # #     app = App("Activation GPIO")
# # # #     
# # # #     button1 = PushButton(app, command=GPIO_26, text="GPIO26_ON ")
# # # #     app.display()
# # # #     led26.off()

    app = App("Reading GPIO")
    text = Text(app, text="1")
    text.repeat(10, scanInput) # Schedule call to scan GPIO input every
    app.when_closed = exitGUI
    app.display()
