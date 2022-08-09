import os

import kivy
from kivy.app import App
from kivy.uix.label import Label # Imports Label element
from kivy.uix.boxlayout import BoxLayout # Imports layout call function which pulls from .kv file with the same name as the class that calls it
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.accordion import Accordion, AccordionItem

import random

# Test
# Internals 
from standardization import getGenericName
import drugstandards
from check_drug import checkDrug, checkInterac



class RootLayout(BoxLayout): # Constructs a UI element based on the kivy BoxLayout class 
    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs) # Calls the superconstructor 
        self.cur_text = ""

    def getGeneric(self):
        text_in: str = self.text_in1.text
        print(text_in)
        generic = getGenericName(text_in)
        self.display_label.text = generic
        pass
    
    def checkBeers(self):
        accordion: Accordion = self.ids.accordion # Use element with "accordion" id (doesn't need to be bound) to assign ScrollView object
        scroll_view: ScrollView = self.ids.scroll_view
        text_in: str = self.text_in1.text
        if "\n" in text_in:
            print("Newline character detected")
        drugs = text_in.split("\n")     
        print("Input texts: ", drugs)
        drugs_std = [drugstandards.standardize([d])[0] for d in drugs]
        drugs_std = [d for d in drugs_std if d] # Filter empty data types
        drugs_std = list(set(drugs_std)) # Screen out duplicates
        print("Standardized: ", drugs_std)
        
        accordion.clear_widgets() # Clear widgets before adding
        ac_item = AccordionItem(title=f"{len(drugs_std)} standardized drugs found")
        label = Label(text=f"{drugs_std} j a;ldkf laksj;d flakjsd;f lkaj;oeifjwapoifjp aodi faposidjfpaoijsdpfo aiwjpe foijwap oefijap oifjpa sodfo;wjae;lkjfoisjdpfo aijpeoqi awjepsofi japsoidjf paoisdfp o;kja;owijv opaoijdsoijafo wiejfp aiwjfp aks;dlkfj; awijefpo a",
                      halign='left',
                    #   text_size=(scroll_view.width, None),
                      )
        label = Label(text='blah blah '* 1000, size_hint=(1, None))
        a = lambda *x: label.setter('text_size')
        b = lambda *x: label.setter('text_size')(label, (label.width, None))
        label.bind(width=lambda *x: label.setter('text_size')(label, (label.width, None)),
        texture_size=lambda *x: label.setter('height')(label, label.texture_size[1]))
        ac_item.add_widget(label)
        accordion.add_widget(ac_item)
        
        report = f"======Drug Screen======\nDrugs detected: {drugs_std}\n"
        for drug in drugs_std:
            drug_warning = checkDrug(drug, std=False)
            if drug_warning:
                report += drug_warning + "\n---------------------\n" # Disable standardization to save computation
        report += "======Interactions======\n"
        report += checkInterac(drugs_std, std=False)
        # self.ids.display_label.text = report
        
    def checkBeers1(self):
        accordian: Accordion = self.ids.accordion # Use element with "accordion" id (doesn't need to be bound) to assign ScrollView object
        for i in range(5):
            ac_item = AccordionItem(title=f"Accordian item {i}")
            ac_item.add_widget(Label(text=f"Some content of {i}"))
            accordian.add_widget(ac_item)
        print(self.ids.accordion)
        







class BeersApp(App): 
    """
    This class inherits the App class from kivy
    The name of this class will also determine the name of the .kv files (for layout/design)
    .kv file name is not case-sensitive to the class name but should be all lowercase to avoid issues
    .kv file name can exclude "App" portion of App class identifier
    """
    
    def build(self): # Returns the UI
        root = RootLayout()
        return root # Return whatever root element you are using for the UI
        


app_instance = BeersApp() # Creates instance of the app
app_instance.run() # Runs the instance of the app 
