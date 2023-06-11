from aqt import mw
from aqt.qt import *
from anki.hooks import addHook

class MultiDeckerDialog(QDialog):
    def __init__(self):
        super().__init__(mw)
        self.setWindowTitle("Create Multiple Empty Decks")
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.instructions_label = QLabel("Enter parent decks, separated by \";\" without spaces.")
        self.layout.addWidget(self.instructions_label)
        
        self.deck_input = QLineEdit()
        self.layout.addWidget(self.deck_input)
        
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_decks)
        self.create_button.clicked.connect(self.accept)
        self.layout.addWidget(self.create_button)
        
    def create_decks(self):
        deck_names = self.deck_input.text().split(";")
        for deck_name in deck_names:
            self.create_deck(deck_name.strip())
        
    def create_deck(self, deck_name):
        deck_id = mw.col.decks.id(deck_name)
        mw.col.decks.save()
        mw.col.decks.currentId = deck_id

def create_multi_decker():
    dialog = MultiDeckerDialog()
    dialog.exec_()

action = QAction("Create Multiple Empty Decks", mw)
mw.form.menuTools.addAction(action)
action.triggered.connect(create_multi_decker)

addHook("profileLoaded", lambda: mw.addonManager.setWebExports(__name__, r"web/(.*)"))
