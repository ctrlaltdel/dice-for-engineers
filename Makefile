all: network.stl sysadmin.stl helpdesk.stl hpc.stl kubernetes.stl

%.stl : %.txt images.py Ultimate_configurable_dice.scad
	./images.py $<
	openscad -o $@ Ultimate_configurable_dice.scad
	rm [1-6].png

clean:
	rm -f *.stl
