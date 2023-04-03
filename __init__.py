from PyQt5.QtWidgets import QAction, QMessageBox

H3_MESSAGE = '''
    <p>
      To create H3 density maps you will need to install the H3 Python Library (<a href="https://h3geo.org/">https://h3geo.org/</a>).<br><br>
      The H3 package can be installed by running the OSGeo4W shell as system administrator and running 'pip install h3' or whatever method you use to install python packages.
    </p>
    <p>
      Please refer to the H3 installation documentation: <a href="https://h3geo.org/docs/installation">https://h3geo.org/docs/installation</a>
    </p>
    <p>
      Once H3 is installed, please restart QGIS.
    </p>
    '''

try:
    import h3
    H3_MESSAGE = 'H3 is natively supported so this plugin is not needed.'
except Exception:
    import os
    import site
    import platform
    if platform.system() == 'Windows':
        site.addsitedir(os.path.abspath(os.path.dirname(__file__) + '/libs'))
        H3_MESSAGE = '<p>H3 was successfully installed.</p><p>To uninstall, you must manually remove this plugin directory "{}" when QGIS is not running.</p><p>Using the QGIS plugin manager to remove it will not work.</p.'.format(os.path.abspath(os.path.dirname(__file__)))
    else:
        H3_MESSAGE = '<p>This plugin only works with Windows. You will need to install H3 as follows:</p>' + H3_MESSAGE

def classFactory(iface):
    return H3Library(iface)

class H3Library:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        # add About window
        self.aboutAction = QAction('About', self.iface.mainWindow())
        self.iface.addPluginToMenu('H3 Status', self.aboutAction)
        self.aboutAction.triggered.connect(self.aboutWindow)

    def unload(self):
        self.iface.removePluginMenu('H3 Status', self.aboutAction)

    def aboutWindow(self):
        windowTitle = 'About H3 Status plugin'
        QMessageBox.information(self.iface.mainWindow(), windowTitle, H3_MESSAGE)
