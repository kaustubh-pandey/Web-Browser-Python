#!/usr/bin/env python
import gtk,webkit

def go_button(widget):
	add=addressBar.get_text()
	#Check for HTTPS
	if(add.startswith("https://")==False):
		add="https://"+add
	addressBar.set_text(add)
	web.open(add)
	

win=gtk.Window()
win.set_default_size(1200,600)
win.set_title("KROMIUM- BY KAUSTUBH")
win.connect('destroy',lambda w:gtk.main_quit())
#Addded a close button

box1=gtk.VBox()
win.add(box1)

box2=gtk.HBox()
box1.pack_start(box2,False)

addressBar=gtk.Entry()
box2.pack_start(addressBar)

gobutton=gtk.Button("GO")
box2.pack_start(gobutton,False)
gobutton.connect('clicked',go_button)

scroller=gtk.ScrolledWindow()
box1.pack_start(scroller)

web=webkit.WebView()
scroller.add(web)

win.show_all()
gtk.main()
