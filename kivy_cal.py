from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#Set the app size

Window.size = (400,600)

#Designate Our .kv design file

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self): 
        self.ids.calc_input.text='0'

    # Remove function
    def remove(self):
        prior=self.ids.calc_input.text
        prior=prior[:-1]
        self.ids.calc_input.text=prior

        if prior=="":
            self.ids.calc_input.text='0'

    # Create a button pressing function
    def button_press(self, button):
        # Create a variable to store the privious value of text box
        prior = self.ids.calc_input.text
        
        # Test for error first
        if "Error" in prior:
            prior=''
        # Determine if 0 is there
        if prior =="0":
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'   

        else:
            self.ids.calc_input.text= f'{prior}{button}'   

    # Addition function
    def sign(self, sign):

        prior = self.ids.calc_input.text
        # print(prior)
        # Test for error first
        if "Error" in prior or "0" in prior:
            prior=''
        
        try:
            if prior[-1]=="+" or prior[-1]=="/" or (prior[-1]=="*" and sign!="*" and prior[-2]!="*") or (prior[-1]=="-" and sign!="-" and prior[-2]!="-"):
                prior=prior[:-1]
                self.ids.calc_input.text=prior
        
        except:
            pass
        print(prior[-2:])
        if prior=="-" and sign=="+":
            prior=prior[:-1]
            self.ids.calc_input.text=prior
            self.ids.calc_input.text= f'{prior}{sign}'
        if (prior[-2:]=="--" and sign!="-") or (prior[-2:]=="**" and sign!="*"):
            print("in")
            prior=prior[:-2]
            self.ids.calc_input.text=f'{prior}{sign}'
        
        elif (prior[-2:]=="--") or (prior[-2:]=="**"):
            pass
            # print("in")
            # prior=prior[:-2]
            # self.ids.calc_input.text=f'{prior}{sign}'


        else:
            self.ids.calc_input.text=f'{prior}{sign}'


    # Dot Function
    def dot(self):
        prior=self.ids.calc_input.text
        
        # Split text box by +
        num_list= prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text=prior

        elif "." in prior:
            pass
        else:
            prior=f'{prior}.'
            self.ids.calc_input.text=prior

    # Equals function
    def equals(self):
        prior=self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text="Error"
    # Make text box positive or negetive function
    def pos_neg(self):
        prior=self.ids.calc_input.text

        if "-" in prior:
            self.ids.calc_input.text=f'{prior.replace("-", "")}'
        
        else:
            self.ids.calc_input.text=f'-{prior}'



class CalculatorApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == '__main__':
    CalculatorApp().run()