''' creates xml files like in template below 
'''
xml_tmpl = '''
<annotation>                            
	<folder>from_ssd</folder>           # 0
	<filename>000000.jpg</filename>     # 1
	<path>C://000000.jpg</path>         # 2
	<source>                            # 3
		<database>Unknown</database>    # 3 0
	</source>                           
	<size>                              # 4
		<width>398</width>              # 4 0
		<height>356</height>            # 4 1
		<depth>1</depth>                # 4 2
	</size>
	<segmented>0</segmented>            # 5
	<object>                            # 6
		<name>plate</name>              # 6 0
		<pose>Unspecified</pose>        # 6 1
		<truncated>0</truncated>        # 6 2
		<difficult>0</difficult>        # 6 3
		<bndbox>                        # 6 4
			<xmin>156</xmin>            # 6 4 0
 			<ymin>272</ymin>            # 6 4 1
			<xmax>241</xmax>            # 6 4 2
			<ymax>296</ymax>            # 6 4 3
		</bndbox>                 
	</object>                           
</annotation>                           
'''

def create_xml(xml_full_path, jpg_full_path, width, height, pt1, pt2):
	''' put given vallues in template and saves xml file'''
	file_content = '' 
	# open template .xml file and read fiilup file content
	with open('template.xml', "r") as f:
		for line in f:
			if "path" in line:
				line = line.replace("><", f">{jpg_full_path}<")
			elif "filename" in line:
				fname = jpg_full_path.split("/")[-1]
				line = line.replace("><", f">{fname}<")
			elif "width" in line:
				line = line.replace("><", f">{width}<")
			elif "height" in line:
				line = line.replace("><", f">{height}<")
			elif "xmin" in line:
				line = line.replace("><", f">{pt1[0]}<")
			elif "ymin" in line:
				line = line.replace("><", f">{pt1[1]}<")
			elif "xmax" in line:
				line = line.replace("><", f">{pt2[0]}<")
			elif "ymax" in line:
				line = line.replace("><", f">{pt2[1]}<")
			file_content += line
	print (file_content)

	with open (xml_full_path, 'w') as f:
		f.write(file_content)

