
import os

import errno
import FreeCAD, FreeCADGui, Part, math, os
from FreeCAD import Base
import DraftVecUtils
from pathlib import Path


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
        FreeCAD.Console.PrintMessage("I guess we should generate and add a bearing now.\n")
        # The 608 bearing is inner d 8, outer D 22, width B 7, dh 10, ds 20, r=0.3, R=0.3, d1 12.15, D1 19.2
        doc = FreeCAD.activeDocument()
#        self.moveScrew(ScrewObj) # attach the Bearing to a selected round feature (see screw_maker.py)
        p0 = Base.Vector( 4.0, 0.0,  7.0)
        p1 = Base.Vector(11.0, 0.0,  7.0)
        p2 = Base.Vector(11.0, 0.0,  0.0)
        p3 = Base.Vector( 4.0, 0.0,  0.0)
        e0 = Part.makeLine(p0, p1)
        e1 = Part.makeLine(p1, p2)
        e2 = Part.makeLine(p2, p3)
        e3 = Part.makeLine(p3, p0)
        aWire = Part.Wire([e0, e1, e2, e3])
        aFace = Part.Face(aWire)
        aBearing = aFace.revolve(Base.Vector(0.0, 0.0, 0.0), Base.Vector(0.0, 0.0, 1.0), 360)

        ScrewObj = doc.addObject("Part::Feature")
        ScrewObj.Label = "BB608"
        ScrewObj.Shape = aBearing

        doc.recompute()
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand("AddBearing608", CmdAddBearing608())


