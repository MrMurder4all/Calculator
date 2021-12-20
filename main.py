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
                text: "Память"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6"
            

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
                            icon: "ruler"
                                        
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
                            id: square_input
                            hint_text: "Введите площадь"
                            
                    BoxLayout:
                        orientation: 'horizontal'                         
                                    
                        MDIconButton:
                            icon: "ruler-square"
                                        
                        MDTextField:
                            id: square1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Исходная СИ"
                            on_focus: if self.focus: app.menu_square1.open()
                        
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            id: square2
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Конечная СИ"
                            on_focus: if self.focus: app.menu_square2.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-up-bold"
                                        
                        MDTextField:
                            id: square_output
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
                                on_release: app.calc_table_square(*args)
            
            MDScreen:
                name: "scr 4"

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
                            icon: "glass-pint-outline"
                                        
                        MDTextField:
                            id: volume1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Исходная СИ"
                            on_focus: if self.focus: app.menu_volume1.open()
                        
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            id: volume2
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Конечная СИ"
                            on_focus: if self.focus: app.menu_volume2.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-up-bold"
                                        
                        MDTextField:
                            id: volume_output
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
                                on_release: app.calc_table_volume(*args)
            
            MDScreen:
                name: "scr 5"

                BoxLayout:
                    orientation: 'vertical'
                    padding: "10dp"   
                                
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-down-bold"
                                        
                        MDTextField:
                            id: time_input
                            hint_text: "Введите время"
                            
                    BoxLayout:
                        orientation: 'horizontal'                         
                                    
                        MDIconButton:
                            icon: "history"
                                        
                        MDTextField:
                            id: time1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Исходная СИ"
                            on_focus: if self.focus: app.menu_time1.open()
                        
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            id: time2
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Конечная СИ"
                            on_focus: if self.focus: app.menu_time2.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-up-bold"
                                        
                        MDTextField:
                            id: time_output
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
                                on_release: app.calc_table_time(*args)
            
            MDScreen:
                name: "scr 6"

                BoxLayout:
                    orientation: 'vertical'
                    padding: "10dp"   
                                
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-down-bold"
                                        
                        MDTextField:
                            id: data_input
                            hint_text: "Введите объем памяти"
                            
                    BoxLayout:
                        orientation: 'horizontal'                         
                                    
                        MDIconButton:
                            icon: "folder"
                                        
                        MDTextField:
                            id: data1
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Исходная СИ"
                            on_focus: if self.focus: app.menu_data1.open()
                        
                        MDIconButton:
                            icon: "arrow-collapse-right"
                                            
                        MDTextField:
                            id: data2
                            size_hint_x: None
                            width: "200dp"
                            hint_text: "Конечная СИ"
                            on_focus: if self.focus: app.menu_data2.open()
                                    
                    BoxLayout:
                        orientation: 'horizontal'                               
                                    
                        MDIconButton:
                            icon: "arrow-up-bold"
                                        
                        MDTextField:
                            id: data_output
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
                                on_release: app.calc_table_data(*args)

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

square = ['м²','мм²','см²','гектары','км²','дюймы²','футы²','акры']
square_num = [1,0.000001,0.0001,10000,1000000,0.000645,0.092903,4046.856]

volume=['мл','л','куб. м','пинты(США)','кварт(США)','галлоны(США)','куб. дюймы','куб. футы','куб. ярды']
volume_num = [0.001,1,1000,0.473176,0.946353,3.785412,0.016387,28.31685,764.5549]

time = ['микро с','мс','с','мин','ч','дни','недели','г']
time_num = [0.000001,0.001,1,60,3600,86400,604800,31557600]

data = ['бит','Байт','КБ','МБ','ГБ','ТБ']
data_num = [1/8192,1/1024,1,1024,1048576,1073741824]




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

        menu_square1_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": square[i],
                "on_release": lambda x=square[i]: self.set_square1(x),
            } for i in range(len(square))]
        self.menu_square1 = MDDropdownMenu(
            caller=self.screen.ids.square1,
            items=menu_square1_items,
            position="bottom",
            width_mult=4,
        )

        menu_square2_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": square[i],
                "on_release": lambda x=square[i]: self.set_square2(x),
            } for i in range(len(square))]
        self.menu_square2 = MDDropdownMenu(
            caller=self.screen.ids.square2,
            items=menu_square2_items,
            position="bottom",
            width_mult=4,
        )

        menu_volume1_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": volume[i],
                "on_release": lambda x=volume[i]: self.set_volume1(x),
            } for i in range(len(volume))]
        self.menu_volume1 = MDDropdownMenu(
            caller=self.screen.ids.volume1,
            items=menu_volume1_items,
            position="bottom",
            width_mult=4,
        )

        menu_volume2_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": volume[i],
                "on_release": lambda x=volume[i]: self.set_volume2(x),
            } for i in range(len(volume))]
        self.menu_volume2 = MDDropdownMenu(
            caller=self.screen.ids.volume2,
            items=menu_volume2_items,
            position="bottom",
            width_mult=4,
        )

        menu_time1_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": time[i],
                "on_release": lambda x=time[i]: self.set_time1(x),
            } for i in range(len(time))]
        self.menu_time1 = MDDropdownMenu(
            caller=self.screen.ids.time1,
            items=menu_time1_items,
            position="bottom",
            width_mult=4,
        )

        menu_time2_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": time[i],
                "on_release": lambda x=time[i]: self.set_time2(x),
            } for i in range(len(time))]
        self.menu_time2 = MDDropdownMenu(
            caller=self.screen.ids.time2,
            items=menu_time2_items,
            position="bottom",
            width_mult=4,
        )

        menu_data1_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": data[i],
                "on_release": lambda x=data[i]: self.set_data1(x),
            } for i in range(len(data))]
        self.menu_data1 = MDDropdownMenu(
            caller=self.screen.ids.data1,
            items=menu_data1_items,
            position="bottom",
            width_mult=4,
        )

        menu_data2_items = [
            {
                "viewclass": "IconListItem",
                "height": dp(56),
                "text": data[i],
                "on_release": lambda x=data[i]: self.set_data2(x),
            } for i in range(len(data))]
        self.menu_data2 = MDDropdownMenu(
            caller=self.screen.ids.data2,
            items=menu_data2_items,
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

    def set_square1(self, text__item):
        self.screen.ids.square1.text = text__item
        self.menu_square1.dismiss()

    def set_square2(self, text__item):
        self.screen.ids.square2.text = text__item
        self.menu_square2.dismiss()

    def set_volume1(self, text__item):
        self.screen.ids.volume1.text = text__item
        self.menu_volume1.dismiss()

    def set_volume2(self, text__item):
        self.screen.ids.volume2.text = text__item
        self.menu_volume2.dismiss()

    def set_time1(self, text__item):
        self.screen.ids.time1.text = text__item
        self.menu_time1.dismiss()

    def set_time2(self, text__item):
        self.screen.ids.time2.text = text__item
        self.menu_time2.dismiss()

    def set_data1(self, text__item):
        self.screen.ids.data1.text = text__item
        self.menu_data1.dismiss()

    def set_data2(self, text__item):
        self.screen.ids.data2.text = text__item
        self.menu_data2.dismiss()

    def calc_table_speed(self, *args):
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
        metrics1 = self.screen.ids.length1.text
        input = float(self.screen.ids.length_input.text)
        metrics2 = self.screen.ids.length2.text

        for i in range(0, len(length)):
            if metrics1 == length[i]:
                input = input * length_num[i]
            if metrics2 == length[i]:
                input = input / length_num[i]
        self.screen.ids.length_output.text = str(input)

    def calc_table_square(self, *args):
        metrics1 = self.screen.ids.square1.text
        input = float(self.screen.ids.square_input.text)
        metrics2 = self.screen.ids.square2.text

        for i in range(0, len(square)):
            if metrics1 == square[i]:
                input = input * square_num[i]
            if metrics2 == square[i]:
                input = input / square_num[i]
        self.screen.ids.square_output.text = str(input)

    def calc_table_volume(self, *args):
        metrics1 = self.screen.ids.volume1.text
        input = float(self.screen.ids.volume_input.text)
        metrics2 = self.screen.ids.volume2.text

        for i in range(0,len(volume)):
            if metrics1 == volume[i]:
                input = input * volume_num[i]
            if metrics2 == volume[i]:
                input = input / volume_num[i]
        self.screen.ids.volume_output.text = str(input)

    def calc_table_time(self, *args):
        metrics1 = self.screen.ids.time1.text
        input = float(self.screen.ids.time_input.text)
        metrics2 = self.screen.ids.time2.text

        for i in range(0, len(time)):
            if metrics1 == time[i]:
                input = input * time_num[i]
            if metrics2 == time[i]:
                input = input / time_num[i]
        self.screen.ids.time_output.text = str(input)

    def calc_table_data(self, *args):
        metrics1 = self.screen.ids.data1.text
        input = float(self.screen.ids.data_input.text)
        metrics2 = self.screen.ids.data2.text

        for i in range(0, len(data)):
            if metrics1 == data[i]:
                input = input * data_num[i]
            if metrics2 == data[i]:
                input = input / data_num[i]
        self.screen.ids.data_output.text = str(input)


    def build(self):
        #return Builder.load_string(KV)
        return self.screen


Calculator().run()
