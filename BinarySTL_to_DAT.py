# -*- encoding: utf-8 -*-

import struct

terminator="\n" #\r\n


def GetIntFromBytes(startbyte,mydata):
    aa = [mydata[startbyte],mydata[startbyte+1],mydata[startbyte+2],mydata[startbyte+3]]
    myfloat = struct.unpack('i', bytearray(aa) )[0]    
    return myfloat

def GetFloatFromBytes(startbyte,mydata):
    aa = [mydata[startbyte],mydata[startbyte+1],mydata[startbyte+2],mydata[startbyte+3]]
    myfloat = struct.unpack('<f', bytearray(aa) )[0]
    return myfloat #"{:e}".format(myfloat)

def CreateMetaData(sFileName, myM):
    #FileName: [j|m|s1|g1|w1|Z|S|U|..]_[000<a|b|..>]_[name,incl category]_[color]
    myM["org_file"] = sFileName + ".stl"
    sFileName=sFileName.lower()
    myM["filename"] = sFileName
    s = sFileName.rsplit("_")
    myM["meta_name"] = "#" + s[1] + " (" + s[0] + "_) " + s[2] 
    myM["fileexportname"] = s[0] + "_" + s[1] + " " + s[2]
    if s[0] == "m": 
        myM["meta_keywords"]="Mobaco, Moubal general"
    elif s[0] == "j":
            myM["meta_keywords"]="Mobaco, Jumbo general"
    elif s[0] == "s1":
            myM["meta_keywords"]="Mobaco, Station No. 1"
    elif s[0] == "s2":
            myM["meta_keywords"]="Mobaco, Station No. 2"
    elif s[0] == "g1":
            myM["meta_keywords"]="Mobaco, Garage No. 1 "
    elif s[0] == "g2":
            myM["meta_keywords"]="Mobaco, Garage No. 2"
    elif s[0] == "gx":
            myM["meta_keywords"]="Mobaco, Garage No. 1 & 2"
    elif s[0] == "gs":
            myM["meta_keywords"]="Mobaco, Small Garage"
    elif s[0] == "w1":
            myM["meta_keywords"]="Mobaco, Windmill No. 1"
    elif s[0] == "w2":
            myM["meta_keywords"]="Mobaco, Windmill No. 2"
    elif s[0] == "z":
            myM["meta_keywords"]="Mobaco, Model Z"
    elif s[0] == "sp":
            myM["meta_keywords"]="Mobaco, Special part"
    elif s[0] == "u":
            myM["meta_keywords"]="Mobaco, User part"
        
    if ("_grey" in sFileName):
        myM["meta_colorcode"] = 8   #7=Light Grey; 8=Dark Grey
        myM["meta_colorname"] = "Grey" 
    elif ("_white" in sFileName):
        myM["meta_colorcode"] = 503 #15=White: 503=Very Light Grey
        myM["meta_colorname"] = "White"
    elif ("_red" in sFileName):
        myM["meta_colorcode"] = 4
        myM["meta_colorname"] = "Red"
    elif ("_green" in sFileName):
        myM["meta_colorcode"] = 2
        myM["meta_colorname"] = "Green"
    elif ("_yellow" in sFileName):
        myM["meta_colorcode"] = 14
        myM["meta_colorname"] = "Yellow"
    elif ("_wood" in sFileName):
        myM["meta_colorcode"] = 92
        myM["meta_colorname"] = "Nougat"
    elif ("_column" in sFileName):
        myM["meta_colorcode"] = 92
        myM["meta_colorname"] = "Nougat"
        
    if ("wall" in sFileName):
        myM["meta_category"] = "wall panel" 
        myM["meta_name"] = myM["meta_name"] + " " + myM["meta_colorname"].lower()
        myM["fileexportname"] = myM["fileexportname"]  + " " + myM["meta_colorname"].lower()
    elif ("window" in sFileName):
        myM["meta_category"] = "window panel" 
        myM["meta_name"] = myM["meta_name"] + " " + myM["meta_colorname"].lower()
        myM["fileexportname"] = myM["fileexportname"]  + " " + myM["meta_colorname"].lower()
    elif ("door" in sFileName):
        myM["meta_category"] = "door panel" 
        myM["meta_name"] = myM["meta_name"] + " " + myM["meta_colorname"].lower()
        myM["fileexportname"] = myM["fileexportname"]  + " " + myM["meta_colorname"].lower()
    elif ("column" in sFileName):
        myM["meta_category"] = "column" 
    elif ("base" in sFileName):
        myM["meta_category"] = "floor plate" 
        myM["meta_colorcode"] = 7
        myM["meta_colorname"] = "Light Grey"        
    elif ("floor" in sFileName):
        myM["meta_category"] = "floor panel" 
    elif ("roof" in sFileName):
        myM["meta_category"] = "roof"         
    elif ("purlin" in sFileName):
        myM["meta_category"] = "purlin"  
    elif ("cantilever" in sFileName):
        myM["meta_category"] = "cantilever"
        myM["meta_name"] = myM["meta_name"] + " " + myM["meta_colorname"].lower()
        myM["fileexportname"] = myM["fileexportname"]  + " " + myM["meta_colorname"].lower()
    elif ("strip" in sFileName):
        myM["meta_category"] = "connector strip"  
    elif ("gable" in sFileName):
        myM["meta_category"] = "gable"  

    elif ("tree" in sFileName):
        myM["meta_category"] = "tree"
    elif ("clock" in sFileName):
        myM["meta_category"] = "clock"
    elif ("chimney" in sFileName):
        myM["meta_category"] = "chimney"
    elif ("truss" in sFileName):
        myM["meta_category"] = "truss"
    
    #redefine special parts category:
    if s[0] == "s": 
        myM["meta_category"] = "special"
    elif s[0] == "z": 
        myM["meta_category"] = "modelz"
    elif s[0] in ["g1","g2","gx","gs"]: 
        myM["meta_category"] = "garage"        
    elif s[0] == "u": 
        myM["meta_category"] = "user"



class MyStlToDatConverter:
    
    def __init__(self):
        self.bRotateAroundX = False
        self.fScaleFactor = 20/57.5
        self.bDoCenterPos = True
        self.bDoMirrorY = True
        self.bDoZeroAtBottom = True
        self.bExportToLDrawDAT = True
        self.bExportToStlAscii = False

        # CREATE META, BASED ON FILENAME:
        self.mymeta = {
          "filename": "",           #dat filename
          "fileexportname": "",     #dat filename
          "solidheader": "",
          "org_file": "",           #orginigal STL filename
          "meta_name": "unknown",   #part name in LeoCAD
          "meta_colorcode": 0,
          "meta_colorname": "black",
          "meta_category": "other",
          "meta_keywords": "",
          "meta_height" : -1,
          "meta_version" : "0.0",
        }
        

    def ReadBinSTL(self, newfilename):
        # CREATE HEADER META DATA:
        CreateMetaData(newfilename, self.mymeta)
        
        # READ BIN STL FILE:
        infile = open( "stl/" + self.mymeta["filename"]+'.stl','rb' ) #import binary STL
        data = infile.read()
        self.myfaces = [] #List, of faces: [xn,yn,zn,vx1,vy1,vz1,vx1,vy1,vz1,vx1,vy1,vz1]
        
        #READ STL SOLID HEADER:
        mysolidheader=""
        for x in range(0,80):
            if not data[x] == 0:
                mysolidheader+= chr( data[x] )
            else:
                #mymodelname+=" "
                pass
        if mysolidheader=="":
            mysolidheader="solid no modelname found"
        if not mysolidheader[:6]=="solid ":
            mysolidheader="solid "
        self.mymeta["solidheader"]=mysolidheader
        
        #READ FACES:
        nroffaces=GetIntFromBytes(80,data)
        print ( "Faces available: " + str(nroffaces) )        
        maxvertic = [0,0,0]
        minvertic = [0,0,0]
        
        for x in range(0,nroffaces):
            xn = GetFloatFromBytes(84+x*50,data) 
            yn = GetFloatFromBytes(88+x*50,data) 
            zn = GetFloatFromBytes(92+x*50,data)  
            if not self.bRotateAroundX:
                newface = [xn,yn,zn]
            else:
                newface = [xn,zn,yn]
            
            for y in range(1,4):   
                if not self.bRotateAroundX:
                    xc = self.fScaleFactor * GetFloatFromBytes(84+y*12+x*50,data) 
                    yc = self.fScaleFactor * GetFloatFromBytes(88+y*12+x*50,data) 
                    zc = self.fScaleFactor * GetFloatFromBytes(92+y*12+x*50,data) 
                else:
                    xc = self.fScaleFactor * GetFloatFromBytes(84+y*12+x*50,data) 
                    zc = self.fScaleFactor * GetFloatFromBytes(88+y*12+x*50,data) 
                    yc = self.fScaleFactor * GetFloatFromBytes(92+y*12+x*50,data) 
                newface +=[xc,yc,zc]
                if x==0 and y==1:
                    maxvertic[0] = xc
                    maxvertic[1] = yc
                    maxvertic[2] = zc
                    minvertic[0] = xc
                    minvertic[1] = yc
                    minvertic[2] = zc
                else:
                    if maxvertic[0] < xc:
                        maxvertic[0] = xc
                    if maxvertic[1] < yc:
                        maxvertic[1] = yc
                    if maxvertic[2] < zc:
                        maxvertic[2] = zc
                    if minvertic[0] > xc:
                        minvertic[0] = xc
                    if minvertic[1] > yc:
                        minvertic[1] = yc
                    if minvertic[2] > zc:
                        minvertic[2] = zc
            self.myfaces.append(newface)
        print ( "Done importing faces: " + str(len(self.myfaces)) )
        print ( "Scale factor: " + str(self.fScaleFactor) ) 
        if self.bRotateAroundX:
            print ( "Including rotation around X." )
        print ( "Object size: X: {}, Y: {}, Z: {}".format(maxvertic[0]-minvertic[0],maxvertic[1]-minvertic[1],maxvertic[2]-minvertic[2]) )
        self.mymeta["meta_height"]=round( (maxvertic[1]-minvertic[1]) ,2)
        print ( "Updated META:" ) 
        print ( self.mymeta )

        # REPOSITION: ROTATE & CENTER XY & BRING ZERO AT BOTTOM (NX to LeoCAD CoordSys)

        if self.bDoCenterPos:
            center = [0,0,0]
            center[0] = ( maxvertic[0] + minvertic[0] ) / 2
            center[1] = ( maxvertic[1] + minvertic[1] ) / 2
            center[2] = ( maxvertic[2] + minvertic[2] ) / 2    
            for i in range(0,nroffaces):
                for j in [3,6,9]:   #[3,6,9]  #range(3,12,3): #NEEDED TO CHANGE FACE ORIENTATION, DUE TO REVERSE NORMAL VECTOR-Y.
                    self.myfaces[i][j]   = self.myfaces[i][j]   - center[0]
                    self.myfaces[i][j+1] = self.myfaces[i][j+1] - center[1]
                    self.myfaces[i][j+2] = self.myfaces[i][j+2] - center[2]
            print ("Done centering.")
                    
        if self.bDoMirrorY:
            for i in range(0,nroffaces):
                tmpface = [0,0,0,0,0,0,0,0,0,0,0,0]
                tmpface[0] =  self.myfaces[i][0]
                tmpface[1] = -self.myfaces[i][1]
                tmpface[2] =  self.myfaces[i][2]
                for j in [3,6,9]:   #[3,6,9] [9,6,3]  #range(3,12,3): #NEEDED TO CHANGE FACE ORIENTATION, DUE TO REVERSE NORMAL VECTOR-Y.
                    tmpface[j]   =  self.myfaces[i][j]
                    tmpface[j+1] = -self.myfaces[i][j+1]
                    tmpface[j+2] =  self.myfaces[i][j+2]
                self.myfaces[i] = tmpface #update current face
            print ("Done mirror Y.")
        
        if self.bDoZeroAtBottom:
            halfoffsetY = (maxvertic[1] - minvertic[1]) / 2
            for i in range(0,nroffaces):
                for j in [3,6,9]:   
                    self.myfaces[i][j+1] = self.myfaces[i][j+1] - halfoffsetY
            print ("Done set zero at bottom.")            


    def WriteDAT(self):
        #WRITE LDraw DAT File: (see: https://www.ldraw.org/article/398)
        out = open( "dat/" +  self.mymeta["fileexportname"] + '.dat', 'w' )                    #export file
        out.write( "0 " +  self.mymeta["meta_name"] + terminator )                    #part description
        out.write( "0 Name: " +self. mymeta["fileexportname"] + '.dat' + terminator )       #filename
        out.write( "0 !LDRAW_ORG Unofficial_Part"  + terminator ) 
        out.write( "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt"  + terminator + terminator ) 
        
        out.write( "0 BFC NOCERTIFY" + terminator + terminator )
        
        out.write( "0 !CATEGORY " + self.mymeta["meta_category"] + terminator )       #category name
        out.write( "0 !KEYWORDS " + self.mymeta["meta_keywords"] + terminator + terminator )       #keywords
        
        out.write( "0 !HISTORY 2021-08-05 Koos Welling - www.khwelling.nl" + terminator + terminator ) 
        
        out.write( "0 !ORIGINALDATA: " + self.mymeta["org_file"] + terminator ) 
        out.write( "0 !HEIGHT: " + str(self.mymeta["meta_height"]) + terminator  ) 
        out.write( "0 !SCALED: " + str( round(100*self.fScaleFactor,4) ) + " procent " + terminator  )
        out.write( "0 !VERSION: " + self.mymeta["meta_version"] + terminator + terminator )
        
        out.write( "0 // Created with BinaryStl_to_DAT.py conversion tool." + terminator ) 
        out.write( "0 // Parts used for virtual building (https://LDraw.org) of vintage construction toy: Mobaco." + terminator ) 
        out.write( "0 // Mobaco was manufactured by the Dutch company 'N.V. Plaatmetaalindustrie van Mouwerik en Bal' between 1924 and 1961, in Zeist, The Netherlands." + terminator ) 
        out.write( "0 // See also: https://mol8.home.xs4all.nl/MOBACO_Seamonkey/Home.html" + terminator + terminator )
        
        out.write( "0 !COLOUR " + self.mymeta["meta_colorname"] + " CODE " + str(self.mymeta["meta_colorcode"]) + terminator ) 
        out.write( " " + terminator) 
        for i in range(0,len(self.myfaces)): # Write triangles:            
            out.write( "3 " + str(self.mymeta["meta_colorcode"]) + " " ) 
            for j in range(3,12):                
                out.write(str( round(self.myfaces[i][j],2) ) + " ") 
            out.write(terminator) 
            # Write lines (only 2 per face): not correct, should only apply single lines, when normals >45 degrees.
            #out.write("2 24 ") 
            #for j in range(3,9):
            #    out.write(str( self.myfaces[i][j] ) + " ") 
            #out.write(terminator)        
        out.close()
        print ( "Done writing: '" + self.mymeta["fileexportname"] + ".dat'" )


    
#Color codes (LeoCAD):
#    0 Black
#    1 Blue
#    2 Green
#    3 Cyan
#    4 Red
#    5 Purple
#    6 Brown
#    7 Light Grey
#    8 Dark Grey
#    14 Yellow
#    15 White
#    18 Light Yellow
#    92 Nougat (Pillars!)
#    226 Bright Light Yellow
#    503 Very Light Grey
# Don't use: 16 & 24.
    

    def WriteSTL_Ascii(self):
        #WRITE ASCII STL FILE: 
        # Should write with this format: ("{:e}".format(myfaces[x][0]) + " ")
        out = open( self.mymeta["fileexportname"] +'_asc.stl', 'w' ) #export file
        out.write( self.mymeta["solidheader"] + terminator )    
        if self.bDoMirrorY:
            verticeorder = [9,6,3]
        else:
            verticeorder = [3,6,9]
        for i in range(0,len(self.myfaces)):
            out.write("facet normal ")   
            out.write(str( round(self.myfaces[i][0],3) ) + " ")  
            out.write(str( round(self.myfaces[i][1],3) ) + " ")
            out.write(str( round(self.myfaces[i][2],3) ) + terminator)
        
            out.write("outer loop"+terminator)
            for j in verticeorder:   #[3,6,9]  #range(3,12,3): #NEEDED TO CHANGE FACE ORIENTATION, DUE TO NEGATIVE NORMAL VECTOR-Y.
                out.write("vertex ")
                out.write(str( round(self.myfaces[i][j]  ,2) ) + " ")
                out.write(str( round(self.myfaces[i][j+1],2) ) + " ")
                out.write(str( round(self.myfaces[i][j+2],2) ) + terminator)
                
            out.write("endloop" + terminator)
            out.write("endfacet" + terminator)
        
        out.write("end" + self.mymeta["solidheader"] + terminator)
        out.close()
        print ("Done writing: '" + self.mymeta["fileexportname"] + "_asc.stl'")

#______________________________________________________________________________


myCnvtr = MyStlToDatConverter()
mySTLs=[]
#myCnvtr.bRotateAroundX = False #!!!
mySTLs.extend([ "M_001_column guardrail height", "M_001.5_column 2-3th story height", "M_002_column 1 story height", "M_003_column 2 stories", "M_004_column 2.5 stories high", "M_005_column 3 stories high", "M_006_column 3.5 stories high", "M_007_column 4 stories high" ])
mySTLs.extend([ "M_013_Peaked (Gothic) door panel_grey", "M_014_Arched door panel_grey", "M_014_Arched door panel_yellow", "M_014_Door panel with rectangular openings_grey", "M_054_Half of arched door panel_grey" ])
mySTLs.extend([ "M_020_window round_green", "M_020_window rectangular_green", "M_020_window rectangular_yellow", "M_019_Short square window panel_yellow", "M_019_Short square window panel_green", "M_015_Peaked (Gothic) window panel_yellow", "M_015_Peaked (Gothic) window panel_white" ])
mySTLs.extend([ "M_011_Full solid wall pannel_red", "M_012_Full solid wall pannel_white", "M_018_Larger solid wall pannel_white", "M_021_Large solid wall pannel_white", "M_022_Medium solid wall pannel_red", "M_023_Medium solid wall pannel_white", "M_024_Medium slotted wall panel_green", "M_024_Medium slotted wall panel_yellow", "M_025_Medium arched wall panel_green", "M_027_Shorter wall pannel_white", "M_028_Short solid wall pannel_white" ])
mySTLs.extend([ "M_080_Purlin, 3.5 bays long_grey", "M_081_Purlin, 3 bays long_grey", "M_082_Purlin, 2.5 bays long_grey", "M_083_Purlin, 2.5 bays long, with slot_grey" , "M_084_Purlin, 2 bays long_grey" , "M_085_Purlin, 1.5 bays long_grey" , "M_086_Purlin, 1 bays long_grey" , "M_087_Purlin, 0.5 bays long_grey"  ])
mySTLs.extend([ "M_180_Peaked gable panel, centred_white", "M_181_Sloping gable panel, 1 bay wide_white", "M_182_Peaked gable panel, 2 bays wide_white" ])
mySTLs.extend([ "M_089_Cantilever truss_grey", "M_089_Cantilever truss_green", "M_088_Zigzag purlin_grey", "M_076_Chimney_wood" ])
mySTLs.extend([ "M_102_Long roof panel, 4 notches wide_red", "M_103_Medium roof panel, 4 notches wide_red", "M_104_Medium roof panel, 4 notches wide with corner notched_red", "M_105_Shorter roof panel, 4 notches wide_red", "M_106_Short roof panel, 4 notches wide_red" ])
mySTLs.extend([ "M_107_Short roof panel, 4 notches wide_red", "M_108_Trapezoidal roof panel, 4 notches wide, mirrored_red", "M_108_Trapezoidal roof panel, 4 notches wide_red", "M_109_Triangular roof panel, 4 notches wide_red" , "M_110_Triangular roof panel, 4 notches wide, mirrored_red", "M_121_Long roof panel, 3 notches wide_red" ])
mySTLs.extend([ "M_122_Long roof panel, 3 notches wide, notched_red", "M_123_Medium roof panel, 3 notches wide_red", "M_124_Short roof panel, 3 notches wide_red", "M_127_Long roof panel, 3 notches wide, notched_red" , "M_131_Long roof panel, 2 notches wide_red" ])
mySTLs.extend([ "M_132_Medium roof panel, 2 notches wide_red", "M_133_Short roof panel, 2 notches wide_red" ])
mySTLs.extend([ "M_140_Cantilever roof panel, 3 bays wide_red", "M_141_Cantilever roof panel, 2 bays wide_red", "M_142_Cantilever roof panel, 1 bays wide_red", "M_143_Flat roof panel_red" , "M_150_Mansard-hip roof panel, middle_red", "M_151_Mansard-hip roof panel, corner_red", "M_152_Mansard-hip roof panel, peak_red", "M_160_Steeple roof (one-fourth)_red" ])
mySTLs.extend([ "M_070_Short tree_green","M_071_Long tree_green", "M_026_Crenelated wall panel_grey" ])
mySTLs.extend([ "Z_011_Half of arched door panel_white", "Z_014_Entry door_white" ])
mySTLs.extend([ "SP_001_Window on cover_white", "SP_002_Window on advertisement_white" ])
mySTLs.extend([ "Z_001_Canopy Bracket_grey", "Z_002_Canopy Roof_red", "Z_003_Balcony Bracket_white", "Z_004_Balcony Railing_white", "Z_006_Bay Window Side_white"] )
mySTLs.extend([ "Z_007_Bay Window Front_white" , "Z_009_Bay Roof_red" , "Z_015_Ladder Side_grey" , "Z_016_Ladder Tread_grey" , "Z_017_Ladder Holder_grey" ] )
mySTLs.extend([ "G1_003A_Short column with mitered bottom and hole_wood", "G1_017_Sloping wall panel with windows, short_yellow", "G1_073_Roof panel with skylights_grey", "G1_184_Low-slope gable end panel, 3 bays_white" , "" , "" , "" , "" , "" ])
mySTLs.extend([ "G2_009_Short column with angled bottom (miter) and hole_wood", "G2_009_Short column with angled bottom (miter) and hole_wood", "G2_016_Sloping wall panel with windows, tall_yellow", "G2_070_Roof panel with skylights_grey" , "G2_183_Low-slope gable end panel, 4 bays_white" , "" , "" , "" , "" ])
mySTLs.extend([ "Gs_002A_One-story column with nail and hole for curtain rod_wood", "Gs_003A_Curtain_grey", "Gs_070_Roof panel with fold-A_grey", "Gs_070_Roof panel with fold-B_grey" , "Gs_071_Low-slope gable end panel, 2.5 bays_white" , "" , "" , "" , "" ])
mySTLs.extend([ "Gx_002A_One-story column with mitered top and hole_wood", "Gx_010_Tapered ramp_wood", "Gx_095_Sliding Garage Door_red" , "" , "" , "" ])

#mySTLs= []
mySTLs.extend([ "W1_003_Guardrails panel_green", "W1_004_Wall panel, solid_white", "W1_005_Wall panel, with window_white" , "W1_006_Wall panel, with arched door opening_white" ])
mySTLs.extend([ "W1_007_Spire wall panel A_red", "W1_008_Spire wall panel B_red", "W1_011_Wooden sail beam_wood" , "W1_012_Sail_white", "W1_013_Tail piece_white" ])
mySTLs.extend([ "W2_003_Guardrails panel_green", "W2_004_Wall panel, solid_white", "W2_005_Wall panel, with window_white" , "W2_006_Wall panel, with arched door opening_white" ])
mySTLs.extend([ "W2_007_Spire wall panel A_red", "W2_008_Spire wall panel B_red", "W2_009_Flat roof panel, top of spire_grey", "W2_011_Wooden sail beam_wood" , "W2_012_Sail_white", "W2_013_Tail piece_white" ])
mySTLs.extend([ "M_161_Cap for steeple roof_red", "Z_012_Chimney_grey", "M_029_Large clock_grey", "M_073_Small clock_grey" ])


#myCnvtr.bRotateAroundX = True #!!!
mySTLr=[]
mySTLr.extend([ "M_039_Connector strip, 1.5 holes_grey", "M_040_Connector strip, 1 hole + cantilever_grey", "M_041_Connector strip, 1 hole + two cantilevers_grey", "M_042_Connector strip, 2 holes_grey", "M_043_Connector strip 2 holes + one cantilever_grey", "M_044_Connector strip, 2 holes + two cantilevers_grey", "M_045_Connector strip, 3 holes_grey", "M_046_Connector strip, 3 holes + one cantilever_grey" ])
mySTLr.extend([ "M_047_Connector strip, 3 holes + two cantilevers_grey", "M_048_Connector strip, 4 holes_grey", "M_049_Connector strip, 4 holes + one cantilever_grey", "M_050_Corner connector strip, 3 holes_grey", "M_051_Corner connector strip, single hole_grey", "M_052_Connector strip, 1 hole_grey" , "M_053_Connector strip, 2 holes, each with slot_grey" ])
mySTLr.extend([ "M_055_Floor panel, 2x 1.5 holes_grey", "M_060_Floor panel, 2 holes, single cantilever_grey" , "M_061_Floor panel, 2 holes, double cantilever_grey", "M_062_Floor panel, 4 holes_grey", "M_063_Floor panel, 4 holes, single cantilever_grey", "M_064_Floor panel, 4 holes, double cantilever_grey" , "M_065_Floor panel, 6 holes_grey" , "M_066_Floor panel, 6 holes, single cantilever_grey" , "M_067_Floor panel, 6 holes, double cantilever_grey" , "M_068_Floor panel, 8 holes_grey" , "M_069_Floor panel, 8 holes, single cantilever_grey"  ])
mySTLr.extend([ "M_200_Base Plate, 2 holes x 2 holes", "M_201_Base Plate, 3 holes x 3 holes", "M_202_Base Plate, 4 holes x 4 holes", "M_203_Base Plate, 4 holes x 8 holes"] )
mySTLr.extend([ "Gx_008_Sliding door track bottom_wood", "Gx_071_Floor panel, 3 holes, single cantilever_grey",  "Gx_072_Sliding door track top_wood", "Z_005_Balcony Floor_grey", "M_171_Narrow roof panel, long_red" ])
mySTLr.extend([ "W1_001_Ground Floor plate_tan", "W1_002_Second Floor plate_tan", "W1_010_Wooden roof cap_black", "W1_009_Flat roof panel, top of spire_grey" ])
mySTLr.extend([ "W2_001_Ground Floor plate_tan", "W2_002_Second Floor plate_tan", "W2_010_Wooden roof cap_black", "W2_009_Flat roof panel, top of spire_grey" ]) 
mySTLr.extend([ "G2_205_Base plate_tan", "G1_206_BasePlate_tan" ])
mySTLr.extend([ "U_001_Floor panel, 2 holes, single cantilever_grey" ])


for sfile in mySTLs:
    if len(sfile)>0:
        myCnvtr.__init__()
        myCnvtr.bRotateAroundX = False
        myCnvtr.fScaleFactor = 40/57.5
        myCnvtr.ReadBinSTL(sfile)
        myCnvtr.WriteDAT()
        #myCnvtr.WriteSTL_Ascii()
