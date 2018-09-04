## Modifications to Upstream Data (Individual Glyph Names)

The following glyph name modifications were made to the upstream source as part of the work in this project:

### Adobe Glyph List for New Fonts set (AGLFN.txt)

- glyph name `H18533` changed to `blackCircle`
- glyph name `H18543` changed to `blackSmallSquare`
- glyph name `H18551` changed to `whiteSmallSquare`
- glyph name `H22073` changed to `whiteSquare`
- glyph name `Ifraktur` changed to `I-fraktur`
- glyph name `Rfraktur` changed to `R-fraktur`
- glyph name `SF010000` changed to `boxLightDownAndRight`
- glyph name `SF020000` changed to `boxLightUpAndRight`
- glyph name `SF030000` changed to `boxLightDownAndLeft`
- glyph name `SF040000` changed to `boxLightUpAndLeft`
- glyph name `SF050000` changed to `boxLightVerticalAndHorizontal`
- glyph name `SF060000` changed to `boxLightDownAndHorizontal`
- glyph name `SF070000` changed to `boxLightUpAndHorizontal`
- glyph name `SF080000` changed to `boxLightVerticalAndRight`
- glyph name `SF090000` changed to `boxLightVerticalAndLeft`
- glyph name `SF100000` changed to `boxLightHorizontal`
- glyph name `SF110000` changed to `boxLightVertical`
- glyph name `SF190000` changed to `boxVerticalSingleAndLeftDouble`
- glyph name `SF200000` changed to `boxVerticalDoubleAndLeftSingle`
- glyph name `SF210000` changed to `boxDownDoubleAndLeftSingle`
- glyph name `SF220000` changed to `boxDownSingleAndLeftDouble`
- glyph name `SF230000` changed to `boxDoubleVerticalAndLeft`
- glyph name `SF240000` changed to `boxDoubleVertical`
- glyph name `SF250000` changed to `boxDoubleDownAndLeft`
- glyph name `SF260000` changed to `boxDoubleUpAndLeft`
- glyph name `SF270000` changed to `boxUpDoubleAndLeftSingle`
- glyph name `SF280000` changed to `boxUpSingleAndLeftDouble`
- glyph name `SF360000` changed to `boxVerticalSingleAndRightDouble`
- glyph name `SF370000` changed to `boxVerticalDoubleAndRightSingle`
- glyph name `SF380000` changed to `boxDoubleUpAndRight`
- glyph name `SF390000` changed to `boxDoubleDownAndRight`
- glyph name `SF400000` changed to `boxDoubleUpAndHorizontal`
- glyph name `SF410000` changed to `boxDoubleDownAndHorizontal`
- glyph name `SF420000` changed to `boxDoubleVerticalAndRight`
- glyph name `SF430000` changed to `boxDoubleHorizontal`
- glyph name `SF440000` changed to `boxDoubleVerticalAndHorizontal`
- glyph name `SF450000` changed to `boxUpSingleAndHorizontalDouble`
- glyph name `SF460000` changed to `boxUpDoubleAndHorizontalSingle`
- glyph name `SF470000` changed to `boxDownSingleAndHorizontalDouble`
- glyph name `SF480000` changed to `boxDownDoubleAndHorizontalSingle`
- glyph name `SF490000` changed to `boxUpDoubleAndRightSingle`
- glyph name `SF500000` changed to `boxUpSingleAndRightDouble`
- glyph name `SF510000` changed to `boxDownSingleAndRightDouble`
- glyph name `SF520000` changed to `boxDownDoubleAndRightSingle`
- glyph name `SF530000` changed to `boxVerticalDoubleAndHorizontalSingle`
- glyph name `SF540000` changed to `boxVerticalSingleAndHorizontalDouble`

### Google Fonts Core Unique Glyph Set (GF-Core-Unique.txt)

- glyph name `NULL` changed to `.null`
- removed private use area code point glyph name `uniE0FF`
- removed private use area code point glyph name `uniEFFD`
- removed private use area code point glyph name`uniF000`


### Google Fonts Latin Expert Unique Glyph Set (GF-Latin-Expert-Unique.txt)

- removed `napostrophe.sc` as this was removed from the upstream data (see discussion in https://github.com/googlefonts/gftools/issues/69)

### Underware Latin-Plus Dutch Set (Dutch.txt)

- removed invalid glyph name `ijacute`
- removed invalid glyph name `IJacute`


## Modifications to Upstream Data (General)

### Adobe Glyph List for New Fonts (AGLFN) data

Glyph names included in the AGLFN data were parsed from the upstream source file.  The parsed data were tested against the data contained in the GlyphData.xml file in an automated fashion and the data were modified when invalid glyph names were identified (see above Data Modifications section for details). The glyph name data in each text file were supplemented with additional data from the Glyphs application GlyphData.xml data. These supplemental data included the following: (1) glyph unicode code point in hexadecimal format; (2) glyph production name (when AGL-like nice name included and production name available); (3) glyph nice name (when glyph production name used and nice name available); (4) Unicode short description string.  These data were added as a comment-delimited line of text directly above the glyph name.

### Google Fonts Glyph Set data

Glyph names in the Google Fonts Core, Plus, Pro, and Expert glyph sets are released in the same file format at the upstream source files.  The data in these files were tested against data contained in the Glyphs application GlyphData.xml file in an automated fashion and the data were modified when invalid glyph names were identified (see above Data Modifications section for details).  The glyph name data in each text file were supplemented with additional data from the Glyphs application GlyphData.xml data. These supplemental data included the following: (1) glyph unicode code point in hexadecimal format; (2) glyph production name (when AGL-like nice name included and production name available); (3) glyph nice name (when glyph production name used and nice name available); (4) Unicode short description string.  These data were added as a comment-delimited line of text directly above the glyph name.

### Underware Latin Plus data

Glyph names included in the Underware Latin Plus data were parsed and reformatted as individual language/dialect-specific filter list files.  Each glyph name was tested against data contained in the Glyphs application GlyphData.xml file in an automated fashion and the data were modified when invalid names were found in the data (see above Data Modifications section for details).  The glyph name data in each text file were supplemented with additional data from the Glyphs application GlyphData.xml data. These supplemental data included the following: (1) glyph unicode code point in hexadecimal format; (2) glyph production name (when AGL-like nice name included and production name available); (3) glyph nice name (when glyph production name used and nice name available); (4) Unicode short description string.  These data were added as a comment-delimited line of text directly above the glyph name.

