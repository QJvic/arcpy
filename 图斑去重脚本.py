layerName="MuDuNanQu"
arcpy.AddField_management(layerName,"m_Area","TEXT","","",50)
arcpy.AddField_management(layerName,"m_Len","TEXT","","",50)

arcpy.CalculateField_management(layerName,"m_Area",'int(!Shape_Length!*10000)', "PYTHON_9.3")
arcpy.CalculateField_management(layerName,"m_Len",'int(!Shape_Area!*10000)', "PYTHON_9.3")

fields = ["m_Area", "m_Len"]
arcpy.DeleteIdentical_management(layerName, fields)
arcpy.DeleteField_management(layerName,fields )
