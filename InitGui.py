# -*- coding: utf-8 -*-
###################################################################################
#
#  InitGui.py
#  
#  Copyright 2022 Matthias Melcher <github at matthiasm dot com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
###################################################################################

import bswb_locator
bsWBpath = os.path.dirname(bswb_locator.__file__)
bsWB_icons_path =  os.path.join( bsWBpath, 'Icons')

global main_bsWB_Icon
main_bsWB_Icon = os.path.join( bsWB_icons_path , 'BSLogo.svg')

BEARINGSWB_VERSION = 'V0.0.2'



class BearingsWorkbench (Workbench):
 
    global main_bsWB_Icon
    
    MenuText = "Bearings"
    ToolTip = "Create Rolling Bearings"
    Icon = main_bsWB_Icon

    list = []
 
    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import os
        import Bwb6BallBearings
#        import BearingsBase # , FSScrewCalc, PEMInserts, FastenersCmd, FSNuts
#        import CountersunkHoles, FSChangeParams
        self.list.extend(Bwb6BallBearings.getCommands())
#        cmdlist = BearingsBase.BSGetCommands("command")
        self.appendToolbar("FS Commands", self.list)
        self.appendMenu("Bearings", self.list) # creates a new menu
##        self.appendMenu("Bearings",cmdlist) # creates a new menu
#        self.list.extend(cmdlist)
#        screwlist1 = FastenerBase.FSGetCommands("screws")
#        screwlist = []
#        for cmd in screwlist1:
#          #FreeCAD.Console.PrintLog("Append toolbar " + str(cmd) + "\n")
#          if isinstance(cmd, tuple): # group in sub toolbars
#            self.appendToolbar(cmd[0],cmd[1])
#            self.list.extend(cmd[1])
#            self.appendMenu(["Fasteners","Add " + cmd[2]],cmd[1])
#          else:
#            screwlist.append(cmd)
#            self.appendMenu(["Fasteners","Add Fasteners"],cmd)
#        if len(screwlist) > 0:
#          self.appendToolbar("FS Screws",screwlist) # creates main screw toolbar
#          self.list.extend(screwlist)
#        FreeCADGui.addIconPath(BearingsBase.iconPath)
#        FreeCADGui.addPreferencePage( os.path.join( FastenerBase.__dir__, 'FSprefs.ui'),'Fasteners' )

#        self.list = ["MyCommand1", "MyCommand2"] # A list of command names created in the line above
#        self.appendToolbar("My Commands",self.list) # creates a new toolbar with your commands
#        self.appendMenu("My New Menu",self.list) # creates a new menu
#        self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu
        return
 
    def Activated(self):
        "This function is executed when the workbench is activated"
        return
 
    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return
 
    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("Bearings",self.list) # add commands to the context menu
 
    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
 
Gui.addWorkbench(BearingsWorkbench())
