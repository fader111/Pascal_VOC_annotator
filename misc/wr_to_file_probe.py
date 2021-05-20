
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



with open('somefile.txt', 'a') as the_file:
    the_file.write('Hello\n')
    the_file.write(object_snippet)
    the_file.write(object_snippet)

with open('somefile.txt', 'a') as the_file:
    the_file.write('Hello\n')
    the_file.write(object_snippet)
    the_file.write(object_snippet)



