from appJar import gui

app = gui("Tip Calculator")

app.addLabel("title", "Tip Calculator")
app.setLabelBg("title", "red")


def press(button):
    app.removeAllWidgets()
    if button == "Bill":
        app.addLabel("billLab", "Bill Amount:", 0, 0)
        app.addEntry("billEnt", 0, 1)
        app.addLabel("splitLab", "Number of splits:", 1, 0)
        app.addEntry("splitEnt", 1, 1)
    else:
        app.stop()


app.addButton("Bill", press)


app.go()