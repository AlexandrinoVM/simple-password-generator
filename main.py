import PySimpleGUI as sg 
import random

class generate_password():
    def __init__(self):
        
            sg.theme('DarkAmber') 
            
            layout = [
                    [sg.Text('generate password',size=(250,1), font="Arial 12",justification='c')],
                    [sg.Text('size', font="Arial 12"),sg.Combo(values=list(range(8,25)),key='size-password', font="Arial 12",default_value=8)],
                    [sg.Text('complexity', font="Arial 12"),sg.Combo(self.complexity(),default_value='medium', font="Arial 12",size=(15,30),key='complexity')],
                    [sg.Output(size=(32,5))],
                    [sg.Button('generate', font="Arial 12")]
            ]

            self.window = sg.Window('password generator',layout,size=(500,300),element_justification='c')
    def complexity(self):
         return ['weak','medium','strong']

    def window_init(self):
        while True:
            event,values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'generate':
                newpass = self.generatepass(values)
                print(newpass)
       

    def generatepass(self,value):
         
        nums = '123456789'
        digts = '!@#$%&*()-+*-,:;'
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        if value['complexity'] == 'weak':
            char =random.choices(chars,k=int(value['size-password']))
            
            newpass = ''.join(char)
         
        elif value['complexity'] == 'medium':
            
            mediumpass = chars + nums
            char =random.choices(mediumpass,k=int(value['size-password']))
             
            newpass = ''.join(char)
        
        else:
            
            strongpass = nums + digts + chars
            char =random.choices(strongpass,k=int(value['size-password']))
             
            newpass = ''.join(char)

        return newpass

passw = generate_password()
passw.window_init()

