# cd Users\MP\OneDrive - Miami Dade College\7-Summer2022\Internships\SRI\application>py kivycourse.py
#change font is on time stamp: 1:18:12 of 5:41:25 (custom font) it is a cool one

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
import socketio
from time import sleep
#class BozLayoutExample(BowxLayout):
#	def __init__(self, **kwargs):


class MainWidget(Widget):
	my_text=StringProperty("hi!")
	def on_buttonup_click(self):	
		print("Button up clicked")
		
		self.my_text= "You clicked, so I send a string to the app"
	
	count=0
	count_text = StringProperty("0")
	def on_buttondown_click(self):
		print("Button down clicked")
		self.count+= 1
		self.count_text=str(self.count)
		

	def on_buttonleft_click(self):
		print("Button left clicked")

	def on_buttonright_click(self):
		print("Button right clicked")
		
	def on_buttonhome_click(self):
		print("Button home clicked")

	#toggle button function

	#def on_toggle_button_state(self, widget):
	#	print("toggle state"+ widget.state)


class kivy_mobileapp(App):
	pass

kivy_mobileapp().run()
