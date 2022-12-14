#
# Category 6: deep grove ball bearings
#
# designation: mandatory
# 'd': mandatory, bore diameter
# D: mandatory, outside diameter
# 'B': mandatory, width
# d1: shoudler diameter
# D2: recess diameter
# ra: shaft and housig fillet
# da: shaft abutment
# Da: housing abutment
# 'F': has flange (F needs a record to describe the actual size of the flange, i.e 'F':{width: 1, h:1.5})
# 'NR': has slot/snap ring (NR needs a record to describe the slot and snap ring size and position)
#
# Unsupported or isufficiently supported
# flange, slot, snap ring, snap ring groove
# single or double row
# seals: one side or two sides, contact or low friction


lut = [
    { 'name':"16001", 'd':12, 'D':28, 'B':7, 'NR':0, 'F':0 },
    { 'name':"16002", 'd':15, 'D':32, 'B':8, 'NR':0, 'F':0 },
    { 'name':"16003", 'd':17, 'D':35, 'B':8, 'NR':0, 'F':0 },
    { 'name':"16004", 'd':20, 'D':42, 'B':8, 'NR':0, 'F':0 },
    { 'name':"16005", 'd':25, 'D':47, 'B':8, 'NR':0, 'F':0 },
    { 'name':"16006", 'd':30, 'D':55, 'B':9, 'NR':0, 'F':0 },
    { 'name':"16007", 'd':35, 'D':62, 'B':9, 'NR':0, 'F':0 },
    { 'name':"16008", 'd':40, 'D':68, 'B':9, 'NR':0, 'F':0 },
    { 'name':"16009", 'd':45, 'D':75, 'B':10, 'NR':0, 'F':0 },
    { 'name':"16010", 'd':50, 'D':80, 'B':10, 'NR':0, 'F':0 },
    { 'name':"16011", 'd':55, 'D':90, 'B':11, 'NR':0, 'F':0 },
    { 'name':"16012", 'd':60, 'D':95, 'B':11, 'NR':0, 'F':0 },
    { 'name':"16013", 'd':65, 'D':100, 'B':11, 'NR':0, 'F':0 },
    { 'name':"16014", 'd':70, 'D':110, 'B':13, 'NR':0, 'F':0 },
    { 'name':"16015", 'd':75, 'D':115, 'B':13, 'NR':0, 'F':0 },
    { 'name':"16016", 'd':80, 'D':125, 'B':14, 'NR':0, 'F':0 },
    { 'name':"16017", 'd':85, 'D':130, 'B':14, 'NR':0, 'F':0 },
    { 'name':"16018", 'd':90, 'D':140, 'B':16, 'NR':0, 'F':0 },
    { 'name':"16019", 'd':95, 'D':145, 'B':16, 'NR':0, 'F':0 },
    { 'name':"16020", 'd':100, 'D':150, 'B':16, 'NR':0, 'F':0 },
    { 'name':"16021", 'd':105, 'D':160, 'B':18, 'NR':0, 'F':0 },
    { 'name':"16024", 'd':120, 'D':180, 'B':19, 'NR':0, 'F':0 },
    { 'name':"16026", 'd':130, 'D':200, 'B':22, 'NR':0, 'F':0 },
    { 'name':"16028", 'd':140, 'D':210, 'B':22, 'NR':0, 'F':0 },
    { 'name':"16030", 'd':150, 'D':225, 'B':24, 'NR':0, 'F':0 },
    { 'name':"16034", 'd':170, 'D':260, 'B':28, 'NR':0, 'F':0 },
    { 'name':"16100", 'd':10, 'D':28, 'B':8, 'NR':0, 'F':0 },
    { 'name':"16101", 'd':12, 'D':30, 'B':8, 'NR':0, 'F':0 },
    { 'name':"60/22", 'd':22, 'D':44, 'B':12, 'NR':0, 'F':0 },
    { 'name':"60/32", 'd':32, 'D':58, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6000", 'd':10, 'D':26, 'B':8, 'NR':0, 'F':0 },
    { 'name':"6000-NR", 'd':10, 'D':26, 'B':8, 'NR':1, 'F':0 },
    { 'name':"6001", 'd':12, 'D':28, 'B':8, 'NR':0, 'F':0 },
    { 'name':"6001-NR", 'd':12, 'D':28, 'B':8, 'NR':1, 'F':0 },
    { 'name':"6002", 'd':15, 'D':32, 'B':9, 'NR':0, 'F':0 },
    { 'name':"6002-NR", 'd':15, 'D':32, 'B':9, 'NR':1, 'F':0 },
    { 'name':"6003", 'd':17, 'D':35, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6003-NR", 'd':17, 'D':35, 'B':10, 'NR':1, 'F':0 },
    { 'name':"6004", 'd':20, 'D':42, 'B':12, 'NR':0, 'F':0 },
    { 'name':"6004-NR", 'd':20, 'D':42, 'B':12, 'NR':1, 'F':0 },
    { 'name':"6005", 'd':25, 'D':47, 'B':12, 'NR':0, 'F':0 },
    { 'name':"6005-NR", 'd':25, 'D':47, 'B':12, 'NR':1, 'F':0 },
    { 'name':"6006", 'd':30, 'D':55, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6006-NR", 'd':30, 'D':55, 'B':13, 'NR':1, 'F':0 },
    { 'name':"6007", 'd':35, 'D':62, 'B':14, 'NR':0, 'F':0 },
    { 'name':"6007-NR", 'd':35, 'D':62, 'B':14, 'NR':1, 'F':0 },
    { 'name':"6008", 'd':40, 'D':68, 'B':15, 'NR':0, 'F':0 },
    { 'name':"6008-NR", 'd':40, 'D':68, 'B':15, 'NR':1, 'F':0 },
    { 'name':"6009", 'd':45, 'D':75, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6009-NR", 'd':45, 'D':75, 'B':16, 'NR':1, 'F':0 },
    { 'name':"6010", 'd':50, 'D':80, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6010-NR", 'd':50, 'D':80, 'B':16, 'NR':1, 'F':0 },
    { 'name':"6011", 'd':55, 'D':90, 'B':18, 'NR':0, 'F':0 },
    { 'name':"6012", 'd':60, 'D':95, 'B':18, 'NR':0, 'F':0 },
    { 'name':"6013", 'd':65, 'D':100, 'B':18, 'NR':0, 'F':0 },
    { 'name':"6014", 'd':70, 'D':110, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6015", 'd':75, 'D':115, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6016", 'd':80, 'D':125, 'B':22, 'NR':0, 'F':0 },
    { 'name':"6017", 'd':85, 'D':130, 'B':22, 'NR':0, 'F':0 },
    { 'name':"6018", 'd':90, 'D':140, 'B':24, 'NR':0, 'F':0 },
    { 'name':"6019", 'd':95, 'D':145, 'B':24, 'NR':0, 'F':0 },
    { 'name':"6020", 'd':100, 'D':150, 'B':24, 'NR':0, 'F':0 },
    { 'name':"6021", 'd':105, 'D':160, 'B':26, 'NR':0, 'F':0 },
    { 'name':"6022", 'd':110, 'D':170, 'B':28, 'NR':0, 'F':0 },
    { 'name':"6024", 'd':120, 'D':180, 'B':28, 'NR':0, 'F':0 },
    { 'name':"6026", 'd':130, 'D':200, 'B':33, 'NR':0, 'F':0 },
    { 'name':"6028", 'd':140, 'D':210, 'B':33, 'NR':0, 'F':0 },
    { 'name':"603", 'd':3, 'D':9, 'B':5, 'NR':0, 'F':0 },
    { 'name':"6030", 'd':150, 'D':225, 'B':35, 'NR':0, 'F':0 },
    { 'name':"6032", 'd':160, 'D':240, 'B':38, 'NR':0, 'F':0 },
    { 'name':"604", 'd':4, 'D':12, 'B':4, 'NR':0, 'F':0 },
    { 'name':"605", 'd':5, 'D':14, 'B':5, 'NR':0, 'F':0 },
    { 'name':"606", 'd':6, 'D':17, 'B':6, 'NR':0, 'F':0 },
    { 'name':"607", 'd':7, 'D':19, 'B':6, 'NR':0, 'F':0 },
    { 'name':"608", 'd':8, 'D':22, 'B':7, 'NR':0, 'F':0 },
    { 'name':"609", 'd':9, 'D':24, 'B':7, 'NR':0, 'F':0 },
    { 'name':"62/22", 'd':22, 'D':50, 'B':14, 'NR':0, 'F':0 },
    { 'name':"62/32", 'd':32, 'D':65, 'B':17, 'NR':0, 'F':0 },
    { 'name':"6200", 'd':10, 'D':30, 'B':9, 'NR':0, 'F':0 },
    { 'name':"6200-NR", 'd':10, 'D':30, 'B':9, 'NR':1, 'F':0 },
    { 'name':"6201", 'd':12, 'D':32, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6201-NR", 'd':12, 'D':32, 'B':10, 'NR':1, 'F':0 },
    { 'name':"6202", 'd':15, 'D':35, 'B':11, 'NR':0, 'F':0 },
    { 'name':"6202-NR", 'd':15, 'D':35, 'B':11, 'NR':1, 'F':0 },
    { 'name':"6203", 'd':17, 'D':40, 'B':12, 'NR':0, 'F':0 },
    { 'name':"6203-NR", 'd':17, 'D':40, 'B':12, 'NR':1, 'F':0 },
    { 'name':"6204", 'd':20, 'D':47, 'B':14, 'NR':0, 'F':0 },
    { 'name':"6204-NR", 'd':20, 'D':47, 'B':14, 'NR':1, 'F':0 },
    { 'name':"6205", 'd':25, 'D':52, 'B':15, 'NR':0, 'F':0 },
    { 'name':"6205-NR", 'd':25, 'D':52, 'B':15, 'NR':1, 'F':0 },
    { 'name':"6206", 'd':30, 'D':62, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6206-NR", 'd':30, 'D':62, 'B':16, 'NR':1, 'F':0 },
    { 'name':"6207", 'd':35, 'D':72, 'B':17, 'NR':0, 'F':0 },
    { 'name':"6207-NR", 'd':35, 'D':72, 'B':17, 'NR':1, 'F':0 },
    { 'name':"6208", 'd':40, 'D':80, 'B':18, 'NR':0, 'F':0 },
    { 'name':"6208-NR", 'd':40, 'D':80, 'B':18, 'NR':1, 'F':0 },
    { 'name':"6209", 'd':45, 'D':85, 'B':19, 'NR':0, 'F':0 },
    { 'name':"6209-NR", 'd':45, 'D':85, 'B':19, 'NR':1, 'F':0 },
    { 'name':"6210", 'd':50, 'D':90, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6210-NR", 'd':50, 'D':90, 'B':20, 'NR':1, 'F':0 },
    { 'name':"6211", 'd':55, 'D':100, 'B':21, 'NR':0, 'F':0 },
    { 'name':"6212", 'd':60, 'D':110, 'B':22, 'NR':0, 'F':0 },
    { 'name':"6213", 'd':65, 'D':120, 'B':23, 'NR':0, 'F':0 },
    { 'name':"6214", 'd':70, 'D':125, 'B':24, 'NR':0, 'F':0 },
    { 'name':"6215", 'd':75, 'D':130, 'B':25, 'NR':0, 'F':0 },
    { 'name':"6216", 'd':80, 'D':140, 'B':26, 'NR':0, 'F':0 },
    { 'name':"6217", 'd':85, 'D':150, 'B':28, 'NR':0, 'F':0 },
    { 'name':"6218", 'd':90, 'D':160, 'B':30, 'NR':0, 'F':0 },
    { 'name':"6219", 'd':95, 'D':170, 'B':32, 'NR':0, 'F':0 },
    { 'name':"6220", 'd':100, 'D':180, 'B':34, 'NR':0, 'F':0 },
    { 'name':"62200", 'd':10, 'D':30, 'B':14, 'NR':0, 'F':0 },
    { 'name':"62201", 'd':12, 'D':32, 'B':14, 'NR':0, 'F':0 },
    { 'name':"62202", 'd':15, 'D':35, 'B':14, 'NR':0, 'F':0 },
    { 'name':"62203", 'd':17, 'D':40, 'B':16, 'NR':0, 'F':0 },
    { 'name':"62204", 'd':20, 'D':47, 'B':18, 'NR':0, 'F':0 },
    { 'name':"62205", 'd':25, 'D':52, 'B':18, 'NR':0, 'F':0 },
    { 'name':"62206", 'd':30, 'D':62, 'B':20, 'NR':0, 'F':0 },
    { 'name':"62207", 'd':35, 'D':72, 'B':23, 'NR':0, 'F':0 },
    { 'name':"62208", 'd':40, 'D':80, 'B':23, 'NR':0, 'F':0 },
    { 'name':"62209", 'd':45, 'D':85, 'B':23, 'NR':0, 'F':0 },
    { 'name':"62210", 'd':50, 'D':90, 'B':23, 'NR':0, 'F':0 },
    { 'name':"6222", 'd':110, 'D':200, 'B':38, 'NR':0, 'F':0 },
    { 'name':"6224", 'd':120, 'D':215, 'B':40, 'NR':0, 'F':0 },
    { 'name':"6226", 'd':130, 'D':230, 'B':40, 'NR':0, 'F':0 },
    { 'name':"623", 'd':3, 'D':10, 'B':4, 'NR':0, 'F':0 },
    { 'name':"62300", 'd':10, 'D':35, 'B':17, 'NR':0, 'F':0 },
    { 'name':"62301", 'd':12, 'D':37, 'B':17, 'NR':0, 'F':0 },
    { 'name':"62302", 'd':15, 'D':42, 'B':17, 'NR':0, 'F':0 },
    { 'name':"62303", 'd':17, 'D':47, 'B':19, 'NR':0, 'F':0 },
    { 'name':"62304", 'd':20, 'D':52, 'B':21, 'NR':0, 'F':0 },
    { 'name':"62305", 'd':25, 'D':62, 'B':24, 'NR':0, 'F':0 },
    { 'name':"62306", 'd':30, 'D':72, 'B':27, 'NR':0, 'F':0 },
    { 'name':"62307", 'd':35, 'D':80, 'B':31, 'NR':0, 'F':0 },
    { 'name':"62308", 'd':40, 'D':90, 'B':33, 'NR':0, 'F':0 },
    { 'name':"62309", 'd':45, 'D':100, 'B':36, 'NR':0, 'F':0 },
    { 'name':"62310", 'd':50, 'D':110, 'B':40, 'NR':0, 'F':0 },
    { 'name':"6238", 'd':190, 'D':340, 'B':55, 'NR':0, 'F':0 },
    { 'name':"624", 'd':4, 'D':13, 'B':5, 'NR':0, 'F':0 },
    { 'name':"625", 'd':5, 'D':16, 'B':5, 'NR':0, 'F':0 },
    { 'name':"626", 'd':6, 'D':19, 'B':6, 'NR':0, 'F':0 },
    { 'name':"627", 'd':7, 'D':22, 'B':7, 'NR':0, 'F':0 },
    { 'name':"628", 'd':8, 'D':24, 'B':8, 'NR':0, 'F':0 },
    { 'name':"629", 'd':9, 'D':26, 'B':8, 'NR':0, 'F':0 },
    { 'name':"63/22", 'd':22, 'D':56, 'B':16, 'NR':0, 'F':0 },
    { 'name':"63/32", 'd':32, 'D':75, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6300", 'd':10, 'D':35, 'B':11, 'NR':0, 'F':0 },
    { 'name':"6300-NR", 'd':10, 'D':35, 'B':11, 'NR':1, 'F':0 },
    { 'name':"63000", 'd':10, 'D':26, 'B':12, 'NR':0, 'F':0 },
    { 'name':"63001", 'd':12, 'D':28, 'B':12, 'NR':0, 'F':0 },
    { 'name':"63002", 'd':15, 'D':32, 'B':13, 'NR':0, 'F':0 },
    { 'name':"63003", 'd':17, 'D':35, 'B':14, 'NR':0, 'F':0 },
    { 'name':"63004", 'd':20, 'D':42, 'B':16, 'NR':0, 'F':0 },
    { 'name':"63005", 'd':25, 'D':47, 'B':16, 'NR':0, 'F':0 },
    { 'name':"63006", 'd':30, 'D':55, 'B':19, 'NR':0, 'F':0 },
    { 'name':"63007", 'd':35, 'D':62, 'B':20, 'NR':0, 'F':0 },
    { 'name':"63008", 'd':40, 'D':68, 'B':21, 'NR':0, 'F':0 },
    { 'name':"63009", 'd':45, 'D':75, 'B':23, 'NR':0, 'F':0 },
    { 'name':"6301", 'd':12, 'D':37, 'B':12, 'NR':0, 'F':0 },
    { 'name':"6301-NR", 'd':12, 'D':37, 'B':12, 'NR':1, 'F':0 },
    { 'name':"63010", 'd':50, 'D':80, 'B':23, 'NR':0, 'F':0 },
    { 'name':"6302", 'd':15, 'D':42, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6302-NR", 'd':15, 'D':42, 'B':13, 'NR':1, 'F':0 },
    { 'name':"6303", 'd':17, 'D':47, 'B':14, 'NR':0, 'F':0 },
    { 'name':"6303-NR", 'd':17, 'D':47, 'B':14, 'NR':1, 'F':0 },
    { 'name':"6304", 'd':20, 'D':52, 'B':15, 'NR':0, 'F':0 },
    { 'name':"6304-NR", 'd':20, 'D':52, 'B':15, 'NR':1, 'F':0 },
    { 'name':"6305", 'd':25, 'D':62, 'B':17, 'NR':0, 'F':0 },
    { 'name':"6305-NR", 'd':25, 'D':62, 'B':17, 'NR':1, 'F':0 },
    { 'name':"6306", 'd':30, 'D':72, 'B':19, 'NR':0, 'F':0 },
    { 'name':"6306-NR", 'd':30, 'D':72, 'B':19, 'NR':1, 'F':0 },
    { 'name':"6307", 'd':35, 'D':80, 'B':21, 'NR':0, 'F':0 },
    { 'name':"6307-NR", 'd':35, 'D':80, 'B':21, 'NR':1, 'F':0 },
    { 'name':"6308", 'd':40, 'D':90, 'B':23, 'NR':0, 'F':0 },
    { 'name':"6308-NR", 'd':40, 'D':90, 'B':23, 'NR':1, 'F':0 },
    { 'name':"6309", 'd':45, 'D':100, 'B':25, 'NR':0, 'F':0 },
    { 'name':"6309-NR", 'd':45, 'D':100, 'B':25, 'NR':1, 'F':0 },
    { 'name':"6310", 'd':50, 'D':110, 'B':27, 'NR':0, 'F':0 },
    { 'name':"6311", 'd':55, 'D':120, 'B':29, 'NR':0, 'F':0 },
    { 'name':"6312", 'd':60, 'D':130, 'B':31, 'NR':0, 'F':0 },
    { 'name':"6313", 'd':65, 'D':140, 'B':33, 'NR':0, 'F':0 },
    { 'name':"6314", 'd':70, 'D':150, 'B':35, 'NR':0, 'F':0 },
    { 'name':"6315", 'd':75, 'D':160, 'B':37, 'NR':0, 'F':0 },
    { 'name':"634", 'd':4, 'D':16, 'B':5, 'NR':0, 'F':0 },
    { 'name':"635", 'd':5, 'D':19, 'B':6, 'NR':0, 'F':0 },
    { 'name':"636", 'd':6, 'D':22, 'B':7, 'NR':0, 'F':0 },
    { 'name':"638", 'd':8, 'D':28, 'B':9, 'NR':0, 'F':0 },
    { 'name':"63800", 'd':10, 'D':19, 'B':7, 'NR':0, 'F':0 },
    { 'name':"63801", 'd':12, 'D':21, 'B':7, 'NR':0, 'F':0 },
    { 'name':"63802", 'd':15, 'D':24, 'B':7, 'NR':0, 'F':0 },
    { 'name':"63803", 'd':17, 'D':26, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6403", 'd':17, 'D':62, 'B':17, 'NR':0, 'F':0 },
    { 'name':"6404", 'd':20, 'D':72, 'B':19, 'NR':0, 'F':0 },
    { 'name':"6405", 'd':25, 'D':80, 'B':21, 'NR':0, 'F':0 },
    { 'name':"6406", 'd':30, 'D':90, 'B':23, 'NR':0, 'F':0 },
    { 'name':"6407", 'd':35, 'D':100, 'B':25, 'NR':0, 'F':0 },
    { 'name':"6408", 'd':40, 'D':110, 'B':27, 'NR':0, 'F':0 },
    { 'name':"6409", 'd':45, 'D':120, 'B':29, 'NR':0, 'F':0 },
    { 'name':"6410", 'd':50, 'D':130, 'B':31, 'NR':0, 'F':0 },
    { 'name':"6411", 'd':55, 'D':140, 'B':33, 'NR':0, 'F':0 },
    { 'name':"6412", 'd':60, 'D':150, 'B':35, 'NR':0, 'F':0 },
    { 'name':"6413", 'd':65, 'D':160, 'B':37, 'NR':0, 'F':0 },
    { 'name':"6414", 'd':70, 'D':180, 'B':42, 'NR':0, 'F':0 },
    { 'name':"6700", 'd':10, 'D':15, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6700-W3", 'd':10, 'D':15, 'B':3, 'NR':0, 'F':0 },
    { 'name':"6701", 'd':12, 'D':18, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6702", 'd':15, 'D':21, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6703", 'd':17, 'D':23, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6704", 'd':20, 'D':27, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6705", 'd':25, 'D':32, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6705-P6-SRL", 'd':25, 'D':32, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6706", 'd':30, 'D':37, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6707", 'd':35, 'D':44, 'B':5, 'NR':0, 'F':0 },
    { 'name':"6708", 'd':40, 'D':50, 'B':6, 'NR':0, 'F':0 },
    { 'name':"6709", 'd':45, 'D':55, 'B':6, 'NR':0, 'F':0 },
    { 'name':"6710", 'd':50, 'D':62, 'B':6, 'NR':0, 'F':0 },
    { 'name':"6800", 'd':10, 'D':19, 'B':5, 'NR':0, 'F':0 },
    { 'name':"6801", 'd':12, 'D':21, 'B':5, 'NR':0, 'F':0 },
    { 'name':"6802", 'd':15, 'D':24, 'B':5, 'NR':0, 'F':0 },
    { 'name':"6803", 'd':17, 'D':26, 'B':5, 'NR':0, 'F':0 },
    { 'name':"6804", 'd':20, 'D':32, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6805", 'd':25, 'D':37, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6806", 'd':30, 'D':42, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6807", 'd':35, 'D':47, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6808", 'd':40, 'D':52, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6809", 'd':45, 'D':58, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6810", 'd':50, 'D':65, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6811", 'd':55, 'D':72, 'B':9, 'NR':0, 'F':0 },
    { 'name':"6812", 'd':60, 'D':78, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6813", 'd':65, 'D':85, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6814", 'd':70, 'D':90, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6815", 'd':75, 'D':95, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6816", 'd':80, 'D':100, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6817", 'd':85, 'D':110, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6818", 'd':90, 'D':115, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6819", 'd':95, 'D':120, 'B':13, 'NR':0, 'F':0 },
    { 'name':"682", 'd':2, 'D':5, 'B':2.3, 'NR':0, 'F':0 },
    { 'name':"682-W1.5", 'd':2, 'D':5, 'B':1.5, 'NR':0, 'F':0 },
    { 'name':"6820", 'd':100, 'D':125, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6821", 'd':105, 'D':130, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6822", 'd':110, 'D':140, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6824", 'd':120, 'D':150, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6826", 'd':130, 'D':165, 'B':18, 'NR':0, 'F':0 },
    { 'name':"6828", 'd':140, 'D':175, 'B':18, 'NR':0, 'F':0 },
    { 'name':"683", 'd':3, 'D':7, 'B':3, 'NR':0, 'F':0 },
    { 'name':"683-W2", 'd':3, 'D':7, 'B':2, 'NR':0, 'F':0 },
    { 'name':"6830", 'd':150, 'D':190, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6832", 'd':160, 'D':200, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6834", 'd':170, 'D':215, 'B':22, 'NR':0, 'F':0 },
    { 'name':"6836", 'd':180, 'D':225, 'B':22, 'NR':0, 'F':0 },
    { 'name':"6838", 'd':190, 'D':240, 'B':24, 'NR':0, 'F':0 },
    { 'name':"684", 'd':4, 'D':9, 'B':4, 'NR':0, 'F':0 },
    { 'name':"684-W2.5", 'd':4, 'D':9, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"6840", 'd':200, 'D':250, 'B':24, 'NR':0, 'F':0 },
    { 'name':"685", 'd':5, 'D':11, 'B':5, 'NR':0, 'F':0 },
    { 'name':"685-W3", 'd':5, 'D':11, 'B':3, 'NR':0, 'F':0 },
    { 'name':"686", 'd':6, 'D':13, 'B':5, 'NR':0, 'F':0 },
    { 'name':"686-W3.5", 'd':6, 'D':13, 'B':3.5, 'NR':0, 'F':0 },
    { 'name':"687", 'd':7, 'D':14, 'B':5, 'NR':0, 'F':0 },
    { 'name':"687-W3.5", 'd':7, 'D':14, 'B':3.5, 'NR':0, 'F':0 },
    { 'name':"688", 'd':8, 'D':16, 'B':5, 'NR':0, 'F':0 },
    { 'name':"688-W4", 'd':8, 'D':16, 'B':4, 'NR':0, 'F':0 },
    { 'name':"688-W6", 'd':8, 'D':16, 'B':6, 'NR':0, 'F':0 },
    { 'name':"689", 'd':9, 'D':17, 'B':5, 'NR':0, 'F':0 },
    { 'name':"689-W4", 'd':9, 'D':17, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6900", 'd':10, 'D':22, 'B':6, 'NR':0, 'F':0 },
    { 'name':"6901", 'd':12, 'D':24, 'B':6, 'NR':0, 'F':0 },
    { 'name':"6902", 'd':15, 'D':28, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6903", 'd':17, 'D':30, 'B':7, 'NR':0, 'F':0 },
    { 'name':"6904", 'd':20, 'D':37, 'B':9, 'NR':0, 'F':0 },
    { 'name':"6905", 'd':25, 'D':42, 'B':9, 'NR':0, 'F':0 },
    { 'name':"6906", 'd':30, 'D':47, 'B':9, 'NR':0, 'F':0 },
    { 'name':"6907", 'd':35, 'D':55, 'B':10, 'NR':0, 'F':0 },
    { 'name':"6908", 'd':40, 'D':62, 'B':12, 'NR':0, 'F':0 },
    { 'name':"6909", 'd':45, 'D':68, 'B':12, 'NR':0, 'F':0 },
    { 'name':"6910", 'd':50, 'D':72, 'B':12, 'NR':0, 'F':0 },
    { 'name':"6911", 'd':55, 'D':80, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6912", 'd':60, 'D':85, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6913", 'd':65, 'D':90, 'B':13, 'NR':0, 'F':0 },
    { 'name':"6914", 'd':70, 'D':100, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6915", 'd':75, 'D':105, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6916", 'd':80, 'D':110, 'B':16, 'NR':0, 'F':0 },
    { 'name':"6917", 'd':85, 'D':120, 'B':18, 'NR':0, 'F':0 },
    { 'name':"6918", 'd':90, 'D':125, 'B':18, 'NR':0, 'F':0 },
    { 'name':"6919", 'd':95, 'D':130, 'B':18, 'NR':0, 'F':0 },
    { 'name':"692", 'd':2, 'D':6, 'B':3, 'NR':0, 'F':0 },
    { 'name':"692-W2.3", 'd':2, 'D':6, 'B':2.3, 'NR':0, 'F':0 },
    { 'name':"6920", 'd':100, 'D':140, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6921", 'd':105, 'D':145, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6922", 'd':110, 'D':150, 'B':20, 'NR':0, 'F':0 },
    { 'name':"6924", 'd':120, 'D':165, 'B':22, 'NR':0, 'F':0 },
    { 'name':"6926", 'd':130, 'D':180, 'B':24, 'NR':0, 'F':0 },
    { 'name':"6928", 'd':140, 'D':190, 'B':24, 'NR':0, 'F':0 },
    { 'name':"693", 'd':3, 'D':8, 'B':4, 'NR':0, 'F':0 },
    { 'name':"693-W3", 'd':3, 'D':8, 'B':3, 'NR':0, 'F':0 },
    { 'name':"6930", 'd':150, 'D':210, 'B':28, 'NR':0, 'F':0 },
    { 'name':"6936", 'd':180, 'D':250, 'B':33, 'NR':0, 'F':0 },
    { 'name':"694", 'd':4, 'D':11, 'B':4, 'NR':0, 'F':0 },
    { 'name':"6940", 'd':200, 'D':280, 'B':38, 'NR':0, 'F':0 },
    { 'name':"695", 'd':5, 'D':13, 'B':4, 'NR':0, 'F':0 },
    { 'name':"696", 'd':6, 'D':15, 'B':5, 'NR':0, 'F':0 },
    { 'name':"696A", 'd':6, 'D':16, 'B':5, 'NR':0, 'F':0 },
    { 'name':"697", 'd':7, 'D':17, 'B':5, 'NR':0, 'F':0 },
    { 'name':"698", 'd':8, 'D':19, 'B':6, 'NR':0, 'F':0 },
    { 'name':"699", 'd':9, 'D':20, 'B':6, 'NR':0, 'F':0 },
    { 'name':"F-6000", 'd':10, 'D':26, 'B':8, 'NR':0, 'F':1 },
    { 'name':"F-6001", 'd':12, 'D':28, 'B':8, 'NR':0, 'F':1 },
    { 'name':"F-6002", 'd':15, 'D':32, 'B':9, 'NR':0, 'F':1 },
    { 'name':"F-6005", 'd':25, 'D':47, 'B':12, 'NR':0, 'F':1 },
    { 'name':"F-6006", 'd':30, 'D':55, 'B':13, 'NR':0, 'F':1 },
    { 'name':"F-604", 'd':4, 'D':12, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-605", 'd':5, 'D':14, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-606", 'd':6, 'D':17, 'B':6, 'NR':0, 'F':1 },
    { 'name':"F-607", 'd':7, 'D':19, 'B':6, 'NR':0, 'F':1 },
    { 'name':"F-608", 'd':8, 'D':22, 'B':7, 'NR':0, 'F':1 },
    { 'name':"F-623", 'd':3, 'D':10, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-624", 'd':4, 'D':13, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-625", 'd':5, 'D':16, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-626", 'd':6, 'D':19, 'B':6, 'NR':0, 'F':1 },
    { 'name':"F-628", 'd':8, 'D':24, 'B':8, 'NR':0, 'F':1 },
    { 'name':"F-634", 'd':4, 'D':16, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-635", 'd':5, 'D':19, 'B':6, 'NR':0, 'F':1 },
    { 'name':"F-6700", 'd':10, 'D':15, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-6800", 'd':10, 'D':19, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-6801", 'd':12, 'D':21, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-6802", 'd':15, 'D':24, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-6803", 'd':17, 'D':26, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-6804", 'd':20, 'D':32, 'B':7, 'NR':0, 'F':1 },
    { 'name':"F-683", 'd':3, 'D':7, 'B':3, 'NR':0, 'F':1 },
    { 'name':"F-683-W2", 'd':3, 'D':7, 'B':2, 'NR':0, 'F':1 },
    { 'name':"F-684", 'd':4, 'D':9, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-684-W2.5", 'd':4, 'D':9, 'B':2.5, 'NR':0, 'F':1 },
    { 'name':"F-685", 'd':5, 'D':11, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-685-W3", 'd':5, 'D':11, 'B':3, 'NR':0, 'F':1 },
    { 'name':"F-685-W5", 'd':5, 'D':11, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-686", 'd':6, 'D':13, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-686-W3.5", 'd':6, 'D':13, 'B':3.5, 'NR':0, 'F':1 },
    { 'name':"F-687", 'd':7, 'D':14, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-687-W3.5", 'd':7, 'D':14, 'B':3.5, 'NR':0, 'F':1 },
    { 'name':"F-688", 'd':8, 'D':16, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-688-W4", 'd':8, 'D':16, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-689", 'd':9, 'D':17, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-6900", 'd':10, 'D':22, 'B':6, 'NR':0, 'F':1 },
    { 'name':"F-6901", 'd':12, 'D':24, 'B':6, 'NR':0, 'F':1 },
    { 'name':"F-6902", 'd':15, 'D':28, 'B':7, 'NR':0, 'F':1 },
    { 'name':"F-6903", 'd':17, 'D':30, 'B':7, 'NR':0, 'F':1 },
    { 'name':"F-6906", 'd':30, 'D':47, 'B':9, 'NR':0, 'F':1 },
    { 'name':"F-692", 'd':2, 'D':6, 'B':3, 'NR':0, 'F':1 },
    { 'name':"F-693", 'd':3, 'D':8, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-693-W3", 'd':3, 'D':8, 'B':3, 'NR':0, 'F':1 },
    { 'name':"F-694", 'd':4, 'D':11, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-695", 'd':5, 'D':13, 'B':4, 'NR':0, 'F':1 },
    { 'name':"F-696", 'd':6, 'D':15, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-697", 'd':7, 'D':17, 'B':5, 'NR':0, 'F':1 },
    { 'name':"F-698", 'd':8, 'D':19, 'B':6, 'NR':0, 'F':1 },
    { 'name':"F-699", 'd':9, 'D':20, 'B':6, 'NR':0, 'F':1 },
    { 'name':"MF-104", 'd':4, 'D':10, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-105", 'd':5, 'D':10, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-106", 'd':6, 'D':10, 'B':3, 'NR':0, 'F':1 },
    { 'name':"MF-115", 'd':5, 'D':11, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-117", 'd':7, 'D':11, 'B':3, 'NR':0, 'F':1 },
    { 'name':"MF-126", 'd':6, 'D':12, 'B':3, 'NR':0, 'F':1 },
    { 'name':"MF-126", 'd':6, 'D':12, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-126-W4", 'd':6, 'D':12, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-128", 'd':8, 'D':12, 'B':3.5, 'NR':0, 'F':1 },
    { 'name':"MF-137", 'd':7, 'D':13, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-137-W4", 'd':7, 'D':13, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-148", 'd':8, 'D':14, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-52-W2", 'd':2, 'D':5, 'B':2, 'NR':0, 'F':1 },
    { 'name':"MF-62", 'd':2, 'D':6, 'B':2.5, 'NR':0, 'F':1 },
    { 'name':"MF-63", 'd':3, 'D':6, 'B':2.5, 'NR':0, 'F':1 },
    { 'name':"MF-63-W2", 'd':3, 'D':6, 'B':2, 'NR':0, 'F':1 },
    { 'name':"MF-74", 'd':4, 'D':7, 'B':2.5, 'NR':0, 'F':1 },
    { 'name':"MF-74-W2", 'd':4, 'D':7, 'B':2, 'NR':0, 'F':1 },
    { 'name':"MF-83", 'd':3, 'D':8, 'B':3, 'NR':0, 'F':1 },
    { 'name':"MF-83-W2.5", 'd':3, 'D':8, 'B':2.5, 'NR':0, 'F':1 },
    { 'name':"MF-84", 'd':4, 'D':8, 'B':3, 'NR':0, 'F':1 },
    { 'name':"MF-84-W2", 'd':4, 'D':8, 'B':2, 'NR':0, 'F':1 },
    { 'name':"MF-85", 'd':5, 'D':8, 'B':2.5, 'NR':0, 'F':1 },
    { 'name':"MF-85-W2", 'd':5, 'D':8, 'B':2, 'NR':0, 'F':1 },
    { 'name':"MF-93", 'd':3, 'D':9, 'B':4, 'NR':0, 'F':1 },
    { 'name':"MF-93-W2.5", 'd':3, 'D':9, 'B':2.5, 'NR':0, 'F':1 },
    { 'name':"MF-95", 'd':5, 'D':9, 'B':3, 'NR':0, 'F':1 },
    { 'name':"MR-104", 'd':4, 'D':10, 'B':4, 'NR':0, 'F':0 },
    { 'name':"MR-104-W3", 'd':4, 'D':10, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-105", 'd':5, 'D':10, 'B':4, 'NR':0, 'F':0 },
    { 'name':"MR-105-W3", 'd':5, 'D':10, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-106", 'd':6, 'D':10, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-106-W2.5", 'd':6, 'D':10, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-115", 'd':5, 'D':11, 'B':4, 'NR':0, 'F':0 },
    { 'name':"MR-115-W3", 'd':5, 'D':11, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-117", 'd':7, 'D':11, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-117-W2.5", 'd':7, 'D':11, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-126", 'd':6, 'D':12, 'B':4, 'NR':0, 'F':0 },
    { 'name':"MR-126-W3", 'd':6, 'D':12, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-128", 'd':8, 'D':12, 'B':3.5, 'NR':0, 'F':0 },
    { 'name':"MR-128-W2.5", 'd':8, 'D':12, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-137", 'd':7, 'D':13, 'B':4, 'NR':0, 'F':0 },
    { 'name':"MR-137-W3", 'd':7, 'D':13, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-148", 'd':8, 'D':14, 'B':4, 'NR':0, 'F':0 },
    { 'name':"MR-148-W3.5", 'd':8, 'D':14, 'B':3.5, 'NR':0, 'F':0 },
    { 'name':"MR-52", 'd':2, 'D':5, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-52-W2", 'd':2, 'D':5, 'B':2, 'NR':0, 'F':0 },
    { 'name':"MR-62", 'd':2, 'D':6, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-63", 'd':3, 'D':6, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-63-W2", 'd':3, 'D':6, 'B':2, 'NR':0, 'F':0 },
    { 'name':"MR-74", 'd':4, 'D':7, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-74-W2", 'd':4, 'D':7, 'B':2, 'NR':0, 'F':0 },
    { 'name':"MR-83", 'd':3, 'D':8, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-83-W2.5", 'd':3, 'D':8, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-84", 'd':4, 'D':8, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-84-W2", 'd':4, 'D':8, 'B':2, 'NR':0, 'F':0 },
    { 'name':"MR-85", 'd':5, 'D':8, 'B':2.5, 'NR':0, 'F':0 },
    { 'name':"MR-85-W2", 'd':5, 'D':8, 'B':2, 'NR':0, 'F':0 },
    { 'name':"MR-93", 'd':3, 'D':9, 'B':4, 'NR':0, 'F':0 },
    { 'name':"MR-95", 'd':5, 'D':9, 'B':3, 'NR':0, 'F':0 },
    { 'name':"MR-95-W2.5", 'd':5, 'D':9, 'B':2.5, 'NR':0, 'F':0 }
]
