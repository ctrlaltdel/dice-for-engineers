all: network.stl

%.stl : %.txt
	./images.py $<
	openscad -o $@ Ultimate_configurable_dice.scad
	rm [1-6].png

clean:
	rm -f *.stl
