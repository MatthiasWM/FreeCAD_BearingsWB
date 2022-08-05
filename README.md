# FreeCAD Bearings Workbench

<!-- add Python code quality alerts here -->

A FreeCAD Workbench to Add/Attach various Bearings to Parts  

<!-- add animated gif (screencast) of using the workbench -->

### Installation

#### Addon Manager
Add the path `https://github.com/MatthiasWM/FreeCAD_BearingsWB` in the Addon 
Manager Preferences under Custom Repositories.
You can then use the [Addon Manager](https://github.com/FreeCAD/FreeCAD-addons/#1-builtin-addon-manager) 
to seamlessly install the Bearings Workbench.

### Usage

#### Quick Start

Select the Bearings Workbench. A very short menu and a single toolbox icon 
will apear. Clicking either will generate a "608" deep groove ball bearing
(also known as the "skate bearing"). 

The bearing properties can be modified in the properties editor. If the size
is change to a known value (e.g. 5x19x6 for a 635 bearing), the Designation 
Property will be updated.
 
The Designation Property is a text field that can be edited. If a know 
Designation is entered ("626" for example), the size of the bearing is updated.

A "Tasks" dialog box is under development that will suggest standard bearings
based on the given sizes in a more interactive manner.

Other bearing type will be added when they deep groove ball bearing 
implementation is sufficiently complete.

<!-- No official Wiki at this point: ### Official Wiki https://www.freecadweb.org/wiki/Bearings_Workbench -->
 
<!-- <details>
  <summary><i>Expand this section for a synopsis on how to use this workbench</i></summary> 

No details yet.

</details> -->

#### To do:
* vectorize `Icons/BSLogo.svg` and all other incoming icons
* set the icon colors to dark orange for metric and dark cyan for imperial
* add screencast and screen shots for this README 
* add database selection dialog box
* add "Tasks" dialog to browse database
* add bearing features (covers, grooves, material, flange, seal, clearance, lubricant...)
* add BOM that works with linked objects

#### Release Notes 
* V0.0.02  04 Aug 2022:  A 608 ball bearing can be created, edited, and saved 
* V0.0.01  04 Aug 2022:  Initial version 

<!-- ### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) -->

### License
GPLv2
