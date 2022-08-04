
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


class Bearing:
    def __init__(self, obj):
        '''Add some custom properties to our box feature'''
        obj.addProperty("App::PropertyLength", "BoreDiameter", "Bearing", "Inner Diameter").BoreDiameter = 8.0
        obj.addProperty("App::PropertyLength", "OuterDiameter", "Bearing", "Outer Diameter").OuterDiameter = 22.0
        obj.addProperty("App::PropertyLength", "Width", "Bearing", "Total Bearing Width").Width = 7.0
        obj.Proxy = self

    def onChanged(self, obj, prop):
        '''Do something when a property has changed'''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        if prop == "BoreDiameter" or prop == "OuterDiameter" or prop == "Width" :
          self.execute(obj)

    def execute(self, obj):
        '''Do something when doing a recomputation, this method is mandatory'''
        p0 = Base.Vector( obj.BoreDiameter,  0.0,  obj.Width)
        p1 = Base.Vector( obj.OuterDiameter, 0.0,  obj.Width)
        p2 = Base.Vector( obj.OuterDiameter, 0.0,  0.0)
        p3 = Base.Vector( obj.BoreDiameter,  0.0,  0.0)
        e0 = Part.makeLine(p0, p1)
        e1 = Part.makeLine(p1, p2)
        e2 = Part.makeLine(p2, p3)
        e3 = Part.makeLine(p3, p0)
        aWire = Part.Wire([e0, e1, e2, e3])
        aFace = Part.Face(aWire)
        aBearing = aFace.revolve(Base.Vector(0.0, 0.0, 0.0), Base.Vector(0.0, 0.0, 1.0), 360)
        obj.Shape = aBearing
        FreeCAD.Console.PrintMessage("Recompute Python Box feature\n")

class ViewProviderBearing:
    "A View provider for custom icon"

    def __init__(self, obj):
        obj.Proxy = self
        self.Object = obj.Object

    def attach(self, obj):
        self.Object = obj.Object
        return

    def updateData(self, fp, prop):
        return

    def getDisplayModes(self, obj):
        modes = []
        return modes

    def setDisplayMode(self, mode):
        return mode

    def onChanged(self, vp, prop):
        return

    def __getstate__(self):
        #        return {'ObjectName' : self.Object.Name}
        return None

    def __setstate__(self, state):
        if state is not None:
            import FreeCAD
            doc = FreeCAD.ActiveDocument
            self.Object = doc.getObject(state['ObjectName'])

    def getIcon(self):
#        if hasattr(self.Object, "type"):
#            return os.path.join(iconPath, self.Object.type + '.svg')
#        elif hasattr(self.Object.Proxy, "type"):
#            return os.path.join(iconPath, self.Object.Proxy.type + '.svg')
        # default to ISO4017.svg
        return os.path.join(iconPath, 'BSLogo.svg')


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
        doc = FreeCAD.activeDocument() # TODO: is there one active?
#        self.moveScrew(ScrewObj) # attach the Bearing to a selected round feature (see screw_maker.py)

        ScrewObj = doc.addObject("Part::FeaturePython", "BB608")
        bb = Bearing(ScrewObj)
#        ScrewObj.Label = ScrewObj.Proxy.itemText
        ViewProviderBearing(ScrewObj.ViewObject)
#        ViewProviderBox(a.ViewObject)
#        ScrewObj = doc.addObject("Part::FeaturePython", "BB608")
#        ScrewObj.Label = "BB608"
#        ScrewObj.Shape = aBearing
#        ScrewObj.addProperty("App::PropertyLength", "InnerDiameter", "Bearing", "Inner Diameter").InnerDiameter = 8.0

        doc.recompute()
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand("AddBearing608", CmdAddBearing608())


