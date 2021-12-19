#Перед работой приложения необходимо написать в терминале
#pip install kivy
#pip install kivymd
#pip install https://github.com/kivymd/KivyMD/archive/3274d62.zip

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu



KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "logo.png"

    MDLabel:
        text: app.tittle
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Физика"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Время"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            OneLineListItem:
                text: "Память"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Калькулятор ЕИ"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                BoxLayout:
                    orientation: 'vertical'
                    padding: "10dp"   
                                
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-down-bold"
                                        
                        MDTextField:
                            hint_text: "remake"
                            
                    BoxLayout:
                        orientation: 'horizontal'                         
                                    
                        MDIconButton:
                            icon: "speedometer"
                                        
                        MDTextField:
                            id: speed1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Введите СИ"
                            on_focus: if self.focus: app.menu.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                                
                                    
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            hint_text: "Months"
                    
                    BoxLayout:
                        orientation: 'horizontal'                                
                                    
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            hint_text: "Months"
                                    

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
            
            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: "Screen 3"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

metres=['mile','yard','foot','inch','km','m','cm','mm']
long=0

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class Calculator(MDApp):
    tittle = "Калькулятор ЕИ"
    by_who = "by MrDark"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": metres[i],
                "on_release": lambda x=metres[i]: self.set_item(x),
            } for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.speed1,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )

    def set_item(self, text__item):
        self.screen.ids.speed1.text = text__item
        self.menu.dismiss()


    def build(self):
        #return Builder.load_string(KV)
        return self.screen





Calculator().run()
