
import os
import FreeCADGui

def getCommands():
  return ["AddBearing608"]


__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Icons' )


class CmdAddBearing608:
    """Add 608 Ball Bearing"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(iconPath, "BSLogo.svg"), # the name of a svg file available in the resources
                #"Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": "Add 608 Ball Bearing",
                "ToolTip" : "Add a 608 Ball Bearing at the selected feature"}

    def Activated(self):
        """Do something here"""
        # The 608 bearing is inner d 8, outer D 22, width B 7, dh 10, ds 20, r=0.3, R=0.3, d1 12.15, D1 19.2
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand("AddBearing608", CmdAddBearing608())


