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
                text: "Скорость"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Расстояние"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                    
            OneLineListItem:
                text: "Площадь"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
            
            OneLineListItem:
                text: "Объем"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"
            
            OneLineListItem:
                text: "Время"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5"
            
            OneLineListItem:
                text: "Температура"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6"
            
            OneLineListItem:
                text: "Давление"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 7"
            
            OneLineListItem:
                text: "Память"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 8"
            
            
            
            


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
                            id: speed_input
                            hint_text: "Введите скорость"
                            
                    BoxLayout:
                        orientation: 'horizontal'                         
                                    
                        MDIconButton:
                            icon: "speedometer"
                                        
                        MDTextField:
                            id: speed1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Исходная СИ"
                            on_focus: if self.focus: app.menu.open()
                        
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            id: speed2
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Конечная СИ"
                            on_focus: if self.focus: app.menu2.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-up-bold"
                                        
                        MDTextField:
                            id: speed_output
                            hint_text: "Итог"
                        
                    BoxLayout:
                        orientation: 'horizontal'
                                    
                        AnchorLayout:
                            anchor_x: 'center'
                                
                            MDRectangleFlatIconButton:
                                icon: "adjust"
                                text: "Рассчет"
                                theme_text_color: "Custom"
                                text_color: 0, 0, 0, 1
                                line_color: 0, 0, 0, 1
                                icon_color: 0, 1, 0, 1
                                md_bg_color: 0.1, 0.1, 0.1, 1
                                adaptive_width: True
                                on_release: app.calc_table_speed(*args)
                                    

            MDScreen:
                name: "scr 2"
                
                BoxLayout:
                    orientation: 'vertical'
                    padding: "10dp"   
                                
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-down-bold"
                                        
                        MDTextField:
                            id: length_input
                            hint_text: "Введите длину"
                            
                    BoxLayout:
                        orientation: 'horizontal'                         
                                    
                        MDIconButton:
                            icon: "speedometer"
                                        
                        MDTextField:
                            id: length1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Исходная СИ"
                            on_focus: if self.focus: app.menu_length1.open()
                        
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            id: length2
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Конечная СИ"
                            on_focus: if self.focus: app.menu_length2.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-up-bold"
                                        
                        MDTextField:
                            id: length_output
                            hint_text: "Итог"
                        
                    BoxLayout:
                        orientation: 'horizontal'
                                    
                        AnchorLayout:
                            anchor_x: 'center'
                                
                            MDRectangleFlatIconButton:
                                icon: "adjust"
                                text: "Рассчет"
                                theme_text_color: "Custom"
                                text_color: 0, 0, 0, 1
                                line_color: 0, 0, 0, 1
                                icon_color: 0, 1, 0, 1
                                md_bg_color: 0.1, 0.1, 0.1, 1
                                adaptive_width: True
                                on_release: app.calc_table_length(*args)
            
            MDScreen:
                name: "scr 3"

                BoxLayout:
                    orientation: 'vertical'
                    padding: "10dp"   
                                
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-down-bold"
                                        
                        MDTextField:
                            id: volume_input
                            hint_text: "Введите площадь"
                            
                    BoxLayout:
                        orientation: 'horizontal'                         
                                    
                        MDIconButton:
                            icon: "speedometer"
                                        
                        MDTextField:
                            id: length1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Исходная СИ"
                            on_focus: if self.focus: app.menu_length1.open()
                        
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            id: length2
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Конечная СИ"
                            on_focus: if self.focus: app.menu_length2.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-up-bold"
                                        
                        MDTextField:
                            id: length_output
                            hint_text: "Итог"
                        
                    BoxLayout:
                        orientation: 'horizontal'
                                    
                        AnchorLayout:
                            anchor_x: 'center'
                                
                            MDRectangleFlatIconButton:
                                icon: "adjust"
                                text: "Рассчет"
                                theme_text_color: "Custom"
                                text_color: 0, 0, 0, 1
                                line_color: 0, 0, 0, 1
                                icon_color: 0, 1, 0, 1
                                md_bg_color: 0.1, 0.1, 0.1, 1
                                adaptive_width: True
                                on_release: app.calc_table_length(*args)

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
speeds = ['км/ч','м/с','км/с','км/мин','м/ч','м/мин','футы/с','миль/ч']
speed_num = [1,3.6,3600,60,0.001,0.06,1.09728,1.6092]
length = ['mile','yard','foot','inch','km','m','cm','mm']
length_num = [1609.344,0.9144,0.3048,0.0254,1000,1,0.01,0.001]
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
                "text": speeds[i],
                "on_release": lambda x=speeds[i]: self.set_speed1(x),
            } for i in range(len(speeds))]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.speed1,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )

        menu2_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": speeds[i],
                "on_release": lambda x=speeds[i]: self.set_speed2(x),
            } for i in range(len(speeds))]
        self.menu2 = MDDropdownMenu(
            caller=self.screen.ids.speed2,
            items=menu2_items,
            position="bottom",
            width_mult=4,
        )

        menu_length1_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": length[i],
                "on_release": lambda x=length[i]: self.set_length1(x),
            } for i in range(len(length))]
        self.menu_length1 = MDDropdownMenu(
            caller=self.screen.ids.length1,
            items=menu_length1_items,
            position="bottom",
            width_mult=4,
        )

        menu_length2_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": length[i],
                "on_release": lambda x=length[i]: self.set_length2(x),
            } for i in range(len(length))]
        self.menu_length2 = MDDropdownMenu(
            caller=self.screen.ids.length2,
            items=menu_length2_items,
            position="bottom",
            width_mult=4,
        )


    def set_speed1(self, text__item):
        self.screen.ids.speed1.text = text__item
        self.menu.dismiss()


    def set_speed2(self, text__item):
        self.screen.ids.speed2.text = text__item
        self.menu2.dismiss()

    def set_length1(self, text__item):
        self.screen.ids.length1.text = text__item
        self.menu_length1.dismiss()

    def set_length2(self, text__item):
        self.screen.ids.length2.text = text__item
        self.menu_length2.dismiss()

    def build(self):
        #return Builder.load_string(KV)
        return self.screen

    def calc_table_speed(self, *args):
        print("button1 pressed")
        metrics1 = self.screen.ids.speed1.text
        input = float(self.screen.ids.speed_input.text)
        metrics2 = self.screen.ids.speed2.text

        for i in range(0,len(speeds)):
            if metrics1 == speeds[i]:
                input = input * speed_num[i]
            if metrics2 == speeds[i]:
                input = input / speed_num[i]
        self.screen.ids.speed_output.text = str(input)

    def calc_table_length(self, *args):
        print("button1 pressed")
        metrics1 = self.screen.ids.length1.text
        input = float(self.screen.ids.length_input.text)
        metrics2 = self.screen.ids.length2.text

        for i in range(0, len(speeds)):
            if metrics1 == length[i]:
                input = input * length_num[i]
            if metrics2 == length[i]:
                input = input / length_num[i]
        self.screen.ids.length_output.text = str(input)






Calculator().run()
