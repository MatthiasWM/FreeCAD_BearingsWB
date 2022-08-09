# FreeCAD Bearings Workbench

<!-- add Python code quality alerts here -->

A FreeCAD Workbench to Add/Attach various Bearings to Parts  

<!-- add animated gif (screencast) of using the workbench -->

## Installation

### Addon Manager
Add the path `https://github.com/MatthiasWM/FreeCAD_BearingsWB` in the Addon 
Manager Preferences under Custom Repositories.
You can then use the [Addon Manager](https://github.com/FreeCAD/FreeCAD-addons/#1-builtin-addon-manager) 
to seamlessly install the Bearings Workbench.

## Usage

### Quick Start

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

## Supported Bearing Types

### Bearing Workbench 5: Deep Groove Ball Bearings (metric)

Deep groove ball bearings are mainly defined by their bore diameter, their
outer diameter and their width. ISO defines a Designation for all standard 
sizes. For example, "608" is the designation for a bearing with an 8m bore,
a 22mm outer diameter, and a 7mm width. The WB will set the Designation as 
"608: 8x22x7" and create a 3d model of a bearing of that size.
The Designation does not define the inner workings of a bearing, such as the 
number of balls.

**Not yet**: The workbench also supports flanges and grooves with or without 
a matching ring. Pleas note that the database contains a list of common bearing 
sizes and attributes, but sizes beyond bore/diameter/width are not standardised. 
For example, the flange width of a bearing can vary considerably depending on 
the manufacturer.

The bearing workbench uses the size values in the Data Properties to generate
the 3d representation of the bearing to allow for non-standard bearing sizes. 
The Designation property is not relevant and should only be seen as a hint.
The Designation Status property will do its best to reflect the validity of
the Designation property.

#### Properties

* Designation (Enumeration)
* Designation Status (Enumeration)
* Bore Diameter (Length)
* Outer Diameter (Length)
* Width (Length)
* Housing Fillet - estimated, experimental
* (Flange Diameter)
* (Flange Width)
* (Groove Offset)
* (Groove Width)
* (Groove Diamter)
* (Ring Diameter)
* (Axial Offset)
* (Flipped)

## To do

* vectorize `Icons/BSLogo.svg` and all other incoming icons
* set the icon colors to dark orange for metric and dark cyan for imperial
* add screencast and screen shots for this README 
* add "Tasks" dialog to browse database (or use custom pulldown menus)
* add bearing features (covers, grooves, material, flange, seal, clearance, lubricant...)
* add BOM that works with linked objects
* add function to align bearings to other concentric object
* add a clearance/distance property
* add a flip property

## Release Notes

* V0.0.03  09 Aug 2022:  Property editor allow user to select bearings from a list of 400
* V0.0.02  04 Aug 2022:  A 608 ball bearing can be created, edited, and saved 
* V0.0.01  04 Aug 2022:  Initial version 

<!-- ### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) -->

## License

GPLv2
