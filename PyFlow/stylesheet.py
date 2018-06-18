from Qt import QtGui
import inspect

class editableStyleSheet():
  def __init__(self):

    self.ORANGE1 =          QtGui.QColor(255, 160, 47)

    self.ORANGELIGHTER =    QtGui.QColor(234, 165, 83)
    self.ORANGELIGHTER2 =   QtGui.QColor(255, 170, 0)
    self.ORANGEDARKER =     QtGui.QColor(215, 128, 26)

    self.BG_DARK =          QtGui.QColor(50, 50, 50)
    self.BLACK =            QtGui.QColor(0, 0, 0)

    self.GREY =             QtGui.QColor(64, 64, 64)
    self.GREYLIGHT =        QtGui.QColor(177, 177, 177)
    self.GREYDARK =         QtGui.QColor(30, 30, 30)

    self.storeDeffaults()
  def storeDeffaults(self):
    for name,obj in inspect.getmembers(self):
      if isinstance(obj,QtGui.QColor):
        obj.default = obj.name()

  def setHue(self,hue):
    for name,obj in inspect.getmembers(self):
      if isinstance(obj,QtGui.QColor) and name in ["ORANGE1","ORANGELIGHTER","ORANGELIGHTER2","ORANGEDARKER"]:
        c = QtGui.QColor(obj.default)
        h,s,l,a = c.getHslF()
        obj.setHslF((h+hue)%1, s, l, a)

  def setBg(self,value):
    self.BG_DARK.setHslF(-1,0,value,1)



  def getStyleSheet(self):
    return """

QToolTip              {{   border: 1px solid black;
                          background-color: {0};
                          padding: 1px;
                          border-radius: 3px;
                          opacity: 100;               }}

QWidget               {{   color: {7};
                          background-color: {1};
                          border-radius: 3px;          }}

QWidget:disabled      {{   color: {6};
                          background-color: {1};   }}

QWidget:focus         {{   /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {2});*/  }}

QWidget:item:hover    {{   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {3});
                          color: {4};              }}

QWidget:item:selected {{   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {2});      }}

QMenuBar::item        {{   background: transparent;     }}

QMenuBar::item:selected
                      {{   background: transparent;
                          border: 1px solid {5};   }}

QMenuBar::item:pressed{{   background:  {6};
                          border: 1px solid {4};
                          background-color: QLinearGradient(  x1:0, y1:0,x2:0, y2:1,stop:1 #212121,stop:0.4 #343434/*,stop:0.2 #343434,stop:0.1 {5}*/);
                          margin-bottom:-1px;
                          padding-bottom:1px;          }}

QMenu                 {{   border: 1px solid {4};      }}

QMenu::item           {{   padding: 2px 20px 2px 20px;  }}

QMenu::item:selected  {{   color: {4};              }}

QMenu::separator      {{   height: 2px;
                          background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
                          color: white;
                          padding-left: 4px;
                          margin-left: 10px;
                          margin-right: 5px;           }}

QAbstractItemView     {{   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);   }}

QLineEdit             {{   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
                          padding: 1px;
                          border-style: solid;
                          border: 1px solid {8};
                          border-radius: 5;            }}
QToolButton:menu-button{{ 
                          color: none;
                          background-color: none;
                          border-style: none;
                          padding-top: 20px;
                          padding-right: 3px;
                           }}                        
QToolButton:menu-arrow:open {{
                          top: 1px; left: 1px; /* shift it a bit */
}}
QPushButton,QToolButton {{ color: {7};
                          background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
                          border-width: 1px;
                          border-color: {8};
                          border-style: solid;
                          border-radius: 6;
                          font-size: 12px;
                          padding: 3px;
                          padding-left: 5px;  padding-right: 5px; }}

QPushButton:pressed,QToolButton::pressed   {{   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525); }}

QComboBox             {{   selection-background-color: {5};
                          background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
                          border-style: solid;
                          border: 1px solid {8};
                          border-radius: 5;              }}
QPushButton:checked{{ 
                          background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
                          border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {2});
                          }}
QComboBox:hover,QPushButton:hover,QSpinBox:hover,QDoubleSpinBox:hover,QToolButton::hover 
                      {{   border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {2});  }}

QComboBox:on          {{   padding-top: 3px;
                          padding-left: 4px;
                          background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
                          selection-background-color: {5};    }}

QComboBox QAbstractItemView 
                      {{   border: 2px solid darkgray;
                          selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {2}); }}

QComboBox::drop-down  {{   subcontrol-origin: padding;
                          subcontrol-position: top right;
                          width: 15px;
                          border-left-width: 0px;
                          border-left-color: darkgray;
                          border-left-style: solid; /* just a single line */
                          border-top-right-radius: 3px; /* same radius as the QComboBox */
                          border-bottom-right-radius: 3px;      }}

QGroupBox             {{   border: 1px solid #9f988f;      }}

QScrollBar:horizontal {{   border: 1px solid #222222;
                          background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
                          height: 12px;
                          margin: 0px 16px 0 16px;        }}

QScrollBar::handle:horizontal
                      {{   background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 {0}, stop: 0.5 {2}, stop: 1 {0});
                          min-height: 20px;
                          border-radius: 2px;   }}

QScrollBar::add-line:horizontal 
                      {{   border: 1px solid #1b1b19;
                          border-radius: 2px;
                          background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 {0}, stop: 1 {2});
                          width: 14px;
                          subcontrol-position: right;
                          subcontrol-origin: margin;    }}

QScrollBar::sub-line:horizontal 
                      {{   border: 1px solid #1b1b19;
                          border-radius: 2px;
                          background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 {0}, stop: 1 {2});
                          width: 14px;
                          subcontrol-position: left;
                          subcontrol-origin: margin;     }}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
                      {{   background: none;             }}

QScrollBar:vertical   {{   background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
                          width: 12px;
                          margin: 16px 0 16px 0;
                          border: 1px solid #222222;    }}

QScrollBar::handle:vertical
                      {{   background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 0.5 {2}, stop: 1 {0});
                          min-height: 20px;
                          border-radius: 2px;           }}

QScrollBar::add-line:vertical
                      {{   border: 1px solid #1b1b19;
                          border-radius: 2px;
                          background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {2});
                          height: 14px;
                          subcontrol-position: bottom;
                          subcontrol-origin: margin;    }}

QScrollBar::sub-line:vertical
                      {{   border: 1px solid #1b1b19;
                          border-radius: 2px;
                          background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {2}, stop: 1 {0});
                          height: 14px;
                          subcontrol-position: top;
                          subcontrol-origin: margin;    }}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                      {{   background: none;             }}

QTextEdit             {{   background-color: #242424;    }}

QPlainTextEdit        {{   background-color: #242424;    }}

QHeaderView::section  {{   background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);
                          background-color: #505050;
                          color: white;
                          padding-left: 4px;
                          border-radius: 2px;
                          border: 1px solid #6c6c6c;  }}                       

QCheckBox:disabled    {{   color: #414141;             }}

QCheckBox::indicator  {{   color: {7};
                          background-color: {1};
                          border: 1px solid {7};
                          width: 13px;
                          height: 13px;               }}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
                      {{   border: 1px solid  {6};     }}

QRadioButton::indicator:checked, QRadioButton::indicator:unchecked
                      {{   color: {7};
                          background-color: {1};
                          border: 1px solid {7};
                          border-radius: 6px;         }}

QRadioButton::indicator:checked
                      {{   background-color: qradialgradient(cx: 0.5, cy: 0.5,fx: 0.5, fy: 0.5, radius: 1.0, stop: 0.25 {5}, stop: 0.3 {1});     }}

QRadioButton::indicator
                      {{   border-radius: 6px;         }}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
                      {{   border: 1px solid {5};  }}

QDockWidget::title    {{   text-align: center;
                          spacing: 3px; /* spacing between items in the tool bar */
                          background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 {1}, stop: 0.5 #242424, stop:1 {1});     }}

QDockWidget::close-button, QDockWidget::float-button
                      {{   text-align: center;
                          spacing: 1px; /* spacing between items in the tool bar */
                          background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 {1}, stop: 0.5 #242424, stop:1 {1});   }}

QDockWidget::close-button:hover, QDockWidget::float-button:hover
                      {{   background: #242424;  }}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed
                      {{   padding: 1px -1px -1px 1px; }}

QMainWindow::separator{{   background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
                          color: white;
                          padding-left: 4px;
                          border: 1px solid #4c4c4c;
                          spacing: 3px; /* spacing between items in the tool bar */ }}

QMainWindow::separator:hover
                      {{   background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 {2}, stop:0.5 #b56c17 stop:1 {0});
                          color: white;
                          padding-left: 4px;
                          border: 1px solid #6c6c6c;
                          spacing: 3px; /* spacing between items in the tool bar */ }}

QProgressBar          {{   border: 2px solid grey;
                          border-radius: 5px;
                          text-align: center;           }}

QProgressBar::chunk   {{   background-color: {2};
                          width: 2.15px;
                          margin: 0.5px;                }}

QTabBar::tab          {{   color: {7};
                          border: 1px solid  {6};
                          border-bottom-style: none;
                          background-color: {1};
                          padding-left: 10px;
                          padding-right: 10px;
                          padding-top: 3px;
                          padding-bottom: 2px;
                          margin-right: -1px;             }}

QTabBar::tab:last     {{   margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
                          border-top-right-radius: 3px;   }}

QTabBar::tab:first:!selected
                      {{   margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */
                          border-top-left-radius: 3px;    }}

QTabBar::tab:!selected{{   color: {7};
                          border-bottom-style: solid;
                          margin-top: 3px;
                          background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);       }}

QTabBar::tab:selected {{   border-top-left-radius: 3px;
                          border-top-right-radius: 3px;
                          margin-bottom: 0px;     }}

QTabBar::tab:!selected:hover
                      {{   /*border-top: 2px solid {5};
                          padding-bottom: 3px;*/
                          border-top-left-radius: 3px;
                          border-top-right-radius: 3px;
                          background-color: QLinearGradient(  x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 {5}  );    }}

QTabWidget::pane      {{   border: 1px solid  {6};
                          top: 1px;               }}

QSpinBox,QDoubleSpinBox {{   
                          selection-background-color: {5};
                          background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
                          border-style: solid;
                          border: 1px solid {8};
                          border-radius: 5;       
                        }}

QSpinBox::up-button,QDoubleSpinBox::up-button   {{   subcontrol-origin: border;
                          subcontrol-position: top right;
                          width: 16px;
                          border-width: 0;
                          border-top-width: 0;    }}

QSpinBox::down-button,QDoubleSpinBox::down-button {{   subcontrol-origin: border;
                          subcontrol-position: bottom right;
                          width: 16px;
                          border-width: 0;
                          border-top-width: 0;    }}

QSpinBox:focus,QDoubleSpinBox:focus,QTreeWidget:focus,QTextEdit:focus,QGroupBox:focus,QLineEdit:focus
                      {{
                          border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 {0}, stop: 1 {2});
                      }}

QComboBox::down-arrow                             {{    image:url(:/arrow_down.png);                   }}

QToolBar::handle                                  {{    spacing: 3px; /* spacing between items in the tool bar */   }}

QCheckBox::indicator:checked                      {{    image:url(:/checkbox.png);                     }}

QCheckBox::indicator:disabled:checked             {{    image:url(:/checkbox_disabled.png);            }}

QSplitter::handle:horizontal                      {{    image:url(:/Orange_spliter_Horizontal.png);    }}

QSplitter::handle:vertical                        {{    image:url(:/Orange_spliter_Vertical_low.png);  }}

QSpinBox::down-arrow,QDoubleSpinBox::down-arrow   {{    image: url(:/arrow_down.png);                   }}

QSpinBox::up-arrow,QDoubleSpinBox::up-arrow       {{    image: url(:/arrow_up.png);                     }}

QTreeView::branch:open:has-children               {{    image: url(:/arrow_down_tree.png);              }}

QTreeView::branch:closed:has-children             {{    image: url(:/arrow_right.png);                  }}



""".format(self.ORANGE1.name(),self.BG_DARK.name(),self.ORANGEDARKER.name(),self.ORANGELIGHTER.name(),self.BLACK.name(),self.ORANGELIGHTER2.name(),self.GREY.name(),self.GREYLIGHT.name(),self.GREYDARK.name())


style = editableStyleSheet()
style.setHue(1)
