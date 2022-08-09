
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

__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Icons' )


def getCommands():
  return ["AddBearing608"]

def PrettyName(bb):
    return "{}: {}x{}x{}".format( bb['name'], bb['d'], bb['D'], bb['B'] )

def ShortDesignation(obj):
    des = obj.Designation
    ix = des.find(':')
    if ix >= 0:
        des = des[:ix]
    return des


class Bearing:

    avoidRecursion = False

    def __init__(self, obj):
        '''
        Add Bearing Properties
        This is called if a bearing is first created.
        It's *not* called when a scene is loaded (see: onDocumentRestored(self, obj) ??)
        '''
        obj.addProperty("App::PropertyEnumeration", "Designation", "Bearing", \
            "Basic ISO Designation")
        obj.Designation = [ "608: 8x22x7", "628: 8x24x8", "abc"]
        obj.Designation = "608: 8x22x7"
        obj.addProperty("App::PropertyEnumeration", "DesignationStatus", "Bearing", \
            "Reflects if the designation was found in the database and if the sizes match the designation")
        obj.DesignationStatus = [ "Match", "Not Found", "Invalid", "Unknown" ]
        obj.DesignationStatus = "Unknown"
        obj.setEditorMode("DesignationStatus", 1)

        obj.addProperty("App::PropertyLength", "BoreDiameter", "Bearing", \
            "Diameter of the inner bore").BoreDiameter = 8.0
        obj.addProperty("App::PropertyLength", "OuterDiameter", "Bearing", \
            "Outer Diameter of the bearing without flanges or rings").OuterDiameter = 22.0
        obj.addProperty("App::PropertyLength", "Width", "Bearing", \
            "Total Bearing Width").Width = 7.0
        obj.addProperty("App::PropertyLength", "HousingFillet", "Bearing",
            "Radius of Shaft and Housing Fillet").HousingFillet = 0.3

        self.UpdateDesignationStatus(obj)
        self.UpdateDesignationChoice(obj)

        # Link to actual object
        obj.Proxy = self    # also switches on the onChanged callback

    def onDocumentRestored(self, obj):
        '''
        This is called when the bearing data is read from a file.
        '''
        # TODO: add missing properties
        self.UpdateDesignationStatus(obj)
        self.UpdateDesignationChoice(obj)
        pass

    def onChanged(self, obj, prop):
        '''
        If one of our custom properties changes, update other properties
        as needed and ask FreeCAD to recompute the model if needed.
        '''
        FreeCAD.Console.PrintMessage("MATT: onChanged: " + str(prop) + "\n")
        if not self.avoidRecursion:
            if prop in ["BoreDiameter", "OuterDiameter", "Width"]:
                self.avoidRecursion = True
                self.UpdateDesignationStatus(obj)
                if self.SetDesignationFromSizes(obj):
                    self.UpdateDesignationStatus(obj)
                    self.UpdateDesignationChoice(obj)
                obj.recompute()
                self.avoidRecursion = False
            if prop == "Designation":
                self.avoidRecursion = True
                if self.SetSizesFromDesignation(obj):
                    obj.recompute()
                # FIXME: the code below makes sure that choice of Designations is updated immediatly
                # instead, we must convice the UI somehow to this in a less intrusive way
                dd = obj.Designation
                obj.removeProperty("Designation")
                obj.addProperty("App::PropertyEnumeration", "Designation", "Bearing", "Basic ISO Designation")
                obj.Designation = [ dd ]
                obj.Designation = dd
                self.UpdateDesignationStatus(obj)
                self.UpdateDesignationChoice(obj)
                self.avoidRecursion = False

    def execute(self, obj):
        '''
        Build a 3D model of the bearing.
        Make sure that the properties are valid to generate a bearing.
        Draw the section of the bearing in X/Z and revolve around the Z axis.
        '''
        FreeCAD.Console.PrintMessage("MATT: Bearing execute\n")
        # TODO: we may want to add different rendering qualities here
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

        obj.Shape = aBearing
        FreeCAD.Console.PrintMessage("Matt: new bearing created\n")

    def SetSizesFromDesignation(self, obj):
        '''
        Find the designation in the database and update the sizes accordingly
        '''
        des = ShortDesignation(obj)
        for i in Bwb6Table.lut:
            if i['name'] == des:
                obj.BoreDiameter = i['d']
                obj.OuterDiameter = i['D']
                obj.Width = i['B']
                return True
        return False

    def SetDesignationFromSizes(self, obj):
        for i in Bwb6Table.lut:
            if i['d'] == obj.BoreDiameter and i['D'] == obj.OuterDiameter and i['B'] == obj.Width:
                pn = PrettyName(i)
                obj.Designation = [ pn ]
                obj.Designation = pn
                return True
        return False

    def UpdateDesignationStatus(self, obj):
        FreeCAD.Console.PrintMessage("MATT: UpdateDesignationStatus: " + obj.Designation + "\n")
        des = ShortDesignation(obj)
        for i in Bwb6Table.lut:
            if i['name']==des:
                if i['d'] != obj.BoreDiameter \
                or i['D'] != obj.OuterDiameter \
                or i['B'] != obj.Width:
                    obj.DesignationStatus = "Invalid"
                else:
                    obj.DesignationStatus = "Match"
                return
        obj.DesignationStatus = "Not Found"

    def UpdateDesignationChoice(self, obj):
        '''
        Update the Designation pulldown menu to provide a list of similar bearings
        '''
        FreeCAD.Console.PrintMessage("MATT: UpdateDesignationChoice: " + obj.Designation + "\n")
        des = ShortDesignation(obj)
        sameType = []
        sameBore = []
        sameDiameter = []
        sameWidth = []
        sameDesignation = [ obj.Designation ]
        for i in Bwb6Table.lut:
            if i['d'] == obj.BoreDiameter and i['D'] == obj.OuterDiameter and i['B'] == obj.Width:
                if i['name'] != des:
                  sameType.append(PrettyName(i))
            else:
                if i['d'] == obj.BoreDiameter:
                    sameBore.append(PrettyName(i))
                if i['D'] == obj.OuterDiameter:
                    sameDiameter.append(PrettyName(i))
                if i['B'] == obj.Width:
                    sameWidth.append(PrettyName(i))
        obj.Designation = sameDesignation + sameType + [ "  -- Same Bore:" ] + sameBore + [ "  -- Same Diameter:"] + sameDiameter + ["  -- Same Width:"] + sameWidth
        FreeCAD.Console.PrintMessage("MATT: UpdateDesignationChoice: " + obj.Designation + "\n")
        return

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
        # TODO: finish the Task Panel only when the Property implementation is perfect
#        taskd = Bwb6Dialog.BearingTaskPanel(self.Object, mode)
#        taskd.obj = vobj.Object
#        taskd.update()
#        FreeCADGui.Control.showDialog(taskd)
        return True

    def unsetEdit(self,vobj,mode):
#        FreeCAD.Console.PrintMessage("MATT: unsetEdit\n")
#        FreeCADGui.Control.closeDialog()
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
    '''
    Add a Deep Groove Ball Bearing
    '''

    def GetResources(self):
        return {"Pixmap"  : os.path.join(iconPath, "BSLogo.svg"), # the name of a svg file available in the resources
                #"Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": "Add Deep Groove Ball Bearing",
                "ToolTip" : "Add a metric deep groove ball bearing to the document"}

    def Activated(self):
        """Do something here"""
        FreeCAD.Console.PrintMessage("I guess we should generate and add a bearing now.\n")
        # The 608 bearing is inner d 8, outer D 22, width B 7, dh 10, ds 20, r=0.3, R=0.3, d1 12.15, D1 19.2
        doc = FreeCAD.activeDocument() # TODO: is there one active?
#        self.moveScrew(ScrewObj) # attach the Bearing to a selected round feature (see screw_maker.py)
        newBearing = doc.addObject("Part::FeaturePython", "Deep_Groove_Ball_Bearing")
        bb = Bearing(newBearing)
#        ScrewObj.Label = ScrewObj.Proxy.itemText
        ViewProviderBearing(newBearing.ViewObject)
        doc.recompute()
#        FreeCADGui.doCommand("Gui.activeDocument().setEdit(App.ActiveDocument.ActiveObject.Name,0)")
        return

    def IsActive(self):
        '''
        Activate the command if there is a document loaded
        '''
        return FreeCAD.ActiveDocument is not None

FreeCADGui.addCommand("AddBearing608", CmdAddBearing608())


