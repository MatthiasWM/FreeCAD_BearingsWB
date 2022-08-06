
import os

import errno
import FreeCAD, FreeCADGui, Part, math, os
from FreeCAD import Base
import DraftVecUtils
from pathlib import Path

if FreeCAD.GuiUp:
    import FreeCADGui
    import Bwb6Dialog
    from PySide import QtCore, QtGui
    from FreeCADGui import PySideUic as uic

import Bwb6Table

def getCommands():
  return ["AddBearing608"]


__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Icons' )

# retrieved_elements = list(filter(lambda x: 'Bird' in x, animals))

def PrettyName(bb):
    return "{}: {}x{}x{}".format( bb['name'], bb['d'], bb['D'], bb['B'] )

class Bearing:

    avoidRecursion = False
    designationChecked = True

    # This is called if a bearing is first created.
    # It's *not* called when a scene is loaded (see: onDocumentRestored(self, obj) ??)
    def __init__(self, obj):
        '''Add some custom properties to our box feature'''
        # Add all properties needed by the Bearing class and fill it with the default 608 bearing data
        obj.addProperty("App::PropertyLength", "BoreDiameter", "Bearing", "Inner Diameter").BoreDiameter = 8.0
        obj.addProperty("App::PropertyLength", "OuterDiameter", "Bearing", "Outer Diameter").OuterDiameter = 22.0
        obj.addProperty("App::PropertyLength", "Width", "Bearing", "Total Bearing Width").Width = 7.0
        obj.addProperty("App::PropertyLength", "HousingFillet", "Bearing", "Radius of Shaft and Housing Fillet").HousingFillet = 0.3
        obj.addProperty("App::PropertyString", "Designation", "Bearing", "Basic ISO Designation").Designation = "608: 8x22x7"
        # Also switches on the onChanged callback
        obj.Proxy = self

    # Find the designation in the database and update the sizes accordingly
    def SetSizesFromDesignation(self, obj, setSizes=True):
        des = obj.Designation
        ix = des.find(':')
        if ix >= 0:
            des = des[:ix]
        FreeCAD.Console.PrintMessage("MATT: Find database entry for <" + des + "> \n")
        found = False
        for i in Bwb6Table.lut:
            if i['name'] == des:
                if setSizes:
                    obj.BoreDiameter = i['d']
                    obj.OuterDiameter = i['D']
                    obj.Width = i['B']
                found = True
                break
        if not found:
            FreeCAD.Console.PrintWarning("Bearing Worbench: no entry found for designation '" + des + "'.\n")
        return found

    def SetDesignationFromSizes(self, obj):
        for i in Bwb6Table.lut:
            if i['d'] == obj.BoreDiameter and i['D'] == obj.OuterDiameter and i['B'] == obj.Width:
                obj.Designation = PrettyName(i)
                return
        obj.Designation = "<not found>"
        return

    def VerifyDesignationAndSize(self, des): # TODO:
        return

    # update the Designation pulldown menu to provide a list of similar bearings
    # TODO: do this in a Bearing Task Editor!
#    def UpdateDesignationChoice(self, obj):
#        FreeCAD.Console.PrintMessage("MATT: UpdateDesignationChoice: " + obj.Designation + "\n")
#        des = obj.Designation
#        ix = des.find(':')
#        if ix >= 0:
#            des = des[:ix]
#        sameType = []
#        sameBore = []
#        sameDiameter = []
#        sameWidth = []
#        sameDesignation = [ obj.Designation ]
#        for i in Bwb6Table.lut:
#            if i['d'] == obj.BoreDiameter and i['D'] == obj.OuterDiameter and i['B'] == obj.Width:
#                if i['name'] != des:
#                  sameType.append(PrettyName(i))
#            else:
#                if i['d'] == obj.BoreDiameter:
#                    sameBore.append(PrettyName(i))
#                if i['D'] == obj.OuterDiameter:
#                    sameDiameter.append(PrettyName(i))
#                if i['B'] == obj.Width:
#                    sameWidth.append(PrettyName(i))
#        obj.Designation = sameDesignation + sameType + [ "-- Same Bore:" ] + sameBore + [ "-- Same Diameter:"] + sameDiameter + ["-- Same Width:"] + sameWidth
#        FreeCAD.Console.PrintMessage("MATT: UpdateDesignationChoice: " + obj.Designation + "\n")
#        return

#    def onDocumentRestored(self, obj): # TODO: check integrity of object for various workbench versions
#        FreeCAD.Console.PrintMessage("MATT: Bearing::onDocumentRestored\n")
#        return

    def onChanged(self, obj, prop):
        '''Do something when a property has changed'''
        FreeCAD.Console.PrintMessage("MATT: Change property: " + str(prop) + "\n")
        if (self.avoidRecursion):
            FreeCAD.Console.PrintMessage("MATT:     Avoiding recursion\n")
            return
        if not self.avoidRecursion:
            if      prop == "BoreDiameter" or \
                    prop == "OuterDiameter" or \
                    prop == "Width" or\
                    prop == "HousingFillet":
                FreeCAD.Console.PrintMessage("MATT: {}: {} {} {}\n".format(obj.Designation, obj.BoreDiameter, obj.OuterDiameter, obj.Width))
                self.avoidRecursion = True
                self.SetDesignationFromSizes(obj)
                self.avoidRecursion = False
                obj.recompute()
            if prop == "Designation":
                found = False
                self.avoidRecursion = True
                found = self.SetSizesFromDesignation(obj)
                self.avoidRecursion = False
                if found:
                    self.designationChecked = True
                    obj.recompute()
                else:
                    self.designationChecked = False
                # else give some kind of warning

    def execute(self, obj):
        '''Do something when doing a recomputation, this method is mandatory'''
        FreeCAD.Console.PrintMessage("MATT: Bearing execute\n")
        if not self.designationChecked:
            self.designationChecked = True
            found = self.SetSizesFromDesignation(obj, False)
            if not found:
              self.avoidRecursion = True
              obj.Designation = "<not found>"
              self.avoidRecursion = False
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
        FreeCAD.Console.PrintMessage("Matt: new bearing created\n")

class ViewProviderBearing:
    "A View provider for custom icon"

    def __init__(self, obj):
        obj.Proxy = self
        self.Object = obj.Object

    def attach(self, obj):
        self.ViewObject = obj
        self.Object = obj.Object
        return

    def updateData(self, fp, prop):
        return

    def setEdit(self, vobj, mode):
        FreeCAD.Console.PrintMessage("MATT: setEdit\n")
        taskd = Bwb6Dialog.BearingTaskPanel(self.Object, mode)
        taskd.obj = vobj.Object
        taskd.update()
        FreeCADGui.Control.showDialog(taskd)
        return True

    def unsetEdit(self,vobj,mode):
        FreeCAD.Console.PrintMessage("MATT: unsetEdit\n")
        FreeCADGui.Control.closeDialog()
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
        FreeCAD.Console.PrintMessage("MATT: __getstate__\n")
        return None

    def __setstate__(self, state):
        import FreeCAD
        FreeCAD.Console.PrintMessage("MATT: __setstate__\n")
        if state is not None:
            import FreeCAD
            doc = FreeCAD.ActiveDocument
            self.Object = doc.getObject(state['ObjectName'])

    def getIcon(self):
# TODO:        return ":/icons/PartDesign_Sprocket.svg"
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
        FreeCADGui.doCommand("Gui.activeDocument().setEdit(App.ActiveDocument.ActiveObject.Name,0)")
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return FreeCAD.ActiveDocument is not None

FreeCADGui.addCommand("AddBearing608", CmdAddBearing608())


