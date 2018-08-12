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

### Use as Glyph Filter Lists with Font Editors

#### Glyphs font editor

The Glyphs font editor supports use of lists of glyph names as filters for new glyph creation, automated OpenType feature generation, and character set coverage determination.  The remote text files in this repository can be imported directly into the Glyphs editor as new glyph name filter lists with the free, open source [Filter List Manager (FLM) plugin](https://github.com/source-foundry/FilterListManager).  Instructions for use with the plugin are available on the project's README.md page.

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

The Underware Latin Plus source was released under the CC-by-4.0 license.  This MODS.md document serves as the description of modifications that have been made to the upstream Underware source file in order to address the "indicate if changes were made" provision in the CC-by-4.0 license.  The modified source files that are derived from Underware data are released in this repository under the MIT License.  You may find the upstream Underware data file on the repository path `data/Underware_Latin_Plus_Data_1.txt`.  The upstream CC-by-4.0 license can be found at https://creativecommons.org/licenses/by/4.0/. You may find the MIT License in the LICENSE file that is located in the root of this source repository.