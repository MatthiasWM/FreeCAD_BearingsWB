
import os

import errno
import FreeCAD, FreeCADGui, Part, math, os
from FreeCAD import Base
import DraftVecUtils
from pathlib import Path

import Bwb6Table

def getCommands():
  return ["AddBearing608"]


__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Icons' )

# retrieved_elements = list(filter(lambda x: 'Bird' in x, animals))

def PrettyName(bb):
    return "{}: {}x{}x{}".format( bb['name'], bb['d'], bb['D'], bb['B'] )

class Bearing:
    def __init__(self, obj):
        '''Add some custom properties to our box feature'''
        obj.addProperty("App::PropertyLength", "BoreDiameter", "Bearing", "Inner Diameter").BoreDiameter = 8.0
        obj.addProperty("App::PropertyLength", "OuterDiameter", "Bearing", "Outer Diameter").OuterDiameter = 22.0
        obj.addProperty("App::PropertyLength", "Width", "Bearing", "Total Bearing Width").Width = 7.0
        obj.addProperty("App::PropertyLength", "HousingFillet", "Bearing", "Radius of Shaft and Housing Fillet").HousingFillet = 0.3
#        obj.addProperty("App::PropertyEnumeration", "RenderQuality", "Bearing", "Level of Detail in Model")
#        obj.RenderQuality = [ "minimal", "good", "detailed" ]
#        obj.RenderQuality = "good"

        obj.addProperty("App::PropertyEnumeration", "Designation", "Bearing", "Basic ISO Designation")
        designationChoice = [ "608" ]
        for i in Bwb6Table.lut:
            if i['d'] == obj.BoreDiameter:
                designationChoice.append( "Same Bore|" + PrettyName(i))
        for i in Bwb6Table.lut:
            if i['D'] == obj.OuterDiameter:
                designationChoice.append( "Same Diameter|" + PrettyName(i))
        for i in Bwb6Table.lut:
            if i['B'] == obj.Width:
                designationChoice.append( "Same Width|" + PrettyName(i))
        obj.Designation = designationChoice
        obj.Designation = "608"
        obj.Proxy = self

    def SizeFromDesignation(self, des): # TODO:

    def DesignationFromSize(self): # TODO:

    def UpdateDesignationChoice(self): # TODO:

    def onChanged(self, obj, prop):
        '''Do something when a property has changed'''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        if  prop == "BoreDiameter" or \
            prop == "OuterDiameter" or \
            prop == "Width" \
            or prop == "HousingFillet":
          self.execute(obj)

    def execute(self, obj):
        '''Do something when doing a recomputation, this method is mandatory'''
#if SIMPLE
#        p0 = Base.Vector( obj.BoreDiameter/2.0,  0.0,  obj.Width)
#        p1 = Base.Vector( obj.OuterDiameter/2.0, 0.0,  obj.Width)
#        p2 = Base.Vector( obj.OuterDiameter/2.0, 0.0,  0.0)
#        p3 = Base.Vector( obj.BoreDiameter/2.0,  0.0,  0.0)
#        e0 = Part.makeLine(p0, p1)
#        e1 = Part.makeLine(p1, p2)
#        e2 = Part.makeLine(p2, p3)
#        e3 = Part.makeLine(p3, p0)
#        aWire = Part.Wire([e0, e1, e2, e3])
#else if GOOD
        ri = obj.BoreDiameter/2
        ro = obj.OuterDiameter/2
        w = obj.Width
        f = obj.HousingFillet
        ff = f*0.292893218813452 # 1-sin(45)
        h = (ro-ri)/4.0

        ## --- How to draw a section of a sealed ball bearing
        p = []
        e = []
        i = 0
        # -- bottom surface
        p.append(Base.Vector(ro, 0.0, f))
        p.append(Base.Vector(ro-ff, 0.0, ff))
        p.append(Base.Vector(ro-f, 0.0, 0.0))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # top right fillet
        p.append(Base.Vector(ro-h+f, 0.0, 0.0))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # top right surface
        p.append(Base.Vector(ro-h+ff, 0.0, ff))
        p.append(Base.Vector(ro-h, 0.0, f))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # outer shell bottom right fillet
        p.append(Base.Vector(ro-h-f, 0.0, 0))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # seal outer edge
        p.append(Base.Vector(ri+h+f, 0.0, 0))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # seal side
        p.append(Base.Vector(ri+h, 0.0, f))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # seal inner edge
        p.append(Base.Vector(ri+h-ff, 0.0, ff))
        p.append(Base.Vector(ri+h-f, 0.0, 0.0))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # inner shell top right fillet
        p.append(Base.Vector(ri+f, 0.0, 0))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # inner shell right side
        p.append(Base.Vector(ri+ff, 0.0, ff))
        p.append(Base.Vector(ri, 0.0, f))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # inner shell bottom right fillet
        # -- mirror the top surface
        p.append(Base.Vector(ri, 0.0, w-f))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # inner shell right side
        p.append(Base.Vector(ri+ff, 0.0, w-ff))
        p.append(Base.Vector(ri+f, 0.0, w))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # inner shell bottom left fillet
        p.append(Base.Vector(ri+h-f, 0.0, w))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # inner shell left side
        p.append(Base.Vector(ri+h-ff, 0.0, w-ff))
        p.append(Base.Vector(ri+h, 0.0, w-f))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # inner shell top right fillet
        p.append(Base.Vector(ri+h+f, 0.0, w))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # seal inner edge
        p.append(Base.Vector(ro-h-f, 0.0, w))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # seal side
        p.append(Base.Vector(ro-h, 0.0, w-f))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # seal outer edge
        p.append(Base.Vector(ro-h+ff, 0.0, w-ff))
        p.append(Base.Vector(ro-h+f, 0.0, w))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # outer shell bottom left fillet
        p.append(Base.Vector(ro-f, 0.0, w))
        e.append(Part.makeLine(p[i], p[i+1])); i+=1 # top right surface
        p.append(Base.Vector(ro-ff, 0.0, w-ff))
        p.append(Base.Vector(ro, 0.0, w-f))
        e.append(Part.Arc(p[i], p[i+1], p[i+2]).toShape()); i+=2 # top left fillet
        e.append(Part.makeLine(p[i], p[0])); i+=1 # close the surface (top)
        aWire = Part.Wire(e)
        aBearing = aWire.revolve(Base.Vector(0.0, 0.0, 0.0), Base.Vector(0.0, 0.0, 1.0), 360)
#else if DETAILED
            # if we go crazy, we can draw the balls here
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
        doc.recompute()
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return FreeCAD.ActiveDocument is not None

FreeCADGui.addCommand("AddBearing608", CmdAddBearing608())


