from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
import socketio
from time import sleep
#class BoxLayoutExample(BowxLayout):
#	def __init__(self, **kwargs):

#____________________________________________________________________
sio = socketio.Client()

@sio.event
def connect():
    print('Connection established with server to send message data.')

def send_msg(msg):
    print("sending")
    sio.emit('msg', msg)

@sio.event
def disconnect():
    print('Disconnected from websocket! Cannot send message data.')

sio.connect('ws://localhost:3000')
#___________________________________________________________________
class MainWidget(Widget):
	my_text=StringProperty("hi!")
	def on_buttonup_click(self):
		send_msg("Button up clicked")	
		print("Button up clicked")
		
		#self.my_text= "You clicked, so I send a string to the app"
	
	count=0
	count_text = StringProperty("0")
	def on_buttondown_click(self):
		send_msg("Button down clicked")
		print("Button down clicked")
		#self.count+= 1
		#self.count_text=str(self.count)
		

	def on_buttonleft_click(self):
		send_msg("Button left clicked")
		print("Button left clicked")

	def on_buttonright_click(self):
		send_msg("Button right clicked")
		print("Button right clicked")
		
	def on_buttonhome_click(self):
		send_msg("Button home clicked")
		sio.disconnect()
		print("Button home clicked")

	#toggle button function

	#def on_toggle_button_state(self, widget):
	#	print("toggle state"+ widget.state)


class kivy_mobileapp(App):
	pass

kivy_mobileapp().run()
