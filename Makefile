all: network

network:
	./images.py network.txt
	openscad -o network.stl Ultimate_configurable_dice.scad
