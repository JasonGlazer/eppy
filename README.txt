Eppy
====

Eppy is a scripting language for E+ idf files, and E+ output files. Eppy is written in the programming language Python. As a result it takes full advantage of the rich data structure and idioms that are avaliable in python. You can programmatically navigate, search, and modify E+ idf files using eppy. The power of using a scripting language allows you to do the following:

- Make a large number of changes in an idf file with a few lines of eppy code.
- Use conditions and filters when making changes to an idf file
- Make changes to multiple idf files.
- Read data from the output files of a E+ simulation run.
- Based to the results of a E+ simulation run, generate the input file for the next simulation run.

So what does this matter? 
Here are some of the things you can do with eppy:


- Change construction for all north facing walls.
- Change the glass type for all windows larger than 2 square meters.
- Change the number of people in all the interior zones.
- Change the lighting power in all south facing zones.
- Change the efficiency and fan power of all rooftop units.
- Find the energy use of all the models in a folder (or of models that were run after a certain date)
- If a model is using more energy than expected, keep increasing the R-value of the roof until you get to the expected energy use.

To see the tutorial go to ../docs/generated/index.html
