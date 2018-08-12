## Glyph Filter Lists

### About

The Glyph Filter List repository contains a collection of over 100 character set lists that are released under free, open licenses.  The glyph name lists are formatted as newline-delimited, annotated text files that are intended for both human and computer use.  They have been compiled from a number of upstream data sources.

### Data Sources

- Adobe Inc.
- Comité Européen de Normalisation
- Google Inc.
- Georg Seifert
- Underware
- Unicode Consortium

### Usage

The filter list files are found in the `filters` directory of this repository.

### Filter List File Formatting

The file name specifies the filter list name.  The filter list files are formatted as newline-delimited text files of glyph names.  The files include `//` and `#` symbols as comment delimiters immediately following the newline character for the previous line in the file.  The entire string through the next newline character is treated as a comment after these delimiters.

The sections of the filter list files include:

#### Header metadata

The header metadata includes the name of the filter list and license information.

#### Comment metadata

Comment lines directly above glyph name lines include a combination of the following data as necessary and when available:

- Unicode code point in hexadecimal format
- production name
- nice name
- Unicode short description

#### Glyph names

AGL-style nice names are the default format used in the filter list files.

An example of the standard formatting in the first several lines of the `filters/Latvian.txt` filter list provides a demonstration of the data sections documented above:

```
// Latvian filter list
// Copyright 2018 Source Foundry authors
// MIT License
//
// Generated with data that were released by Underware
// under a CC-by-4.0 license

# U+0100 | LATIN CAPITAL LETTER A WITH MACRON
Amacron

# U+0101 | LATIN SMALL LETTER A WITH MACRON
amacron

# U+010C | LATIN CAPITAL LETTER C WITH CARON
Ccaron

# U+010D | LATIN SMALL LETTER C WITH CARON
ccaron

# U+0112 | LATIN CAPITAL LETTER E WITH MACRON
Emacron

# U+0113 | LATIN SMALL LETTER E WITH MACRON
emacron

# U+0122 | uni0122 | LATIN CAPITAL LETTER G WITH CEDILLA
Gcommaaccent

# U+0123 | uni0123 | LATIN SMALL LETTER G WITH CEDILLA
gcommaaccent
```

### Use as Glyph Filter Lists with Font Editors

#### Glyphs font editor

The Glyphs font editor supports use of lists of glyph names as filters for new glyph creation, automated OpenType feature generation, and character set coverage determination.  The remote text files in this repository can be imported directly into the Glyphs editor as new glyph name filter lists with the free, open source [Filter List Manager (FLM) plugin](https://github.com/source-foundry/FilterListManager).  You can learn how to specify your remote filter list definition files in [the FLM plugin documentation](https://github.com/source-foundry/FilterListManager#remote-definition-files).

## Contributing

Contributions to this project are welcomed.  We encourage the addition of new character sets and greatly appreciate feedback and error reports.

Please open a new issue report if you have suggestions or identify any errors in the existing files.  Fork the Github repository and submit a pull request to propose contributions to the project source.  Please indicate the relevant upstream licensing for any new data that you propose as additions to this project.  Only OSI-approved free, open source licensed contributions are accepted in this project.

## Licenses

Unless otherwise specified the work in this project is licensed under the [MIT License](LICENSE).  Modifications to upstream source files are documented in the [docs/MODS.md](docs/MODS.md) file.  Changes in this project are documented in the [CHANGELOG.md](CHANGELOG.md).

Upstream data used in this project were released under a variety of free, open licenses.  Individual filter list files may be licensed under a free, open license other than the MIT License.  The header metadata in each filter list file contains the applicable license information. Details about these licenses and the license history in this project follow.

### Adobe Glyph List for New Fonts data

The Adobe AGLFN source was released under the BSD 3-clause license.  The modifications to the upstream source are released in this repository under the MIT License.  The BSD 3-clause license for the upstream source files can be found in the header of the upstream data file on the repository path `data/agfln.txt`.

### Glyphs application GlyphData.xml data

The upstream GlyphData.xml source was released under the MIT license.  These data were used to supplement glyph name lists with supplemental metadata included in comments that are found on the lice preceding the glyph name line in most source files released in this repository.  The MIT License for the GlyphData.xml file can be found at https://github.com/schriftgestalt/GlyphsInfo/blob/master/LICENSE.

### Google Fonts data

The Google Fonts glyph set source (including the Core, Plus, Pro, and Expert sets) was released under the Apache License 2.0.  The modifications to the upstream source are released in this repository under the Apache License 2.0.  The Apache License 2.0 for the upstream data can be found at https://github.com/googlefonts/gftools/blob/master/LICENSE

### Underware Latin Plus data

The Underware Latin Plus source was released under the CC-by-4.0 license.  The [docs/MODS.md](docs/MODS.md) document serves as the description of modifications that have been made to the upstream Underware source file in order to address the "indicate if changes were made" provision in the CC-by-4.0 license.  The modified source files that are derived from Underware data are released in this repository under the MIT License.  You may find the upstream Underware data file on the repository path `data/Underware_Latin_Plus_Data_1.txt`.  The upstream CC-by-4.0 license can be found at https://creativecommons.org/licenses/by/4.0/.