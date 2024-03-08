from formcreator import mainForm

def SetDateIn():
    print(mainForm.dateEditIn.dateTime().toString('dd.MM.yyyy'))

def SetDateOut():
    print(mainForm.dateEditOut.dateTime().toString('dd.MM.yyyy'))