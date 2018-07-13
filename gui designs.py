from appJar import gui

app = gui("","600x300")
app.setBg("Blue")
app.setFont(20)

def select(rb):
    print(app.getRadioButton("option"))
          
app.addRadioButton("option","Start Game")
app.addRadioButton("option","Game Only")
app.addRadioButton("option","Questions Only")
app.addRadioButton("option","Level Select")
app.addRadioButton("option","Exit")

app.setRadioButtonNew("option",select)
app.addButton("Enter",select)

app.go()

app.addCheckBox("ans")
app.addCheckBox("ans")
app.addCheckBox("ans")
app.addCheckBox("ans")

app.setCheckBox("ans", ticked=True, callFunction=True)


app = gui("Grid","1000x1000")
app.setSticky("Board")
app.setExpand("both")
app.setFont(26)

app.addLabel("l1",0,0)
app.addLabel("l2",0,1)
app.addLabel("l1",0,2)
app.addLabel("l1",0,3)
app.addLabel("l1",0,4)
app.addLabel("l1",0,5)
app.addLabel("l1",1,0)
app.addLabel("l1",1,1)
app.addLabel("l1",1,2)
app.addLabel("l1",1,3)
app.addLabel("l1",1,4)
app.addLabel("l1",1,5)
app.addLabel("l1",2,0)
app.addLabel("l1",2,1)
app.addLabel("l1",2,2)
app.addLabel("l1",2,3)
app.addLabel("l1",2,4)
app.addLabel("l1",2,5)
app.addLabel("l1",3,0)
app.addLabel("l1",3,1)
app.addLabel("l1",3,2)
app.addLabel("l1",3,3)
app.addLabel("l1",3,4)
app.addLabel("l1",3,5)
app.addLabel("l1",4,0)
app.addLabel("l1",4,1)
app.addLabel("l1",4,2)
app.addLabel("l1",4,3)
app.addLabel("l1",4,4)
app.addLabel("l1",4,5)
app.addLabel("l1",5,0)

for i in range(25):
    app




















app.go
