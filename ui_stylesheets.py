
class Styles:

    def actionbutton(self):
        self.styleref = '''
            QPushButton {
                color:rgb(86,85,85);
                background-color:rgb(154,250,230);
                border-radius: 10px;
                font: bold 14px;
                min-width: 5em;
                padding: 6px;
            }
            QPushButton:hover {
                color:rgb(86,85,85);
                background-color:rgb(114, 185, 170);
                border-radius: 10px;
                font: bold 14px;
                min-width: 5em;
                padding: 6px;
            }
        '''

        return self.styleref

    def additionbutton(self):
        self.styleref = '''
            QPushButton {
                color:rgb(86,85,85);
                background-color:rgb(154,250,230);
                border-radius: 10px;
                font: 9px;
                min-width: 5em;
                padding: 6px;
            }
            QPushButton:hover {
                color:rgb(86,85,85);
                background-color:rgb(114, 185, 170);
                border-radius: 10px;
                font: 9px;
                min-width: 5em;
                padding: 6px;
            }
        '''

        return self.styleref

    def cancelbutton(self):
        self.styleref = '''
        QPushButton {
            color:rgb(4,255,203);
            background-color:rgb(151,150,150);
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 5em;
            padding: 6px;
        }
        QPushButton:hover{
            color:rgb(4,255,203);
            background-color:rgb(151,200,200);
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 5em;
            padding: 6px;
        }
        '''

        return self.styleref

    def listview(self):
        self.styleref = '''
        background-color:white;
        color:rgb(86,85,85);
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        '''

        return self.styleref

    def windowbackground(self):
        self.styleref = '''
        background-color:rgb(86,85,85);
        color:white;
        '''

        return self.styleref

    def groupbox(self):
        self.styleref = '''
        color:rgb(4,255,203);
        background-color: transparent; 
        border: 1px solid white; 
        border-radius: 5px; 
        margin-top: 1px;        
        '''

        return self.styleref

    def combobox(self):
        self.styleref = '''
                background-color:white;
        color:rgb(86,85,85);
        border-width: 1px;
        border-radius: 5px;
        '''

        return self.styleref


    def bodytext(self):
        self.styleref='''
        color:rgb(154,250,230);
        font-size:18;
        border:none;
        '''

        return self.styleref

    def headingtextbold(self):
        self.styleref= '''
        color:rgb(154,250,230);
        font-weight:bold;
        '''

        return self.styleref