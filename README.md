# Mobaco
Vintage building toy - virtual library of all parts.
<br><img src="https://user-images.githubusercontent.com/66367852/130675242-68ae032c-c97c-4cf9-8ed1-f8d71ee7b658.png" width="25%" height="25%">

## History
Mobaco was manufactured by the Dutch company N.V. Plaatmetaalindustrie van Mouwerik en Bal between 1924 and 1961, in Zeist, The Netherlands.
Moubal, as the company was commonly known, was a manufacturer of sheet metal products. Story has it that a few times a year they would clean their machines and make Mobaco parts.
Starting in 1948, Jumbo, a toy and puzzle company, took over sales and marketing. They redesigned the sets and manuals, added a few parts and turned it into more of a mass market product.
With the advent of Lego, interest waned. In 1962, Mobaco was discontinued, and in 1981 Moubal went bankrupt. Unfortunately, their archives were destroyed. Which makes it difficult to put together an accurate history...

## The system
The Mobaco system consists of square wooden columns of various lengths that fit into evenly spaced holes in a thick fiberboard base board. The columns have slots on all four sides, into which cardboard panels are slid. The panels have different colors, and are either solid, or have window or door cut-outs of various shapes.
Structural rigidity comes from horizontal cardboard strips and floor plates that slide over the columns and rest on the wall panels. To make rigid corners and to make long walls stiff, two layers of these strips are installed, overlapping at seams and corners.
The system allows for pitched roofs. There are special gable ends and purlins that form the structural support for the roof. Opposite roof panels interlock at the ridge with hooks, and hang from the ridge beam. There are many roof panel shapes, allowing for complex roof designs.
With a limited number of parts, elaborate models can be made. Models are pleasing to the eye and have a distinct 19th century look. They are really easy to put together.

Much more information could be found on this extensive [Mobaco website](https://mol8.home.xs4all.nl/MOBACO_Seamonkey/Home.html), created by C. Mol.

## Numbering
Since the numbering system is not very well organized (sometimes double and sometimes missing numbers).
So filenames including some set identifiers:

* A filename consists of: x_yyy_z_c, where:
* x: set identifier, see below.
* yyy: original part number (if exists)
* z: name of part, about the same as website.
* c: color of parts. (sometimes set & part number are equal, so the color is the diffentiator.)

### Set identifier:
* M_yyy:  Moubaul range: basically all sets: 000, 00, 0, 1, 2, 3, 4
* J_yyy:  Jumbo range: When Jumbo Toy manufacture took the game over, they made it a bit smaller and added a few more parts. (Not used atm.)
* Gy_yyy: There are 3 different garage sets: Garage No.1, Garage No.2, Garage Small. Some parts are used for both No.1 & No.2 and referd as Gx_yyy
* Wx_yyy: For the 2 special sets: Windmill No.1, Windmill No.2
* Z_yyy:  Special Model Z. Mobaco did advertize with this one, but it's never produced.
* SP_yyy: Special parts, like 2 different windows found on brochures.
* U_yyy:  Identifier for user parts.

## STL's
All parts are generated in a CAD package and convert to STL.
This makes it easier to export to other libraries or 3d print a couple.
STL files could also be used with a STL editor, like 'Microsoft 3D Builder' and saved in 3MF format, including colors.

## LDraw (DAT)
All STL files are also converted into the [LDraw](https://ldraw.org/) DAT type files.
Original, these files are used for creating virtual Lego like models, using an editor.
The free [LeoCAD editor](https://www.leocad.org/) is able to import the complete library.
(LeoCAD is created by [leozide](https://github.com/leozide/leocad).)

Some more information is added:
* HowToUse_LeoCAD_v0.x.pdf
* The complete Mobaco city, as advertized: Mobaco_City_v2.ldr

## STLtoDAT converter
Also uploaded a Phyton script, for converting binary STL files into DAT files, including META data extracted from the filename.
