''' creates xml files like in template below
'''
# it just for reference. real template gets from file. Look at the code below.
''' file looks like this
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
		<name>car</name>                # 6 0
		<pose>Unspecified</pose>        # 6 1
		<truncated>0</truncated>        # 6 2
		<difficult>0</difficult>        # 6 3
		<bndbox>                        # 6 4
			<xmin>0</xmin>            # 6 4 0
 			<ymin>0</ymin>            # 6 4 1
			<xmax>0</xmax>            # 6 4 2
			<ymax>0</ymax>            # 6 4 3
		</bndbox>
	</object>
</annotation>
'''
xml_tmpl = '''
<annotation>
	<folder></folder>
	<filename></filename>
	<path></path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width></width>
		<height></height>
		<depth>1</depth>
	</size>
	<segmented>0</segmented>
'''

# NOTE!!! xml_tmpl has no <object> section and no </annotation> closing tag
# see the code below
# This one is the snippet to inserting to the file if more then one car in the picture

object_snippet = \
    '''	<object>
		<name>car</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin></xmin>
			<ymin></ymin>
			<xmax></xmax>
			<ymax></ymax>
		</bndbox>
	</object>
'''


def create_xml(xml_full_path, jpg_full_path, width, height, pt_vector):
    ''' put given values in template and saves xml file
            pt_vector - list of (x_min, x_max, y_min, y_max)
            of all the vehicles on the picture
    '''
    file_content = xml_tmpl
    file_content = file_content.replace(
        "<path></path>", f"<path>{jpg_full_path}</path>")
    fname = jpg_full_path.split("/")[-1]
    file_content = file_content.replace("<filename></filename>",
                                        f"<filename>{fname}</filename>")
    file_content = file_content.replace(
        "<width></width>", f"<width>{width}</width>")
    file_content = file_content.replace(
        "<height></height>", f"<height>{height}</height>")

    for bbox in pt_vector:  # bbox == (x1, y1, w, h)
        # change <xmin></xmin> and others to <xmin>value from bbox</xmin> in object_snippet
        cur_obj_cont = object_snippet
        cur_obj_cont = cur_obj_cont.replace(
            "<xmin></xmin>", f"<xmin>{bbox[0]}</xmin>")
        cur_obj_cont = cur_obj_cont.replace(
            "<ymin></ymin>", f"<ymin>{bbox[1]}</ymin>")
        cur_obj_cont = cur_obj_cont.replace(
            "<xmax></xmax>", f"<xmax>{bbox[0] + bbox[2]}</xmax>")
        cur_obj_cont = cur_obj_cont.replace(
            "<ymax></ymax>", f"<ymax>{bbox[1] + bbox[3]}</ymax>")
        file_content += cur_obj_cont

    file_content += "</annotation>"
    # print(file_content)
    return file_content


def append_xml():
    '''	if more then one car in the picture, append new <object> 
            section into the xml
    '''
    pass
