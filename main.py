import os
import sys
from MainWindow import Ui_MainWindow
from AddWindow import Ui_AddQuote
from EditWindow import Ui_EditQuote
from QuoteWindow import Ui_QuoteWindow
from AboutWindow import Ui_About
from OptionsWindow import Ui_AdvancedOptionsDialog
from PySide6.QtWidgets import (QMainWindow, QApplication, 
                               QMessageBox, QDialog, 
                               QStyledItemDelegate, QAbstractItemView, 
                               QSystemTrayIcon, QMenu, QWidget)
from PySide6.QtCore import (Qt, QStringListModel, QModelIndex, 
                            QSortFilterProxyModel, QTimer, 
                            QSize, QRectF, QPropertyAnimation,
                            QEasingCurve)
from PySide6.QtGui import (QScreen, QPen, QColor, QAction, QIcon, 
                           QFontDatabase, QFont,QGuiApplication, 
                           QPainterPath, QRegion, QPixmap)
import qdarktheme
import webbrowser
import json
import platform
from tendo import singleton
if platform.system() == "Windows":
    import winreg
from random import randint
import pygame


class CustomItemDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        # Center quotes' text
        option.displayAlignment = Qt.AlignCenter  # Set text alignment to center

    def paint(self, painter, option, index):
        super().paint(painter, option, index)

        # Draw the gray line under each item
        line_rect = option.rect.adjusted(0, 8, 0, 8)
        gray_line_color = QColor(169, 169, 169)
        line_pen = QPen(gray_line_color)
        painter.setPen(line_pen)
        painter.drawLine(line_rect.bottomLeft(), line_rect.bottomRight())

# Class to search string from quotes
class StringFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filter_string = ""

    def setFilterString(self, filter_string):
        self.filter_string = filter_string
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        source_model = self.sourceModel()
        index = source_model.index(sourceRow, 0, sourceParent)
        item_text = source_model.data(index, Qt.DisplayRole)
        return self.filter_string.lower() in item_text.lower()

class RoundWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.clicked_flag = 0

    def paintEvent(self, event):
        # Round corners
        radius = 20.0
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

    def mousePressEvent(self, event):
        # Check if the left mouse button is pressed
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())
        self.clicked_flag = 1
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Add the icon
        self.icon = QIcon()
        self.icon.addFile(u"Icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(self.icon)

        # Initialize OptionsWidget
        self.options_dialog = QDialog()
        self.options_dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.options_dialog.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.options_dialog.ui = Ui_AdvancedOptionsDialog()
        self.options_dialog.ui.setupUi(self.options_dialog)
        self.options_dialog.setWindowIcon(self.icon)
        self.options_dialog.setStyleSheet(
            "QDialog {"
            "   border: 1px solid #dedbd2;"
            "}"
        ) 
        

        # Disable autostart if not from windows executable
        self.options_dialog.ui.AutostartCheckBox.setDisabled(True)
        if platform.system() == "Windows" and getattr(sys, 'frozen', False):
            self.options_dialog.ui.AutostartCheckBox.setEnabled(True)

        # Set fonts for title, labels and texts:
        self.font_id_tit = QFontDatabase.addApplicationFont(os.path.abspath("Fonts/BebasNeue-Regular.ttf"))
        self.font_family_tit = QFontDatabase.applicationFontFamilies(self.font_id_tit)[0]
        self.custom_font_tit = QFont(self.font_family_tit)
        self.custom_font_tit.setPointSize(22)
        self.font_id = QFontDatabase.addApplicationFont(os.path.abspath("Fonts/Montserrat-Regular.ttf"))
        self.font_family = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        self.custom_font = QFont(self.font_family)
        self.custom_font.setPointSize(9)
        self.custom_font_text = QFont(self.font_family)
        self.custom_font_text.setPointSize(11)
        self.font_id_q = QFontDatabase.addApplicationFont(os.path.abspath("Fonts/Montserrat-MediumItalic.ttf"))
        self.font_family_q = QFontDatabase.applicationFontFamilies(self.font_id_q)[0]
        self.custom_font_text_q = QFont(self.font_family_q)
        self.custom_font_text_q.setPointSize(11)
        self.custom_font_text_q.setItalic(True)
        self.custom_font_tit_about = QFont(self.font_family_tit)
        self.custom_font_tit_about.setPointSize(11)
        
        # Change fonts for items
        self.ui.QuoteLabel.setFont(self.custom_font_tit)
        self.ui.MinutesLabel.setFont(self.custom_font)
        self.options_dialog.ui.RandomLabel.setFont(self.custom_font)
        self.options_dialog.ui.AutostartLabel.setFont(self.custom_font)
        self.options_dialog.ui.MinimizedLabel.setFont(self.custom_font)
        self.ui.SearchBar.setFont(self.custom_font_text)
        self.ui.ListView.setFont(self.custom_font_text)
        self.options_dialog.ui.SecondsLabel.setFont(self.custom_font)
        self.ui.AboutButton.setFont(self.custom_font_tit_about)
        self.ui.OptionsButton.setFont(self.custom_font_tit_about)
        self.options_dialog.ui.DarkThemeLabel.setFont(self.custom_font)
        self.options_dialog.ui.PositionLabel.setFont(self.custom_font)
        self.options_dialog.ui.DisableSoundLabel.setFont(self.custom_font)

        # Create empty list to crate a json with
        empty_list = []
        # Check if we are executing from exe
        if getattr(sys, 'frozen', False):
            empty_tmp = {
                        "quote_n": 0,
                        "randomize": 1,
                        "timer_running": 0,
                        "autostart": 1,
                        "minimized": 0,
                        "minutes": 30,
                        "seconds": 17,
                        "position": 0,
                        "darktheme": 0,
                        "disablesound": 0
            }
        else:
            empty_tmp = {
                        "quote_n": 0,
                        "randomize": 1,
                        "timer_running": 0,
                        "autostart": 0,
                        "minimized": 0,
                        "minutes": 30,
                        "seconds": 11,
                        "position": 0,
                        "darktheme": 0,
                        "disablesound": 0
            }
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Quotes\\list.json")
        self.file_path2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Prefs\\tmp.json")
        self.sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sound\\new-positive-notice.wav")
        self.convert_path_for_open()
        # Create empty jsons list if the json file doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump(empty_list, file)
        if not os.path.exists(self.file_path2):
            with open(self.file_path2, 'w') as file:
                json.dump(empty_tmp, file)
        
        # Open the json files and load them
        with open(self.file_path, 'r') as file:
            self.array_of_quotes = json.load(file)   

        with open(self.file_path2, 'r') as file:
            self.tmp_status = json.load(file)     


        # Create a string model
        self.model = QStringListModel()

        # Set the listView to display it
        self.ui.ListView.setModel(self.model)

        # Load the list from the json into it
        self.model.setStringList(self.array_of_quotes)
        # Accessing the QListView instance and setting the delegate to draw line
        # and center text
        delegate = CustomItemDelegate(self.ui.ListView)
        self.ui.ListView.setItemDelegate(delegate)
        self.ui.ListView.setSelectionMode(QAbstractItemView.SingleSelection)

        # Check if systray is available
        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(None, "No System tray", "No System tray detected!")
            sys.exit(1)

        # Create tray icon
        self.ui.tray_icon = QSystemTrayIcon(self)
        self.ui.tray_icon.setIcon(QIcon(os.path.abspath("Icons/icon.png")))

        # Open program if tray double clicked
        self.ui.tray_icon.activated.connect(self.tray_icon_activated)

        # Create a context menu for the system tray icon
        self.ui.tray_menu = QMenu()

        # Add an action to the context menu to show the main window
        self.ui.open_action = QAction("Open Program", self)
        self.ui.open_action.triggered.connect(self.open)
        self.ui.tray_menu.addAction(self.ui.open_action)

        # Add a gaming mode action to the context menu
        self.gaming = 0
        self.ui.gaming_action = QAction("Gaming mode", self)
        self.ui.gaming_action.setCheckable(True)
        self.ui.gaming_action.setChecked(False)
        self.ui.gaming_action.triggered.connect(self.toggle_gaming_mode)
        self.ui.tray_menu.addAction(self.ui.gaming_action)
        
        # Add an exit action to the context menu
        self.ui.exit_action = QAction("Exit", self)
        self.ui.exit_action.triggered.connect(self.exit_app)
        self.ui.tray_menu.addAction(self.ui.exit_action)

        self.ui.tray_icon.setContextMenu(self.ui.tray_menu)
        self.ui.tray_icon.show()

        # Initialize list for combobox
        combo_box_list = ["UpCenter", "UpRight", "UpLeft", "DownRight", "DownLeft"]
        self.options_dialog.ui.PositionComboBox.insertItems(0, combo_box_list)
        # Create counter to store which quotes have been displayed
        self.quote_counter = 0
        # Create a timer
        self.timer = QTimer(self)
        # Make it show notification everytime it ends
        self.timer.timeout.connect(self.show_reminder)
        # Create a second timer to automatically close quote
        self.quote_timer = QTimer(self)
        self.quote_timer.setSingleShot(True)
        self.quote_timer.timeout.connect(self.start_closing_animation)   
        # Create a third timer to wait a bit before displaying quote
        # to prevent artifacts
        self.before_show_quote_timer = QTimer(self)
        self.before_show_quote_timer.setSingleShot(True)
        self.before_show_quote_timer.timeout.connect(self.show_quote)
        # Create a fourth timer to wait for disappearing animation to end
        self.end_animation_timer = QTimer(self)
        self.end_animation_timer.setSingleShot(True)
        self.end_animation_timer.timeout.connect(self.close_quote)
        # Initiate based on tmp-status file
        self.options_dialog.ui.RandomCheckBox.setChecked(bool(self.tmp_status["randomize"]))
        self.quote_counter = self.tmp_status["quote_n"]
        self.ui.MinutesSpinBox.setValue(self.tmp_status["minutes"])
        self.options_dialog.ui.AutostartCheckBox.setChecked(bool(self.tmp_status["autostart"]))
        self.options_dialog.ui.MinimizedCheckBox.setChecked(bool(self.tmp_status["minimized"]))
        self.options_dialog.ui.SecondsSpinBox.setValue(self.tmp_status["seconds"])  
        if self.tmp_status["timer_running"]:
            self.start_timer()
        self.options_dialog.ui.DarkThemeCheckBox.setChecked(bool(self.tmp_status["darktheme"]))
        self.options_dialog.ui.PositionComboBox.setCurrentIndex(self.tmp_status["position"])
        self.options_dialog.ui.DisableSoundCheckBox.setChecked(bool(self.tmp_status["disablesound"]))

        # Initiate pygame
        pygame.init()
        pygame.mixer.init()

        # Set Dark theme icons:
        if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
            self.ui.searchicon.setPixmap(QPixmap("Icons/light_search.ico"))
            self.ui.AddButton.setIcon(QIcon("Icons/light_add.png"))
            self.ui.RemoveButton.setIcon(QIcon("Icons/light_remove.png"))
            self.ui.UpButton.setIcon(QIcon("Icons/light_arrow_up.png"))
            self.ui.DownButton.setIcon(QIcon("Icons/light_arrow_down.png"))
            self.ui.EditButton.setIcon(QIcon("Icons/light_edit.png"))

        # Set stylesheet for options dialog
        if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
            qdarktheme.setup_theme("dark")
            self.options_dialog.ui.CloseButton_2.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
            """)
            self.options_dialog.ui.CloseButton_2.setIcon(QIcon("Icons/closeicondark.png"))
        else:
            qdarktheme.setup_theme("light")
            self.options_dialog.ui.CloseButton_2.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
            self.options_dialog.ui.CloseButton_2.setIcon(QIcon("Icons/closeicon.png"))

        # Preparation for the functions that allow moving a frameless window
        self.dragging = False
        self.offset = None

        # Reset startup in case executable had been moved:
        if self.options_dialog.ui.AutostartCheckBox.isEnabled():
            self.add_to_startup()        
        # Connect buttons and signals
        self.ui.DonateButton.clicked.connect(self.open_donate)
        self.ui.AddButton.clicked.connect(self.open_dialog_to_add)
        self.ui.RemoveButton.clicked.connect(self.remove_item)
        self.ui.UpButton.clicked.connect(self.move_item_up)
        self.ui.DownButton.clicked.connect(self.move_item_down)
        self.ui.EditButton.clicked.connect(self.open_edit_dialog)
        self.ui.SearchBar.textEdited.connect(self.search)
        self.ui.MinutesSpinBox.valueChanged.connect(self.reset_timer_database)
        self.options_dialog.ui.RandomCheckBox.stateChanged.connect(self.reset_timer_database)
        self.options_dialog.ui.AutostartCheckBox.stateChanged.connect(self.add_to_startup)
        self.options_dialog.ui.MinimizedCheckBox.stateChanged.connect(self.save_changes_to_settings)
        self.ui.AboutButton.clicked.connect(self.open_about)
        self.ui.CloseButton.clicked.connect(self.hide_window)
        self.options_dialog.ui.SecondsSpinBox.valueChanged.connect(self.save_changes_to_settings)
        self.options_dialog.ui.DarkThemeCheckBox.stateChanged.connect(self.toggle_darktheme)
        self.options_dialog.ui.PositionComboBox.currentIndexChanged.connect(self.move_quote)
        self.ui.OptionsButton.clicked.connect(self.open_options)
        self.options_dialog.ui.DisableSoundCheckBox.stateChanged.connect(self.save_changes_to_settings)
        self.options_dialog.ui.CloseButton_2.clicked.connect(self.close_options)


    def open_dialog_to_add(self):
        self.dialog = QDialog()
        self.dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.dialog.ui = Ui_AddQuote()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setWindowIcon(self.icon)

        if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
                self.dialog.ui.AddButton.setStyleSheet("""
                    QPushButton {
                        background-color: #202124;
                    }
                    QPushButton:hover {
                        background-color: #272e3b;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: #2d3b53;  /* Change this to your desired click color */
                    }
                """)
                self.dialog.ui.QuitButton.setStyleSheet("""
                    QPushButton {
                        background-color: #202124;
                    }
                    QPushButton:hover {
                        background-color: #272e3b;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: #2d3b53;  /* Change this to your desired click color */
                    }
                """)
                self.dialog.ui.AddButton.setIcon(QIcon("Icons/light_add.png"))
                self.dialog.ui.QuitButton.setIcon(QIcon("Icons/closeicondark.png"))
        else:  
            self.dialog.ui.AddButton.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
            self.dialog.ui.QuitButton.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
        self.dialog.setStyleSheet(
            "QDialog {"
            "   border: 1px solid #dedbd2;"
            "}"
        ) 
        self.dialog.ui.PlainTextEdit.setFont(self.custom_font_text)
        self.dialog.ui.AddButton.clicked.connect(self.add_item)
        self.dialog.ui.QuitButton.clicked.connect(self.close_dialog)
        self.dialog.show()

    def add_item(self):
        if self.dialog.ui.PlainTextEdit.toPlainText():
            # Add quote to model
            self.model.insertRows(self.model.rowCount(), 1)
            self.model.setData(self.model.index(self.model.rowCount() - 1),
                                self.dialog.ui.PlainTextEdit.toPlainText())
            self.reset_timer_database()
            self.save_changes_to_quotes()
            self.dialog.close()
    
    def open_quote(self, text):
        if self.gaming == 0:
            self.quote_dialog = RoundWidget()
            self.quote_dialog.setWindowFlag(Qt.FramelessWindowHint)
            self.quote_dialog.setWindowFlag(Qt.WindowStaysOnTopHint)
            self.quote_dialog.ui = Ui_QuoteWindow()
            self.quote_dialog.ui.setupUi(self.quote_dialog)
            self.quote_dialog.setWindowIcon(self.icon)

            # Dark theme legend
            #202124 background
            #f1f1f1 text
            #272e3b hovered button
            #2d3b53 pressed button
            
            if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
                self.quote_dialog.ui.CloseQuoteButton.setIcon(QIcon(os.path.abspath("Icons/closeicondark.png")))
                self.quote_dialog.ui.CloseQuoteButton.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
                """)
            else:
                self.quote_dialog.ui.CloseQuoteButton.setStyleSheet("""
                    QPushButton {
                        background-color: #f8f9fa;
                    }
                    QPushButton:hover {
                        background-color: #e2ecf7;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: lightblue;  /* Change this to your desired click color */
                    }
                """)
                self.quote_dialog.ui.CloseQuoteButton.setIcon(QIcon(os.path.abspath("Icons/closeicon.png")))
            self.quote_dialog.ui.QuoteText.setFont(self.custom_font_text_q)
            self.quote_dialog.ui.QuoteText.setText(text)   
            self.quote_dialog.ui.CloseQuoteButton.clicked.connect(self.close_quote_even_centered)
            # Make it resize if quote is larger than window
            self.quote_dialog.adjustSize()            
            self.move_quote()
            self.before_show_quote_timer.setInterval(500)
            self.before_show_quote_timer.start()

    def show_quote(self):
        # Start timer to then close window
        self.quote_timer.setInterval(self.options_dialog.ui.SecondsSpinBox.value() * 1000)
        self.quote_timer.start()
        # Add fade in animation
        self.quote_dialog.animation = QPropertyAnimation(self.quote_dialog, b"windowOpacity")
        self.quote_dialog.animation.setDuration(750)  # Set the duration of the animation in milliseconds
        self.quote_dialog.animation.setStartValue(0)
        self.quote_dialog.animation.setEndValue(1)    
        self.quote_dialog.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.quote_dialog.show()
        self.quote_dialog.animation.start()
        if not self.options_dialog.ui.DisableSoundCheckBox.isChecked():
            self.play_quote_sound()

    def start_closing_animation(self):
        # Add fade out animation
        if self.quote_dialog.clicked_flag == 0:
            self.quote_dialog.animation = QPropertyAnimation(self.quote_dialog, b"windowOpacity")
            self.quote_dialog.animation.setDuration(550)  # Set the duration of the animation in milliseconds
            self.quote_dialog.animation.setStartValue(1)
            self.quote_dialog.animation.setEndValue(0)    
            self.quote_dialog.animation.setEasingCurve(QEasingCurve.InOutCubic)
            self.quote_dialog.animation.start()
            self.end_animation_timer.setInterval(550)
            self.end_animation_timer.start()

    def move_quote(self):
        # Get the geometry of the screen
        screen = QGuiApplication.primaryScreen()
        # Handle position of quote
        if self.quote_dialog.clicked_flag == 0:    
            try:
                match self.options_dialog.ui.PositionComboBox.currentText():
                        case "UpCenter":
                            # Calculate the position to move the dialog to the top center
                            x_position = (screen.availableGeometry().width() // 2) - (self.quote_dialog.width() // 2)
                            y_position = 26  
                            # Move the dialog to the specified position
                            self.quote_dialog.move(x_position, y_position)
                        case "UpRight":
                            # Calculate the position to move the dialog to the top right corner
                            x_position = screen.availableGeometry().width() - self.quote_dialog.width() - 26
                            y_position = 26  # Adjust the y-position as needed
                            # Move the dialog to the specified position
                            self.quote_dialog.move(x_position, y_position)
                        case "DownRight":
                            # Calculate the position to move the dialog to the bottom right corner
                            x_position = screen.availableGeometry().width() - self.quote_dialog.width() - 26
                            y_position = screen.availableGeometry().height() - self.quote_dialog.height() - 26
                            # Move the dialog to the specified position
                            self.quote_dialog.move(x_position, y_position)
                        case "DownLeft":
                            # Calculate the position to move the dialog to the bottom right corner
                            x_position = 26
                            y_position = screen.availableGeometry().height() - self.quote_dialog.height() - 26
                            # Move the dialog to the specified position
                            self.quote_dialog.move(x_position, y_position)
                        case "UpLeft":
                            # Calculate the position to move the dialog to the top left corner
                            x_position = 26
                            y_position = 26
                            # Move the dialog to the specified position
                            self.quote_dialog.move(x_position, y_position)
            except AttributeError:
                pass
        self.save_changes_to_settings()


    def close_quote(self):
        if self.quote_dialog.clicked_flag == 0:
            self.quote_dialog.close()
        if self.quote_timer.isActive():
            self.quote_timer.stop()
        if self.before_show_quote_timer.isActive():
            self.before_show_quote_timer.stop()
        if self.end_animation_timer.isActive():
            self.end_animation_timer.stop()
    
    def close_quote_even_centered(self):
        self.quote_dialog.close()
        
    def close_dialog(self):
        self.dialog.close()

    def open_edit_dialog(self):
        # Check if something is selected
        selected_index = self.get_selected_index()
        if selected_index is not None:
            self.edit_dialog = QDialog()
            self.edit_dialog.setWindowFlag(Qt.FramelessWindowHint)
            self.edit_dialog.ui = Ui_EditQuote()
            self.edit_dialog.ui.setupUi(self.edit_dialog)
            self.edit_dialog.setWindowIcon(self.icon)
            self.edit_dialog.ui.EditplainTextEdit.setFont(self.custom_font_text)
            self.edit_dialog.ui.EditButton.clicked.connect(self.edit_item)
            self.edit_dialog.ui.CloseEditButton.clicked.connect(self.close_edit_dialog)
            self.copy_selected_text_to_edit_dialog()
            
            if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
                self.edit_dialog.ui.EditButton.setStyleSheet("""
                    QPushButton {
                        background-color: #202124;
                    }
                    QPushButton:hover {
                        background-color: #272e3b;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: #2d3b53;  /* Change this to your desired click color */
                    }
                """)
                self.edit_dialog.ui.CloseEditButton.setStyleSheet("""
                    QPushButton {
                        background-color: #202124;
                    }
                    QPushButton:hover {
                        background-color: #272e3b;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: #2d3b53;  /* Change this to your desired click color */
                    }
                """)
                self.edit_dialog.ui.EditButton.setIcon(QIcon("Icons/light_edit.png"))
                self.edit_dialog.ui.CloseEditButton.setIcon(QIcon("Icons/closeicondark.png"))
            else:  
                self.edit_dialog.ui.EditButton.setStyleSheet("""
                    QPushButton {
                        background-color: #f8f9fa;
                    }
                    QPushButton:hover {
                        background-color: #e2ecf7;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: lightblue;  /* Change this to your desired click color */
                    }
                """)
                self.edit_dialog.ui.CloseEditButton.setStyleSheet("""
                    QPushButton {
                        background-color: #f8f9fa;
                    }
                    QPushButton:hover {
                        background-color: #e2ecf7;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: lightblue;  /* Change this to your desired click color */
                    }
                """)
            self.edit_dialog.setStyleSheet(
            "QDialog {"
            "   border: 1px solid #dedbd2;"
            "}"
            ) 
            self.edit_dialog.show()

    def edit_item(self):
        if self.ui.SearchBar.text():
            selected_index = self.get_selected_index()
            if selected_index is not None:
                if self.edit_dialog.ui.EditplainTextEdit.toPlainText():
                    # Edit item in the proxy model
                    self.proxy_model.setData(selected_index, self.edit_dialog.ui.EditplainTextEdit.toPlainText())

                    # Get the corresponding index in the original model using the mapped index
                    source_index = self.proxy_model.mapToSource(selected_index)

                    # Edit in the original model
                    self.model.setData(source_index, self.edit_dialog.ui.EditplainTextEdit.toPlainText())
                    self.reset_timer_database()
                else:
                    self.remove_item()
                    self.reset_timer_database()

        else:
            selected_index = self.get_selected_index()
            if self.edit_dialog.ui.EditplainTextEdit.toPlainText():
                if selected_index is not None:
                    self.model.setData(selected_index, self.edit_dialog.ui.EditplainTextEdit.toPlainText())
                    self.reset_timer_database()
            else:
                self.remove_item()
                self.reset_timer_database()
        self.close_edit_dialog()
        self.save_changes_to_quotes()
    

    def close_edit_dialog(self):
        self.edit_dialog.close()

    def get_selected_text(self):
        if self.ui.SearchBar.text():
            selected_index = self.get_selected_index()
            if selected_index is not None:
                return selected_index.data()
        else:
            selected_index = self.get_selected_index()
            return selected_index.data()

    def copy_selected_text_to_edit_dialog(self):
        self.edit_dialog.ui.EditplainTextEdit.setPlainText(self.get_selected_text())

    def get_selected_row(self):
        selected_index = self.ui.ListView.selectedIndexes()
        if selected_index:
            return selected_index[0].row()
        else:
            return None
    
    def get_selected_index(self):
        selected_index = self.ui.ListView.selectedIndexes()
        if selected_index:
            return selected_index[0]
        else:
            return None

    def remove_item(self):
        if self.ui.SearchBar.text():
            selected_row = self.get_selected_row()
            if selected_row is not None:
                # Get the corresponding index in the proxy model
                self.proxy_index = self.proxy_model.index(selected_row, 0)

                # Remove from the proxy model
                self.proxy_model.removeRows(selected_row, 1)

                # Get the corresponding index in the original model using the mapped index
                source_index = self.proxy_model.mapToSource(self.proxy_index)

                # Remove from the original model
                self.model.removeRows(source_index.row(), 1)
                self.reset_timer_database()
                self.stop_timer_if_empty()
                self.save_changes_to_quotes()

        else:
            selected_row = self.get_selected_row()
            if selected_row is not None:
                self.model.removeRows(selected_row, 1)
            self.reset_timer_database()
            self.stop_timer_if_empty()
            self.save_changes_to_quotes()

    def stop_timer_if_empty(self):
        if self.model.rowCount() == 0:
            self.timer.stop()

    def move_item_up(self):
        if self.get_selected_row():
            if self.get_selected_row() > 0:
                self.model.moveRow(QModelIndex(), self.get_selected_row(), 
                                QModelIndex(), self.get_selected_row() - 1)
                self.reset_timer_database()
                self.save_changes_to_quotes()

    def move_item_down(self):
        if self.get_selected_row() is not None:
            if self.get_selected_row() < self.model.rowCount() - 1:
                self.model.moveRow(QModelIndex(), self.get_selected_row(), 
                                QModelIndex(), self.get_selected_row() + 2)
                self.reset_timer_database()
                self.save_changes_to_quotes()
    
    def search(self):       
        if self.ui.SearchBar.text():
            # Create a proxy model from the original one to use in search
            self.proxy_model = StringFilterProxyModel()
            self.proxy_model.setSourceModel(self.model)
            self.ui.ListView.setModel(self.proxy_model)
            self.proxy_model.setFilterString(self.ui.SearchBar.text())
            self.disable_buttons_while_searching()
        else:
            self.ui.ListView.setModel(self.model)
            self.enable_buttons_after_search()

    def filter_strings_by_search(search_list, target_string):
        return [string for string in search_list if target_string in string]
    
    def disable_buttons_while_searching(self):
        self.ui.AddButton.setEnabled(False)
        self.ui.UpButton.setEnabled(False)
        self.ui.DownButton.setEnabled(False)
        self.ui.OptionsButton.setEnabled(False)
        self.ui.AddButton.setStyleSheet("""
        QPushButton {
                background-color: #bfbfbf;
        }
        """)
        self.ui.UpButton.setStyleSheet("""
        QPushButton {
                background-color: #bfbfbf;
        }
        """)
        self.ui.DownButton.setStyleSheet("""
        QPushButton {
                background-color: #bfbfbf;
        }
        """)
        self.ui.OptionsButton.setStyleSheet("""
        QPushButton {
                background-color: #bfbfbf;
        }
        """)

    def enable_buttons_after_search(self):
        self.ui.AddButton.setEnabled(True)
        self.ui.UpButton.setEnabled(True)
        self.ui.DownButton.setEnabled(True)
        self.ui.OptionsButton.setEnabled(True)
        if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
            self.ui.AddButton.setStyleSheet("""
            QPushButton {
                    background-color: #202124;
            }
            """)
            self.ui.UpButton.setStyleSheet("""
            QPushButton {
                    background-color: #202124;
            }
            """)
            self.ui.DownButton.setStyleSheet("""
            QPushButton {
                    background-color: #202124;
            }
            """)
            self.ui.OptionsButton.setStyleSheet("""
            QPushButton {
                    background-color: #202124;
            }
            """)           
        else:
            self.ui.AddButton.setStyleSheet("""
            QPushButton {
                    background-color: #f8f9fa;
            }
            """)
            self.ui.UpButton.setStyleSheet("""
            QPushButton {
                    background-color: #f8f9fa;
            }
            """)
            self.ui.DownButton.setStyleSheet("""
            QPushButton {
                    background-color: #f8f9fa;
            }
            """)
            self.ui.OptionsButton.setStyleSheet("""
            QPushButton {
                    background-color: #f8f9fa;
            }
            """)

    def open(self):
        self.show()

    def toggle_gaming_mode(self):
        if self.ui.gaming_action.isChecked():
            self.gaming = 1
        else:
            self.gaming = 0            
    
    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            # Perform action on double-click
            self.show()
            self.raise_()
            self.activateWindow()

    def reset_timer_database(self):
        self.array_of_quotes = self.model.stringList()
        self.start_timer()
        self.stop_timer_if_empty()
        self.quote_counter = 0
        self.save_changes_to_settings()

    def start_timer(self):
        if self.timer.isActive():
            self.timer.stop()
        self.timer.setInterval(60*1000*self.ui.MinutesSpinBox.value())
        self.timer.start()

    def show_reminder(self):
        if self.options_dialog.ui.RandomCheckBox.isChecked():
            self.open_quote(self.array_of_quotes[randint(0, len(self.array_of_quotes) - 1)])
        else:
            self.open_quote(self.array_of_quotes[self.quote_counter])
            self.quote_counter += 1
            if self.quote_counter == len(self.array_of_quotes):
                self.quote_counter = 0
            
    def open_donate(self):
        webbrowser.open("https://www.paypal.com/donate/?hosted_button_id=D3QUYDFUGGBPJ")
    
    def mousePressEvent(self, event):
        # Check if the left mouse button is pressed
        if event.buttons() == Qt.LeftButton:
            # Set the dragging flag to True
            self.dragging = True

            # Calculate the offset between the mouse click position and the window position
            self.offset = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        # Check if the left mouse button is pressed and dragging is enabled
        if event.buttons() == Qt.LeftButton and self.dragging:
            # Move the window to the current mouse position with the offset
            self.move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        # Reset the dragging flag when the mouse button is released
        self.dragging = False 

    def add_to_startup(self):  
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        program_name = "Quote Reminder"

        # Get the full path of the Python executable
        python_executable = sys.executable

        # Get the full path of the Python program
        script_path = os.path.abspath(__file__)

        # Construct the full command to run the program
        script_command = f'"{python_executable}" "{script_path}"'
        if self.options_dialog.ui.AutostartCheckBox.isChecked():
            if platform.system() == "Windows" and getattr(sys, 'frozen', False):
                try:
                    # Open the registry key for writing
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as registry_key:
                        # Set the registry value to the executable path
                        winreg.DeleteValue(registry_key, program_name)

                except:
                    pass              
                try:
                    # Open the registry key for writing
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as registry_key:
                        # Set the registry value to the executable path
                        winreg.SetValueEx(registry_key, program_name, 0, winreg.REG_SZ, python_executable)

                except Exception as e:
                    QMessageBox.critical(None, 'Error', f"Failed to add {program_name} to startup. Error: {e}")
        else:
            if platform.system() == "Windows" and getattr(sys, 'frozen', False):
                try:
                    # Open the registry key for writing
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as registry_key:
                        # Set the registry value to the executable path
                        winreg.DeleteValue(registry_key, program_name)

                except Exception as e:
                    QMessageBox.critical(None, 'Error', f"Failed to remove {program_name} from startup. Error: {e}")
        self.save_changes_to_settings()
    


    def hide_window(self):
        self.hide()

    def convert_path_for_open(self):
        # Convert backslashes to forward slashes (Windows-specific)
        self.file_path = self.file_path.replace('\\', '/')
        self.file_path2 = self.file_path2.replace('\\', '/')

    def closeEvent(self, event):
        # Store model to json for future usage
        event.ignore()
        self.hide()

    def save_changes_to_quotes(self):
        # Store model to json for future usage
        with open(self.file_path, 'w') as file:
            json.dump(self.model.stringList(), file)
    
    def save_changes_to_settings(self):
        # Store temporary values to json for future usage
        self.tmp_status["quote_n"] = self.quote_counter
        self.tmp_status["randomize"] = int(self.options_dialog.ui.RandomCheckBox.isChecked())
        self.tmp_status["timer_running"] = int(self.timer.isActive())
        self.tmp_status["minutes"] = self.ui.MinutesSpinBox.value()
        self.tmp_status["autostart"] = int(self.options_dialog.ui.AutostartCheckBox.isChecked())
        self.tmp_status["minimized"] = int(self.options_dialog.ui.MinimizedCheckBox.isChecked())
        self.tmp_status["seconds"] = self.options_dialog.ui.SecondsSpinBox.value()
        self.tmp_status["darktheme"] = int(self.options_dialog.ui.DarkThemeCheckBox.isChecked())
        self.tmp_status["position"] = int(self.options_dialog.ui.PositionComboBox.currentIndex())
        self.tmp_status["disablesound"] = int(self.options_dialog.ui.DisableSoundCheckBox.isChecked())
        with open(self.file_path2, 'w') as file:
            test = json.dump(self.tmp_status, file)

    def play_quote_sound(self):
        sound = pygame.mixer.Sound(self.sound_path)
        sound.play()

    def open_about(self):
        self.about_dialog = QDialog()
        self.about_dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.about_dialog.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.about_dialog.ui = Ui_About()
        self.about_dialog.ui.setupUi(self.about_dialog)
        self.about_dialog.setWindowIcon(self.icon)

        if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
            self.about_dialog.ui.CloseButton.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
            """)
            self.about_dialog.ui.CloseButton.setIcon(QIcon("Icons/closeicondark"))
        else:
            self.about_dialog.ui.CloseButton.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
        self.about_dialog.ui.TitleLabel.setFont(self.custom_font_tit_about)
        self.about_dialog.ui.AboutLabel.setFont(self.custom_font)   
        self.about_dialog.ui.CloseButton.clicked.connect(self.close_about)
        self.about_dialog.ui.GithubButton.clicked.connect(self.open_github)
        self.about_dialog.setStyleSheet(
            "QDialog {"
            "   border: 1px solid #dedbd2;"
            "}"
        ) 
        self.about_dialog.show()
        # Make it resize if quote is larger than window
        self.about_dialog.adjustSize()

    def toggle_darktheme(self):            
        if self.options_dialog.ui.DarkThemeCheckBox.isChecked():
            qdarktheme.setup_theme("dark")
            self.options_dialog.ui.CloseButton_2.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
            """)
            self.options_dialog.ui.CloseButton_2.setIcon(QIcon("Icons/closeicondark.png"))
            self.ui.searchicon.setPixmap(QPixmap("Icons/light_search.ico"))
            self.ui.AddButton.setIcon(QIcon("Icons/light_add.png"))
            self.ui.RemoveButton.setIcon(QIcon("Icons/light_remove.png"))
            self.ui.UpButton.setIcon(QIcon("Icons/light_arrow_up.png"))
            self.ui.DownButton.setIcon(QIcon("Icons/light_arrow_down.png"))
            self.ui.EditButton.setIcon(QIcon("Icons/light_edit.png"))
            try:
                self.quote_dialog.ui.CloseQuoteButton.setIcon(QIcon(os.path.abspath("Icons/closeicondark.png")))
                self.quote_dialog.ui.CloseQuoteButton.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
                """)
            except AttributeError:
                pass
            self.ui.AddButton.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
                """)
            self.ui.UpButton.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
                """)
            self.ui.DownButton.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
                """)
            self.ui.OptionsButton.setStyleSheet("""
                QPushButton {
                    background-color: #202124;
                }
                QPushButton:hover {
                    background-color: #272e3b;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: #2d3b53;  /* Change this to your desired click color */
                }
                """)
        else:
            qdarktheme.setup_theme("light")
            self.options_dialog.ui.CloseButton_2.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
            self.options_dialog.ui.CloseButton_2.setIcon(QIcon("Icons/closeicon.png"))
            self.ui.searchicon.setPixmap(QPixmap("Icons/baseline_search_black_20.ico"))
            self.ui.AddButton.setIcon(QIcon("Icons/add_FILL0_wght400_GRAD0_opsz24.png"))
            self.ui.RemoveButton.setIcon(QIcon("Icons/remove_FILL0_wght400_GRAD0_opsz24.png"))
            self.ui.UpButton.setIcon(QIcon("Icons/expand_less_FILL0_wght400_GRAD0_opsz24.png"))
            self.ui.DownButton.setIcon(QIcon("Icons/keyboard_arrow_down_FILL0_wght400_GRAD0_opsz24.png"))
            self.ui.EditButton.setIcon(QIcon("Icons/edit.png"))
            try:
                self.quote_dialog.ui.CloseQuoteButton.setStyleSheet("""
                    QPushButton {
                        background-color: #f8f9fa;
                    }
                    QPushButton:hover {
                        background-color: #e2ecf7;  /* Change this to your desired hover color */
                    }
                    QPushButton:pressed {
                        background-color: lightblue;  /* Change this to your desired click color */
                    }
                """)
            except AttributeError:
                pass
            self.ui.AddButton.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
            self.ui.UpButton.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
            self.ui.DownButton.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
            self.ui.OptionsButton.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                }
                QPushButton:hover {
                    background-color: #e2ecf7;  /* Change this to your desired hover color */
                }
                QPushButton:pressed {
                    background-color: lightblue;  /* Change this to your desired click color */
                }
            """)
            try:
                self.quote_dialog.ui.CloseQuoteButton.setIcon(QIcon(os.path.abspath("Icons/closeicon.png")))
            except AttributeError:
                pass
        self.save_changes_to_settings()      

    def open_github(self):
        webbrowser.open("https://github.com/funghetto/Quote-Reminder")  

    def close_about(self):
        self.about_dialog.close()
    
    def open_options(self):
        self.options_dialog.show()
    
    def close_options(self):
        self.options_dialog.close()

    def exit_app(self):
        self.save_changes_to_quotes()
        self.save_changes_to_settings()
        # Close open dialogs
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QDialog):
                widget.reject()
        try:
            if self.quote_dialog.isEnabled():
                self.close_quote()
        except AttributeError:
            pass

        try:
            if self.options_dialog.isEnabled():
                self.close_options()
        except AttributeError:
            pass

        # Close app
        app = QApplication.instance()
        app.quit()

if __name__ == "__main__":
    # Checks if program is running and exit otherwise
    try:
        me = singleton.SingleInstance()
    except singleton.SingleInstanceException:
        sys.exit()

    app = QApplication(sys.argv)

    window = MainWindow()    
    if not window.options_dialog.ui.MinimizedCheckBox.isChecked():
        window.show()
    # Center the window
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())

    # Prevent app from closing
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())