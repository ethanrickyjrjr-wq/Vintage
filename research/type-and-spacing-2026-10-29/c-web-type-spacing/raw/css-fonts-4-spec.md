<!-- SOURCE: https://www.w3.org/TR/css-fonts-4/ (fetched 2026-10-29T05:12:49Z via curl + html->text) -->



1. 

Introduction

This specification includes and expands on
the basic font features described in  the CSS3 Fonts specification (
[CSS-FONTS-3]
).

1.1. 

Value Definitions

This specification follows the 
CSS property definition conventions
 from 
[CSS2]

	using the 
value definition syntax
 from 
[CSS-VALUES-3]
.
	Value types not defined in this specification are defined in CSS Values & Units 
[CSS-VALUES-3]
.
	Combination with other CSS modules may expand the definitions of these value types.

In addition to the property-specific values listed in their definitions,
	all properties defined in this specification
	also accept the 
CSS-wide keywords
 as their property value.
	For readability they have not been repeated explicitly.

1.2. 

Interaction With Font-Relative Units

The following properties defined in this specification are 
font-affecting properties
:

All longhands (including 
reset-only sub-properties
) of the 
font
 shorthand,
except 
font-variant-emoji
 and 
line-height

All longhands of the 
font-synthesis
 shorthand

Note:
 Some properties that can affect the size of text are not 
font-affecting properties
,
	because they do so via font shaping,
	which the 
font-relative lengths
 explicitly do not take into account.

2. 

Basic Font Properties

The particular font face used to render a character is determined by
	the font family and other font properties that apply to a given element.
	This structure allows settings to be varied independently of each
	other.

2.1. 

Font family: the 
font-family
 property

Name:

font-family

Value:

[ 
<font-family-name>

|

<generic-font-family>
 ]
#

Initial:

depends on user agent

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

list, each item a string and/or 
<generic-font-family>
 keywords

Canonical order:

per grammar

Animation type:

discrete

Tests

font-family-name-000.xht

(live test)

(source)

font-family-name-001.xht

(live test)

(source)

font-family-name-002.xht

(live test)

(source)

font-family-name-003.xht

(live test)

(source)

font-family-name-004.xht

(live test)

(source)

font-family-name-005.xht

(live test)

(source)

font-family-name-006.xht

(live test)

(source)

font-family-name-007.xht

(live test)

(source)

font-family-name-008.xht

(live test)

(source)

font-family-name-009.xht

(live test)

(source)

font-family-name-010.xht

(live test)

(source)

font-family-name-011.xht

(live test)

(source)

font-family-name-012.xht

(live test)

(source)

font-family-name-013.xht

(live test)

(source)

font-family-name-014.xht

(live test)

(source)

font-family-name-015.xht

(live test)

(source)

font-family-name-016.xht

(live test)

(source)

font-family-name-017.xht

(live test)

(source)

font-family-name-018.xht

(live test)

(source)

font-family-name-019.xht

(live test)

(source)

font-family-name-020.xht

(live test)

(source)

font-family-name-021.xht

(live test)

(source)

font-family-name-022.xht

(live test)

(source)

font-family-name-023.xht

(live test)

(source)

font-family-name-024.xht

(live test)

(source)

font-family-name-025.html

(live test)

(source)

generic-family-keywords-003.html

(live test)

(source)

getComputedStyle-fontFamily.html

(live test)

(source)

standard-font-family-10.html

(live test)

(source)

standard-font-family-11.html

(live test)

(source)

standard-font-family-12.html

(live test)

(source)

standard-font-family-13.html

(live test)

(source)

standard-font-family-14.html

(live test)

(source)

standard-font-family-15.html

(live test)

(source)

standard-font-family-16.html

(live test)

(source)

standard-font-family-17.html

(live test)

(source)

standard-font-family-18.html

(live test)

(source)

standard-font-family-19.html

(live test)

(source)

standard-font-family-2.html

(live test)

(source)

standard-font-family-20.html

(live test)

(source)

standard-font-family-3.html

(live test)

(source)

standard-font-family-4.html

(live test)

(source)

standard-font-family-5.html

(live test)

(source)

standard-font-family-6.html

(live test)

(source)

standard-font-family-7.html

(live test)

(source)

standard-font-family-8.html

(live test)

(source)

standard-font-family-9.html

(live test)

(source)

standard-font-family.html

(live test)

(source)

test_font_family_parsing.html

(live test)

(source)

system-fonts.html

(live test)

(source)

font-family-computed.html

(live test)

(source)

font-family-invalid.html

(live test)

(source)

font-family-valid.html

(live test)

(source)

This property specifies a prioritized list of font family names or generic family names.
	A font family defines a set of faces that vary in weight, width or slope.
	CSS uses the combination of a family name with other font properties to select an individual face.
	Using this selection mechanism,
	rather than selecting a face via the style name as is often done in design applications,
	allows some degree of regularity in textual display when fallback occurs.

Component values are a comma-separated list indicating alternatives.
	A user agent iterates through the list of family names
	until it matches an available font
	that contains a glyph for the character to be rendered.
	(See 
§ 5.3 Cluster matching
.)
	This allows for differences in available fonts across platforms and
	for differences in the range of characters supported by individual fonts.

body 
{

font-family
:
 Helvetica
,
 Verdana
,
 sans-serif
;

}

If Helvetica is available, it will be used when rendering.
		If neither Helvetica nor Verdana is present,
		then the generic font-family 
sans-serif
 font will be used.

There are three types of font family names, two of which may be used with this property:

<font-family-name>

	        The name of a font family, such as Helvetica or Verdana in the previous example.

This might be a locally-instaled font, or might be a web font.

<generic-font-family>

	        Each 
<generic-font-family>
 keyword represents
	        a generic font choice,
	        and behaves as a potential alias for one or more locally-installed fonts
	        belonging to the specified generic font category.
	        A 
<generic-font-family>
 can thus be used as a fallback
	        for when an author’s more specific font choices are not available.

There are three types of generic family:

Generics which apply to all Unicode characters
and will 
always
 match a locally installed font.
For example, 
monospace
.

Generics which apply to all Unicode characters
but may not match to a locally installed font
on some systems.
For example, 
ui-rounded
.

Generics which are writing-system specific,
only apply to a subset of Unicode characters,
and may not match to a locally installed font
on some systems.
For example, 
generic(fangsong)
.

Authors are encouraged to append a generic font family as a last alternative
			for improved robustness,
			and to use a more specific generic font family, if applicable,
			to prefer a specific style even if the individual named font family is not available.

Note that 
<generic-font-family>
 keywords cannot be quoted
	        (otherwise they are interpreted as a 
<font-family-name>
).

The set of generic family keywords is defined in 
§ 2.1.5 Generic font families
.

<system-font-family-name>

			A locally installed system font, whose use is subject to certain constraints.
			In particular, it may not be used with the 
font-family
 property,
			but can be used with the 
font
 shorthand.

The following values refer to system fonts:

caption

The font used for captioned controls (e.g., buttons, drop-downs, etc.).

icon

The font used to label icons.

menu

The font used in menus (e.g., dropdown menus and menu lists).

message-box

The font used in dialog boxes.

small-caption

The font used for labeling small controls.

status-bar

The font used in window status bars.

Tests

system-fonts-serialization.tentative.html

(live test)

(source)

2.1.1. 

Syntax of 
<font-family-name>

<font-family-name>
 = 
<string>

|

<custom-ident>
+

Font family names other than generic families or system font families
	must either be given quoted as 
<string>
s,
	or unquoted as a sequence of one or more 
<custom-ident>
.

Note:
 This means most punctuation characters and digits at the start of
	each token must be escaped in unquoted font family names.

		To illustrate this, the following declarations are invalid:

font-family
:
 Red/Black
,
 sans-serif
;

font-family
:

"Lucida"
 Grande
,
 sans-serif
;

font-family
:
 Ahem!
,
 sans-serif
;

font-family
:
 test
@foo
,
 sans-serif
;

font-family
:
 #POUND
,
 sans-serif
;

font-family
:
 Hawaii 
5
-
0
,
 sans-serif
;

Any identifier
	which could be misinterpreted
	as a pre-defined keyword in the font-family value definition,
	or the 
CSS-wide keywords
,
	is not allowed.

Note:
 this means that if you really have a font
	whose name
	is the same as one of the 
<generic-font-family>
 names,
	or the system font names,
	or the 
CSS-wide keywords
,
	it 
must
 be quoted.

		To illustrate this,
		the following unusual font family names are valid
		because they are quoted:

font-family
:

"sans-serif"
,
 sans-serif
;

font-family
:

"default"
,
 sans-serif
;

font-family
:

"initial"
,
 sans-serif
;

font-family
:

"inherit"
,
 sans-serif
;

If a sequence of identifiers is given as a 
<font-family-name>
,
	the computed value is the name
	converted to a string
	by joining all the identifiers in the sequence by single spaces.

To avoid mistakes in escaping,
	it is recommended to quote font family names
	that contain white space, digits,
	or punctuation characters other than hyphens:

		Quoting font families prevents escaping mistakes.

body 
{

font-family
:

"New Century Schoolbook"
,
 serif 
}

<body style=
"font-family: '21st Century', fantasy"
>

Font family 
names
 that happen to be the same as
	a 
font-family
 keyword value
	(e.g. 
CSS-wide keywords
 such as 
inherit
, or

<generic-font-family>
 keywords such as 
serif
)
	must be quoted to prevent confusion
	with the keywords of the same names.
	UAs must not consider these keywords as matching the 
<font-family-name>
 type.

2.1.2. 

Syntax of 
<generic-font-family>

<generic-font-family>
 = 
<generic-font-script-specific>
|

<generic-font-complete>

|

<generic-font-incomplete>

<generic-font-script-specific>
 = 
generic
(
fangsong
)

|

generic
(
kai
)

|

generic
(
khmer-mul
)

|

generic
(
nastaliq
)

<generic-font-complete>
 = 
serif

|

sans-serif

|

system-ui

|

cursive

|

fantasy

|

math

|

monospace

<generic-font-incomplete>
 = 
ui-serif

|

ui-sans-serif

|

ui-monospace

|

ui-rounded

To make the syntax less succeptible to clashes, more recently defined generic font families are identified using a functional syntax.

body 
{

font-family
:

"Adobe Fangsong Std R"
,

generic
(
fangsong
),
 serif
}

The first choice in this example is a specific, named font, in Fang Song (仿宋) style.
		The family name is enclosed in quotes as it contains space characters.
		The second is a recently added script-specific generic font; it is unicode-range specific
		and so may not match to an actual installed font on some systems;
		but if it exists it will be an example of the requested style.
		The third is a universal generic font, which is guaranteed to match on all systems.

2.1.3. 

Syntax of 
<system-font-family-name>

<system-font-family-name>
 = 
caption

|

icon

|

menu

|

message-box

|

small-caption

|

status-bar

2.1.4. 

Relationship Between Faces and Families

A font family name only specifies a name given to a set of font faces;
	it does not specify an individual face.

		For example, given the availability of the fonts below,
		Futura would match but Futura Medium would not:

Family and individual face names

Note:
 The CSS definition of font attributes used for selection
	are explicitly not intended to define a font taxonomy.
	A type designer’s idea of a family can often extend
	to a set of faces that vary along axes other than just
	the standard axes of
	weight (
font-weight
),
	width (
font-width
),
	and slant (
font-style
).
	A family can vary along axes that are unique to that family.
	The CSS font selection mechanism merely
	provides a way to determine the “closest” match
	when substitution is necessary.

Note:
 The precise way a set of fonts are grouped into font families
	varies depending upon the platform font management APIs.
	For example, the Windows GDI API only allows four faces to be grouped into a family,
	while the DirectWrite API,
	Core Text API,
	and other platforms support
	font families with a variety of weights, widths, and slopes
	(see 
Appendix A: Mapping platform font properties to CSS properties
 for more details).

See 
§ 5.1 Localized name matching
 below for information on how
	font-family names are matched.

2.1.5. 

Generic font families

A generic font family is a font family which has a standard name (as defined by CSS), but which is an alias for an existing installed font family present on the system.
	However, a single generic font family may be a 
composite face

	combining different typefaces based on such things as
	the Unicode range of the character,
	the 
content language
 of the containing element,
	user preferences, system settings, etc.
	Different generic font families may map to the same used font.

Tests

generic-family-keywords-001.html

(live test)

(source)

generic-family-keywords-002.html

(live test)

(source)

Note:
 Generic font families are intended to be widely implemented on many platforms, unlike arbitrary 
<font-family-name>
s which are usually platform-specific names. They are expected to map to different fonts on different platforms. Authors may specify these generic family names if they desire their text to follow a particular design on many platforms, and are not particular about which specific font is chosen on those platforms.

User agents should provide reasonable default choices for the generic font families,
	that express the characteristics of each family as well as possible,
	within the limits allowed by the underlying technology.
	User agents are encouraged to allow users to select alternative faces for the generic font families.

serif

	        Serif fonts represent
	        glyphs that have finishing strokes,
	        flared or tapering ends,
	        or have actual serifed endings (including slab serifs).
	        Serif fonts are typically proportionately-spaced.
	        They often display a greater variation between thick and thin strokes
	        than fonts from the 
sans-serif
 generic font family.

Note:

serif
 and 
sans-serif

			only apply to a small handful of writing scripts.
			Their use as generic font families in CSS is historical,
			and reflects the Latin-centric nature
			of early Web development.
			Better and more widely applicable names would have been,
			for example, "modulated" and "monoline".
			However, for reasons of Web compatibility,
			these names cannot be changed.

CSS uses the term "serif" to apply to a font for any script,
			although other names might be more familiar for particular scripts,
			such as Mincho (Japanese),
			Sung or Song (Chinese),
			Batang (Korean).
			For Arabic, the Naskh style would correspond to 
serif
.

serif
 must always map to at least one matched font face.

Note:
 No guarantee is placed on the character coverage of that font
			face. Therefore, the font 
serif
 is mapped to may not end up being
			used for all content.

Sample serif fonts

sans-serif

			Glyphs in sans-serif fonts,
			as the term is used in CSS,
			are generally low contrast
			(vertical and horizontal stems have the close to the same thickness)
			and have stroke endings that are plain
			(without any flaring, cross stroke, or other ornamentation).
			Sans-serif fonts are typically proportionately-spaced.
			They often have little variation between thick and thin strokes,
			compared to fonts from the 
serif
 family.
			CSS uses the term "sans-serif" to apply to a font for any script,
			although other names might be more familiar for particular scripts,
			such as Gothic (Japanese),
			Hei (Chinese),
			or Gulim (Korean).

sans-serif
 must always map to at least one matched font face.

Note:
 No guarantee is placed on the character coverage of that font
			face. Therefore, the font 
sans-serif
 is mapped to may not end up being
			used for all content.

Sample sans-serif fonts

cursive

			Glyphs in cursive fonts generally use a script style,
			and the result looks more like handwritten pen or brush writing than printed letterwork.
			CSS uses the term "cursive" to apply to a font for any script,
			although other names such as Chancery, Brush, Swing and Script are also used in font names.

Sample cursive fonts

fantasy

			Fantasy fonts are primarily decorative or expressive fonts
			that contain decorative or expressive representations of characters.
			These do not include Pi or Picture fonts which do not represent actual characters.

Sample fantasy fonts

monospace

			The sole criterion of a monospace font is that all glyphs have the same fixed width.
			This is often used to render samples of computer code.

monospace
 must always map to at least one matched font face.

Note:
 No guarantee is placed on the character coverage of that font
			face. Therefore, the font 
monospace
 is mapped to may not end up being
			used for all content.

Sample monospace fonts

system-ui

			This generic font family lets text render with the default user interface font
			(which, as with all 
§ 2.1.5 Generic font families
, may be a composite font)
			on the platform on which the UA is running.
			A cross-platform UA should use different fonts on its different supported platforms.
			The purpose of 
system-ui
 is to allow web content
			to integrate with the look and feel of the native OS.
			This is useful for hybrid, web or cross-platform applications.

Tests

system-ui-ar.html

(live test)

(source)

system-ui-ja-vs-zh.html

(live test)

(source)

system-ui-ja.html

(live test)

(source)

system-ui-mixed.html

(live test)

(source)

system-ui-ur-vs-ar.html

(live test)

(source)

system-ui-ur.html

(live test)

(source)

system-ui-zh.html

(live test)

(source)

system-ui.html

(live test)

(source)

The precise font(s) used will depend on factors such as
			platform support, platform language, locale settings, 
			user preferences, Unicode coverage and the content language.
			UA may optionally choose to use the text rendering engine provided by the platform when using

system-ui
 to match the appearance of the default user interface more closely.

				As with other generic font families,
				the substitution of specific installed fonts for 
system-ui

				does not affect the computed style.

<div id=
"system-text"
 style=
"font-family: system-ui"
></div>
...
window.
getComputedStyle
(
document.
getElementById
(
"system-text"
))
.
getPropertyValue
(
"font-family"
);

The script above should not have any knowledge of how 
system-ui

				is expanded to include a collection of system user interface fonts.
				In particular, the above script should yield a result of "system-ui" on every platform.

Note:

system-ui
 is highly dependent on the platform environment as multiple factors may
			affect the default user interface font, and may have verying level of text rendering support.
			This may cause the displayed typeface to be undesirable for some end users 
			(e.g. Simplified Chinese users might get a monospaced serif font on older version of Windows; 

lang
 attribute might not affect displayed font in cases like 
lang="uk"
 in Russian locale
			or 
lang="ja"
 in Chinese locale). 
			Some operating system vendors does not offer means to customise 
system-ui
, 
			unlike UAs that generally allow users to customise the generic 
sans-serif
 or 
serif
 font family.
			As the name implies, 
system-ui
 is intended for use with UI elements in web applications, 
			and may or may not be suitable for large paragraphs of text 
			or articles, depending on operating system vendor implementation.

math

			This font family is intended for use with mathematical expressions.

Such fonts may include additional data
			(for example, the OpenType MATH table)
			to help with the hierarchical process of equation layout.
			In particular, they may contain
			stylistic and stretching glyph variants
			useful in setting mathematical equations.

generic(fangsong)

			This font family is used for Fang Song (仿宋) typefaces in Chinese.
			Fang Song is a relaxed, intermediate form
			between Song (
serif
) and Kai (
generic(kai)
).
			Typically, the horizontal lines are tilted,
			the endpoint flourishes are smaller,
			and there is less variation in stroke width,
			compared to a Song style.
			Fang Song is often used for official Chinese Government documents.

Note:

generic(fangsong)
 might not map to any locally installed font,
			but if it does, that font will be in Fang Song style.

Chinese text displayed with sample fang song fonts

generic(kai)

			This font family is used in
			Simplified & Traditional Chinese.
			A major typeface, which provides calligraphic styles for Chinese text.
			It shows notable handwriting features.
			Kai is commonly used in official documents and textbooks.
			Most official documents in Taiwan use Kai in full text.
			Kai can also be combined with other typefaces
			to be used in text that needs to be differentiated
			from the rest of the content,
			for example, headlines, references, quotations, and dialogs.

Note:

generic(kai)
 might not map to any locally installed font,
			but if it does, that font will be in Kai style.

Chinese text displayed with sample kai fonts

generic(khmer-mul)

			This font family is used in
			the Khmer language (used in Cambodia),
			for titles and headings,
			or to emphasise important names or nouns.
			Compared to the upright (âksâr chôr) style,
			which is used for regular text,
			âksâr mul is characterized by 
			heavier, more rounded letter shapes, 
			and may include more ligated forms.

Despite the visually heavier style,
			the font weight for regular text in 

generic(khmer-mul)
 is unchanged (400).

Note:

generic(khmer-mul)
 might not map to
			any locally installed font,
			but if it does, that font will be in âksâr mul style.

Cambodian text displayed in:
					(top) âksâr chôr style, set in Khmer OS Battambang;
					(center) âksâr mul style, set in Khmer OS Moul v6, with no ligatures;
					(bottom) âksâr mul style, set in Khmer OS Moul v4, with two ligatures. All fonts by Dan Hong.

generic(nastaliq)

			This font family is the standard way of writing Urdu and Kashmiri,
			and is also often a preferred style for Persian and other language text,
			especially in literary genres such as poetry.
			Key features include a sloping baseline for joined letters,
			and overall complex shaping and positioning for base letters and diacritics alike.
			There are also distinctive shapes for many glyphs and ligatures.
			It is important not to fall back to a naskh style
			for languages such as Urdu and Kashmiri.

Note:

generic(nastaliq)
 might not map to any locally installed font,
			but if it does, that font will be in Nastaliq style.

Urdu text displayed with a sample nastaliq font (Noto Nastaliq Urdu)

Urdu text displayed with a fallback naskh font (Scheherazade New)

ui-serif

			This font family is used for the serif variant of the system’s
			user interface. The purpose of 
ui-serif
 is to allow web
			content to integrate with the look and feel of the native OS.

Note:

ui-serif
 is not expected to map to any font on platforms
			without an appropriate system font.

Note:
 see notes on 
system-ui
 for potential issues.

Sample ui-serif font on macOS Catalina and iOS 13: New York

ui-sans-serif

			This font family is used for the sans-serif variant of the system’s
			user interface. The purpose of 
ui-sans-serif
 is to allow web
			content to integrate with the look and feel of the native OS.

Note:

ui-sans-serif
 is not expected to map to any font on platforms
			without an appropriate system font.

Note:
 see notes on 
system-ui
 for potential issues.

Sample ui-sans-serif font on macOS Catalina and iOS 13: San Francisco

ui-monospace

			This font family is used for the monospaced variant of the
			system’s user interface. The purpose of 
ui-monospace
 is to
			allow web content to integrate with the look and feel of the
			native OS.

Note:

ui-monospace
 is not expected to map to any font on platforms
			without an appropriate system font.

Note:
 see notes on 
system-ui
 for potential issues.

Sample ui-monospace font on macOS Catalina and iOS 13: SF Mono

ui-rounded

			This font family is used for the rounded variant of the system’s
			user interface. The purpose of 
ui-rounded
 is to allow web
			content to integrate with the look and feel of the native OS.

Note:

ui-rounded
 is not expected to map to any font on platforms
			without an appropriate system font.

Note:
 see notes on 
system-ui
 for potential issues.

Sample ui-rounded font on macOS Catalina and iOS 13: SF Rounded

2.2. 
Font weight: the 
font-weight
 property

Name:

font-weight

Value:

<font-weight-absolute>

|
 bolder 
|
 lighter

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

a number, see below

Canonical order:

per grammar

Animation type:

by computed value type

Tests

font-weight-bolder-001.xht

(live test)

(source)

font-weight-lighter-001.xht

(live test)

(source)

font-weight-normal-001.xht

(live test)

(source)

font-weight-normal-variable.html

(live test)

(source)

font-weight-sign-function.html

(live test)

(source)

test-synthetic-bold.html

(live test)

(source)

synthetic-bold-space-width.html

(live test)

(source)

synthetic-bold-combining-mark-001.html

(live test)

(source)

synthetic-bold-combining-mark-002.html

(live test)

(source)

synthetic-bold-does-not-widen-advances.html

(live test)

(source)

font-weight-composition.html

(live test)

(source)

font-weight-computed.html

(live test)

(source)

font-weight-invalid.html

(live test)

(source)

font-weight-valid.html

(live test)

(source)

font-parse-numeric-stretch-style-weight.html

(live test)

(source)

font-weight-interpolation.html

(live test)

(source)

font-weight-lighter-bolder.html

(live test)

(source)

font-weight-matching-installed-fonts.html

(live test)

(source)

font-weight-matching.html

(live test)

(source)

font-weight-metrics.html

(live test)

(source)

font-weight-parsing.html

(live test)

(source)

font-weight-3.html

(live test)

(source)

The 
font-weight
 property specifies the weight of glyphs in the font,
	their degree of blackness, or stroke thickness.

This property accepts values of the following:

<font-weight-absolute>
 = 
[
 normal 
|
 bold 
|

<number 
[
1
,
1000
]
>

]

Values have the following meanings:

<number [1,1000]>

			Each number indicates a weight that is at least as dark as its predecessor.
			Only values greater than or equal to 1, and less than or equal to 1000, are valid,
			and all other values are 
invalid
.
			Numeric values typically correspond to the commonly used weight names below.

100 - Thin

200 - Extra Light (Ultra Light)

300 - Light

400 - Normal

500 - Medium

600 - Semi Bold (Demi Bold)

700 - Bold

800 - Extra Bold (Ultra Bold)

900 - Black (Heavy)

Note:
 A font might internally provide its own weight name mappings,
			but those mappings within the font are disregarded in CSS.

normal

			Same as 
400
.

bold

			Same as 
700
.

bolder

			Specifies a bolder weight than the inherited value.
			See 
§ 2.2.1 Relative Weights
.

lighter

			Specifies a lighter weight than the inherited value.
			See 
§ 2.2.1 Relative Weights
.

Font formats that use a scale other than a nine-step scale
	should map their scale onto the CSS scale
	so that 400 roughly corresponds with a face that would be labeled as Regular, Book, Roman
	and 700 roughly matches a face that would be labeled as Bold.
	Alternately, weights may be inferred from style names
	that correspond roughly with the scale above.
	The scale is relative,
	so a face with a larger weight value must never appear lighter.
	If style names are used to infer weights,
	care should be taken to handle variations in style names across locales.

2.2.1. 

Relative Weights

Specified values of 
bolder
 and 
lighter
 indicate weights
	relative to the weight of the parent element.
	The computed weight is calculated based on the inherited 
font-weight
 value
	using the chart below.

Inherited value (
w
)

bolder

lighter

w
 < 100

400

No change

100 ≤ 
w
 < 350

400

100

350 ≤ 
w
 < 550

700

100

550 ≤ 
w
 < 750

900

400

750 ≤ 
w
 < 900

900

700

900 ≤ 
w

No change

700

Note:
 The table above is equivalent to selecting the next relative bolder or lighter face,
	given a font family containing normal and bold faces
	along with a thin and a heavy face.
	Authors who desire finer control over the exact weight values used for a given element
	can use numerical values instead of relative weights.

2.2.2. 

Missing weights

Quite often there are only a few weights available for a particular font family.
	When a weight is specified for which no face exists, a face with a nearby weight is used.
	In general, bold weights map to faces with heavier weights and light weights map to faces with lighter weights.
	(See the 
§ 5 Font Matching Algorithm
 for a precise definition.)

		The examples here illustrate which face is used for different weights.
		Grey indicates that a face for the desired weight does not exist, so a face with a nearby weight is used.

Weight mappings for a font family with 400, 700 and 900 weight faces

Weight mappings for a font family with 300 and 600 weight faces

Most user agents model a font as having a particular weight
	which often corresponds to one of the numbers in the nine-step scale
	described 
above
.
	While this is true of most fonts, some fonts might be configurable so as to support a range of weights.
	In this situation, the user agent uses a face with a weight as close as possible to the weight requested
	(see 
§ 5 Font Matching Algorithm
 for the precise algorithm).
	In particular, a user agent using a font which supports a range of weights
	should behave the same as if a font is present at each individual weight in the range.
	For TrueType / OpenType fonts that use variations,
	the 
wght
 variation is used to implement varying weights.
	Fractional weights are valid.

Although the practice is not well-loved by typographers,
	bold faces are often synthesized by user agents for families that lack actual bold faces.
	For the purposes of font matching,
	these faces must be treated as if they exist within the family.
	Authors can explicitly avoid this behavior by using the 
font-synthesis
 property.

2.3. 

Font width: the 
font-width
 property

Name:

font-width

Value:

normal 
|

<percentage [0,∞]>

|
 ultra-condensed 
|
 extra-condensed 
|
 condensed 
|
 semi-condensed 
|
 semi-expanded 
|
 expanded 
|
 extra-expanded 
|
 ultra-expanded

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

Not resolved

Computed value:

a percentage, see below

Canonical order:

per grammar

Animation type:

by computed value type

Tests

font-stretch-01.html

(live test)

(source)

font-stretch-02.html

(live test)

(source)

font-stretch-03.html

(live test)

(source)

font-stretch-04.html

(live test)

(source)

font-stretch-05.html

(live test)

(source)

font-stretch-06.html

(live test)

(source)

font-stretch-07.html

(live test)

(source)

font-stretch-08.html

(live test)

(source)

font-stretch-09.html

(live test)

(source)

font-stretch-10.html

(live test)

(source)

font-stretch-11.html

(live test)

(source)

font-stretch-12.html

(live test)

(source)

font-stretch-13.html

(live test)

(source)

font-stretch-14.html

(live test)

(source)

font-stretch-15.html

(live test)

(source)

font-stretch-16.html

(live test)

(source)

font-stretch-17.html

(live test)

(source)

font-stretch-18.html

(live test)

(source)

font-stretch-interpolation.html

(live test)

(source)

font-width-computed.html

(live test)

(source)

font-width-invalid.html

(live test)

(source)

font-width-valid.html

(live test)

(source)

font-parse-numeric-stretch-style-weight.html

(live test)

(source)

font-stretch.html

(live test)

(source)

The 
font-width
 property selects a normal,
	condensed, or expanded face from a font family.
	Values are specified either as percentages
	or as keywords which map to a percentage
	as defined in the following table:

Absolute keyword value

Numeric value

ultra-condensed

50%

extra-condensed

62.5%

condensed

75%

semi-condensed

87.5%

normal

100%

semi-expanded

112.5%

expanded

125%

extra-expanded

150%

ultra-expanded

200%

<percentage [0,∞]>

	values represent the fractional width of the glyphs,
	with 100% representing “normal” glyph widths
	(as defined by the font designer).
	Values less than 0% are 
invalid
.

When a face does not exist for a given width,
	values less than 100% map to a narrower face if one exists, otherwise a wider face.
	Conversely, values greater than or equal to 100% map to a wider face if one exists, otherwise a narrower face.
	Some fonts might support a range of width values;
	if the requested width value is not available in the font,
	the closest supported value is used, using the same mapping rules
	(see the 
§ 5 Font Matching Algorithm
 for the precise algorithm).
	For TrueType / OpenType fonts that support variations,
	the 
wdth
 variation is used to implement varying widths.

		The figure below shows how nine font-width property settings
		affect font matching for a font family containing a variety of discrete widths.
		Grey indicates a width for which no face exists and a different width is substituted:

Width mappings for a font family with condensed, normal and expanded width faces

getComputedStyle()
 always serializes its value as a 
<percentage>
, regardless of how the value was specified by the author, or whether or not a keyword happens to map to the value.

2.3.1. 

		Font width: the 
font-stretch
 legacy name alias

For historical reasons,
	a 
font-stretch
 property exists
	which is a 
legacy name alias

	and functions in the identical way to
	the 
font-width
.

		For example, here the legacy 
font-stretch
 is used
		on level one headings.

h1 
{
font-stretch
:
 condensed
;

}

The specified value of the 
font-width

		on those headings
		becomes set to 
condensed
'.

		For example, here the 
font-width
 is used
		on level one headings.

h1 
{
font-width
:
 condensed
;

}

The specified value of the 
font-stretch

		on those headings
		becomes set to 
condensed
.

Tests

font-stretch-01.html

(live test)

(source)

font-stretch-02.html

(live test)

(source)

font-stretch-03.html

(live test)

(source)

font-stretch-04.html

(live test)

(source)

font-stretch-05.html

(live test)

(source)

font-stretch-06.html

(live test)

(source)

font-stretch-07.html

(live test)

(source)

font-stretch-08.html

(live test)

(source)

font-stretch-09.html

(live test)

(source)

font-stretch-10.html

(live test)

(source)

font-stretch-11.html

(live test)

(source)

font-stretch-12.html

(live test)

(source)

font-stretch-13.html

(live test)

(source)

font-stretch-14.html

(live test)

(source)

font-stretch-15.html

(live test)

(source)

font-stretch-16.html

(live test)

(source)

font-stretch-17.html

(live test)

(source)

font-stretch-18.html

(live test)

(source)

font-stretch-interpolation-math-functions.html

(live test)

(source)

font-stretch-interpolation.html

(live test)

(source)

font-width-computed.html

(live test)

(source)

font-width-invalid.html

(live test)

(source)

font-width-valid.html

(live test)

(source)

font-parse-numeric-stretch-style-weight.html

(live test)

(source)

font-stretch.html

(live test)

(source)

User agents must not synthesize condensed or expanded faces
	for font families which lack such faces
	and which do not have a width variation axis.
	In particular, user agents must not geometrically stretch such faces.

2.4. 

Font style: the 
font-style
 property

Name:

font-style

Value:

normal 
|
 italic 
|
 left 
|
 right 
|
 oblique 
<angle [-90deg,90deg]>
?

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

the keyword specified, plus angle in degrees if specified

Canonical order:

per grammar

Animation type:

by computed value type; 
normal
 animates as 
oblique 0deg

Tests

font-style-angle.html

(live test)

(source)

test-synthetic-italic-2.html

(live test)

(source)

test-synthetic-italic-3.html

(live test)

(source)

test-synthetic-italic.html

(live test)

(source)

font-style-interpolation.html

(live test)

(source)

font-style-computed.html

(live test)

(source)

font-style-invalid.html

(live test)

(source)

font-style-valid.html

(live test)

(source)

font-parse-numeric-stretch-style-weight.html

(live test)

(source)

font-slant-1.html

(live test)

(source)

font-slant-2a.html

(live test)

(source)

font-slant-2b.html

(live test)

(source)

font-slant-2c.html

(live test)

(source)

font-slant-3.html

(live test)

(source)

font-style-interpolation.html

(live test)

(source)

font-style-parsing.html

(live test)

(source)

ital-variable.html

(live test)

(source)

slnt-backslant-variable.html

(live test)

(source)

slnt-variable.html

(live test)

(source)

variable-avar2-rvrn.html

(live test)

(source)

variable-avar2-warp.html

(live test)

(source)

variable-gpos-avar2.html

(live test)

(source)

The 
font-style
 property allows italic or oblique faces to be selected.
	Italic forms are generally cursive in nature while oblique faces are typically sloped versions of the regular face.

		Compare the artificially sloped renderings of Palatino "a" and Baskerville "N" in grey
		with the actual italic versions:

Artificial sloping versus real italics

Values have the following meanings:

normal

			Matches against a face that is classified as a normal face,
			one that is neither italic or obliqued.
			This represents an oblique value of "0".

italic

			Matches against a font that is labeled as an italic face,
			or an oblique face if one does not exist.
			The angle and direction of slant is unspecified.

left

			Matches against a font that is labeled as an italic face,
			with a positive (clockwise) slant;
			or an oblique face with positive slant, if one does not exist.

right

			Matches against a font that is labeled as an italic face,
			with a negative (counter-clockwise) slant;
			or an oblique face with negative slant, if one does not exist.

oblique 
<angle [-90deg,90deg]>
?

			Controls matching against an oblique face.
			Positive angles represent a clockwise slant;
			negative angles represent a counter-clockwise slant.
			The lack of an 
<angle>
 represents 
14deg
.
			(Note that a font might internally provide its own mapping for "oblique",
			but the mapping within the font is disregarded.)
			Fractional and negative values are accepted; however,
			values less than -90deg or values greater than 90deg are 
invalid
.
			If no oblique faces exist,
			and 
font-synthesis-style
 has the value auto,
			a synthetic oblique face will be generated.

An italic face with negative slant. 
			The font is Mf Autumn Breeze,
			by Misti Hammers.

A font family might contain no italic or oblique faces,
	only an italic face and no oblique,
	only an oblique face and no italic,
	both an oblique and an italic,
	multiple oblique faces at various angles,
	or various combinations thereof.
	The font matching routine will select a font to use
	which is of the correct sign as the requested angle,
	and (if there are multiple such faces) closest to the requested angle.
	In general, for a requested angle greater or equal to 11deg,
	larger angles are preferred;
	otherwise, smaller angles are preferred.
	(See 
§ 5 Font Matching Algorithm
.)
	For TrueType / OpenType fonts that use variations,
	the 
slnt
 variation is used to implement oblique values,
	and the 
ital
 variation with a value of 1 is used to implement the italic values.

Note:
 the OpenType 
slnt
 axis is defined
	with a positive angle meaning a counter-clockwise slant,
	the opposite direction to CSS.
	The CSS implementation will take this into account
	when using variations
	to produce oblique faces.

 What direction should positive and negative obliques skew in vertical writing mode?
	How do we achieve skews in the opposite dimension
	(needed for vertical writing)?

If no italic or oblique face is available,
	oblique faces may be synthesized by rendering non-obliqued faces
	with an artificial obliquing operation.
	The use of these artificially obliqued faces
	can be disabled using the 
font-synthesis
 property.

Note:
 While oblique faces can be simulated by artificially sloping the glyphs of the regular face,
	this is not equivalent to a true oblique,
	in which optical stroke thicknesses are properly preserved despite the slant.
	It is always better to use an actual oblique font rather than rely on a synthetic version.

For the purposes of font matching,
	User agents may treat 
italic
 as a synonym for 
oblique
.
	For user agents that treat these values distinctly,
	synthesis must not be performed for 
italic
.

Note:
 Authors should also be aware that synthesized approaches might not be suitable
	for scripts like Cyrillic, where italic forms are very different in shape.
	It is always better to use an actual italic font rather than rely on a synthetic version.

Note:
 Many scripts lack the tradition of mixing a cursive form within text rendered with a normal face.
	Chinese, Japanese and Korean fonts almost always lack italic or oblique faces.
	Fonts that support a mixture of scripts
	will sometimes omit specific scripts, such as Arabic,
	from the set of glyphs supported in the italic face.
	User agents should be careful about making 
character map
 assumptions across faces
	when implementing synthesis across fonts,
	as italic faces in a family can have different 
character maps
 than Roman faces.

2.5. 

Font size: the 
font-size
 property

Name:

font-size

Value:

<absolute-size>

|

<relative-size>

|

<length-percentage [0,∞]>

|

math

Initial:

medium

Applies to:

all elements and text

Inherited:

yes

Percentages:

refer to parent element’s font size

Computed value:

an absolute length

Canonical order:

per grammar

Animation type:

by computed value type

Tests

font-family-comma.html

(live test)

(source)

font-size-computed-keyword.html

(live test)

(source)

font-size-computed-no-child.html

(live test)

(source)

font-size-computed.html

(live test)

(source)

font-size-relative-across-calc-ff-bug-001.html

(live test)

(source)

font-size-zero-1.html

(live test)

(source)

font-size-zero-2.html

(live test)

(source)

font-size-zero-3.html

(live test)

(source)

font-size-zero-ligatures.html

(live test)

(source)

font-size-xxx-large.html

(live test)

(source)

rem-in-monospace.html

(live test)

(source)

font-size-composition.html

(live test)

(source)

font-size-interpolation-001.html

(live test)

(source)

font-size-interpolation-002.html

(live test)

(source)

font-size-interpolation-003.html

(live test)

(source)

font-size-computed.html

(live test)

(source)

font-size-invalid.html

(live test)

(source)

font-size-valid.html

(live test)

(source)

This property indicates the desired height of glyphs from the font.
	For scalable fonts, the font-size is a scale factor applied to the EM unit of the font.
	For non-scalable fonts, the font-size is converted into absolute units
	and matched against the declared font-size of the font,
	using the same absolute coordinate space for both of the matched values.

Note:
 There is no requirement on how closely a glyph should fit its EM box.
	Individual fonts can have a different apparent visual size
	when rendered at the same 
font-size
.
	Additionally, glyphs might render arbitrarily far outside their EM box;
	and if they overflow their 
containing block

	can induce 
ink overflow
.

Values have the following meanings:

<absolute-size>

			An 
<absolute-size>
 keyword refers to an entry in a table of font sizes
			computed and kept by the user agent.
			See 
§ 2.5.1 Absolute Size Keyword Mapping Table
.

Possible values are:

[
 xx-small 
|
 x-small 
|
 small 
|
 medium 
|
 large 
|
 x-large 
|
 xx-large 
|
 xxx-large 
]

<relative-size>

			A 
<relative-size>
 keyword is interpreted
			relative to the computed 
font-size
 of the parent element
			and possibly the table of font sizes. Possible values are:

[
 larger 
|
 smaller 
]

If the parent element has a keyword font size in the absolute size keyword mapping table,

larger
 may compute the font size to the next entry in the table,
			and 
smaller
 may compute the font size to the previous entry in the table.
			For example, if the parent element has a font size of 
font-size:medium
,
			specifying a value of 
larger
 may make the font size of the child element 
font-size:large
.

Instead of using next and previous items in the previous keyword table,
			User agents may instead use a simple ratio
			to increase or decrease the font size
			relative to the parent element.
			The specific ratio is unspecified,
			but should be around 1.2–1.5.
			This ratio may vary across different elements.

Note:
 A sight-impaired user may request a user agent use a higher ratio than default,
			in order to aid readability.
			In addition, a user agent may choose to use different ratios
			when it detects paragraph text as opposed to title text.

<length-percentage [0,∞]>

			A length value specifies an absolute font size
			(independent of the user agent’s font table).
			Negative lengths are invalid.

A percentage value specifies an absolute font size relative
			to the parent element’s computed 
font-size
.
			Negative percentages are invalid.

Note:
 Use of percentage values or 
font-relative lengths

			such as 
em
s and 
rem
s
			leads to more robust and cascadable style sheets.

math

			Special 

			mathematical scaling rules
 must be applied
			when determining the computed value of the 
font-size

			property.

		The following style sheet demonstrates
		various ways of specifying the font size.

p 
{

font-size
:

12
pt
;

}

blockquote 
{

font-size
:
 larger 
}

em 
{

font-size
:

150
%

}

em 
{

font-size
:

1.5
em

}

Note:
 The used value of this property
	can differ from its computed value
	due to 
font-size-adjust
.
	However, child elements inherit the computed 
font-size
 value,
	which is not affected by 
font-size-adjust

	(otherwise, the effect of 
font-size-adjust
 would compound).

The actual value of this property can differ from the used value
	due to the unavailability of certain font sizes.

		font-size can be clamped, for responsive typography.

font-size
:

clamp
(
10
px
,
 ...
,

36
px
);

2.5.1. 

	Absolute Size Keyword Mapping Table

The following table provides user agent guidelines for the absolute-size scaling factor
	and their mapping to HTML heading and absolute font-sizes.
	The 
medium
 value is used as the reference middle value.
	The user agent may fine-tune these values for different fonts or different types of display devices.

CSS absolute-size values

xx-small

x-small

small

medium

large

x-large

xx-large

xxx-large

scaling factor

3/5

3/4

8/9

1

6/5

3/2

2/1

3/1

HTML headings

h6

h5

h4

h3

h2

h1

HTML 
font
 sizes

1

2

3

4

5

6

7

Note:
 In CSS1, the suggested scaling factor between adjacent indexes was 1.5,
	which user experience proved to be too large.
	In CSS2, the suggested scaling factor for computer screen between adjacent indexes was 1.2
	which still created issues for the small sizes.
	The new scaling factor varies between each index to provide a better readability.

To preserve readability, an UA applying these guidelines
	should nevertheless avoid creating font sizes
	of less than 9 device pixels per EM unit.

2.6. 

Relative sizing: the 
font-size-adjust
 property

Name:

font-size-adjust

Value:

none 
|

<number [0,∞]>

Initial:

none

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/A

Computed value:

a number or the keyword 
none

Canonical order:

per grammar

Animation type:

by computed value type

Tests

font-size-adjust-001.html

(live test)

(source)

font-size-adjust-002.html

(live test)

(source)

font-size-adjust-003.xht (visual test) 
(source)

font-size-adjust-005.xht

(live test)

(source)

font-size-adjust-006.xht

(live test)

(source)

font-size-adjust-007.xht

(live test)

(source)

font-size-adjust-008.xht

(live test)

(source)

font-size-adjust-009.html

(live test)

(source)

font-size-adjust-010.html

(live test)

(source)

font-size-adjust-011.html

(live test)

(source)

font-size-adjust-012.html

(live test)

(source)

font-size-adjust-013.html

(live test)

(source)

font-size-adjust-014.html

(live test)

(source)

font-size-adjust-interpolation-math-functions.html

(live test)

(source)

font-size-adjust-metrics-override.html

(live test)

(source)

font-size-adjust-order-001.html

(live test)

(source)

font-size-adjust-reload.html

(live test)

(source)

font-size-adjust-units-001.html

(live test)

(source)

font-size-adjust-zero-1.html

(live test)

(source)

font-size-adjust-zero-2.html

(live test)

(source)

size-adjust-03.html

(live test)

(source)

font-size-adjust-composition.html

(live test)

(source)

font-size-adjust-interpolation.html

(live test)

(source)

font-face-size-adjust.html

(live test)

(source)

font-size-adjust-computed.html

(live test)

(source)

font-size-adjust-invalid.html

(live test)

(source)

font-size-adjust-valid.html

(live test)

(source)

For any given font size, the apparent size and effective legibility of text
	varies across fonts.
	For bicameral scripts such as Latin or Cyrillic that
	distinguish between upper and lowercase letters,
	the relative height of lowercase letters
	compared to their uppercase counterparts
	is a determining factor of legibility.
	This is commonly referred to as the 
aspect value

	and is equal to the x-height of a font
	divided by the font size.

Note:
 For text which uses diacritics,
	too large an x-height will actually decrease legibility
	as the diacritics become cramped.

In situations where font fallback occurs,
	fallback fonts might not share the same aspect value
	as the desired font family
	and will thus be less readable.
	The 
font-size-adjust
 property is a way
	to preserve the readability of text when font fallback occurs.
	It does this by adjusting the font-size
	so that the x-height is the same
	regardless of the font used.

		The style defined below defines Verdana as the desired font family,
		but if Verdana is not available Futura or Times will be used.
		One paragraph also has font-size-adjust specified.

p 
{

font-family
:
 Verdana
,
 Futura
,
 Times
;

}

p.adj 
{

font-size-adjust
:

0.545
;

}

<p>Lorem ipsum dolor sit amet
,
 ...</p>
<p class=
"adj"
>Lorem ipsum dolor sit amet
,
 ...</p>

Verdana has a relatively high aspect value of 0.545,
		meaning lowercase letters are relatively tall
		compared to uppercase letters,
		so at small sizes text appears legible.
		Times has a lower aspect value of 0.447,
		and so if fallback occurs,
		the text will be less legible at small sizes than Verdana
		unless font-size-adjust is also specified.

How text rendered in each of these fonts compares is shown below,
	the columns show text rendered in Verdana, Futura and Times.
	The same font-size value is used across cells
	within each row and red lines are included to show the differences in x-height.
	In the upper half, each row is rendered in the same font-size value.
	The same is true for the lower half,
	but in this half the 
font-size-adjust
 property is also set
	to 0.545,
	so that the actual font size is adjusted
	to preserve the x-height of Verdana across each row.
	Note how small text remains relatively legible across each row in the lower half.

Text with and without the use of 
font-size-adjust

This property allows authors to specify an 
aspect value
 for an element
	that will effectively preserve the x-height of the first choice font,
	whether it is substituted or not.
	Values have the following meanings:

none

			Do not preserve the font’s x-height.

<number [0,∞]>

			Specifies the 
aspect value
 used in the calculation below
			to calculate the adjusted font size:

c  =  
(
 a / a' 
)
 s

where:

s  =  font-size value
a  =  
aspect value
 as specified by the 
'font-size-adjust'
 property
a' =  
aspect value
 of actual font
c  =  adjusted font-size to use

Negative values are invalid.

This value applies to any font that is selected
			but in typical usage it should be based on the 
aspect value

			of the first font in the font-family list.
			If this is specified accurately,
			the 
(
a/a'
)
 term in the formula above
			is effectively 1 for the first font
			and no adjustment occurs.
			If the value is specified inaccurately,
			text rendered using the first font in the family list
			will display differently in older user agents
			that don’t support 
font-size-adjust
.

The value of 
font-size-adjust
 affects the used value of 
font-size

	but does not affect the computed value.
	It affects the size of relative units
	that are based on font metrics
	such as 
ex
 and 
ch

	but does not affect the size of 
em
 units.
	Since numeric values of 
line-height

	refer to the computed size of 
font-size
,

font-size-adjust
 does not affect the used value of 
line-height
.

Note:
 In CSS, authors often specify 
line-height

	as a multiple of the 
font-size
.
	Since the 
font-size-adjust
 property affects the used value of 
font-size
,
	authors should take care setting the line height
	when 
font-size-adjust
 is used.
	Setting the line height too tightly can result in
	overlapping lines of text in this situation.

		Authors can calculate the 
aspect value
 for a given font
		by comparing spans with the same content
		but different 
font-size-adjust
 properties.
		If the same font-size is used, the spans will match
		when the 
font-size-adjust
 value is accurate for the given font.

Two spans with borders are used to determine the 
aspect value
 of a font.
		The 
font-size
 is the same for both spans
		but the 
font-size-adjust
 property is specified only for the right span.
		Starting with a value of 0.5,
		the aspect value can be adjusted
		until the borders around the two letters line up.

p 
{

font-family
:
 Futura
;

font-size
:

500
px
;

}

span 
{

border
:
 solid 
1
px
 red
;

}

.adjust 
{

font-size-adjust
:

0.5
;

}

<p><span>b</span><span class=
"adjust"
>b</span></p>

Futura with an 
aspect value
 of 0.5

The box on the right is a bit bigger than the one on the left, so the 
aspect value
 of this font is something less than 0.5.
		Adjust the value until the boxes align.

2.7. 

Shorthand font property: the 
font
 property

Name:

font

Value:

[ [ 
<'font-style'>

||

<font-variant-css2>

||

<'font-weight'>

||

<font-width-css3>
 ]
?

<'font-size'>
 [ / 
<'line-height'>
 ]
?

<'font-family'>
#
 ] 
|

<system-font-family-name>

Initial:

see individual properties

Applies to:

all elements and text

Inherited:

yes

Percentages:

see individual properties

Computed value:

see individual properties

Canonical order:

per grammar

Animation type:

see individual properties

Tests

inheritance.html

(live test)

(source)

font-family-comma.html

(live test)

(source)

font-shorthand-serialization-001.html

(live test)

(source)

font-shorthand-serialization-font-stretch.html

(live test)

(source)

font-shorthand-serialization-prevention.html

(live test)

(source)

font-shorthand-subproperties-reset.html

(live test)

(source)

quoted-generic-ignored.html

(live test)

(source)

font-computed.html

(live test)

(source)

font-invalid.html

(live test)

(source)

font-valid.html

(live test)

(source)

font-shorthand.html

(live test)

(source)

The syntax of this property is based on a traditional
	typographical shorthand notation
	to set multiple properties related to fonts.
	For historical and backwards-compatibility reasons,
	it is 
almost
 a shorthand property.

The 
font
 property is,
	except as described below,
	a shorthand property for setting

font-style
, 
font-variant
,

font-weight
, 
font-width
,

font-size
, 
line-height
, 
font-family

	at the same place in the stylesheet.

Values for the 
font-variant
 property can also be included
	but only those supported in CSS 2.1;
	none of the 
font-variant
 values added in
	CSS Fonts Levels 3 or 4
	can be used in the

font
 shorthand:

<font-variant-css2>

    = normal 
|
 small-caps

Values for the 
font-width
 property can also be included
	but only those supported in CSS Fonts level 3,
	none of the 
font-width
 values added in this specification
	can be used in the 
font
 shorthand:

<font-width-css3>

    = normal 
|
 ultra-condensed 
|
 extra-condensed 
|
 condensed 
|

    semi-condensed 
|
 semi-expanded 
|
 expanded 
|
 extra-expanded 
|

    ultra-expanded

Therefore we have the following classification
	of font-related properties
	and their interaction with the 
font
 property:

Set Explicitly

These longhand properties may also be set using the 
font
 shorthand property:

font-family

font-size

font-width

font-stretch
 (css3)

font-style

font-variant-caps
 (css2)

font-weight

line-height

Reset Implicitly

These properties are a 
reset-only sub-property
 of the 
font
 property 
			and thus may not be set, but are reset to their initial values:

font-feature-settings

font-kerning

font-language-override

font-optical-sizing

font-size-adjust

font-variant-alternates

font-variant-caps
 (css3 and above)

font-variant-east-asian

font-variant-emoji

font-variant-ligatures

font-variant-numeric

font-variant-position

font-variation-settings

Cascaded Independently

These (despite the property name starting with "font-")
			are not 
longhand properties
 of the 
font

			and thus are neither set nor reset by the 
font
 property:

font-palette

font-synthesis-weight

font-synthesis-style

font-synthesis-small-caps

font-synthesis-position

All subproperties of the 
font
 property
	in the Set Explicitly and Reset Implicitly groups
	are first reset
	to their initial values.

Then, those properties the Set Explicitly group
	that are given explicit values
	in the 
font
 shorthand
	are set to those values.
	For a definition of allowed and initial values,
	see the individual longhand property definitions.

p 
{

font
:

12
pt
/
14
pt
 sans-serif 
}

p 
{

font
:

80
%
 sans-serif 
}

p 
{

font
:
 x-large/
110
%

"new century schoolbook"
,
 serif 
}

p 
{

font
:
 bold italic large Palatino
,
 serif 
}

p 
{

font
:
 normal small-caps 
120
%
/
120
%
 fantasy 
}

p 
{

font
:
 condensed oblique 
12
pt

"Helvetica Neue"
,
 serif
;

}

p 
{

font
:
 condensed oblique 
25
deg

753

12
pt

"Helvetica Neue"
,
 serif
;

}

In the second rule, the font size percentage value ("80%")
		refers to the computed 
font-size
 of the parent element.
		In the third rule, the line height percentage ("110%")
		refers to the font size of the element itself.

The first three rules do not specify
		the 
font-variant
 and

font-weight
 explicitly,
		so these properties
		receive their initial values (
normal
).
		Notice that the font family name 
"new century schoolbook"
,
		which contains spaces,
		is enclosed in quotes.
		The fourth rule sets the 
font-weight
 to 
bold
,
		the 
font-style
 to 
italic
,
		and implicitly sets 
font-variant
 to 
normal
.

The fifth rule sets the 
font-variant
 (
small-caps
),
		the 
font-size
 (120% of the parent’s font size),
		the 
line-height
 (120% of the font size) and
		the 
font-family
 (
fantasy
).
		It follows that the keyword 
normal

		applies to the two remaining properties:

font-style
 and 
font-weight
.

The sixth rule sets the 
font-style
,

font-width
,

font-size
, and

font-family
,
		the other font properties being set to their initial values.

The seventh rule sets 
font-style
 to 
oblique 25deg
,

font-weight
 to 
753
, and

font-width
 to 
condensed
.
		Note that the 
25deg
 in this rule must be
		immediately following the "oblique" keyword.

Since the 
font-width
 property was not defined in CSS 2.1,
	when using 
font-width
 values within 
font
 rules,
	authors should include a extra version compatible with older user agents:

p 
{

font
:

80
%
 sans-serif
;

/* for older user agents */

  font: condensed 
80
%
 sans-serif
;

}

System fonts can only be set as a whole;
	that is, the font family, size, weight, style, etc.
	are all set at the same time.
	These values can then be altered individually if desired.
	If no font with the indicated characteristics exists
	on a given platform,
	the user agent should either intelligently substitute
	(e.g., a smaller version of the 
caption
 font might be used
	for the 
small-caption
 font),
	or substitute a user agent default font.
	As for regular fonts,
	if, for a system font, any of the individual properties
	are not part of the operating system’s available user preferences,
	those properties
	should be set to their initial values.

That is why this property is "almost" a shorthand property:
	system fonts can only be specified with this property,
	not with 
font-family
 itself,
	so 
font

	allows authors to do more than the
	sum of its subproperties.
	However, the individual properties
	such as 
font-weight

	are still given values
	taken from the system font,
	which can be independently varied.

Note that the keywords used for the system fonts listed above
	are only treated as keywords
	when they occur in the initial position,
	in other positions the same string is treated
	as part of the font family name:

font
:
 menu
;

/* use the font settings for system menus */

font: large menu
;

/* use a font family named "menu" */

button 
{

font
:

300
 italic 
1.3
em
/
1.7
em

"FB Armada"
,
 sans-serif 
}

button p 
{

font
:
 menu 
}

button p em 
{

font-weight
:
 bolder 
}

If the font used for dropdown menus
		on a particular system
		happened to be, for example,
		9-point Charcoal, with a weight of 600,
		then P elements that were descendants of BUTTON
		would be displayed as if
		this rule were in effect:

button p 
{

font
:

600

9
pt
 Charcoal 
}

Because the 
font
 shorthand
		resets to its initial value
		any property not explicitly given a value,
		this has the same effect as
		this declaration:

button p 
{

font-style
:
 normal
;

font-variant
:
 normal
;

font-weight
:

600
;

font-size
:

9
pt
;

line-height
:
 normal
;

font-family
:
 Charcoal

}

2.8. 

Controlling synthetic faces

Synthetic font faces are a fallback strategy
	to provide an approximation to the requested font
	when a font family lacks a suitable face.

		For example, a user agent might:

synthesize a bold face by drawing a thin stroke around each glyph

synthesize small-caps, superscripts, or subscripts by
rendering regular glyphs at a smaller size and positioning them appropriately

synthesize an oblique face by geometrical shearing of each glyph

Synthesis is a fallback strategy
	because the end result,
	while perhaps better than nothing at all,
	does not meet the level of quality
	of a face designed for the purpose.

Variable fonts,
	where the font designer has provided
	one or more axes of variation
	do 
not
 count as font synthesis
	and their use is not affected by the 
font-synthesis
 property.

2.8.1. 

Controlling synthesized bold: The 
font-synthesis-weight
 property

Name:

font-synthesis-weight

Value:

auto 
|
 none

Initial:

auto

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/A

Computed value:

specified keyword

Canonical order:

per grammar

Animation type:

discrete

Media:

visual

Tests

font-synthesis-weight-binary.html

(live test)

(source)

font-synthesis-weight-first-letter.html

(live test)

(source)

font-synthesis-weight-first-line.html

(live test)

(source)

font-synthesis-weight.html

(live test)

(source)

font-synthesis-weight-webfont-bold.html

(live test)

(source)

synthetic-bold-combining-mark-001.html

(live test)

(source)

synthetic-bold-combining-mark-002.html

(live test)

(source)

synthetic-bold-does-not-widen-advances.html

(live test)

(source)

synthetic-bold-zero-advance-glyph.html

(live test)

(source)

font-synthesis-weight-invalid.html

(live test)

(source)

font-synthesis-weight-valid.html

(live test)

(source)

This property controls whether user agents are allowed
	to synthesize bold font faces
	when a font family lacks bold faces.

auto

			Synthesis of bold faces is allowed

none

			Synthesis of bold faces is not allowed

2.8.2. 

Controlling synthesized oblique: The 
font-synthesis-style
 property

Name:

font-synthesis-style

Value:

auto 
|
 none 
|
 oblique-only

Initial:

auto

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/A

Computed value:

specified keyword

Canonical order:

per grammar

Animation type:

discrete

Media:

visual

Tests

font-synthesis-style-binary.html

(live test)

(source)

font-synthesis-style-first-letter.html

(live test)

(source)

font-synthesis-style-first-line.html

(live test)

(source)

font-synthesis-style.html

(live test)

(source)

font-synthesis-style-invalid.html

(live test)

(source)

font-synthesis-style-valid.html

(live test)

(source)

This property controls whether user agents are allowed
	to synthesize oblique font faces
	when a font family lacks oblique faces.

auto

			Synthesis of oblique faces is allowed

none

			Synthesis of oblique faces is not allowed

oblique-only

				Synthesis of oblique faces is allowed,
				but they must not be used as fallback
				if italic is specified

		In vertical text,
		for positive oblique angles,
		the glyph is skewed
		such that the line-over edge shifts towards the line-right side
		while the line-under edge shifts towards the line-left side.
		For negative oblique angles,
		the glyph is skewed
		such that the line-over edge shifts towards the line-left side
		while the line-under edge shifts towards the line-right side.
		Skewing is about the center of the glyph.

Tests

synthetic-oblique-out-of-capabilities-range.html

(live test)

(source)

Synthetic oblique in vertical text, positive oblique angle

2.8.3. 

Controlling synthesized small caps: The 
font-synthesis-small-caps
 property

Name:

font-synthesis-small-caps

Value:

auto 
|
 none

Initial:

auto

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/A

Computed value:

specified keyword

Canonical order:

per grammar

Animation type:

discrete

Tests

font-synthesis-small-caps-first-letter.html

(live test)

(source)

font-synthesis-small-caps-first-line.html

(live test)

(source)

font-synthesis-small-caps-not-applied.html

(live test)

(source)

font-synthesis-small-caps.html

(live test)

(source)

font-synthesis-small-caps-invalid.html

(live test)

(source)

font-synthesis-small-caps-valid.html

(live test)

(source)

This property controls whether user agents are allowed
	to synthesize small caps font faces
	when a font family lacks small caps faces.

auto

			Synthesis of small caps faces is allowed

none

			Synthesis of small caps faces is not allowed

2.8.4. 

Controlling synthesized super- and subscripts: The 
font-synthesis-position
 property

Name:

font-synthesis-position

Value:

auto 
|
 none

Initial:

auto

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/A

Computed value:

specified keyword

Canonical order:

per grammar

Animation type:

discrete

Tests

font-synthesis-position-001.html

(live test)

(source)

font-synthesis-position-invalid.html

(live test)

(source)

font-synthesis-position-valid.html

(live test)

(source)

This property controls whether user agents are required to synthesize
	superscript and subscript glyphs for 
font-variant-position

	when a font lacks them.

auto

			Synthesis of superscript and subscript forms is required

none

			Synthesis of superscript and subscript forms is not allowed

2.8.5. 

Controlling synthetic faces: the 
font-synthesis
 shorthand

Name:

font-synthesis

Value:

none 
|
 [ weight 
||
 style 
||
 small-caps 
||
 position]

Initial:

weight style small-caps position

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/A

Computed value:

specified keyword(s)

Canonical order:

per grammar

Animation type:

discrete

Tests

font-synthesis-01.html

(live test)

(source)

font-synthesis-02.html

(live test)

(source)

font-synthesis-03.html

(live test)

(source)

font-synthesis-04.html

(live test)

(source)

font-synthesis-05.html

(live test)

(source)

font-synthesis-06.html

(live test)

(source)

font-synthesis-07.html

(live test)

(source)

font-synthesis-08.html

(live test)

(source)

font-synthesis-style-oblique-only.html

(live test)

(source)

oblique-last-resort-weight-selection.html

(live test)

(source)

oblique-request-italic-only-family-no-crash.html

(live test)

(source)

synthetic-bold-space-width.html

(live test)

(source)

font-synthesis-computed.html

(live test)

(source)

font-synthesis-invalid.html

(live test)

(source)

font-synthesis-valid.html

(live test)

(source)

This property is a shorthand for the 
font-synthesis-weight
,

font-synthesis-style
,

font-synthesis-small-caps
,
	and 
font-synthesis-position
 properties. Values are mapped as following:

font-synthesis
 value

font-synthesis-weight
 value

font-synthesis-style
 value

font-synthesis-small-caps
 value

font-synthesis-position
 value

none

none

none

none

none

weight

auto

none

none

none

style

none

auto

none

none

small-caps

none

none

auto

none

position

none

none

none

auto

weight style

auto

auto

none

none

weight small-caps

auto

none

auto

none

weight position

auto

none

none

auto

style small-caps

none

auto

auto

none

style position

none

auto

none

auto

small-caps position

none

none

auto

auto

weight style small-caps

auto

auto

auto

none

weight style position

auto

auto

none

auto

weight small-caps position

auto

none

auto

auto

style small-caps position

none

auto

auto

auto

weight style small-caps position

auto

auto

auto

auto

		The style rule below disables the use of synthetically obliqued Arabic:

*:lang
(
ar
)

{

font-synthesis
:
 none
;

}

3. 

Font Rendering Controls

3.1. 

Introduction to Font Rendering Controls

When using downloadable Web Fonts via 
@font-face
,
	the user agent needs to know what to do while the font is actively loading.
	Most web browsers have adopted some form of timeout:

Browser

Timeout

Fallback

Swap

Chrome 35+

3 seconds

yes

yes

Opera

3 seconds

yes

yes

Firefox

3 seconds

yes

yes

Internet Explorer

0 seconds

yes

yes

Safari

3 seconds

yes

yes

Chrome and Firefox have a 3 second timeout after which the text is shown with the fallback font.
Eventually, a swap occurs:
the text is re-rendered with the intended font once it becomes available.

Internet Explorer has a 0 second timeout which results in immediate text rendering:
if the requested font is not yet available,
fallback is used,
and text is rerendered later once the requested font becomes available.

While these default behaviors are reasonable,
	they’re unfortunately inconsistent across browsers.
	Worse, no single approach is sufficient to cover the range of use-cases
	required by modern user-experience– and performance–conscious applications.

The Font Loading API 
[CSS-FONT-LOADING-3]
 allows a developer to override some of the above behaviors,
	but that requires scripting,
	a non-trivial amount of effort,
	and ultimately doesn’t provide sufficient hooks to cover 
all
 reasonable cases.
	Additionally,
	the developer needs to either inline the loading script into their page
	or load an external library,
	introducing additional network latency before the fonts can be loaded
	and delaying text rendering.

Design/performance-conscious web developers have a good sense
	for the relative importance of a given Web Font
	for the intended user experience.
	This specification provides them the ability to control
	font timeout and rendering behavior.
	Specifically, it lets developers:

Define the font display policy when
text is ready to be painted:
block, or paint with fallback.

Define the font display policy once
the desired font is available:
rerender text with the new font,
or leave it with the fallback.

Define custom timeout values for each font.

Define custom display and timeout policies per element.

3.2. 

The Font Display Timeline

At the moment the user agent first attempts
	to use a given downloaded font face on a page,
	the font face’s 
font download timer
 is started.
	This timer advances through three periods of time
	associated with the font face—​the 
block period
,
	the 
swap period
, and
	the 
failure period
—​which dictate the rendering behavior of any elements using the font face:

The first period is the 
font block period
.
During this period,
if the font face is not loaded,
any element attempting to use it must instead

render with an invisible fallback font face
.
If the font face successfully loads during the 
block period
,
the font face is then used normally.

The second period, occurring immediately after the 
block period
,
is the 
font swap period
.
During this period,
if the font face is not loaded,
any element attempting to use it must instead

render with a fallback font face
.
If the font face successfully loads during the 
swap period
,
the font face is then used normally.

The third period, occurring immediately after the 
swap period
,
is the 
font failure period
.
If the font face is not yet loaded when this period starts,
it’s marked as a failed load,
causing normal font fallback.
Otherwise, the font face is used normally.

To 
render with a fallback font face
 for a given element,
	the user agent must find the first font face
	specified in the element’s 
font-family
 list
	which is already loaded,
	and use that for rendering text.
	Doing this must not trigger loads of any of the fallback fonts.

To 
render with an invisible fallback font face

	for a given element,
	find a font face as per "
render with a fallback font face
".
	Create an anonymous font face
	with the same metrics as the selected font face
	but with all glyphs "invisible" (containing no "ink"),
	and use that for rendering text.
	Doing this must not trigger loads of any of the fallback fonts.

fallback
 and 
optional
 can result in some faces in a family being used
	while others are required to fallback,
	giving a "ransom note" look.
	Perhaps require that all fonts in a family have the same behavior (all swapped in, or all fallback)?
	See also the @font-feature-values for controlling the behavior on a font family basis.

4. 

Font Resources

4.1. 

The 
@font-face
 rule

The 
@font-face
 rule allows for linking to fonts
	that are automatically fetched and activated when needed.
	This allows authors to select a font
	that closely matches the design goals for a given page
	rather than limiting the font choice
	to a set of fonts available on a given platform.
	A set of font descriptors define the location of a font resource,
	either locally or externally,
	along with the style characteristics of an individual face.
	Multiple 
@font-face
 rules can be used to construct font families with a variety of faces.
	Using CSS font matching rules,
	a user agent can selectively download
	only those faces that are needed for a given piece of text.

Its syntax is:

@font-face

{

<declaration-list>

}

Tests

downloadable-font-in-iframe-print.html

(live test)

(source)

downloadable-font-print.html

(live test)

(source)

remove-loaded-font-face-rule.html

(live test)

(source)

at-font-face-descriptors.html

(live test)

(source)

The 
@font-face
 rule accepts the descriptors defined in this specification.

Each 
@font-face
rule specifies a value for every font descriptor,
	either implicitly or explicitly.
	Those not given explicit values in the rule
	take the initial value listed with each descriptor in this specification.
	These descriptors apply solely within the context of the 
@font-face
 rule
	in which they are defined,
	and do not apply to document language elements.
	There is no notion of which elements the descriptors apply to
	or whether the values are inherited by child elements.
	When a given descriptor occurs multiple times in a given 
@font-face
 rule,
	only the last descriptor declaration is used
	and all prior declarations for that descriptor are ignored.

		To use a downloadable font called Gentium:

@font-face

{

font-family
:
 Gentium
;

src
:

url
(
http://example.com/fonts/Gentium.woff
);

}

p 
{

font-family
:
 Gentium
,
 serif
;

}

The user agent will download Gentium and use it when rendering text
		within paragraph elements.  If for some reason the site serving the font
		is unavailable, the default serif font will be used.

A given set of 
@font-face
 rules define a set of fonts
	available for use within the documents that contain these rules.
	When font matching is done, fonts defined using these rules
	are considered before other available fonts on a system.

Downloaded fonts are only available to documents that reference them.
	The process of activating these fonts must not
	make them available to other applications
	or to documents that don’t directly link to the same font.
	User agent implementers might consider it convenient
	to use downloaded fonts when rendering characters
	in other documents for which
	no other available font exists
	as part of the 
installed font fallback
 procedure.
	However, this would cause a security leak
	since the contents of one page would be able to affect other pages,
	something an attacker could use as an attack vector.
	These restrictions do not affect caching behavior,
	fonts are cached the same way other web resources are cached.

Tests

downloadable-font-scoped-to-document.html

(live test)

(source)

web-font-no-longer-accessible-when-stylesheet-removed.html

(live test)

(source)

This at-rule follows the forward-compatible parsing rules of CSS.
	Like properties in a declaration block,
	declarations of any descriptors that are not supported by the user agent
	must be ignored.

@font-face
 rules require a 
font-family

	and 
src
 descriptor;
	if either of these are missing,
	the 
@font-face
 rule must not be considered
	when performing the 
font matching algorithm
.

In cases where user agents have limited platform resources
	or implement the ability to disable downloadable font resources,

@font-face
 rules must simply be ignored;
	the behavior of individual descriptors
	as defined in this specification
	should not be altered.

4.2. 
Font family: the 
font-family
 descriptor

Name:

font-family

For:

@font-face

Value:

<font-family-name>

Initial:

N/A

This descriptor defines the font family name
	that will be used in all CSS font family name matching.
	It overrides the font family names
	contained in the underlying font data.
	If the font family name is the same
	as a font family available in a given user’s environment,
	it effectively hides the underlying font
	for documents that use the stylesheet.
	This permits a web author to freely choose font-family names
	without worrying about conflicts with font family names
	present in a given user’s environment.
	Likewise, platform substitutions
	for a given font family name
	must not be used.

4.3. 
Font reference: the 
src
 descriptor

Name:

src

For:

@font-face

Value:

<font-src-list>

Initial:

N/A

This descriptor specifies the resource containing font data.
	Its value is
	a prioritized,
	comma-separated list
	of external references
	or locally-installed font face names.
	When a font is needed
	the user agent iterates over the set of references listed,
	using the first one it can successfully parse and activate.
	Parsing this descriptor is more complicated than parsing other descriptors;
	see 
§ 4.3.1 Parsing the src descriptor
 for the parsing rules.
	Activation of a font involves downloading the file
	or reading it from disk,
	parsing it,
	and perhaps additional user-agent-dependent steps.
	Fonts containing invalid data
	or local font faces
	that are not found
	are ignored
	and the user agent loads the next font in the list.

4.3.1. 
Parsing the 
src
 descriptor

To parse a 
<font-src-list>
 production, 
parse a list
 of 
<font-src>
s.

<font-src>
 = 
<url>

[

format
(

<font-format>

)

]
?

[

tech
(

<font-tech>
#

)

]
?

|

local
(

<font-family-name>

)

<font-format>

    = 
[

<string>

|
 collection 
|
 embedded-opentype 
|
 opentype

|
 svg 
|
 truetype 
|
 woff 
|
 woff2 
]

<font-tech>

    = 
[

<font-features-tech>

|

<color-font-tech>

|
 variations 
|
 palettes 
|
 incremental 
]

<font-features-tech>

    = 
[
 features-opentype 
|
 features-aat 
|
 features-graphite 
]

<color-font-tech>

    = 
[
 color-COLRv0 
|
 color-COLRv1 
|
 color-SVG 
|
 color-sbix 
|
 color-CBDT 
]

Tests

font-face-local-not-family.html

(live test)

(source)

font-family-src-quoted.html

(live test)

(source)

font-face-src-format.html

(live test)

(source)

font-face-src-list.html

(live test)

(source)

font-face-src-local.html

(live test)

(source)

font-face-src-tech.html

(live test)

(source)

While keywords are preferred to identify font formats,
	for reasons of backwards compatibility the following strings are also accepted,
	and have the same effect as if the equivalent modern syntax had been used.

String form

Equivalent syntax

format("woff2")

format(woff2)

format("woff")

format(woff)

format("truetype")

format(truetype)

format("opentype")

format(opentype)

format("collection")

format(collection)

format("woff2-variations")

format(woff2) tech(variations)

format("woff-variations")

format(woff) tech(variations)

format("truetype-variations")

format(truetype) tech(variations)

format("opentype-variations")

format(opentype) tech(variations)

Tests

format-specifiers-variations.html

(live test)

(source)

Note:
 The CSS WG does not anticipate extending this list of format strings in the future.

If a component value is parsed correctly
	and is of a 
font format
 or

font tech

	that the UA supports,
	add it to the list of supported sources.
	If parsing a component value results in a parsing error
	or its format or tech are unsupported,
	do not add it to the list of supported sources.

If there are no supported entries at the end of this process,
	the value for the 
src
 descriptor is a parse error.

These parsing rules allow for graceful fallback of fonts
	for user agents which don’t support a particular font tech
	or font format.

		For example,
		when incremental transfer is not supported,
		a woff2 compressed version of the font
		is supplied,
		for optimal performance.
		Then, for

incremental transfer
,
		the raw uncompressed OpenType font is provided,
		portions of which will be loaded on demand.

@font-face

{

font-family
:

"MyIncrementallyLoadedWebFont"
;

src
:

url
(
"FallbackURLForBrowsersWhichDontSupportIncrementalLoading.woff2"
)

format
(
"woff2"
);

src
:

url
(
"MyIncrementallyLoadedWebFont.otf"
)

format
(
opentype
)

tech
(
incremental
);

}

4.3.2. 
Loading an individual item in the 
src
 descriptor

As with other URLs in CSS,
	the URL can be relative,
	in which case
	it is resolved relative to the location of the style sheet
	containing the 
@font-face
 rule.
	In the case of SVG fonts,
	the URL points to an element within a document
	containing SVG font definitions.
	If the element reference is omitted,
	a reference to the first defined font is implied.
	Similarly, font container formats
	that can contain more than one font
	must load one and only one of the fonts
	for a given 
@font-face
 rule.
	Fragment identifiers are used to indicate which font to load;
	these use the PostScript name of the font
	as defined in 
[RFC8081]
.

Tests

font-opentype-collections.html

(live test)

(source)

Conformant user agents must not use a face
	from the resource
	unless its PostScript name exactly matches
	the fragment identifier,
	and must skip downloading the resource
	if the given fragment identifier
	cannot be a valid PostScript name.

src
:

url
(
fonts/simple.woff
);

/* load simple.woff relative to stylesheet location */

src: 
url
(
/fonts/simple.woff
);

/* load simple.woff from absolute location */

src: 
url
(
fonts/coll.otc#foo
);

/* load font foo from collection coll.otc

src: url(fonts/coll.woff2#foo);    /* load font foo from woff2 collection coll.woff2

src: url(fonts.svg#simple);        /* load SVG font with id 'simple' */

4.3.3. 
Selecting items in the 
src

External references consist of a URL,
	followed by an optional hint
	describing the format of the font resource referenced by that URL.
	Conformant user agents
	must skip downloading a font resource
	if the format hint indicates an unsupported or unknown font format,
	or if any of the font technologies are unsupported by the user agent.
	If no format hint is supplied,
	the user agent should download the font resource.

		For example, the following shows how to load a WOFF 2 font if possible,
		otherwise a WOFF 1,
		otherwise use an OpenType font

@font-face

{

font-family
:
 bodytext
;

src
:

url
(
ideal-sans-serif.woff2
)

format
(
"woff2"
),

url
(
ideal-sans-serif.woff
)

format
(
"woff"
),

url
(
basic-sans-serif.ttf
)

format
(
"opentype"
);

}

		In this example, if woff2 is not supported,
		an unsupported and fictitious "zebra" format is skipped
		and the opentype font is downloaded:

src
:

url
(
ideal.woff2
)

format
(
"woff2"
),

url
(
unsupported.zeb
)

format
(
"zebra"
),

url
(
basic.ttf
)

format
(
"opentype"
);

Here an individual instance in a collection is loaded,
		or if collections are not supported, download an individual font instead.

@font-face

{

font-family
:
 源ノ角ゴシック Code JP
;

src
:

url
(
SourceHanCodeJP.otc#Regular
)

format
(
"collection"
),

url
(
SourceHanCodeJP-Regular.ttf
)

format
(
"opentype"
);

}

4.3.3.1. 
Local font fallback

When authors would prefer to use
	a locally available copy of a given font
	and download it if it’s not,

local
()
 can be used.
	The locally-installed 
<font-family-name>
 argument to 
local
()

	is a format-specific string
	that uniquely identifies a single font face
	within a larger family.
	The name can optionally be enclosed in quotes.
	If unquoted,
	the 
unquoted font family name processing conventions
 apply;
	in other words,
	the name must be a sequence of identifiers
	separated by 
whitespace

	which is converted to a string
	by joining the identifiers together
	separated by a single space;
	and thus,

CSS-wide keywords
 such as 
inherit
, and

<generic-font-family>
 keywords such as 
serif

	are not allowed inside 
local
()
.

/* regular face of Gentium */

@font-face

{

font-family
:
 MyGentium
;

src
:

local
(
Gentium
),

/* prefer locally available Gentium */

url
(
Gentium.woff
);

/* otherwise, download it */

}

		For example, this use of 
local
()
 would be an error:

@font-face

{

font-family
:
 foo
;

src
:

local
(
inherit
);

}

For OpenType and TrueType fonts,
	this string is used to match only the Postscript name
	or the full font name
	in the name table of locally available fonts.
	Which type of name is used varies by platform
	and font,
	so authors should include both of these names
	to assure proper matching across platforms.
	Platform substitutions for a given font name must not be used.

/* bold face of Gentium */

@font-face

{

font-family
:
 MyGentium
;

src
:

local
(
Gentium Bold
),

/* full font name */

local
(
Gentium-Bold
),

/* Postscript name */

url
(
GentiumBold.woff
);

/* otherwise, download it */

  font-weight: bold
;

}

Just as an 
@font-face
 rule specifies
	the characteristics of a single font
	within a family,
	the unique name used with 
local
()

	specifies a single font,
	not an entire font family.
	Defined in terms of OpenType font data,
	the Postscript name is found in
	the font’s

name table
,
	in the name record with nameID = 6
	(see 
[OPENTYPE]
 for more details).
	The Postscript name is the commonly used key for all fonts on OSX
	and for Postscript CFF fonts under Windows.
	The full font name (nameID = 4) is used as a unique key
	for fonts with TrueType glyphs on Windows.

For OpenType fonts with multiple localizations of the full font name,
	the US English version must be used
	(language ID = 0x409 for Windows and language ID = 0 for Macintosh)
	or the first localization
	when a US English full font name is not available
	(the OpenType specification recommends that

all fonts
	minimally include US English names
).
	User agents that also match other full font names,
	e.g. matching the Dutch name when the current system locale is set to Dutch,
	are considered non-conformant.

Note:
 This is done,
	not to prefer English,
	but to avoid matching inconsistencies
	across font versions and OS localizations,
	since font style names (e.g. "Bold")
	are frequently localized into many languages
	and the set of localizations available
	varies widely across platform and font version.

User agents that match a concatenation of
	family name (nameID = 1) with
	style name (nameID = 2)
	are considered non-conformant.

Note:
 This also allows for referencing faces
	that belong to larger families
	that cannot otherwise be referenced.

		Use a local font or reference an SVG font in another document:

@font-face

{

font-family
:
 Headline
;

src
:

local
(
Futura-Medium
),

url
(
images/fonts.svg#MyGeometricModern
)

format
(
"svg"
);

}

Create an alias for local Japanese fonts on different platforms:

@font-face

{

font-family
:
 jpgothic
;

src
:

local
(
HiraKakuPro-W3
),

local
(
Meiryo
),

local
(
IPAPGothic
);

}

Reference a font face that cannot be matched within a larger family:

@font-face

{

font-family
:
 Hoefler Text Ornaments
;

/* has the same font properties as Hoefler Text Regular */

  src: 
local
(
HoeflerText-Ornaments
);

}

Since localized fullnames never match,
		a document with the header style rules below
		would always render using the default serif font,
		regardless whether a particular system locale parameter is set to Finnish or not:

@font-face

{

font-family
:
 SectionHeader
;

src
:

local
(
"Arial Lihavoitu"
);

/* Finnish fullname for Arial Bold, should fail */

  font-weight: bold
;

}

h2 
{

font-family
:
 SectionHeader
,
 serif
;

}

A conformant user agent would never load the font 'gentium.eot'
		in the example below,
		since it is included in the first definition of the 
src
 descriptor
		which is overridden by the second definition in the same 
@font-face
 rule:

@font-face

{

font-family
:
 MainText
;

src
:

url
(
gentium.eot
);

/* for use with older user agents */

  src: 
local
(
"Gentium"
),

url
(
gentium.woff
);

/* Overrides src definition */

}

4.4. 

Font property descriptors: the 
font-style
, 
font-weight
, and

font-width
 descriptors

Name:

font-style

For:

@font-face

Value:

auto 
|
 normal 
|
 italic 
|
 left 
|
 right 
|
 oblique [ 
<angle [-90deg,90deg]>
{1,2}
 ]
?

Initial:

auto

Name:

font-weight

For:

@font-face

Value:

auto 
|

<font-weight-absolute>
{1,2}

Initial:

auto

Name:

font-width

For:

@font-face

Value:

auto 
|

<'font-width'>
{1,2}

Initial:

auto

Tests

font-face-range-order.html

(live test)

(source)

font-face-stretch-auto-static.html

(live test)

(source)

font-face-stretch-auto-variable.html

(live test)

(source)

font-face-stretch-default-variable.html

(live test)

(source)

font-face-style-normal.html

(live test)

(source)

font-face-style-auto-static.html

(live test)

(source)

font-face-style-auto-variable.html

(live test)

(source)

font-face-style-default-variable.html

(live test)

(source)

font-face-weight-auto-static.html

(live test)

(source)

font-face-weight-auto-variable.html

(live test)

(source)

font-face-weight-default-variable.html

(live test)

(source)

font-face-sign-function.html

(live test)

(source)

font-size-sign-function.html

(live test)

(source)

font-style-sign-function.html

(live test)

(source)

font-face-width.html

(live test)

(source)

font-descriptor-range-reversed.html

(live test)

(source)

font-descriptor-range-reversed-002.html

(live test)

(source)

These descriptors define the characteristics of a font face
	and are used in the process of matching styles to specific faces.
	For a font family defined with several 
@font-face
 rules,
	user agents can either download all faces in the family
	or use these descriptors to selectively download font faces that match actual styles used in document.
	The meaning of the values for these descriptors
	are the same as those for the corresponding font properties
	except that relative keywords are not allowed,

bolder
 and 
lighter
.
	If these descriptors are omitted,
	initial values are assumed.
	If specified values are out of range
	of the accepted values of the property of the same name,
	the descriptor is treated as a parse error.

Ranges are accepted in these three descriptors in place of a single value.
	Where a single value is specified,
	it has the same meaning as a range with identical startpoint and endpoint.
	User agents must swap the computed value of the startpoint and endpoint of the range
	in order to forbid decreasing ranges.
	Both endpoints are inclusive.
	The ranges are used in the 
Font Matching Algorithm
 below.

Tests

font-face-range-order.html

(live test)

(source)

range-descriptor-reversed.html

(live test)

(source)

The auto values for these three descriptors have the following effects:

For font selection purposes, the font is selected as if
the appropriate normal value
(
normal
, 
normal
 or 
normal
)
is chosen

For variation axis clamping, clamping does not occur

The value for these font face style attributes
	is used in place of the style implied by the underlying font data.
	This allows authors to combine faces in flexible combinations,
	even in situations where the original font data was arranged differently.
	User agents that implement synthetic bolding and obliquing
	must only apply synthetic styling in cases
	where the font descriptors imply this is needed,
	rather than based on the style attributes implied by the font data.
	However, variation values applied to fonts defined with '@font-face'
	will be clamped to both the values specified in these descriptors,
	or implied by the application of variation parameters
	(such as manipulation of the 
wght
 axis
	to satisfy the requested 
font-weight
),
	as well as the values supported by the font file itself.

Tests

synthetic-bold-out-of-capabilities-range.html

(live test)

(source)

		The font descriptors defined in this section
		are used for selecting a font
		from within the set of fonts defined by 
@font-face
 rules for a given family.

Consider a family containing a single, regular face:

@font-face

{

font-family
:
 BaskervilleSimple
;

src
:

url
(
baskerville-regular.woff2
);

}

Unstyled text would display using the regular face
		defined in the 
@font-face
 rule:

However, italic text would display in most user agents
		using synthetically obliqued glyphs from the regular face,
		since a separate italic face is not defined:

Now consider a family for which an actual italic face is defined:

@font-face

{

font-family
:
 BaskervilleFull
;

src
:

url
(
baskerville-regular.woff2
);

}

@font-face

{

font-family
:
 BaskervilleFull
;

src
:

url
(
baskerville-italic.woff2
);

font-style
:
 italic
;

}

The second 
@font-face
 rule
		defines the font resource 
baskerville-italic.woff

		to have style attributes of normal weight, normal stretch and italic style.
		When displaying italic text,
		the user agent will use this font,
		since it’s the closest match for italic text.
		Thus, the text will display using glyphs designed by a type designer
		rather than using synthetically obliqued glyphs from the regular face:

See the section on 
font matching

		for more complete details of the process used
		to select a particular face within a font family.

		Fonts may advertise the range of 
font-weight
, 
font-width
, and 
font-style
 they are
		compatible with.

@font-face

{

font-family
:
 Lastima
;

src
:

url
(
lastima-varfont.woff2
);

font-weight
:

100

399
;

}

The above 
@font-face
 rule indicates that 
lastima-varfont.woff
 should be used when

font-weight
 is between 100 and 399. Depending on if there are any other 
@font-face
 rules which specify

font-family
:
 Lastima
, 
lastima-varfont.woff
 might be used for values of 
font-weight

		outside of the 100 - 399 range. For more details, see the 
§ 5 Font Matching Algorithm
.

As 
above
, multiple 
@font-face
 rules may be joined together into a single
		family, spanning multiple ranges of 
font-weight
, 
font-width
, and/or 
font-style
:

@font-face

{

font-family
:
 Lastima
;

src
:

url
(
lastima-varfont-lightrange.woff2
);

font-weight
:

100

399
;

}

@font-face

{

font-family
:
 Lastima
;

src
:

url
(
lastima-varfont-heavyrange.woff2
);

font-weight
:

400

700
;

}

The above 
@font-face
 rules indicate that 
lastima-varfont-lightrange.woff
 should be used when

font-weight
 is between 100 and 399, whereas 
lastima-varfont-heavyrange.woff
 should be used when

font-weight
 is between 400 and 700.

4.4.1. 

	Font width: the 
font-stretch
 legacy name alias

For historical reasons,
	a 
font-stretch
 descriptor exists
	which is a 
legacy name alias

	and functions in the identical way to
	the 
font-width
 descriptor.

Tests

font-stretch-alias.html

(live test)

(source)

font-width-computed.html

(live test)

(source)

font-width-invalid.html

(live test)

(source)

font-width-valid.html

(live test)

(source)

4.5. 

Character range: the 
unicode-range
 descriptor

Name:

unicode-range

For:

@font-face

Value:

<unicode-range-token>
#

Initial:

U+0-10FFFF

Tests

font-face-unicode-range-2.html

(live test)

(source)

font-face-unicode-range-nbsp.html

(live test)

(source)

font-face-unicode-range.html (visual test) 
(source)

This descriptor defines the set of Unicode codepoints that may be
	supported by the font face for which it is declared. The descriptor
	value is a comma-delimited list of Unicode range token (
<unicode-range-token>
)
	values. The union of these ranges defines the set of codepoints that
	serves as a hint for user agents when deciding whether or not to
	download a font resource for a given text run.

Each 
<unicode-range-token>
 value is a
	token made up of a "U+" or "u+" prefix
	followed by a codepoint range in one of the three forms listed below.
	Ranges that do not fit one of these forms are invalid
	and cause the declaration to be ignored.

single codepoint (e.g. U+416)

a Unicode codepoint, represented as one to six hexadecimal digits

interval range (e.g. U+400-4ff)

represented as two hyphen-separated Unicode codepoints
		indicating the inclusive start and end codepoints of a range

wildcard range (e.g. U+4??)

defined by the set of codepoints implied when
		trailing '?' characters signify any hexadecimal digit

Individual codepoints are written using hexadecimal values that correspond to

Unicode character codepoints
.
	Unicode codepoint values must be between 0 and 10FFFF inclusive. Digit
	values of codepoints are 
ASCII case-insensitive
. For interval ranges,
	the start and end codepoints must be within the range noted above and
	the end codepoint must be greater than or equal to the start
	codepoint.

Wildcard ranges specified with ‘?’ that lack an
	initial digit (e.g. "U+???") are valid and equivalent
	to a wildcard range with an initial zero digit (e.g. "U+0???" = "U+0000-0FFF").
	Wildcard ranges that extend beyond the range of
	Unicode codepoints are invalid. Because of this, the maximum
	number of trailing '?' wildcard characters is five, even though the

UNICODE-RANGE

	token accepts six.

Within the comma-delimited list of Unicode ranges in a

unicode-range
 descriptor declaration, ranges may overlap. The union
	of these ranges defines the set of codepoints for which the
	corresponding font may be used. User agents must not download or use
	the font for codepoints outside this set. User agents may normalize
	the list of ranges into a list that is different but represents the
	same set of codepoints.

The associated font might not contain glyphs for the entire set of
	codepoints defined by the 
unicode-range
 descriptor. When the font
	is used, the 
effective character map
 is the intersection of the
	codepoints defined by 
unicode-range
 with the font’s 
character map
.
	This allows authors to define supported ranges in terms of broad
	ranges without worrying about the precise codepoint ranges supported
	by the underlying font.

4.5.1. 
Using character ranges to define composite fonts

Multiple 
@font-face
 rules with different unicode ranges for the same
	family and style descriptor values can be used to create composite fonts
	that mix the glyphs from different fonts for different scripts. This
	can be used to combine fonts that only contain glyphs for a single
	script (e.g. Latin, Greek, Cyrillic) or it can be used by authors as a
	way of segmenting a font into fonts for commonly used characters and
	less frequently used characters. Since the user agent will only pull
	down the fonts it needs this helps reduce page bandwidth.

If the unicode ranges overlap for a set of 
@font-face
 rules with the
	same family and style descriptor values, the rules are ordered in the
	reverse order they were defined; the last rule defined is the first to
	be checked for a given character.

Example ranges for specific languages or characters:

unicode-range: U+A5;

a single code point, the yen/yuan symbol

unicode-range: U+0-7F;

code range for basic ASCII characters

unicode-range: U+590-5ff;

code range for Hebrew characters

unicode-range: U+A5, U+4E00-9FFF, U+30??, U+FF00-FF9F;

code range for Japanese kanji, hiragana and katakana characters plus yen/yuan symbol

		The BBC provides news services in a wide variety of languages, many
		that are not well supported across all platforms. Using an 
@font-face

		rule, the BBC could provide a font for any of these languages, as it
		already does via a manual font download.

@font-face

{

font-family
:
 BBCBengali
;

src
:

url
(
fonts/BBCBengali.woff
)

format
(
"woff"
);

unicode-range
:
 U
+00
-FF
,
 U
+980
-
9
FF
;

}

		Technical documents often require a wide range of symbols.  The STIX
		Fonts project is one project aimed at providing fonts to support a wide
		range of technical typesetting in a standardized way.  The example below
		shows the use of a font that provides glyphs for many of the
		mathematical and technical symbol ranges within Unicode:

@font-face

{

font-family
:
 STIXGeneral
;

src
:

local
(
STIXGeneral
),

url
(
/stixfonts/STIXGeneral.otf
);

unicode-range
:
 U
+000
-
49
F
,
 U
+2000
-
27
FF
,
 U
+2900
-
2
BFF
,
 U
+1
D
400
-
1
D
7
FF
;

}

		This example shows how an author can override the glyphs used for
		Latin characters in a Japanese font with glyphs from a different font.
		The first rule specifies no range so it defaults to the entire range.
		The range specified in the second rule overlaps but takes precedence
		because it is defined later.

@font-face

{

font-family
:
 JapaneseWithGentium
;

src
:

local
(
MSMincho
);

/* no range specified, defaults to entire range */

}

@font-face

{

font-family
:
 JapaneseWithGentium
;

src
:

url
(
../fonts/Gentium.woff
);

unicode-range
:
 U
+0
-
2
FF
;

}

		Consider a family constructed to optimize bandwidth by separating out
		Latin, Japanese and other characters into different font files:

/* fallback font - size: 4.5MB */

@font-face

{

font-family
:
 DroidSans
;

src
:

url
(
DroidSansFallback.woff
);

/* no range specified, defaults to entire range */

}

/* Japanese glyphs - size: 1.2MB */

@font-face

{

font-family
:
 DroidSans
;

src
:

url
(
DroidSansJapanese.woff
);

unicode-range
:
 U
+3000
-
9
FFF
,
 U+ff??
;

}

/* Latin, Greek, Cyrillic along with some

  punctuation and symbols - size: 190KB */

@font-face

{

font-family
:
 DroidSans
;

src
:

url
(
DroidSans.woff
);

unicode-range
:
 U
+000
-
5
FF
,
 U
+1e00
-
1
fff
,
 U
+2000
-
2300
;

}

For simple Latin text, only the font for Latin characters is downloaded:

body 
{

font-family
:
 DroidSans
;

}

<p>This is that</p>

In this case the user agent first checks the unicode-range for the
		font containing Latin characters (DroidSans.woff).  Since all the
		characters above are in the range U+0-5FF, the user agent downloads the
		font and renders the text with that font.

Next, consider text that makes use of an arrow character (⇨):

<p>This &#x21e8
;
 that<p>

The user agent again first checks the unicode-range of the font
		containing Latin characters. Since U+2000-2300 includes the arrow
		code point (U+21E8), the user agent downloads the font. For this
		character however the Latin font does not have a matching glyph, so the
		effective unicode-range used for font matching excludes this code point.
		Next, the user agent evaluates the Japanese font. The unicode-range for
		the Japanese font, U+3000-9FFF and U+ff??, does not include U+21E8, so
		the user agent does not download the Japanese font.
		Next the fallback font is considered. The 
@font-face
 rule for the
		fallback font does not define unicode-range so its value defaults to
		the range of all Unicode code points. The fallback font is downloaded and
		used to render the arrow character.

4.6. 

Font features and variations: the 
font-feature-settings
 and 
font-variation-settings
 descriptors

Name:

font-feature-settings

For:

@font-face

Value:

normal 
|

<feature-tag-value>
#

Initial:

normal

Tests

font-feature-resolution-001.html

(live test)

(source)

font-feature-resolution-002.html

(live test)

(source)

font-feature-settings-descriptor-01.html

(live test)

(source)

font-feature-settings-descriptor-02.html

(live test)

(source)

font-feature-settings-descriptor-binary.html

(live test)

(source)

font-feature-settings-serialization-001.html

(live test)

(source)

Name:

font-variation-settings

For:

@font-face

Value:

normal 
|
 [ 
<string>

<number>
]
#

Initial:

normal

Tests

calc-in-font-variation-settings.html

(live test)

(source)

font-variation-settings-descriptor-01.html

(live test)

(source)

font-variation-settings-descriptor-02.html

(live test)

(source)

font-variation-settings-descriptor-03.html

(live test)

(source)

font-variation-settings-descriptor-04.html

(live test)

(source)

font-variation-settings-serialization-001.html

(live test)

(source)

font-variation-settings-serialization-002.html

(live test)

(source)

font-variation-settings-composition.html

(live test)

(source)

font-variation-settings-interpolation.html

(live test)

(source)

font-variation-settings-computed.html

(live test)

(source)

font-variation-settings-invalid.html

(live test)

(source)

font-variation-settings-valid.html

(live test)

(source)

font-variation-settings-inherit.html

(live test)

(source)

These descriptors define initial settings that apply when the font defined by
	an 
@font-face
 rule is rendered.  They do not affect font selection.
	Values are identical to those defined for the corresponding

font-feature-settings
 and

font-variation-settings
 properties defined below
	except that the 
CSS-wide keywords
 are omitted. When multiple font
	feature descriptors, properties, or variations are used, optionally along with a named instance,
	the cumulative effect on
	text rendering is detailed in the section

§ 7 Font Feature and Variation Resolution
 below.

These descriptors set features and variation values
	on the font object which the 
@font-face
 rule represents,
	rather than on an entire element.
	Therefore, when using these descriptors,
	only some glyphs in an element may be rendered with that feature,
	due to 
§ 5.3 Cluster matching
.

4.7. 
Using named instances from variable fonts: the 
font-named-instance
 descriptor

Name:

font-named-instance

For:

@font-face

Value:

auto 
|

<string>

Initial:

auto

If the 
font-named-instance
 descriptor is set
	to a value other than 
auto
,
	then the appropriate stage in the 
§ 7 Font Feature and Variation Resolution

	will inspect the font file to find the first named instance in
	the font which has a localized name equal to the given 
<string>

	according to the rules given in 
§ 5.1 Localized name matching
.
	If no such named instance exists,
	this descriptor is treated as if it has a value of 'font-named-instance/auto'.
	Otherwise, this named instance’s variation axis values
	are applied to this position in the 
§ 7 Font Feature and Variation Resolution
.

		For example, the following 
@font-face
 block will
		apply the instance named "Grotesque"
		but will override the "XHGT" axis to have a value of 0.7.

@font-face

{

font-family
:

"AccuroVar"
;

src
:

url
(
"accurovar.otf"
)

format
(
"opentype"
);

font-named-instance
:

"Grotesque"
;

font-variation-settings
:

"XHGT"

0.7
;

}

Note:
 Because the variation axis values supplied in the

font-weight
, 
font-width
, and 
font-style
 properties
		are applied before
		the value in the 
font-named-instance
 descriptor,
		there is no need to change the value of those properties
		when a named instance is desired.

4.8. 
Font request guidelines

4.8.1. 
Font loading guidelines

The 
@font-face
 rule is designed to allow lazy loading
	of font resources that are only downloaded when used within a
	document. A stylesheet can include 
@font-face
 rules for
	a library of fonts of which only a select set are used; user agents
	must only download those fonts that are referred to within the style
	rules applicable to a given page. User agents that download all fonts
	defined in 
@font-face
 rules without considering whether
	those fonts are in fact used within a page are considered
	non-conformant. In cases where a font might be downloaded in character
	fallback cases, user agents may download a font if it’s contained within
	the computed value of 
font-family

	for a given text run.

@font-face

{

font-family
:
 GeometricModern
;

src
:

url
(
font.woff
);

}

p 
{

/* font will be downloaded for pages with p elements */

  font-family: GeometricModern
,
 sans-serif
;

}

h2 
{

/* font may be downloaded for pages with h2 elements, even if Futura is available locally */

  font-family: Futura
,
 GeometricModern
,
 sans-serif
;

}

In cases where textual content is loaded before downloadable fonts are available,
	user agents must render text according to the 
font-display
 descriptor of that 
@font-face
 block.
	In cases where the font download fails, user agents must
	display the text visibly. Authors are advised to use fallback fonts in
	their font lists that closely match the metrics of the
	downloadable fonts to avoid large page reflows where possible.

4.8.2. 

Font fetching requirements

		To 
fetch a font
 given a selected 
<url>

url
 for 
@font-face

rule
,

fetch

url
,
		with ruleOrDeclaration being 
rule
,
		destination "font",
		CORS mode "cors",
		and processResponse being the following steps given 
response

res
 and null, failure or a
		byte stream 
stream
:

If 
stream
 is null, return.

 Load a font from 
stream
 according to its type.

Note:
 The implications of this for authors are that fonts
	will typically not be loaded cross-origin unless authors specifically
	take steps to permit cross-origin loads. Sites can explicitly allow
	cross-site loading of font data using the 
Access-Control-Allow-Origin

	HTTP header.  For other schemes, no explicit mechanism to allow
	cross-origin loading, beyond what is permitted by the

fetch

	algorithm, is defined or required.

Tests

test_datafont_same_origin.html

(live test)

(source)

		For the examples given below, assume that a document is located at

https
:
//example.com/page.html
 and all URLs link to valid
		font resources supported by the user agent.

Fonts defined with the 
src
 descriptor values below will be loaded:

/* same origin (i.e. domain, scheme, port match document) */

    src: 
url
(
fonts/simple.woff
);

/* data urls with no redirects are treated as same origin */

    src: 
url
(
"data:application/font-woff;base64,..."
);

/* cross origin, different domain */

/* Access-Control-Allow-Origin response header set to '*' */

    src: 
url
(
http://another.example.com/fonts/simple.woff
);

Fonts defined with the 
src
 descriptor values below will fail to load:

/* cross origin, different scheme */

/* no Access-Control-xxx headers in response */

    src: 
url
(
http://example.com/fonts/simple.woff
);

/* cross origin, different domain */

/* no Access-Control-xxx headers in response */

    src: 
url
(
http://another.example.com/fonts/simple.woff
);

4.9. 

Controlling Font Display Per Font-Face: the 
font-display
 descriptor

The 
font-display
 descriptor for 
@font-face

	determines how a font face is displayed,
	based on whether and when it is downloaded and ready to use.

Name:

font-display

For:

@font-face

Value:

auto 
|
 block 
|
 swap 
|
 fallback 
|
 optional

Initial:

auto

Tests

font-display-change.html

(live test)

(source)

font-display-failure-fallback.html

(live test)

(source)

font-display-preload.html

(live test)

(source)

font-display.html

(live test)

(source)

Note:
 For all of these values,
	user agents may use slightly different durations,
	or more sophisticated behaviors that can’t be directly expressed in the 
font-display
 syntax,
	in order to provide more useful behavior for their users.
	They may also provide the ability for users to override author-chosen behavior
	with something more desirable;
	for example, forcing all fonts to have a 
0s

block period
.

auto

			The font display policy is user-agent-defined.

Note:
 Many browsers have a default policy similar to that specified by 
block
.

block

			Gives the font face a short 
block period

			(
3s
 is recommended in most cases)
			and an infinite 
swap period
.

Note:
 In other words, the browser draws "invisible" text at first if it’s not loaded,
			but swaps the font face in as soon as it loads.

This value must only be used when rendering text in a particular font is required for the page to be usable.
			It must only be used for small pieces of text.

				For example, badly designed "icon fonts" might associate a "⎙" (printer) icon
				with an unrelated character like "P",
				so if the text is displayed with a fallback font instead
				there will be confusing letters scattered around the page
				rather than the desired icon.
				In this case, temporary blank spots are better than using a fallback font.

(However, the fallback font is used 
eventually
,
				as having confusing letters scattered around the page
				is better than having links and such never show up at all.)

A better solution is described in the

Accessibility Considerations
 section.

swap

			Gives the font face an extremely small 
block period

			(
100ms
 or less is recommended in most cases)
			and an infinite 
swap period
.

Note:
 In other words, the browser draws the text immediately with a fallback if the font face isn’t loaded,
			but swaps the font face in as soon as it loads.

This value should only be used when rendering text in a particular font is very important for the page,
			but rendering in any font will still get a correct message across.
			It should only be used for small pieces of text.

				For example,
				if a website has a custom font for rendering their logo,
				rendering that logo correctly is fairly important for branding purposes,
				but displaying the logo in any font will at least get the point across without confusion.

fallback

			Gives the font face an extremely small 
block period

			(
100ms
 or less is recommended in most cases)
			and a short 
swap period

			(
3s
 is recommended in most cases).

Note:
 In other words, the font face is rendered with a fallback at first if it’s not loaded,
			but it’s swapped in as soon as it loads.
			However, if too much time passes,
			the fallback will be used for the rest of the page’s lifetime instead.

This value should be used for body text,
			or any other text where the use of the chosen font is useful and desired,
			but it’s acceptable for the user to see the text in a fallback font.
			This value is appropriate to use for large pieces of text.

				For example,
				in large pieces of body text,
				it’s most important just to get the text rendered quickly,
				so the user can begin to read as quickly as possible.
				Further, once the user has started reading,
				they shouldn’t be disturbed by the text suddenly "shifting"
				as a new font is swapped in,
				as that’s distracting and annoying to re-find where one was in the text.

optional

			If the font can be loaded "immediately"
			(such that it’s available to be used for the "first paint" of the text),
			the font is used.

Otherwise, the font is treated
			as if its 
block period
 and 
swap period
 both expired before it finished loading.
			If the font is not used due to this,
			the user agent may choose to abort the font download,
			or download it with a very low priority.
			If the user agent believes it would be useful for the user,
			it may avoid even starting the font download,
			and proceed immediately to using a fallback font.

An 
optional
 font 
must never

			cause the layout of the page to "jump" as it loads in.
			A user agent 
may
 choose to slightly delay rendering an element using an optional font
			to give it time to load from a possibly-slow local cache,
			but once the text has been painted to the screen with a fallback font instead,
			it must not be rendered with the 
optional
 font for the rest of the page’s lifetime.

This value should be used for body text,
			or any other text where the chosen font is purely a decorative "nice-to-have".
			It should be used anytime it is more important that the web page render quickly on first visit,
			than it is that the user wait a longer time to see everything perfect immediately.

				For example, body text is perfectly readable in one of the browser default fonts,
				though a downloadable font face might be more attractive
				and mesh with the site’s aesthetics better.
				First time visitors to a site generally care far more about the site being quickly usable
				than they do about the finer points of its display,
				and 
optional
 provides a good behavior for them.
				If they return later,
				the desired font faces might have finished downloading,
				giving them the "intended" experience without slowing down
				either their first or subsequent visits.

Users on very slow connections might not ever receive the "intended" experience,
				but 
optional
 ensures they can actually 
use
 the site,
				rather than quitting and going elsewhere because the site takes too long to load.

				To increase the chance that an 
optional
 font will be available
				in time to use for rendering some text,
				it is recommended that the user agent employ heuristics
				to make it faster to access
				or to judge when it would be worthwhile to delay rendering some text,
				such as checking if the font is preloaded in HTML,
				or moving the file from slower to faster in-memory caches
				as soon as it is seen in a stylesheet
				(before it’s known whether it will be used on the page).

These heuristics cannot be relied upon by authors, however;
				it must be understood that the 
optional
 value
				can result in the font never being used.
				If a somewhat higher assurance of the font being used is needed,
				authors should consider using the 
fallback
 value.

4.9.1. 

Controlling Font Display Per Font-Family via 
@font-feature-values

The 
font-display
 descriptor for 
@font-feature-values

	determines how a font family is displayed,
	by setting the "default" font-display value
	for 
@font-face
 rules targeting the same font family.
	When 
font-display
 is omitted in an 
@font-face
 rule,
	the user agent uses the 
font-display
 value
	set via 
@font-feature-values
 for the relevant font-family if one is set,
	and otherwise defaults to 
auto
.

This mechanism can be used to set a default display policy for an entire font-family,
	and enables developers to set a display policy for 
@font-face
 rules
	that are not directly under their control.
	For example, when a font is served by a third-party font foundry,
	the developer does not control the 
@font-face
 rules
	but is still able to set a default font-display policy for the provided font-family.
	The ability to set a default policy for an entire font-family
	is also useful to avoid the ransom note effect
	(i.e. mismatched font faces)
	because the display policy is then applied to the entire font family.

Name:

font-display

For:

@font-feature-values

Value:

auto 
|
 block 
|
 swap 
|
 fallback 
|
 optional

Initial:

auto

4.10. 

Default font language overriding: the 
font-language-override
 descriptor

Name:

font-language-override

For:

@font-face

Value:

normal 
|

<string>

Initial:

normal

This descriptor defines initial settings that apply when the font defined by an @font-face rule is rendered. It does not affect font selection. Values are identical to those defined for the 
font-language-override
 property defined below except that the value inherit is omitted. When multiple font feature descriptors, properties, or variations are used, the cumulative effect on text rendering is detailed in the section 
§ 7 Font Feature and Variation Resolution
 below.

4.11. 

Default font metrics overriding:
the 
ascent-override
,

descent-override
 and

line-gap-override
 descriptors

Name:

ascent-override

For:

@font-face

Value:

normal 
|

<percentage [0,∞]>

Initial:

normal

Tests

ascent-descent-override.html

(live test)

(source)

metrics-override-normal-keyword.html

(live test)

(source)

font-face-metric-overrides.html

(live test)

(source)

Name:

descent-override

For:

@font-face

Value:

normal 
|

<percentage [0,∞]>

Initial:

normal

Tests

ascent-descent-override.html

(live test)

(source)

metrics-override-normal-keyword.html

(live test)

(source)

font-face-metric-overrides.html

(live test)

(source)

Name:

line-gap-override

For:

@font-face

Value:

normal 
|

<percentage [0,∞]>

Initial:

normal

Tests

line-gap-override.html

(live test)

(source)

metrics-override-normal-keyword.html

(live test)

(source)

font-face-metric-overrides.html

(live test)

(source)

The 
ascent-override
,

descent-override
 and

line-gap-override
 descriptors define the

ascent metric
, 
descent metric
 and

line gap metric
 of the font, respectively.

When the descriptor value is 
normal
, the corresponding metric value is obtained from the
	font file directly.

Note:
 User agents may draw data from different places from the font file as the metric values,
	which results in different text layouts.

When the descriptor value is a percentage, the corresponding metric value is resolved as the
	given percentage multiplied by the used font size. Negative values are invalid at parse time.

		The percentage is resolved against different font sizes for different elements.

@font-face

{

font-family
:
 overridden-font
;

ascent-override
:

50
%
;

  ...

}

<span style=
"font-family: overridden-font; font-size: 20px;"
>
  Outer span content
  <span style=
"font-size: 150%;"
>Inner span content</span>
</span>

The outer span uses an 
ascent
 value of
		10px, whereas the inner span uses 15px.

		We may override the metrics of a local fallback font to match the primary font, which
		is a web font. This reduces layout shifting when switching from fallback to the
		primary font.

@font-face

{

font-family
:
 cool-web-font
;

src
:

url
(
"https://example.com/font.woff"
);

}

@font-face

{

font-family
:
 fallback-to-local
;

src
:

local
(
Some Local Font
);

/* Override metric values to match cool-web-font */

  ascent-override: 
125
%
;

descent-override
:

25
%
;

line-gap-override
:

0
%
;

}

<div style=
"font-family: cool-web-font, fallback-to-local"
>Title goes here</div>
<img src=
"https://example.com/largeimage"
 alt=
"A large image that you don't want to shift"
>

The image will not be vertically shifted when the user agent finishes loading and
		switches to use the web font.

5. 
Font Matching Algorithm

The algorithm below describes how fonts are associated with individual runs of text.
	For each character in the run
	a font family is chosen
	and a particular font face is selected
	containing a glyph for that character.

The set of  
installed fonts
 available
	to the Font Matching Algorithm
	is explicitly undefined.

The default set of installed fonts will vary
	by UA, platform, and locale;
	it is important that users be able to customise
	which installed fonts are available for rendering web pages
	and to which generic font families, if any,
	these fonts are mapped.

UAs may choose to expose all installed fonts to the web,
	regardless of how that font was installed;
	doing so is likely to have good internationalization properties
	for users whose primary language is not supported
	by fonts shipping with their operating system.

UAs may alternatively choose
	to not initially expose any user-installed fonts to aid privacy on the web;
	for the set of installed fonts a user has installed
	is often used as a tracking vector to track users across the web.
	Users should then be able to add to or remove fonts from that set,
	according to their needs.

UAs may choose a hybrid approach, where some user-installed fonts
	are initially exposed for internationalization,
	but others aren’t.
	Again, users should be able to customise this starting set.

UAs are expected to make informed decisions
	on which fonts they expose to the web by default,
	so as to balance between internationalization and privacy.
	UAs are expected to also provide a convenient means
	for users to add and subtract fonts
	to meet their particular needs.

Tests

fallback-remote-to-data-url.html

(live test)

(source)

fallback-url-to-local.html

(live test)

(source)

at-font-face-font-matching.html

(live test)

(source)

5.1. 
Localized name matching

Some font file formats allow
	font faces to carry multiple localizations
	of a particular string
	(e.g. family name or named instance).
	User agents must recognize and correctly match all of these names
	independent of the underlying platform localization,
	system API used, or document encoding.

		For example,
		for each of the fonts listed below,
		the author can use either the Latin name
		or the localized name
		in the 
font-family
 property,
		and the results will be identical on all systems:

Localized family names

User agents must match these names case insensitively,
	using the "Default Caseless Matching" algorithm outlined in the Unicode specification 
[UNICODE]
.
	This algorithm is detailed in section 3.13 entitled "Default Case Algorithms".
	Specifically, the algorithm must be applied
	without normalizing the strings involved
	and without applying any language-specific tailorings.
	The case folding method specified by this algorithm
	uses the case mappings with status field "C" or "F"
	in the CaseFolding.txt file of the Unicode Character Database.

Note:
 For authors this means that font family names are matched case insensitively,
	whether those names exist in a platform font
	or in the 
@font-face
 rules contained in a stylesheet.
	Authors should take care to ensure that names
	use a character sequence consistent with the actual font family name,
	particularly when using combining characters such as diacritical marks.
	For example, a family name that contains a lowercase a (U+0061)
	followed by a combining ring (U+030A)
	will 
not
 match a name that looks identical
	but which uses the precomposed lowercase a-ring character (U+00E5)
	instead of the combining sequence.

Note:
 Implementors should take care to verify that a given caseless string comparison implementation
	uses this precise algorithm
	and not assume that a given platform string matching routine follows it,
	as many of these have locale-specific behavior
	or use some level of string normalization.

5.2. 
Matching font styles

The procedure for choosing a font
	for a given character in a run of text
	consists of iterating over the font families named by the 
font-family
 property,
	selecting a font face with the appropriate style
	based on other font properties
	and then determining whether a glyph exists for the given character.
	This is done using the 
character map
 of the font,
	data which maps characters to the default glyph for that character.
	A font is considered to 
support
 a given character if
	(1) the character is contained in the font’s 
character map
 and
	(2) if required by the containing script, shaping information is available for that character.

Some legacy fonts might include a given character in the 
character map

	but lack the shaping information
	(e.g. 
OpenType layout tables

	or 
Graphite tables
)
	necessary for correctly rendering text runs containing that character.

Codepoint sequences consisting of a base character
	followed by a sequence of combining characters
	are treated slightly differently,
	see the section on 
cluster matching
 below.

For this procedure,
	the 
default font face
 for a given font family
	is defined to be the face that would be selected
	if all font style properties were set to their initial value.

Using the computed font property values for a given element,
the user agent starts with the first family name
specified by the 
font-family
 property.

If the family name is a generic family keyword, the user agent
looks up the appropriate font family name to be used.  User
agents may choose the generic font family to use based on the
language of the containing element or the Unicode range of the
character.

For other family names, the user agent attempts to find the
family name among fonts defined via 
@font-face
 rules and then
among available installed fonts
(this may include font aliases),
matching names with a

§ 5.1 Localized name matching
 as outlined
in the section above.
If the font
resources defined for a given face in an 
@font-face
 rule are either
not available or contain invalid font data, then the face should be
treated as not present in the family. If no faces are present for a
family defined via 
@font-face
 rules, the family should be treated as
missing; matching a platform font with the same name must not occur
in this case.

If a font family match occurs, the user agent assembles the set
of font faces in that family and then narrows the set to a single
face using other font properties in the order given below. Fonts might be
present in this group which can support a range of

font-width
, 
font-style
, or 
font-weight
 properties. In
this case, the algorithm proceeds as if each supported combination of
values is a unique font in the set. If such a font is ultimately
selected by this algorithm, particular values for

font-width
, 
font-style
, and 
font-weight
 must be applied
before any layout or rendering occurs. The application of these values
must be applied in the 
Apply
font matching variations
 step detailed in

§ 7 Font Feature and Variation Resolution
.
A group
of faces defined via 
@font-face
 rules with identical font
descriptor values but differing 
unicode-range
 values are considered to be
a single 
composite font face
 for this step:

Tests

fixed-stretch-style-over-weight.html

(live test)

(source)

stretch-distance-over-weight-distance.html

(live test)

(source)

style-ranges-over-weight-direction.html

(live test)

(source)

font-width
 is tried first. If a font
does not have any concept of varying strengths of width values, its width value
is mapped according table in the 
property definition
.
If the matching set includes faces with width values
containing the 
font-width
 desired value, faces with width values which do not include the desired width value
are removed from the matching set. If there is no face
which contains the desired value, a width value is chosen using the rules below:

If the desired width value is less than or equal to 100%, width values below the
desired width value are checked in descending order followed by
width values above the desired width value in ascending order until a
match is found.

Otherwise, width values above the
desired width value are checked in ascending order followed by
width values below the desired width value in descending order until a
match is found.

Once the
closest matching width has been determined by this process,
faces with widths which do not include this determined width are removed from the matching set.

	This search algorithm can be thought of as a distance function, where the lowest-distance value present in the font family is selected, and all fonts not including that value are eliminated.

Consider a font family with three fonts, named A, B, and C, each with associated supported ranges for the 
font-width
 descriptor. If an element is styled with "font-width: 125%", the search algorithm can be visualized as follows:

The font width ranges supported by fonts A, B, and C are shown in the graph above. As you can see, because font B contains the minimum width value across the entire family, font B would be selected by this algorithm. However, if font B were somehow eliminated from the family, font C would then contain the lowest distance in the family, so it would be selected.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-width: 75%":

As you can see, because font B contains the minimum width value across the entire family, font B would be selected by this algorithm. However, if font B were somehow eliminated from the family, font A would then contain the lowest distance in the family, so it would be selected.

font-style
 is tried next
(see 
§ 5.2 Matching font styles
).
If a font does not have any concept of varying strengths of italics or oblique angles, its style
is mapped according to the description in the 
font-style
 property definition.

If the value of 
font-style
 is 
italic
:

If the matching set includes faces with italic values containing the mapped value of 
italic
,
then faces with italic values which do not include the desired italic mapped value are removed from the matching set.

Otherwise, italic values above the desired italic value are checked in ascending order followed by
italic values below the desired italic value, until 0 is hit. Only positive values of italic values are checked
in this stage.

For variable fonts with an ital axis,
a match is created by setting the ital value to 1.

If no match is found, oblique values greater than or equal to 11deg are checked in ascending order
followed by oblique values below 11deg in descending order, until 0 is hit. Only positive values of oblique values
are checked in this stage.

 The threshold for preferring oblique over normal 
should be lower than the average angle
.

If no match is found, italic values less than or equal to 0 are checked in descending order until a match is found.

If no match is found, oblique values less than or equal to 0deg are checked in descending order until a match is found.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-style: italic":

As you can see, because font D contains the minimum italic value across the entire family, font D would be selected by this algorithm. However, if font D were somehow eliminated from the family, font E would then contain the lowest distance in the family, so it would be selected. If E were eliminated, C would be selected. If C were eliminated, font B would not be chosen immediately; instead, oblique values would be consulted and an oblique value might be chosen. However, if no oblique value is chosen, font B would then be selected, followed by font A.

If the value of 
font-style
 is 
oblique
 and the requested angle is greater than or equal to 11deg,

If the matching set includes faces with oblique values containing the value of 
oblique
,
faces with oblique values which do not include the desired oblique value are removed from the matching set.

Otherwise, oblique values above the desired oblique value are checked in ascending order followed by
oblique values below the desired oblique value, until 0 is hit. Only positive values of oblique values are checked in this stage.

For variable fonts with a slnt axis,
a match is created by setting the slnt value
with the specified oblique value.
Otherwise, if 
font-synthesis-style
 has the value

auto
,
then a fallback match is produced
by geometric shearing to the specified oblique value.
The ital axis is not used to satisfy an 
oblique
 request.

If no match is found, italic values greater than or equal to 1 are checked in ascending order
followed by italic values below 1 in descending order, until 0 is hit. Only positive values of italic values are checked in this stage.

If no match is found, oblique values less than or equal to 0deg are checked in descending order until a match is found.

If no match is found, italic values less than or equal to 0 are checked in descending order until a match is found.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-style: oblique 40deg":

As you can see, because font D contains the minimum oblique value across the entire family, font D would be selected by this algorithm. However, if font D were somehow eliminated from the family, font E would then contain the lowest distance in the family, so it would be selected. If E were eliminated, C would be selected. If C were eliminated, font B would not be chosen immediately; instead, italic values would be consulted and an italic value might be chosen. However, if no italic value is chosen, font B would then be selected, followed by font A.

If the value of 
font-style
 is 
oblique
 and the requested angle is greater than or equal to 0deg and less than 11deg,

If the matching set includes faces with oblique values containing the value of 
oblique
,
faces with oblique values which do not include the desired oblique value are removed from the matching
set.

Otherwise, oblique values below the desired oblique value are checked in descending order until 0 is hit, followed by
oblique values above the desired oblique value. Only positive values of oblique values are checked
in this stage.

For variable fonts with a slnt axis,
a match is created by setting the slnt value
with the specified oblique value.
Otherwise, if 
font-synthesis-style
 has the value 
auto
,
then a fallback match is produced
by geometric shearing to the specified oblique value.
The ital axis is not used to satisfy an 
oblique
 request.

If no match is found, italic values less than 1 are checked in descending order until 0 is hit,
followed by italic values above 1 in ascending order. Only positive values of italic values
are checked in this stage.

If no match is found, oblique values less than or equal to 0deg are checked in descending order until a match is found.

If no match is found, italic values less than or equal to 0 are checked in descending order until a match is found.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-style: oblique 13deg":

As you can see, because font D contains the minimum oblique value across the entire family, font D would be selected by this algorithm. However, if font D were somehow eliminated from the family, font C would then contain the lowest distance in the family, so it would be selected. If C were eliminated, E would be selected. If E were eliminated, font B would not be chosen immediately; instead, italic values would be consulted and an italic value might be chosen. However, if no italic value is chosen, font B would then be selected, followed by font A.

If the value of 
font-style
 is 
oblique
 and the requested angle is less than 0deg and greater than -11deg, follow the steps 
above
, except with the negated values and opposite directions. If the value of 
font-style
 is 
oblique
 and the requested angle is less than or equal to -11deg, follow the steps 
above
, except with the negated values and opposite directions.

If the value of 
font-style
 is 
normal
,

Oblique values greater than or equal to 0 are checked in ascending order.

If no match is found, italic values greater than or equal to 0 are checked in ascending

If no match is found, oblique values less than 0deg are checked in descending order until a match is found.

If no match is found, italic values less than 0 are checked in descending order until a match is found.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-style: normal":

As you can see, because font C contains the minimum oblique value across the entire family, font C would be selected by this algorithm. However, if font C were somehow eliminated from the family, font B would not be chosen immediately; instead, italic values would be consulted and an italic value might be chosen. However, if no italic value is chosen, font B would then be selected, followed by font A.

If an oblique angle was found in the above search, all faces which don’t include that oblique angle are excluded from the matching set. Otherwise, if an italic value was found in the above search, all faces which don’t include that italic value are excluded from the matching set.

Tests

oblique-last-resort-weight-selection.html

(live test)

(source)

oblique-request-italic-only-family-no-crash.html

(live test)

(source)

User agents are not required to distinguish between italic and oblique fonts. In such user agents, the 
font-style
 matching steps above are performed by mapping both italic values and oblique angles onto a common scale. The exact nature of this mapping is undefined, however, an italic value of 1 must map to the same value that an oblique angle of 11deg maps to. Within font
families defined via 
@font-face
 rules, italic and oblique
faces must be distinguished using the value of the

font-style
 descriptor.

For families that lack any italic or oblique faces, user agents
may create artificial oblique faces, if this is permitted by the
value of the 
font-synthesis
 property.

font-weight
 is matched next. If a font does not have any concept of varying strengths of weights, its weight is mapped according list in the 
property definition
. If bolder/lighter relative weights are used, the effective weight is calculated based on the inherited weight value, as described in the definition of the 
font-weight
 property. If the matching set after performing the steps above includes faces with weight values containing the font-weight desired value, faces with weight values which do not include the desired font-weight value are removed from the matching set. If there is no face which contains the desired value, a weight value is chosen using the rules below:

If the desired weight is inclusively between 400 and 500, weights greater than or equal to the target weight are checked in ascending order until 500 is hit and checked, followed by weights less than the target weight in descending order, followed by weights greater than 500, until a match is found.

If the desired weight is less than 400, weights less than or equal to the
desired weight are checked in descending order followed by
weights above the desired weight in ascending order until a
match is found.

If the desired weight is greater than 500, weights greater than or equal to the
desired weight are checked in ascending order followed by
weights below the desired weight in descending order until a
match is found.

Tests

font-weight-search-direction.html

(live test)

(source)

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-weight: 400":

As you can see, because font B contains the minimum distance across the entire family, font B would be selected by this algorithm. However, if font B were somehow eliminated from the family, font C would then contain the lowest distance in the family, so it would be selected. If C were eliminated, D would be selected, followed by fonts A and then E.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-weight: 450":

As you can see, because font C contains the minimum distance across the entire family, font C would be selected by this algorithm. However, if font C were somehow eliminated from the family, font D would then contain the lowest distance in the family, so it would be selected. If D were also eliminated, B would be selected, followed by fonts A and then E.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-weight: 500":

As you can see, because font D contains the minimum distance across the entire family, font D would be selected by this algorithm. However, if font D were somehow eliminated from the family, font B would then contain the lowest distance in the family, so it would be selected. If B were eliminated, C would be selected, followed by fonts B, A, and then E.

	Similar to the 
previous example
, here is the conceptual distance graph for an element styled with "font-weight: 300":

As you can see, because font B contains the minimum distance across the entire family, font B would be selected by this algorithm. However, if font B were somehow eliminated from the family, font A would then contain the lowest distance in the family, so it would be selected. If A were eliminated, C would be selected.

Once the closest matching weight has been determined by this process,
faces with weights which do not include this determined weight are removed from the matching set.

Note:
 There is a small behavior change between 
[CSS-FONTS-3]
 and this specification
with the animation of the 
font-weight
 property.
Previously, interpolated values of font-weight were rounded to their closest multiple of 100,
and the font-matching algorithm was run on these rounded values.
In this specification, the font-matching algorithm is able to accept any value,
so no rounding occurs.
The small behavior change is due to the discontinuous nature of the font-matching algorithm.

font-size
 must be
matched within a UA-dependent margin of tolerance. (Typically, sizes
for scalable fonts are rounded to the nearest whole pixel, while the
tolerance for bitmapped fonts could be as large as 20%.) Further
computations, e.g., by 
em
 values in other properties, are based on
the 
font-size
 value that
is used, not the one that is specified.

Note that more than one font might be remaining in the matching set after performing
the above steps. If so, the user agent must choose a single font from
the matching set and continue these steps with it. The choice of which
font to choose can differ between multiple user agents and multiple operating
system platforms; however, it must not differ between two elements in the same document.

If the matched face is defined via 
@font-face

rules, user agents must use the procedure below to select a single
font:

If the font resource has not been loaded and the range of
characters defined by the 
unicode-range
 descriptor value
includes the character in question, load the font.

After downloading, if the 
effective character map

supports the character in question, select that font.

When the matched face is a 
composite face
, user agents must use
the procedure above on each of the faces in the 
composite face
 in
reverse order of 
@font-face
 rule definition.

While the download occurs, user agents must either wait until the
font is downloaded or render once with substituted font metrics and
render again once the font is downloaded.

If no matching face exists or the matched face does not contain
a glyph for the character to be rendered, the next family name is
selected and the previous three steps repeated.  Glyphs from other
faces in the family are not considered.  The only exception is that
user agents may optionally substitute a synthetically obliqued version of the

default face
 if that face supports a given glyph and synthesis
of these faces is permitted by the value of the 
font-synthesis
 property.
For example, a synthetic italic version of the regular face might be used if the
italic face doesn’t support glyphs for Arabic.

If there are no more font families to be evaluated and no matching
face has been found, then the user agent performs an 
installed font
fallback
 procedure to find the best match for the character to be
rendered.  The result of this procedure can vary across user agents.

If a particular character cannot be displayed using any
font, the user agent should indicate by some means that a
character is not being displayed, displaying either a
symbolic representation of the missing glyph (e.g. using a 
Last
Resort Font
) or using the missing character glyph from
a default font.

Optimizations of this process are allowed
	provided that an implementation behaves as if the algorithm had been followed exactly.
	Matching occurs in a well-defined order
	to ensure that the results are as consistent as possible across user agents,
	given an identical set of available fonts and rendering tech.

The 
first available font
,
	used for example in the definition of 
font-relative lengths
 such as 
ex

	or in the definition of the 
line-height
 property,
	is defined to be the first font
	for which the character U+0020 (space)
	is not excluded by a 
unicode-range
,
	given the font families in the 
font-family
 list
	(or a user agent’s default font if none are available).

Installed fonts referenced directly by family name,
	rather than via @font-face rules,
	are considered to have a 
unicode-range

	that covers the entire Unicode code space.

Tests

first-available-font-001.html

(live test)

(source)

first-available-font-002.html

(live test)

(source)

first-available-font-003.html

(live test)

(source)

first-available-font-004.html

(live test)

(source)

first-available-font-005.html

(live test)

(source)

first-available-font-006.html

(live test)

(source)

first-available-font-007.html

(live test)

(source)

italic-oblique-fallback.html

(live test)

(source)

Note:
 it does not matter whether that font actually has a glyph for the space character.

5.3. 

Cluster matching

When text contains characters such as combining marks,
	ideally
	the base character should be rendered
	using the same font as the mark,
	this assures proper placement of the mark.
	For this reason,
	the font matching algorithm for clusters
	is more specialized
	than the general case of matching a single character by itself.
	For sequences containing variation selectors,
	which indicate the precise glyph to be used for a given character,
	user agents always attempt 
installed font fallback

	to find the appropriate glyph
	before using the default glyph of the base character.

A sequence of codepoints containing combining mark
	or other modifiers
	is termed a grapheme cluster
	(see 
[CSS3TEXT]
 and 
[UAX29]
 for a more complete description).
	For a given cluster containing a base character,

b
 and a sequence of combining characters

c1, c2…
, the entire cluster is matched using these steps:

     For each family in the font list,
			a face is chosen using the style selection rules
			defined in the previous section.

If all characters in the sequence 
b + c1 + c2 …

				are completely supported by the font,
				select this font for the sequence.

If a sequence of multiple codepoints
					is canonically equivalent to a single character
					and the font 
supports
 that character,
					select this font for the sequence
					and use the glyph associated with
					the canonically equivalent character
					for the entire cluster.

     If no font was found in the font list in step 1:

If 
c1
 is a variation selector,
					system fallback must be used
					to find a font that 
supports

					the full sequence of 
b + c1
.
					If no font on the system 
supports
 the full sequence,
					match the single character 
b

					using the normal procedure for matching
					single characters
					and ignore the variation selector.
					Note: a sequence with more than one variation selector
					must be treated as an encoding error
					and the trailing selectors must be ignored. 
[UNICODE]

Otherwise, the user agent may optionally use
					installed font fallback
					to match a font that 
supports

					the entire cluster.

If no font is found in step 2,
			use the matching sequence
			from step 1 to determine the longest sequence
			that is completely 
supported

			by a font in the font list
			and attempt to match the remaining combining characters
			separately using the rules for single characters.

5.4. 

Character handling issues

CSS font matching is always performed on
	text runs containing Unicode characters 
[UNICODE]
,
	so documents using legacy encodings are assumed
	to have been transcoded before matching fonts.
	For fonts containing 
character maps

	for both legacy encodings and Unicode,
	the contents of the legacy encoding 
character map

	must have no effect on the results
	of the font matching process.

The font matching process does not assume
	that text runs are in either normalized or denormalized form
	(see 
[CHARMOD-NORM]
 for more details).
	Fonts may only support precomposed forms
	and not the decomposed sequence of base character plus combining marks.
	Authors should always tailor their choice of fonts to their content,
	including whether that content contains
	normalized or denormalized character streams.

If a given character is a Private-Use Area Unicode codepoint,
	user agents must only
	match font families named in the 
font-family
 list
	that are not generic families.
	If none of the families
	named in the 
font-family
 list
	contain a glyph for that codepoint,
	user agents must display some form of missing glyph symbol
	for that character
	rather than attempting 
installed font fallback

	for that codepoint.
	When matching the replacement character U+FFFD,
	user agents may skip the font matching process
	and immediately display
	some form of missing glyph symbol,
	they are not required to display
	the glyph from the font
	that would be selected
	by the font matching process.

In general,
	the fonts for a given family
	will all have the same
	or similar 
character maps
.
	The process outlined here
	is designed to handle even font families
	containing faces with widely variant 
character maps
.
	However,
	authors are cautioned that
	the use of such families
	can lead to unexpected results.

Tests

font-unicode-PUA.html

(live test)

(source)

font-unicode-PUA-primary-font.html

(live test)

(source)

6. 

Font Feature Properties

Modern font technologies support a variety of
	advanced typographic and language-specific font features.
	Using these features,
	a single font can provide glyphs
	for a wide range of
	ligatures,
	contextual and stylistic alternates,
	tabular and old-style figures,
	small capitals,
	automatic fractions,
	swashes,
	and alternates specific to a given language.
	To allow authors control over these font capabilities,
	the 
font-variant
 property has been expanded.
	It now functions as a shorthand
	for a set of properties
	that provide control over
	stylistic font features.

6.1. 

Glyph selection and positioning

This section is non-normative

Simple fonts used for displaying Latin text
	use a very basic processing model.
	Fonts contain a 
character map

	which maps each character
	to a glyph for that character.
	Glyphs for subsequent characters
	are simply placed one after the other along a run of text.
	Modern font formats
	such as OpenType
	and AAT (Apple Advanced Typography)
	use a richer processing model.
	The glyph for a given character can be
	chosen and positioned
	not just based on the codepoint of the character itself,
	but also on adjacent characters
	as well as the language,
	script,
	and features enabled for the text.
	Font features may be
	required for specific scripts,
	or recommended as enabled by default
	or they might be stylistic features
	meant to be used under author control.
	The point at which font selection and positioning happens
	in the overall order of text processing operations
	(such as text transformation, text orientation and text alignment)
	is described in 
CSS Text 3
 § A Text Processing Order of Operations
.

For a detailed description of glyph processing
	for OpenType fonts,
	see 
[WINDOWS-GLYPH-PROC]
.

Stylistic font features can be classified
	into two broad categories:
	ones that affect the harmonization of glyph shapes
	with the surrounding context,
	such as kerning and ligature features,
	and ones such as the small-caps,
	subscript/superscript and alternate features
	that affect shape selection.

The subproperties of 
font-variant
 listed below
	are used to control these stylistic font features.
	They do not control features
	that are required for displaying certain scripts,
	such as the OpenType features used when displaying Arabic or Indic language text.
	They affect glyph selection and positioning,
	but do not affect font selection
	as described in the font matching section
	(except in cases required for compatibility with CSS 2.1).

To assure consistent behavior across user agents,
	the equivalent OpenType property settings
	are listed for individual properties
	and are normative.
	When using other font formats
	these should be used as a guideline
	to map CSS font feature property values
	to specific font features.

6.2. 

Language-specific display

OpenType also supports language-specific glyph selection and
	positioning, so that text can be displayed correctly in cases where
	the language dictates a specific display behavior. Many languages
	share a common script, but the shape of certain letters can vary
	across those languages. For example, certain Cyrillic letters have
	different shapes in Russian text than in Bulgarian. In Latin text,
	it’s common to render "fi" with an explicit fi-ligature that lacks a
	dot on the "i". However, in languages such as Turkish which uses both
	a dotted-i and a dotless-i, it’s important to not use this ligature or
	use a specialized version that contains a dot over the "i".

Tests

language-specific-01.html (visual test) 
(source)

mvs-shaping.html

(live test)

(source)

The example below shows language-specific variations based on stylistic
	traditions found in Spanish, Italian and French orthography:

If the content language of the element is known according to the
	rules of the 
document language
,
	user agents are required to infer the OpenType language system from
	the 
content language
 and use that when selecting and positioning
	glyphs using an OpenType font.
	If a writing system has been explicitly specified,
	it must take precedence over the customary one implied by the 
content language
.

For OpenType fonts, in some cases it may be necessary to explicitly
	declare the OpenType language to be used, for example when displaying
	text in a given language that uses the typographic conventions of
	another language or when the font does not explicitly support a given
	language but supports a language that shares common typographic
	conventions. The 
font-language-override
 property is used for this
	purpose.

6.3. 

Kerning: the 
font-kerning
 property

Name:

font-kerning

Value:

auto 
|
 normal 
|
 none

Initial:

auto

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-kerning-01.html

(live test)

(source)

font-kerning-02.html

(live test)

(source)

font-kerning-03.html

(live test)

(source)

font-kerning-04.html

(live test)

(source)

font-kerning-05.html

(live test)

(source)

cjk-kerning.html

(live test)

(source)

hiragana-katakana-kerning.html

(live test)

(source)

font-kerning-computed.html

(live test)

(source)

font-kerning-invalid.html

(live test)

(source)

font-kerning-valid.html

(live test)

(source)

Kerning is the contextual adjustment
	of inter-glyph spacing of proportionally-spaced glyphs.
	It is not intended to apply to fixed-width glyphs,
	and to do so is an error.

This property controls metric kerning,
	kerning that utilizes adjustment data
	contained in the font.

auto

Specifies that kerning is applied, to proportionally-spaced glyphs, at the discretion of the user agent

normal

Specifies that kerning is applied, to proportionally-spaced glyphs

none

Specifies that kerning is not applied

Kerning proportionally-spaced Latin characters

For fonts that do not include kerning data,
	this property will have no visible effect.

Some CJK fonts have Proportional Alternate Widths;
	whereby glyphs designed to be set on full-em widths
	are re-spaced to be proportional.
	In OpenType, this is enabled with the

palt

	feature
.
	In that case,  if requested, kerning can be applied to these glyphs.
	(It is valid to apply 
palt
. if requested,
	and 
not
 apply kerning).
	For these glyphs, if kerned, the 

kern

	feature should not be used; instead, if available, the Kerning for Alternate Proportional Widths should be applied, using the

apkn

	feature.

When kerning is enabled,
	the relevant OpenType kerning features are enabled
	(for horizontal 
typographic modes

	and for 
sideways typesetting
 in vertical 
typographic modes
,
	the 
kern
 feature;
	for 
upright typesetting
 in 
vertical typographic modes
,
	the 
vkrn
 feature).
	User agents must also support fonts
	that only support kerning
	via data contained in a

kern
 font table,
	as detailed in the OpenType specification.
	If the 
letter-spacing
 property is defined,
	kerning adjustments are considered part of the default spacing
	and letter spacing adjustments are made

after
 kerning has been applied.

When set to 
auto
,
	user agents can determine
	whether to apply kerning or not
	based on a number of factors:
	text size,
	script, or
	other factors that influence text processing speed.
	Authors who want proper kerning
	should use 
normal

	to explicitly enable kerning
	of proportionally-spaced glyphs.
	Likewise,
	some authors may prefer to disable kerning
	in situations where performance
	is more important than precise appearance.
	However, in well-designed modern implementations
	the use of kerning generally
	does not have a large impact
	on text rendering speed.

6.4. 

Ligatures: the 
font-variant-ligatures
 property

Name:

font-variant-ligatures

Value:

normal

|

none

|
 [ 
<common-lig-values>

||

<discretionary-lig-values>

||

<historical-lig-values>

||

<contextual-alt-values>
 ]

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-variant-ligatures-01.html

(live test)

(source)

font-variant-ligatures-02.html

(live test)

(source)

font-variant-ligatures-03.html

(live test)

(source)

font-variant-ligatures-04.html

(live test)

(source)

font-variant-ligatures-05.html

(live test)

(source)

font-variant-ligatures-06.html

(live test)

(source)

font-variant-ligatures-07.html

(live test)

(source)

font-variant-ligatures-08.html

(live test)

(source)

font-variant-ligatures-09.html

(live test)

(source)

font-variant-ligatures-10.html

(live test)

(source)

font-variant-ligatures-11.optional.html

(live test)

(source)

font-variant-ligatures.html

(live test)

(source)

font-features-across-space-1.html

(live test)

(source)

font-features-across-space-2.html

(live test)

(source)

font-features-across-space-3.html

(live test)

(source)

font-variant-ligatures-computed.html

(live test)

(source)

font-variant-ligatures-invalid.html

(live test)

(source)

font-variant-ligatures-valid.html

(live test)

(source)

Ligatures and contextual forms
	are ways of combining glyphs
	to produce more harmonized forms.

<common-lig-values>
        = 
[
 common-ligatures 
|
 no-common-ligatures 
]

<discretionary-lig-values>
 = 
[
 discretionary-ligatures 
|
 no-discretionary-ligatures 
]

<historical-lig-values>
    = 
[
 historical-ligatures 
|
 no-historical-ligatures 
]

<contextual-alt-values>
    = 
[
 contextual 
|
 no-contextual 
]

Individual values have the following meanings:

normal

A value of 
normal

			specifies that common default features are enabled,

as described in detail
			in the next section
.
			For OpenType fonts,
			common ligatures and contextual forms are on by default,
			discretionary and historical ligatures are not.

none

Specifies that all types of ligatures and contextual forms
			covered by this property
			are explicitly disabled.
			In situations where ligatures are not considered necessary,
			this 
may

			improve the speed of text rendering.

common-ligatures

     Enables display of common ligatures
			(OpenType features: 
liga, clig
).
			For OpenType fonts,
			common ligatures are enabled by default.

no-common-ligatures

Disables display of common ligatures
			(OpenType features: 
liga, clig
).

discretionary-ligatures

     Enables display of discretionary ligatures
			(OpenType feature: 
dlig
).
			Which ligatures are discretionary or optional is decided by the type designer,
			so authors will need to refer to
			the documentation of a given font
			to understand which ligatures are considered discretionary.

no-discretionary-ligatures

Disables display of discretionary ligatures
			(OpenType feature: 
dlig
).

historical-ligatures

     Enables display of historical ligatures
			(OpenType feature: 
hlig
).

no-historical-ligatures

Disables display of historical ligatures
			(OpenType feature: 
hlig
).

contextual

     Enables display of contextual alternates
			(OpenType feature: 
calt
).
			Although not strictly a ligature feature,
			like ligatures this feature is commonly used
			to harmonize the shapes of glyphs with the surrounding context.
			For OpenType fonts,
			this feature is on by default.

no-contextual

Disables display of contextual alternates
			(OpenType feature: 
calt
).

Required
 ligatures,
	needed for correctly rendering complex scripts,
	are not affected by the settings above,
	including 
none

	(OpenType feature: 
rlig
).

6.5. 

Subscript and superscript forms: the 
font-variant-position
 property

Name:

font-variant-position

Value:

normal 
|
 sub 
|
 super

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-variant-position-01.html

(live test)

(source)

font-variant-position-02.html

(live test)

(source)

font-variant-position-03.html

(live test)

(source)

font-variant-position-04.html

(live test)

(source)

font-variant-position-05.html

(live test)

(source)

font-variant-position.html

(live test)

(source)

font-variant-position-computed.html

(live test)

(source)

font-variant-position-invalid.html

(live test)

(source)

font-variant-position-valid.html

(live test)

(source)

This property is used
	to enable typographic subscript and superscript glyphs.
	These are alternate glyphs
	designed within the same em-box as default glyphs
	and are intended to be laid out
	on the same baseline
	as the default glyphs,
	with no resizing or repositioning of the baseline.
	They are explicitly designed
	to match the surrounding text
	and to be more readable
	without affecting the line height.

Subscript glyphs (top) vs. typical synthesized subscripts (bottom)

Individual values have the following meanings:

normal

None of the features listed below are enabled.

sub

Enables display of subscript variants
		(OpenType feature: 
subs
).

super

Enables display of superscript variants
		(OpenType feature: 
sups
).

Because of the semantic nature of subscripts and superscripts,
	when the value is either 
sub
 or 
super

	for a given contiguous run of text,
	if a variant glyph is not available for all the characters in the run,
	simulated glyphs  should be synthesized
	for all characters
	using reduced forms of the glyphs
	that would be used
	without this feature applied.
	This is done per run
	to avoid a mixture of variant glyphs and synthesized ones
	that would not align correctly.
	In the case of OpenType fonts
	that lack subscript or superscript glyphs
	for a given character,
	user agents 
must
 synthesize
	appropriate subscript and superscript glyphs.

Superscript alternate glyph (left), synthesized superscript glyphs (middle), and incorrect mixture of the two (right)

In situations where text decorations
	are only applied to runs of text
	containing superscript or subscript glyphs,
	the synthesized glyphs may be used,
	to avoid problems with the placement of decorations.

In the past,
	user agents have used font-size
	and vertical-align
	to simulate subscripts and superscripts
	for the

sub

	and 
sup
 elements.
	To allow a backwards compatible way
	of defining subscripts and superscripts,
	it is recommended
	that authors use conditional rules 
[CSS3-CONDITIONAL]

	so that older user agents will still render
	subscripts and superscripts via
	the older mechanism.

Because 
font-size
:
 smaller

	is often used for these elements,
	the effective scaling factor
	applied to subscript and superscript text
	varies depending upon the size.
	For larger text,
	the font size is often reduced by a third
	but for smaller text sizes,
	the reduction can be much less.
	This allows subscripts and superscripts
	to remain readable
	even within elements using small text sizes.
	User agents should consider this
	when deciding how to synthesize
	subscript and superscript glyphs.

The OpenType font format
	defines subscript and superscript metrics
	in the

OS/2 table

[OPENTYPE]

	but these are not always accurate in practice
	and so cannot be relied upon
	when synthesizing subscript and superscript glyphs.

Authors should note
	that fonts typically only provide
	subscript and superscript glyphs
	for a subset of all characters
	supported by the font.
	For example,
	while subscript and superscript glyphs
	are often available for Latin numbers,
	glyphs for punctuation and letter characters
	are less frequently provided.
	The synthetic fallback rules
	defined for this property
	try to ensure that subscripts and superscripts
	will always appear
	but the appearance may not match author expectations
	if the font used does not provide
	the appropriate alternate glyph
	for all characters contained in a
	subscript or superscript.

This property is not cumulative.
	Applying it to elements
	within a subscript or superscript
	won’t nest the placement
	of a subscript or superscript glyph.
	Images contained within text runs
	where the value of this property
	is 
sub
 or 
super
 will be drawn
	just as they would
	if the value was 
normal
.

Because of these limitations,

font-variant-position

	is not recommended for use in user agent stylesheets.
	Authors should use it
	in cases where subscripts or superscripts
	will only contain the narrow range of characters
	supported by the fonts specified.

The variant glyphs
	use the same baseline
	as the default glyphs would use.
	There is no shift in the placement along the baseline,
	so the use of variant glyphs doesn’t affect
	the height of the inline box
	or alter the height of the linebox.
	This makes superscript and subscript variants
	ideal for situations where it’s important
	that leading remain constant,
	such as in multi-column layout.

A typical user agent default style for the 
sub
 element:

sub 
{

vertical-align
:
 sub
;

font-size
:
 smaller
;

line-height
:
 normal
;

}

Using 
font-variant-position

		to specify typographic subscripts
		in a way that will still show subscripts
		in older user agents:

@supports

(
 font-variant-position: sub 
)

{

      sub 
{

vertical-align
:
 baseline
;

font-size
:

100
%
;

line-height
:
 inherit
;

font-variant-position
:
 sub
;

}

}

User agents that support the 
font-variant-position
 property
		will select a subscript variant glyph
		and render this
		without adjusting the baseline or font-size.
		Older user agents will ignore
		the 
font-variant-position
 property definition
		and use the standard defaults for subscripts.

6.6. 

Capitalization: the 
font-variant-caps
 property

Name:

font-variant-caps

Value:

normal 
|
 small-caps 
|
 all-small-caps 
|
 petite-caps 
|
 all-petite-caps 
|
 unicase 
|
 titling-caps

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-variant-caps-01.html

(live test)

(source)

font-variant-caps-02.html

(live test)

(source)

font-variant-caps-03.html

(live test)

(source)

font-variant-caps-04.html

(live test)

(source)

font-variant-caps-05.html

(live test)

(source)

font-variant-caps-06.html

(live test)

(source)

font-variant-caps-07.html

(live test)

(source)

font-variant-caps.html

(live test)

(source)

font-variant-caps-invalidation-container-sizing.html

(live test)

(source)

small-caps-letter-spacing-001.html

(live test)

(source)

small-caps-letter-spacing-002.html

(live test)

(source)

font-variant-caps-computed.html

(live test)

(source)

font-variant-caps-invalid.html

(live test)

(source)

font-variant-caps-valid.html

(live test)

(source)

This property allows
	the selection of alternate glyphs
	used for small or petite capitals or for titling.
	These glyphs are specifically designed
	to blend well with the surrounding normal glyphs,
	to maintain the weight and readability
	which suffers when text is simply resized
	to fit this purpose.

Individual values have the following meanings:

normal

None of the features listed below are enabled.

small-caps

     Enables display of small capitals
			(OpenType feature: 
smcp
).
			Small-caps glyphs typically use the form of uppercase letters
			but are reduced to the size of lowercase letters.

all-small-caps

Enables display of small capitals for both upper and lowercase letters
			(OpenType features: 
c2sc, smcp
).

petite-caps

Enables display of petite capitals
			(OpenType feature: 
pcap
).

all-petite-caps

Enables display of petite capitals for both upper and lowercase letters
			(OpenType features: 
c2pc, pcap
).

unicase

Enables display of mixture of small capitals for uppercase letters
			with normal lowercase letters
			(OpenType feature: 
unic
).

titling-caps

Enables display of titling capitals
			(OpenType feature: 
titl
).
			Uppercase letter glyphs are often designed for use with lowercase letters.
			When used in all uppercase titling sequences
			they can appear too strong.
			Titling capitals are designed specifically for this situation.

The availability of these glyphs
	is based on whether a given feature is defined or not
	in the feature list of the font.
	User agents can optionally decide this
	on a per-script basis
	but should explicitly not decide this
	on a per-character basis.

Some fonts may only support a subset
	or none
	of the features
	described for this property.
	For backwards compatibility with CSS 2.1,
	if 
small-caps
 or 
all-small-caps
 is specified
	but small-caps glyphs are not available for a given font,
	user agents should simulate a small-caps font,
	for example by taking a normal font
	and replacing the glyphs for lowercase letters
	with scaled versions of the glyphs
	for uppercase characters
	(replacing the glyphs for both upper and lowercase letters
	in the case of 
all-small-caps
).

Synthetic vs. real small-caps

The 
font-feature-settings
 property
	also affects the decision of
	whether or not to use a simulated small-caps font
	(unlike CSS Fonts 3).

#example1 
{

font-variant-caps
:
 small-caps
;

}

      #example2 
{

font-variant-caps
:
 small-caps
;

font-feature-settings
:

'smcp'

0
;

}

For fonts which don’t support small caps, both #example1 and #example2
		should be rendered with synthesized small caps. However, for fonts which
		do support small caps, #example1 should be rendered with native small
		caps, while #example2 should be rendered without any small-caps (native
		or synthesized).

To match the surrounding text,
	a font may provide alternate glyphs
	for caseless characters
	when these features are enabled
	but when a user agent simulates small capitals,
	it must not attempt to simulate alternates
	for codepoints which are considered caseless.

Caseless characters with small-caps, all-small-caps enabled

If either 
petite-caps
 or 
all-petite-caps
' is specified
	for a font that doesn’t support these features,
	the property behaves as if

small-caps
 or 
all-small-caps
, respectively,
	had been specified.
	If 
unicase
 is specified
	for a font that doesn’t support that feature,
	the property behaves as if 
small-caps
 was applied
	only to lowercased uppercase letters.
	If 
titling-caps
 is specified
	with a font that does not support this feature,
	this property has no visible effect.
	When simulated small capital glyphs are used,
	for scripts that lack uppercase and lowercase letters,

small-caps
, 
all-small-caps
, 
petite-caps
,

all-petite-caps
 and 
unicase

	have no visible effect.

When casing transforms are used
	to simulate small capitals,
	the casing transformations must match
	those used for the 
text-transform
 property.

As a last resort,
	unscaled uppercase letter glyphs
	in a normal font
	may replace glyphs in a small-caps font
	so that the text appears
	in all uppercase letters.

Using small capitals to improve readability in acronym-laden text

Quotes rendered italicized, with small-caps on the first line:

blockquote            
{

font-style
:
 italic
;

}

    blockquote:first-line 
{

font-variant
:
 small-caps
;

}

    <blockquote>
I'll be honor-bound to slap them like a haddock.
</blockquote>

6.7. 

Numerical formatting: the 
font-variant-numeric
 property

Name:

font-variant-numeric

Value:

normal 
|
 [ 
<numeric-figure-values>

||

<numeric-spacing-values>

||

<numeric-fraction-values>

||
 ordinal 
||
 slashed-zero ]

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-variant-numeric-01.html

(live test)

(source)

font-variant-numeric-02.html

(live test)

(source)

font-variant-numeric-03.html

(live test)

(source)

font-variant-numeric-04.html

(live test)

(source)

font-variant-numeric-05.html

(live test)

(source)

font-variant-numeric-06.html

(live test)

(source)

font-variant-numeric-07.html

(live test)

(source)

font-variant-numeric-08.html

(live test)

(source)

font-variant-numeric-09.html

(live test)

(source)

font-variant-numeric.html

(live test)

(source)

font-variant-numeric-computed.html

(live test)

(source)

font-variant-numeric-invalid.html

(live test)

(source)

font-variant-numeric-valid.html

(live test)

(source)

Specifies control over numerical forms. The example below shows how
	some of these values can be combined to influence the rendering of
	tabular data with fonts that support these features. Within normal
	paragraph text, proportional numbers are used while tabular numbers
	are used so that columns of numbers line up properly:

Using number styles

Possible combinations:

<numeric-figure-values>
   = 
[
 lining-nums 
|
 oldstyle-nums 
]

<numeric-spacing-values>
  = 
[
 proportional-nums 
|
 tabular-nums 
]

<numeric-fraction-values>
 = 
[
 diagonal-fractions 
|
 stacked-fractions 
]

Individual values have the following meanings:

normal

None of the features listed below are enabled.

lining-nums

Enables display of lining numerals
			(OpenType feature: 
lnum
).

oldstyle-nums

Enables display of old-style numerals
			(OpenType feature: 
onum
).

proportional-nums

Enables display of proportional numerals
			(OpenType feature: 
pnum
).

tabular-nums

Enables display of tabular numerals
			(OpenType feature: 
tnum
).

diagonal-fractions

     Enables display of lining diagonal fractions
			(OpenType feature: 
frac
).

stacked-fractions

     Enables display of lining stacked fractions
			(OpenType feature: 
afrc
).

ordinal

     Enables display of letter forms used with ordinal numbers
			(OpenType feature: 
ordn
).

slashed-zero

     Enables display of slashed zeros
			(OpenType feature: 
zero
).

In the case of 
ordinal
, although ordinal forms
		are often the same as superscript forms, they are marked up
		differently.

For superscripts, the variant property is only applied
		to the sub-element containing the superscript:

sup 
{

font-variant-position
:
 super
;

}

x<sup>
2
</sup>

For ordinals, the variant property is applied
		to the entire ordinal number rather than
		just to the suffix (or to the containing paragraph):

.ordinal 
{

font-variant-numeric
:
 ordinal
;

}

<span class=
"ordinal"
>
17
th
</span>

In this case only the "th" will appear in ordinal form,
		the digits will remain unchanged.
		Depending upon the typographic traditions used in a given language,
		ordinal forms may differ from superscript forms.
		In Italian, for example,
		ordinal forms sometimes include an underline in the ordinal design.

A simple flank steak marinade recipe,
		rendered with automatic fractions and old-style numerals:

.amount 
{

font-variant-numeric
:
 oldstyle-nums diagonal-fractions
;

}

    <h4>Steak marinade:</h4>
    <ul>
      <li><span class=
"amount"
>
2
</span> tbsp olive oil</li>
      <li><span class=
"amount"
>
1
</span> tbsp lemon juice</li>
      <li><span class=
"amount"
>
1
</span> tbsp soy sauce</li>
      <li><span class=
"amount"
>
1

1
/
2
</span> tbsp dry minced onion</li>
      <li><span class=
"amount"
>
2

1
/
2
</span> tsp italian seasoning</li>
      <li>Salt &amp
;
 pepper</li>
    </ul>

    <p>Mix the meat with the marinade
    and let it sit covered in the refrigerator
    for a few hours or overnight.</p>

Note that the fraction feature
		is only applied to values
		not the entire paragraph.
		Fonts often implement this feature using contextual rules
		based on the use of the slash ('/') character.
		As such, it’s not suitable for use as a paragraph-level style.

6.8. 

Alternates and swashes: the 
font-variant-alternates
 property

Name:

font-variant-alternates

Value:

normal 
|
 [ stylistic(
<font-feature-value-name>
) 
||

historical-forms 
||

styleset(
<font-feature-value-name>
#
) 
||

character-variant(
<font-feature-value-name>
#
) 
||

swash(
<font-feature-value-name>
) 
||

ornaments(
<font-feature-value-name>
) 
||

annotation(
<font-feature-value-name>
) ]

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

alternates-order.html

(live test)

(source)

font-variant-alternates-01.html

(live test)

(source)

font-variant-alternates-02.html

(live test)

(source)

font-variant-alternates-03.html

(live test)

(source)

font-variant-alternates-04.html

(live test)

(source)

font-variant-alternates-05.html

(live test)

(source)

font-variant-alternates-06.html

(live test)

(source)

font-variant-alternates-07.html

(live test)

(source)

font-variant-alternates-08.html

(live test)

(source)

font-variant-alternates-09.html

(live test)

(source)

font-variant-alternates-10.html

(live test)

(source)

font-variant-alternates-11.html

(live test)

(source)

font-variant-alternates-12.html

(live test)

(source)

font-variant-alternates-13.html

(live test)

(source)

font-variant-alternates-14.html

(live test)

(source)

font-variant-alternates-15.html

(live test)

(source)

font-variant-alternates-16.html

(live test)

(source)

font-variant-alternates-17.html

(live test)

(source)

font-variant-alternates-18.html

(live test)

(source)

font-variant-alternates-19.html

(live test)

(source)

font-variant-alternates-layers.html

(live test)

(source)

font-variant-alternates-parsing.html

(live test)

(source)

font-variant-alternates-invalid.html

(live test)

(source)

font-variant-alternates-valid.html

(live test)

(source)

<font-feature-index>
 = 
<integer>

<font-feature-value-name>
 = 
<ident>

For any given character, fonts can provide a variety of alternate
	glyphs in addition to the default glyph for that character. This
	property provides control over the selection of these alternate
	glyphs.

For many of the property values listed below, several different
	alternate glyphs are available. How many alternates are available
	and what they represent is font-specific, so these are each marked

font specific
 in the value definitions below.  Because the nature
	of these alternates is font-specific, the

@font-feature-values
 rule is used to define values for a
	specific font family or set of families that associate a font-specific
	numeric 
<font-feature-index>
 with a custom

<font-feature-value-name>
, which is then used in this
	property to select specific alternates:

@font-feature-values
 Noble Script 
{

@swash

{

swishy
:

1
;

flowing
:

2
;

}

}

p 
{

font-family
:
 Noble Script
;

font-variant-alternates
:

swash
(
flowing
);

/* use swash alternate #2 */

}

When a particular 
<font-feature-value-name>
 has not
	been defined for a given family or for a particular feature type, the
	computed value must be the same as if it had been defined.  However,
	property values that contain these undefined 
<font-feature-value-name>

	identifiers must be ignored when choosing glyphs.

/* these two style rules are effectively the same */

p 
{

font-variant-alternates
:

swash
(
unknown-value
);

}

/* not a defined value, ignored */

p 
{

font-variant-alternates
:
 normal
;

}

This allows values to be defined and used for a given set of font
	families but ignored if fallback occurs, since the font family name
	would be different. If a given value is outside the range supported by
	a given font, the value is ignored.  These values never apply to
	generic font families.

Individual values have the following meanings:

normal

None of the features listed below are enabled.

historical-forms

     Enables display of historical forms (OpenType feature: 
hist
).

stylistic(
<font-feature-value-name>
)

     Enables display of stylistic alternates (
font specific
, OpenType feature: 
salt 
<font-feature-index>
).

styleset(
<font-feature-value-name>
#)

     Enables display with stylistic sets (
font specific
, OpenType feature: 
ss
<font-feature-index>

			OpenType currently defines 
ss01
 through 
ss20
).

character-variant(
<font-feature-value-name>
#)

Enables display of specific character variants (
font specific
, OpenType feature: 
cv
<font-feature-index>

			OpenType currently defines 
cv01
 through 
cv99
).

swash(
<font-feature-value-name>
)

     Enables display of swash glyphs (
font specific
, OpenType feature: 
swsh 
<font-feature-index>
, cswh 
<font-feature-index>
).

ornaments(
<font-feature-value-name>
)

     Enables replacement of default glyphs with ornaments, if provided in the font (
font specific
, OpenType feature: 
ornm 
<font-feature-index>
).
			Some fonts may offer ornament glyphs as alternates for a wide collection of characters; however, displaying arbitrary
			characters (e.g., alphanumerics) as ornaments is poor practice as it distorts the semantics of the data. Font designers
			are encouraged to encode all ornaments (except those explicitly encoded in the Unicode Dingbats blocks, etc.) as
			alternates for the bullet character (U+2022) to allow authors to select the desired glyph using 
ornaments()
.

annotation(
<font-feature-value-name>
)

     Enables display of alternate annotation forms (
font specific
, OpenType feature: 
nalt 
<font-feature-index>
).

6.9. 

Defining font specific alternates: the 
@font-feature-values
 rule

Several of the possible values of 
font-variant-alternates
 listed above
	are labeled as 
font specific
;
	a font can define not just a single glyph for the feature,
	but 
multiple
 possible glyph variants,
	and associate each one with a numeric index
	to let you choose which to turn on.

These numeric indexes are idiosyncratic to each face;
	a 
swsh 
1
 feature on one font face might turn on the swash version of capital Q,
	while on another font face it turns on the swash version of the &.
	Thus, specifying the index in 
font-feature-settings

	requires that the author know 
exactly
 which font will be used on an element;
	if they get it wrong (due to font fallback selecting a different font)
	they might end up turning on an entirely different,
	and undesirable,
	feature to what they wanted!
	It also means that the author can’t easily turn on similar features for elements with different fonts;
	they have to individually set different 
font-feature-settings
 values for each
	that uses the correct numeric indexes for the desired features.

To fix this issue,
	the 
@font-feature-values
 rule lets an author assign,
	for each font face,
	a human-friendly name to specific feature indexes.
	Using these friendly names,
	an author can easily turn on similar features regardless of the font in use
	(if they’ve defined that name for all the fonts),
	and be sure they’re not accidentally turning on unrelated features
	(as fonts without those names defined for them simply won’t do anything).

Using a commonly named value allows authors to use a single style rule
		to cover a set of fonts for which the underlying selector is different for
		each font. If either font in the example below is found, a circled number
		glyph will be used:

@font-feature-values
 Otaru Kisa 
{

@annotation

{

circled
:

1
;

black-boxed
:

3
;

}

}

@font-feature-values
 Taisho Gothic 
{

@annotation

{

boxed
:

1
;

circled
:

4
;

}

}

h3.title 
{

/* circled form defined for both fonts */

  font-family: Otaru Kisa
,
 Taisho Gothic
;

font-variant
:

annotation
(
circled
);

}

Trying to turn on the "circled" forms for either font explicitly,
		using 
@font-feature-values
,
		would require the author know 
for certain
 which font will be used;
		if they expected "Otaru Kisa" and wrote 
font-feature-settings: "nalt" 1;
,
		it would turn on "circled" characters in Otara Kisa,
		but would instead turn on 
boxed
 characters
		if the system fell back to Taisho Gothic,
		as that’s what Taisho Gothic associates with 
nalt 
1
!

6.9.1. 
Basic syntax

An 
@font-feature-values
 rule’s prelude
	contains a list of font family names,
	followed by a block containing multiple 
feature value blocks
,
	a special type of subsidiary at-rule.
	Each 
feature value block
 contains declarations
	mapping author-chosen human-friendly names
	(such as "flowing")
	to feature indexes for the associated feature.

Each 
font feature value
 has the same meaning
	as the corresponding value of the 
font-variant-alternates
 property.

@font-feature-values
 = 
@font-feature-values

<font-family-name>
#

{

<declaration-rule-list>

}

<font-feature-value-type>
 = 
<
@stylistic
>

|

<
@historical-forms
>

|

<
@styleset
>

|

<
@character-variant
>

|

<
@swash
>

|

<
@ornaments
>

|

<
@annotation
>

@stylistic
 = 
@stylistic

{

<declaration-list>

}

@historical-forms
 = 
@historical-forms

{

<declaration-list>

}

@styleset
 = 
@styleset

{

<declaration-list>

}

@character-variant
 = 
@character-variant

{

<declaration-list>

}

@swash
 = 
@swash

{

<declaration-list>

}

@ornaments
 = 
@ornaments

{

<declaration-list>

}

@annotation
 = 
@annotation

{

<declaration-list>

}

Tests

alternates-order.html

(live test)

(source)

test_font_feature_values_parsing.html

(live test)

(source)

The 
@font-feature-values
 prelude
	is a comma-delimited list of font family names that match the definition of 
<font-family-name>

	for the 
font-family
 property.
	This means that only named font families are allowed;
	rules that include generic or system fonts in the list of font families are syntax errors.
	However, if a user agent defines a generic font to be a specific named font (e.g. Helvetica),
	the settings associated with that family name will be used.
	If syntax errors occur within the 
<font-family-name>
 list,
	the entire rule 
@font-feature-values
 rule is invalid
	and must be ignored.

The 
@font-feature-values
 block accepts 
<declaration-rule-list>
 as its contents;
	these list items are either:

at-rules
 named by one of the 
<font-feature-value-type>
 at-keyword tokens

or

the 
font-display
 descriptor.

Specifying the same 
<font-feature-value-type>
 more than once is valid;
	their contents are cascaded together.
	Each 
feature value block
 accepts a list of 
declarations
,
	the 
font feature value declarations
,
	where the declaration’s name can be any 
css identifier
,
	and the value must be a list of one or more non-negative 
<integer>
s.

The 
feature value blocks
 accept any declaration name;
	these names must be 
<font-feature-value-name>
,
	per standard CSS syntax rules,
	and are 
case-sensitive

	(so 
foo: 1;
 and 
FOO: 2
 define two different features).

Each declaration’s value in 
@annotation
, 
@ornaments
, 
@stylistic
, 
@swash
,
	must match the grammar 
<font-feature-index>
,
	or else the declaration is invalid and must be ignored.

Each declaration’s value in 
@character-variant

	must match the grammar 
<font-feature-index [0,99]>

<font-feature-index [0,∞]>
,
	or else the declaration is invalid and must be ignored.

Each declaration’s value in 
@styleset

	must match the grammar 
<font-feature-index [0,20]>
+,
	or else the declaration is invalid and must be ignored.

Note:
 Each feature name is unique only within a single 
feature value block
.
	Between different 
feature value blocks
,
	or the same type of 
feature value blocks
 in separate 
@font-feature-values
 rules,
	names can be reused without colliding.

For each 
<font-family-name>
 in the 
@font-feature-values
 prelude,
	each 
font feature value declaration
 defines a mapping between a
	(family name, feature block name, declaration name) 
tuple

	and the list of one or more integers from the declaration’s value.
	If the same tuple appears more than once in a document
	(such as if a single block),
	the last-defined one is used.

		For example, the following all define the exact same set of font feature values:

/* Default */

@font-feature-values
 foo 
{

@swash

{

pretty
:

1
;

cool
:

2
;

}

}

/* Repeated declaration names */

@font-feature-values
 foo 
{

@swash

{

pretty
:

0
;

pretty
:

1
;

cool
:

2
;

}

}

/* Multiple blocks of the same type */

@font-feature-values
 foo 
{

@swash

{

pretty
:

1
;

}

@swash

{

cool
:

2
;

}

}

/* Multiple rules for the same family */

@font-feature-values
 foo 
{

@swash

{

pretty
:

1
;

}

}

@font-feature-values
 foo 
{

@swash

{

cool
:

2
;

}

}

A syntax error within a 
font feature value declaration

	makes the declaration invalid and ignored,
	but does not invalidate the 
font feature value block
 it occurs in.
	An unknown at-rule within a 
@font-feature-values
 block
	(not using one of the predefined list of allowed at-keywords)
	makes that at-rule invalid and ignored,
	but does not invalidate the 
@font-feature-values
 rule.

		Rules that are equivalent given syntax error handling:

@font-feature-values
 Bongo 
{

@swash

{

ornate
:

1
;

}

  annotation 
{

boxed
:

4
;

}

/* should be @annotation! */

@swash

{

double-loops
:

1
;

flowing
:

-1
;

}

/* negative value */

@ornaments

;

/* incomplete definition */

@styleset

{

double-W
:

14
;

sharp-terminals
:

16

1

}

/* missing ; */

  redrum  
/* random editing mistake */

}

The example above is equivalent to:

@font-feature-values
 Bongo 
{

@swash

{

ornate
:

1
;

}

@swash

{

double-loops
:

1
;

}

@styleset

{

double-W
:

14
;

sharp-terminals
:

16

1
;

}

}

If multiple 
@font-feature-values
 rules are defined for
	a given family, the resulting values definitions are the union of the
	definitions contained within these rules. This allows a set of named
	values to be defined for a given font family globally for a site and
	specific additions made per-page.

		Using both site-wide and per-page feature values:

site.css:

@font-feature-values
 Mercury Serif 
{

@styleset

{

stacked-g
:

3
;

/* "two-storey" versions of g, a */

    stacked-a: 
4
;

}

}

page.css:

@font-feature-values
 Mercury Serif 
{

@styleset

{

geometric-m
:

7
;

/* alternate version of m */

}

}

body 
{

font-family
:
 Mercury Serif
,
 serif
;

/* enable both the use of stacked g and alternate m */

  font-variant-alternates: 
styleset
(
stacked-g
,
 geometric-m
);

}

6.9.2. 

Multi-valued feature value definitions

Most 
font specific
 functional values of the 
font-variant-alternates
 property
	take a single value (e.g. 
swash()
) which enables the feature.

@font-feature-values
 Jupiter Serif 
{

@swash

{

swishy
:

5
;

/* implies ss05 = 1 */

      swirly: 
2
;

/* implies ss02 = 1 */

}

}

The 
character-variant()
 property value and the 
@character-variant
 descriptor allow two values,
	which enables a feature (from the first value) and sets it to a given (second) value.

@font-feature-values
 MM Greek 
{

@character-variant

{

alpha-2
:

1

2
;

}

/* implies cv01 = 2 */

@character-variant

{

beta-3
:

2

3
;

}

/* implies cv02 = 3 */

}

For the 
styleset()
 property value and 
@styleset
 rule,
	multiple values indicate the style
	sets to be enabled.  Values between 1 and 99 enable OpenType features

ss01
 through 
ss99
.
	However, the OpenType standard only officially defines

ss01
 through 
ss20
.
	For OpenType fonts, values greater than 99 or equal to 0 do not
	generate a syntax error when parsed but enable no OpenType features.

@font-feature-values
 Mars Serif 
{

@styleset

{

alt-g
:

1
;

/* implies ss01 = 1 */

      curly-quotes: 
3
;

/* implies ss03 = 1 */

      code: 
4

5
;

/* implies ss04 = 1, ss05 = 1 */

}

@styleset

{

dumb
:

125
;

/* >99, ignored */

}

@swash

{

swishy
:

3

5
;

/* more than 1 value for swash, syntax error */

}

}

  p.codeblock 
{

/* implies ss03 = 1, ss04 = 1, ss05 = 1 */

    font-variant-alternates: 
styleset
(
curly-quotes
,
 code
);

}

For 
<@character-variant>
, a single value between 1 and 99 indicates
	the enabling of OpenType feature 
cv01
 through

cv99
. For OpenType fonts, values greater than
	99 or equal to 0 are ignored but do not generate a syntax error when parsed
	but enable no OpenType features. When two values are listed, the first
	value indicates the feature used and the second the value passed for
	that feature.  If more than two values are assigned to a given name, a
	syntax error occurs and the entire
	feature value definition is
	ignored.

@font-feature-values
 MM Greek 
{

@character-variant

{

alpha-2
:

1

2
;

}

/* implies cv01 = 2 */

@character-variant

{

beta-3
:

2

3
;

}

/* implies cv02 = 3 */

@character-variant

{

epsilon
:

5

3

6
;

}

/* more than 2 values, syntax error, definition ignored */

@character-variant

{

gamma
:

12
;

}

/* implies cv12 = 1 */

@character-variant

{

zeta
:

20

3
;

}

/* implies cv20 = 3 */

@character-variant

{

zeta-2
:

20

2
;

}

/* implies cv20 = 2 */

@character-variant

{

silly
:

105
;

}

/* >99, ignored */

@character-variant

{

dumb
:

323

3
;

}

/* >99, ignored */

}

  #title 
{

/* use the third alternate beta, first alternate gamma */

    font-variant-alternates: 
character-variant
(
beta-3
,
 gamma
);

}

  p 
{

/* zeta-2 follows zeta, implies cv20 = 2  */

    font-variant-alternates: 
character-variant
(
zeta
,
 zeta-2
);

}

  .special 
{

/* zeta follows zeta-2, implies cv20 = 3  */

    font-variant-alternates: 
character-variant
(
zeta-2
,
 zeta
);

}

Byzantine seal text displayed with character variants

In the figure above, the text in red is rendered using a font containing
		character variants that mimic the character forms found on a Byzantine seal
		from the 8th century A.D.  Two lines below is the same text displayed in
		a font without variants.  Note the two variants for U and N used on the
		seal.

@font-feature-values
 Athena Ruby 
{

@character-variant

{

leo-B
:

2

1
;

leo-M
:

13

3
;

leo-alt-N
:

14

1
;

leo-N
:

14

2
;

leo-T
:

20

1
;

leo-U
:

21

2
;

leo-alt-U
:

21

4
;

}

}

    p 
{

font-variant
:
 discretionary-ligatures

character-variant
(
leo-B
,
 leo-M
,
 leo-N
,
 leo-T
,
 leo-U
);

}

    span.alt-N 
{

font-variant-alternates
:

character-variant
(
leo-alt-N
);

}

    span.alt-U 
{

font-variant-alternates
:

character-variant
(
leo-alt-U
);

}

    <p>ENO....UP͞RSTU<span class=
"alt-U"
>U</span>͞<span class=
"alt-U"
>U</span>ΚΑΙTỤẠG̣IUPNS</p>

    <p>LEON|ΚΑΙCONSTA|NTI<span class=
"alt-N"
>N</span>OS..|STOIBAṢ.|LIṢROM|AIO<span class=
"alt-N"
>N</span></p>

6.10. 

East Asian text rendering: the 
font-variant-east-asian
 property

Name:

font-variant-east-asian

Value:

normal 
|
 [ 
<east-asian-variant-values>

||

<east-asian-width-values>

||
 ruby ]

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-variant-east-asian-01.html

(live test)

(source)

font-variant-east-asian-02.html

(live test)

(source)

font-variant-east-asian-03.html

(live test)

(source)

font-variant-east-asian-04.html

(live test)

(source)

font-variant-east-asian-05.html

(live test)

(source)

font-variant-east-asian-06.html

(live test)

(source)

font-variant-east-asian-07.html

(live test)

(source)

font-variant-east-asian-08.html

(live test)

(source)

font-variant-east-asian-09.html

(live test)

(source)

font-variant-east-asian-10.html

(live test)

(source)

font-variant-east-asian.html

(live test)

(source)

font-variant-east-asian-computed.html

(live test)

(source)

font-variant-east-asian-invalid.html

(live test)

(source)

font-variant-east-asian-valid.html

(live test)

(source)

Allows control of glyph substitution and sizing in East Asian text.

<east-asian-variant-values>
 = 
[
 jis78 
|
 jis83 
|
 jis90 
|
 jis04 
|
 simplified 
|
 traditional 
]

<east-asian-width-values>
   = 
[
 full-width 
|
 proportional-width 
]

Individual values have the following meanings:

normal

None of the features listed below are enabled.

jis78

     Enables rendering of JIS78 forms
			(OpenType feature: 
jp78
).

jis83

Enables rendering of JIS83 forms
			(OpenType feature: 
jp83
).

jis90

Enables rendering of JIS90 forms
			(OpenType feature: 
jp90
).

jis04

     Enables rendering of JIS2004 forms
			(OpenType feature: 
jp04
).

The various JIS variants reflect
			the glyph forms defined in different Japanese national standards.
			Fonts generally include glyphs
			defined by the most recent national standard,
			but it’s sometimes necessary
			to use older variants,
			to match signage for example.

simplified

Enables rendering of simplified forms
			(OpenType feature: 
smpl
).

traditional

     Enables rendering of traditional forms
			(OpenType feature: 
trad
).

The 
simplified
 and 
traditional
 values
			allow control over the glyph forms
			for characters which have been simplified over time
			but for which the older, traditional form
			is still used in some contexts.
			The exact set of characters and glyph forms
			will vary to some degree
			by the context for which a given font was designed.

full-width

Enables rendering of full-width variants
			(OpenType feature: 
fwid
).

proportional-width

     Enables rendering of proportionally-spaced variants
			(OpenType feature: 
pwid
).

ruby

     Enables display of ruby variant glyphs
			(OpenType feature: 
ruby
).
			Since ruby text is generally smaller
			than the associated body text,
			font designers can design special glyphs for use with ruby
			that are more readable than scaled down versions
			of the default glyphs.
			Only glyph selection is affected,
			there is no associated font scaling
			or other change that affects line layout.

The red ruby text below
			is shown with default glyphs (top)
			and with ruby variant glyphs (bottom).
			Note the slight difference
			in stroke thickness.

6.11. 

Overall shorthand for font rendering: the 
font-variant
 property

Name:

font-variant

Value:

normal 
|
 none 
|
 [ [ 
<common-lig-values>

||

<discretionary-lig-values>

||

<historical-lig-values>

||

<contextual-alt-values>
 ] 
||
 [ small-caps 
|
 all-small-caps 
|
 petite-caps 
|
 all-petite-caps 
|
 unicase 
|
 titling-caps ] 
||
 [ stylistic(
<font-feature-value-name>
) 
||
 historical-forms 
||
 styleset(
<font-feature-value-name>
#
) 
||
 character-variant(
<font-feature-value-name>
#
) 
||
 swash(
<font-feature-value-name>
) 
||
 ornaments(
<font-feature-value-name>
) 
||
 annotation(
<font-feature-value-name>
) ] 
||
 [ 
<numeric-figure-values>

||

<numeric-spacing-values>

||

<numeric-fraction-values>

||
 ordinal 
||
 slashed-zero ] 
||
 [ 
<east-asian-variant-values>

||

<east-asian-width-values>

||
 ruby ] 
||
 [ sub 
|
 super ] 
||
 [ text 
|
 emoji 
|
 unicode ] ]

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-variant-01.html

(live test)

(source)

font-variant-02.html

(live test)

(source)

font-variant-03.html

(live test)

(source)

font-variant-04.html

(live test)

(source)

font-shorthand-variant.html

(live test)

(source)

font-variant-invalid.html

(live test)

(source)

font-variant-valid.html

(live test)

(source)

The 
font-variant
 property
	is a shorthand for all font-variant subproperties:

font-variant-ligatures

font-variant-position

font-variant-caps

font-variant-numeric

font-variant-alternates

font-variant-east-asian

font-variant-emoji

The value 
normal

	resets all subproperties of 
font-variant

	to their initial value.
	The 
none
 value
	sets 
font-variant-ligatures
 to 'font-variant-ligatures/none'
	and resets all other font feature properties to their initial value.
	Like other shorthands,
	using 
font-variant

	resets unspecified 
font-variant
 subproperties
	to their initial values.

It does not reset the values of

font-language-override
,

font-feature-settings

	or 
font-variation-settings
.

6.12. 

Low-level font feature settings control: the 
font-feature-settings
 property

Name:

font-feature-settings

Value:

normal 
|

<feature-tag-value>
#

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

as specified

Canonical order:

per grammar

Animation type:

discrete

Tests

font-features-across-space-1.html

(live test)

(source)

font-features-across-space-2.html

(live test)

(source)

font-features-across-space-3.html

(live test)

(source)

font-feature-settings-tibetan.html

(live test)

(source)

font-feature-settings-computed.html

(live test)

(source)

font-feature-settings-invalid.html

(live test)

(source)

font-feature-settings-valid.html

(live test)

(source)

This property provides
	low-level control over OpenType font features.
	It is intended as a way of providing access
	to font features
	that are not widely used
	but are needed for a particular use case.

		Authors should 
not
 use

font-feature-settings
 to set any of the font features in
		the table below. Instead, please use the higher-level replacement properties, because:

The higher-level properties cascade individually. You can set one without setting the whole 
font-feature-settings
 list

Some higher-level properties can be synthesized for fonts that do not support the font feature.

If you want to set this font feature

then use this 
instead of

font-feature-settings

Notes

Kerning (
kern
) or Vertical Kerning (
vkrn
)

font-kerning
: 
normal

The 
font-kerning
 property will set the 
kern
 or 
vkrn
 feature depending on the 
writing-mode
.

Standard Ligatures (
liga
) or Contextual Ligatures (
clig
)

font-variant-ligatures
: 
common-ligatures

Discretionary Ligatures (
dlig
)

font-variant-ligatures
: 
discretionary-ligatures

Historical Ligatures (
hlig
)

font-variant-ligatures
: 
historical-ligatures

Contextual Alternates (
calt
)

font-variant-ligatures
: 
contextual

Subscript (
subs
)

font-variant-position
: 
sub

Superscript (
sups
)

font-variant-position
: 
super

Small Capitals (
smcp
)

font-variant-caps
: 
small-caps

Small Capitals From Capitals (
c2sc
)

font-variant-caps
: 
all-small-caps

Petite Capitals (
pcap
)

font-variant-caps
: 
petite-caps

Petite Capitals From Capitals (
c2pc
)

font-variant-caps
: 
all-petite-caps

Unicase (
unic
)

font-variant-caps
: 
unicase

Titling (
titl
)

font-variant-caps
: 
titling-caps

Lining Figures (
lnum
)

font-variant-numeric
: 
lining-nums

Oldstyle Figures (
onum
)

font-variant-numeric
: 
oldstyle-nums

Proportional Figures (
pnum
)

font-variant-numeric
: 
proportional-nums

Tabular Figures (
tnum
)

font-variant-numeric
: 
tabular-nums

Fractions (
frac
)

font-variant-numeric
: 
diagonal-fractions

Alternative Fractions (
afrc
)

font-variant-numeric
: 
stacked-fractions

Ordinals (
ordn
)

font-variant-numeric
: 
ordinal

Slashed Zero (
zero
)

font-variant-numeric
: 
slashed-zero

Historical Forms (
hist
)

font-variant-alternates
: 
historical-forms

Stylistic Alternates (
salt
)

font-variant-alternates
: 
stylistic()

Define which alternate gets used by making an 
@font-feature-values
 rule

Character Variant 1 - Character Variant 99 (
cv01
 - 
cv99
)

font-variant-alternates
: 
character-variant()

Define which character variant gets used by making an 
@font-feature-values
 rule

Swash (
swsh
) or Contextual Swash (
cswh
)

font-variant-alternates
: 
swash()

Define which swash gets used by making an 
@font-feature-values
 rule

Ornaments (
ornm
)

font-variant-alternates
: 
ornaments()

Define which ornament gets used by making an 
@font-feature-values
 rule

Alternate Annotation Forms (
nalt
)

font-variant-alternates
: 
annotation()

Define which annotation gets used by making an 
@font-feature-values
 rule

JIS78 Forms (
jp78
)

font-variant-east-asian
: 
jis78

JIS83 Forms (
jp83
)

font-variant-east-asian
: 
jis83

JIS90 Forms (
jp90
)

font-variant-east-asian
: 
jis90

JIS2004 Forms (
jp04
)

font-variant-east-asian
: 
jis04

Simplified Forms (
smpl
)

font-variant-east-asian
: 
simplified

Traditional Forms (
trad
)

font-variant-east-asian
: 
traditional

Full Widths (
fwid
)

font-variant-east-asian
: 
full-width

Proportional Widths (
pwid
)

font-variant-east-asian
: 
proportional-width

Ruby Notation Forms (
ruby
)

font-variant-east-asian
: 
ruby

For example, there is no font-variant value to control
		Scientific Inferiors (small numerals used in chemical formulae).
		Readability is enhanced by using them, so they must be enabled
		using font-feature-settings:

.chem 
{

font-feature-settings
:

'sinf'

}

Scientific inferiors improve readability of chemical formulae

The entire property value is set at once.
		Unlike the font-variant properties,
		there is no way to modify
		the inherited value
		by adding or removing individual features.

A value of

normal

	means that no change
	in glyph selection or positioning
	occurs due to this property.

Feature tag values have the following syntax:

<feature-tag-value>
 = <opentype-tag> 
[
 <integer 
[
0
,
∞
]
> 
|
 on 
|
 off 
]
?

<opentype-tag>
 = <string>

The 
<opentype-tag>
 is a case-sensitive OpenType feature tag.
	As specified in the OpenType specification 
[OPENTYPE]
,
	feature tags contain four ASCII characters.
	Tag strings longer or shorter than four characters,
	or containing characters outside the U+20–7E codepoint range
	are invalid.
	Feature tags need only match
	a feature tag defined in the font,
	so they are not limited to
	explicitly registered OpenType features.
	Fonts defining custom feature tags
	should follow the

tag name rules

	defined in the OpenType specification 
[OPENTYPE-FEATURES]
.

Feature tags
	not present in the font are ignored;
	a user agent must not attempt to synthesize fallback behavior
	based on these feature tags.
	The one exception is that
	user agents may synthetically support the 
kern
 feature
	with fonts that contain kerning data in the form of a 
kern
 table
	but lack 
kern
 feature support
	in the 
GPOS
 table.

In general, authors should
	use the 
font-kerning
 property
	to explicitly enable or disable kerning
	since this property always affects fonts
	with either type of kerning data.

If present,
	a value indicates an index used for glyph selection.
	An 
<integer>
 value must be 0 or greater.
	A value of 0 indicates that the feature is disabled.
	For boolean features,
	a value of 1 enables the feature.
	For non-boolean features,
	a value of 1 or greater enables the feature
	and indicates the feature selection index. A
	value of 
on
 is synonymous with 1
	and 
off
 is synonymous with 0.
	If the value is omitted, a value of 1 is assumed.

The computed value
	of font-feature-settings is a map,
	so any duplicates in the specified value
	must not be preserved.
	If the same feature tag appears more than once,
	the value associated with the last appearance supersedes
	any previous value for that axis.

The computed value contains the de-duplicated feature tags,
		sorted in ascending order by 
code unit
.

font-feature-settings
:

"sinf"

1
;

/* sinf=1 enable Scientific Inferiors */

font-feature-settings: 
"sinf"
 on
;

/* sinf=1 enable Scientific Inferiors */

font-feature-settings: 
'sinf'
;

/* sinf=1 enable Scientific Inferiors */

font-feature-settings: 
"sinf"
 off
;

/* sinf=0 disable Scientific Inferiors */

font-feature-settings: 
"sinf"
,

'twid'
;

/* sinf=1, twid=1 enable Scientific Inferiors and Third Widths */

font-feature-settings: 
"sinf"

"twid"
;

/* invalid, need a comma-delimited list */

font-feature-settings: 
"silly"
 off
;

/* invalid, tag too long */

font-feature-settings: 
"PKRN"
;

/* PKRN=1 enable custom feature */

font-feature-settings: sinf
;

/* invalid, tag must be a string */

When values greater than the range
	supported by the font
	are specified,
	the behavior is explicitly undefined.
	For boolean features, in general these will enable the feature.
	For non-boolean features,
	out of range values will in general
	be equivalent to a 0 value.
	However,
	in both cases the exact behavior
	will depend upon the way the font is designed
	(specifically, which type of lookup is used
	to define the feature).

Implementations may choose to ignore
	turning off features which
	the OpenType specification says are always required,
	such as required ligatures "rlig".

Tests

font-variant-ligatures-11.optional.html

(live test)

(source)

Although specifically defined for OpenType feature tags,
	feature tags for other modern font formats
	that support font features
	may be added in the future.
	Where possible,
	features defined for other font formats
	should attempt to follow
	the pattern of registered OpenType tags.

The Japanese text below will be rendered with half-width kana characters:

body 
{

font-feature-settings
:

"hwid"
;

/* Half-width OpenType feature */

}

<p>毎日
カレー
食べてるのに、飽きない</p>

6.13. 
Font language override: the 
font-language-override
 property

Name:

font-language-override

Value:

normal 
|

<string>

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/A

Computed value:

specified string or the keyword 
none

Canonical order:

per grammar

Animation type:

discrete

Tests

font-language-override-01.html

(live test)

(source)

font-language-override-02.html

(live test)

(source)

font-language-override-03.html

(live test)

(source)

font-language-override-computed.html

(live test)

(source)

font-language-override-invalid.html

(live test)

(source)

font-language-override-valid.html

(live test)

(source)

Normally, authors can control the use of language-specific glyph substitutions and positioning
	by setting the content language of an element, as 
described above
:

<!-- Display text using S'gaw Karen specific features -->

    <p lang=
"ksw"
>...</p>

In some cases, authors may need to specify a language system
	that differs from the content language, for example due to the need to mimic another language’s
	typographic traditions. The 
font-language-override
 property allows authors to explicitly specify
	the language system of the font, overriding the language system implied by the content language.

Values have the following meanings:

normal

specifies that when rendering with OpenType fonts,
			the content language of the element is used to infer the OpenType language system

<string>

single four-character case-sensitive OpenType 
language system tag
,
			specifies the OpenType language system to be used instead of the language system implied by the language of the element.
			If the string is shorter than four characters,
			it is padded at the end with space (U+0020) characters
			such that the length is 4, before being matched.

Unknown OpenType language system tags are silently ignored, and do not affect
	glyph selection and placement.

		The 
Universal Declaration of
		Human Rights
 has been translated into a wide variety of languages.  In Turkish,
		Article 9 of this document might be marked up as below:

<body lang=
"tr"
>
    <h4>Madde 
9
</h4>
    <p>Hiç kimse keyfi olarak tutuklanamaz
,
 alıkonulanamaz veya sürülemez.</p>

Here the user agent uses the value of the 
lang
 attribute when rendering text and
		appropriately renders this text without 'fi' ligatures. There is no need
		to use the 
font-language-override
 property.

However, a given font may lack support for a specific language. In this
		situation authors may need to use the typographic conventions of a related language
		that are supported by that font:

<body lang=
"mk"
>     <!-- Macedonian lang code -->
    body 
{

font-language-override
:

"SRB"
;

/* Serbian OpenType language tag */

}

    <h4>Члeн 
9
</h4>
    <p>Никoj чoвeк нeмa дa бидe пoдлoжeн нa прoизвoлнo aпсeњe
,
 притвoр или прoгoнувaњe.</p>

As the content creator knows that font specified supports Serbian, the Macedonian text
		here will be rendered using Serbian typographic conventions.

7. 

Font Feature and Variation Resolution

As described in the previous section,
	font features and variations can be enabled in a variety of ways,
	either via the use of 
font-variant
,

font-feature-settings
, or

font-variation-settings
 in a style rule
	or within an 
@font-face
 rule.
	The resolution order for the union of these settings is defined below.
	Features defined via CSS properties are applied on top of layout engine default features.

7.1. 

Default features

For OpenType fonts,
	user agents must enable the default features
	defined in the OpenType documentation
	for a given script and writing mode.
	Required ligatures, common ligatures and contextual forms
	must be enabled by default
	(OpenType features: 
rlig, liga, clig, calt
),
	along with localized forms
	(OpenType feature: 
locl
),
	and features required for proper display of composed characters and marks
	(OpenType features: 
ccmp, mark, mkmk
).
	These features must always be enabled,
	even when the value of the 
font-variant
 and 
font-feature-settings
 properties is 
normal
.
	Individual features are only disabled when explicitly overridden by the author,
	as when 
font-variant-ligatures
 is set to 'font-variant-ligatures/no-common-ligatures'.

Tests

font-default-01.html

(live test)

(source)

font-default-02.html

(live test)

(source)

font-default-03.html

(live test)

(source)

font-default-04.html

(live test)

(source)

For handling complex scripts such as

Arabic
,

Mongolian
 or

Devanagari

	additional features are required.
	For upright text within vertical text runs,
	vertical alternates (OpenType feature: 
vert
) must be enabled.

7.2. 

Feature and variation precedence

General and 
font specific
 font feature property settings are
	resolved in the order below, in ascending order of precedence.  This ordering is
	used to construct a combined list of font features that affect a given
	text run.

Font features enabled by default are applied, including features required for a given script.
	See 
§ 7.1 Default features
 for a description of these.

Font variations as enabled by the 
font-weight
,

font-width
, and 
font-style
 properties are applied.

The application of the value enabled by

font-style
 is affected by font selection, because this property might select an
italic or an oblique font. The value applied is the closest matching value as determined
by the 
font matching algorithm
. User agents must apply
at most one value due to the 
font-style
 property; both "ital" and "slnt" values must
not be set together.

If the selected font is defined in an 
@font-face
 rule, then the values applied at this step
should be clamped to the value of the 
font-weight
, 
font-width
,
and 
font-style

descriptors in that 
@font-face
 rule.

Then, the values applied in this step should be clamped (possibly again) to the values
that are supported by the font.

The language specified by the inherited value of lang/xml:lang is applied.

If the font is defined via an 
@font-face
 rule, the font language override
implied by the 
font-language-override
 descriptor in the 
@font-face
 rule is applied.

If the font is defined via an 
@font-face
 rule, that 
@font-face
 rule includes
at least one valid 
font-named-instance
 descriptor
with a value other than 'font-named-instance/none',
and the loaded font resource includes a named instance with that name
according to the 
§ 5.1 Localized name matching
 rules,
then all the variation values represented by that named instance are applied.
These values are clamped to the values that are supported by the font.

If the font is defined via an 
@font-face
 rule, the font variations
implied by the 
font-variation-settings
 descriptor in the 
@font-face
 rule are applied.

If the font is defined via an 
@font-face
 rule, the font features
implied by the 
font-feature-settings
 descriptor in the 
@font-face
 rule are applied.

The font language override implied by the value of the 
font-language-override
 property is applied.

Font variations implied by the value of the 
font-optical-sizing
 property are applied.

Font features implied by the value of the 
font-variant
 property,
the related 
font-variant
 subproperties and any other CSS property
that uses OpenType features (e.g. the 
font-kerning
 property) are applied.

Feature settings determined by properties other than 
font-variant
 or

font-feature-settings
 are applied. For example, setting a
non-default value for the 
letter-spacing
 property disables optional ligatures.

Font variations implied by the value of the 
font-variation-settings
 property are applied.
These values should be clamped to the values that are supported by the font.

Font features implied by the value of 
font-feature-settings
 property are applied.

Tests

font-feature-resolution-001.html

(live test)

(source)

font-feature-resolution-002.html

(live test)

(source)

lang-attribute-affects-rendering.html

(live test)

(source)

lang-attribute-affects-rendering-of-second-text-run.html

(live test)

(source)

This ordering allows authors to set up a general set of defaults
	for fonts within their 
@font-face
 rules, then override them with
	property settings for specific elements. General property settings
	override the settings in 
@font-face
 rules and low-level font feature
	settings override 
font-variant
 property settings.

For situations where the combined list of font feature settings
	contains more than one value for the same feature, the last value is
	used. When a font lacks support for a given underlying font feature,
	text is simply rendered as if that font feature was not enabled; font
	fallback does not occur and no attempt is made to synthesize the
	feature except where explicitly defined for specific properties.

7.3. 

Feature precedence examples

		With the styles below, numbers are rendered proportionally when used within
		a paragraph but are shown in tabular form within tables of prices:

body 
{

font-variant-numeric
:
 proportional-nums
;

}

table.prices td 
{

font-variant-numeric
:
 tabular-nums
;

}

		The 
@font-face
 rule can also be used to access font features in locally available
		fonts via the use of 
local
()
 in the 
src
 descriptor of the 
@font-face
 definition:

@font-face

{

font-family
:
 BodyText
;

src
:

local
(
"HiraMaruPro-W4"
);

font-variant
:
 proportional-width
;

font-feature-settings
:

"ital"
;

/* Latin italics within CJK text feature */

}

body 
{

font-family
:
 BodyText
,
 serif
;

}

If available, a Japanese font "Hiragino Maru Gothic" will be used.  When text
		rendering occurs, Japanese kana will be proportionally spaced and Latin text will
		be italicized.  Text rendered with the fallback serif font will use default
		rendering properties.

		In the example below, discretionary ligatures are enabled only for a downloadable font
		but are disabled within spans of class "special":

@font-face

{

font-family
:
 main
;

src
:

url
(
fonts/ffmeta.woff
)

format
(
"woff"
);

font-variant
:
 discretionary-ligatures
;

}

body         
{

font-family
:
 main
,
 Helvetica
;

}

span.special 
{

font-variant-ligatures
:
 no-discretionary-ligatures
;

}

Suppose one adds a rule using 
font-feature-settings
 to enable discretionary ligatures:

body         
{

font-family
:
 main
,
 Helvetica
;

}

span         
{

font-feature-settings
:

"dlig"
;

}

span.special 
{

font-variant-ligatures
:
 no-discretionary-ligatures
;

}

In this case, discretionary ligatures 
will
 be rendered
		within spans of class "special".
		This is because both the 
font-feature-settings
 and 
font-variant-ligatures
 properties
		apply to these spans.
		Although the 
no-discretionary-ligatures
 setting of 
font-variant-ligatures

		effectively disables the OpenType "dlig" feature,
		because the 
font-feature-settings
 is resolved after that,
		the "dlig" value reenables discretionary ligatures.

8. 

Font Variation Properties

Note:
 The technology in use in this section is named "font variations."
	An instance of one such font as a "variable font."

8.1. 

Optical sizing control: the 
font-optical-sizing
 property

Name:

font-optical-sizing

Value:

auto 
|
 none

Initial:

auto

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

specified keyword

Canonical order:

per grammar

Animation type:

discrete

Tests

font-optical-sizing-computed.html

(live test)

(source)

font-optical-sizing-invalid.html

(live test)

(source)

font-optical-sizing-valid.html

(live test)

(source)

Typographically,
	text rendered at different sizes
	often benefits from slightly different visual representations.
	For example, to aid reading at small text sizes,
	strokes are often thicker with larger serifs.
	Larger text often has a more delicate figure
	with more contrast between thicker and thinner strokes.

auto

			The user agent may modify the shape of glyphs
			based on the font-size and the pixel density of the screen.
			For OpenType and TrueType fonts using font variations,
			this is often done by using the "opsz" font variation.

none

			The user agent must not modify the shape of glyphs for optical size.

			Each size of Century Expanded as it existed in analog metal form.
			The different optical sizes,
			normalized here to the same physical size,
			have design variations to maintain stylistic traits and improve readability.

font-size
 must be considered when selecting a variation value for the "opsz" axis,
	but other signals may also be considered.

Note:
 User agents are expected to supply a value for the "opsz" axis
	which is close to the used value for 
font-size
.
	However, user agents might wish to consider other factors
	such as pixel density of the screen,
	or the solid angle the text subtends in the viewer’s retina.

Experiments have shown
,
	however, that disregarding these other ancillary factors
	and using only 
font-size
 might be the best way for a user agent to select this value.

Pixel density as well as visual size of the text
	may influence the variation value chosen for 
font-optical-sizing
.
	When either pixel density or visual size of the text
	changes in response to a user operation or style change,
	user agents must not choose a new value for this variation value
	unless the change is layout-causing.
	User agents are free to determine which changes are layout-causing.

Note:
 Some user operations,
	such as pinch-zoom,
	can be considered not-layout-causing
	if they do not cause text to reflow.
	However, other user operations,
	such as increasing text size for accessibility purposes,
	can be considered layout-causing because they cause text to reflow.
	Similarly, the 
transform
 property can be considered not-layout-causing
	because transforms generally do not cause text to reflow.
	Each user-agent is free to decide
	whether or not each operation is layout-changing or not.

User agents must not synthesize optical sizing
	when it is not performed by the font directly.

User agents must not select a value for the "opsz" axis
	which is not supported by the font used for rendering the text.
	This can be accomplished by clamping a chosen value to the range supported by the font.

font-optical-sizing
 interacts with 
font-size-adjust
. When applying optical sizing, User agents must
	apply an optical sizing value appropriate for the adjusted font size, subject to the above restrictions.

8.2. 

Low-level font variation settings control: the 
font-variation-settings
 property

Name:

font-variation-settings

Value:

normal 
|
 [ 
<opentype-tag>

<number>
 ]
#

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

n/a

Computed value:

the keyword 
normal
 or a list, each item a string paired with a number

Canonical order:

per grammar

Animation type:

see prose

Tests

font-variation-settings-calc.html

(live test)

(source)

variable-in-font-variation-settings.html

(live test)

(source)

variable-box-font.html

(live test)

(source)

variable-gpos-m2b.html

(live test)

(source)

variable-gsub.html

(live test)

(source)

variable-opsz-size-adjust.html

(live test)

(source)

variable-opsz.html

(live test)

(source)

This property provides low-level control
	over OpenType or TrueType font variations.
	It is intended as a way of providing access to font variations
	that are not widely used but are needed for a particular use case.

    Authors should 
not
 use

font-variation-settings
 to set any of the variation axes in
		the table below. Instead, please use the higher-level replacement properties, because:

The higher-level properties cascade individually. You can set one without setting the whole 
font-variation-settings
 list

Some higher-level properties can be synthesized for fonts that do not support the font variation.

If you want to set this variation axis

then use this 
instead of

font-variation-settings

Notes

Weight (
wght
)

font-weight

The 
font-weight
 property will set the 
wght
 axis if one is present.

Width (
wdth
)

font-width

The 
font-width
 property will set the 
wdth
 axis if one is present.

Slant (
slnt
) or Italic (
ital
)

font-style

The 
font-style
 property will set the 
slnt
 or 
ital
 axis, depending on its value.

Optical size (
opsz
)

font-optical-sizing

The 
font-optical-sizing
 property will set the 
opsz
 axis if one is present.

The use of font variation settings
	does not affect font selection
	where a fallback font is to be used,
	where using font properties for the same axis
	would have an effect on font selection.

When possible,
	authors should generally use the other properties related to font variations
	(such as 
font-optical-sizing
),
	and only use this property for special cases
	where its use is the only way of accessing a particular infrequently used font variation.

For example,
	it is preferable to use 
font-weight
: 700
	rather than 
font-variation-settings
: "wght" 700.

A value of 
normal
 means that no change in glyph shape, matching, or positioning occurs due to this property.

The 
<opentype-tag>
 is a case-sensitive OpenType or TrueType variation axis name.
	As specified in the OpenType / TrueType specifications,
	axis names contain four ASCII characters.
	Axis name strings longer or shorter than four characters,
	or containing characters outside the U+20–7E codepoint range
	are invalid.
	Axis names need only match an axis tag defined in the font,
	so they are not limited to explicitly registered OpenType / TrueType variation axes.
	Fonts defining custom axis names
	should follow the 
name rules
 defined in the OpenType specification.

If a given axis is not supported by a font,
	its value setting is ignored and therefore has no effect;
	a user agent must not attempt to synthesize fallback behavior based on these axis tags.
	Other axis values within the same CSS 
font-variation-settings
 statement are not ignored.

If a variation axis is supported by a font
	but its set value is greater or less than the predefined font range,
	it will be clamped to the closest value supported by the font.

Values are allowed to be fractional or negative.

Note:
 it is preferable to obtain slanted faces
	by using the 
font-style
 property.
	However, if using the 
slnt
 axis directly,
	via 
font-variation-settings
,
	remember that it is defined
	with a positive angle meaning a counter-clockwise slant,
	the opposite direction to CSS.

If the same axis name appears more than once, the value associated with the last appearance supersedes any previous value for that axis. This deduplication is observable by accessing the computed value of this property.

The computed value contains the de-duplicated axis names,
	sorted in ascending order by 
code unit
.

Although specifically defined for OpenType / TrueType variations,
	variation axes for other modern font formats that support font variations
	might be added in the future.
	Where possible,
	variations defined for other font formats
	should attempt to follow the pattern of registered variation axes.

Animating font-variation-settings is possible
	using the following mechanism. Two declarations of font-feature-settings can be animated between if they are "like".
	"Like" declarations are ones where the same set of properties appear (in any order). Because successive duplicate properties are applied instead of prior duplicate properties, two declarations can be "like" even if they have differing number of properties.
	If two declarations are "like"
	then animation occurs pairwise between corresponding values in the declarations.
	Otherwise, animation is not possible.
	In this situation,
	the "from" values of the animation are swapped to the "to" values
	at an unspecified time during the animation.

9. 

Color Font Support

Color fonts allow for font files to describe,
	not just the contours describing the edges of glyphs,
	but also the colors present inside the glyphs.

Multicolore, by Ivan Filipov

Magical Unicorn Neue Pro, by Arthur Reinders Folmer

Reem Kufi Ink, by Khaled Hosny and Santiago Orozco 

For some uses, such as emoji,
	having the colors fixed in the font is appropriate.
	For others, there is a need to control the colors used from a stylesheet.

Tests

font-colorization.html

(live test)

(source)

CSS provides two ways to do this.
	The 
font-palette
 property allows selecting
	one of several different palettes
	contained in the font.
	The 
@font-palette-values
 rule allows overriding
	one or more colors from within a palette
	or even
	the creation of an entirely different palette.

9.1. 

Controlling Color Font Palettes: The 
font-palette
 property

Many color font file formats allow colors within glyphs to be parameterized.
	In these fonts, colors are referenced by index when describing the geometry of each glyph.
	These indices are resolved within a current active palette
	using a lookup table present inside the font.
	However, many fonts contain multiple palettes,
	each containing a set of complementary colors
	chosen by the font designer to provide pleasing visual results.

In addition, some color font file formats
	provide a regular, uncolored glyph outline
	as well as the colored versions.

Name:

font-palette

Value:

normal 
|
 light 
|
 dark 
|

<palette-identifier>

|

<palette-mix()>

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/a

Computed value:

specified keyword, identifier or 
<palette-mix()>
 function.

<palette-mix()>
 must be simplified to a single keyword or identifier if resulting palette is equivalent.

Canonical order:

per grammar

Animation type:

by computed value

Tests

font-palette-10.html

(live test)

(source)

font-palette-11.html

(live test)

(source)

font-palette-12.html

(live test)

(source)

font-palette-13.html

(live test)

(source)

font-palette-14.html

(live test)

(source)

font-palette-15.html

(live test)

(source)

font-palette-16.html

(live test)

(source)

font-palette-17.html

(live test)

(source)

font-palette-18.html

(live test)

(source)

font-palette-19.html

(live test)

(source)

font-palette-2.html

(live test)

(source)

font-palette-20.html

(live test)

(source)

font-palette-21.html

(live test)

(source)

font-palette-22.html

(live test)

(source)

font-palette-23.html

(live test)

(source)

font-palette-23b.html

(live test)

(source)

font-palette-24.html

(live test)

(source)

font-palette-25.html

(live test)

(source)

font-palette-26.html

(live test)

(source)

font-palette-27.html

(live test)

(source)

font-palette-28.html

(live test)

(source)

font-palette-29.html

(live test)

(source)

font-palette-3.html

(live test)

(source)

font-palette-30.html

(live test)

(source)

font-palette-31.html

(live test)

(source)

font-palette-32.html

(live test)

(source)

font-palette-33.html

(live test)

(source)

font-palette-34.html

(live test)

(source)

font-palette-35.html

(live test)

(source)

font-palette-36.html

(live test)

(source)

font-palette-4.html

(live test)

(source)

font-palette-5.html

(live test)

(source)

font-palette-6.html

(live test)

(source)

font-palette-7.html

(live test)

(source)

font-palette-8.html

(live test)

(source)

font-palette-9.html

(live test)

(source)

font-palette-add-2.html

(live test)

(source)

font-palette-add.html

(live test)

(source)

font-palette-empty-font-family.html

(live test)

(source)

font-palette-modify-2.html

(live test)

(source)

font-palette-modify.html

(live test)

(source)

font-palette-non-ident-font-family.html

(live test)

(source)

font-palette-relative-color-crash.html

(live test)

(source)

font-palette-remove-2.html

(live test)

(source)

font-palette-remove.html

(live test)

(source)

font-palette.html

(live test)

(source)

font-palette-values-relative-colors.html

(live test)

(source)

font-palette-interpolation.html

(live test)

(source)

font-palette-vs-shorthand.html

(live test)

(source)

font-palette-computed.html

(live test)

(source)

font-palette-invalid.html

(live test)

(source)

font-palette-valid.html

(live test)

(source)

With the 
palette-mix()
 function defined as follows:

<palette-mix()>
 = palette-mix( 
<color-interpolation-method>
?

,

    [ 
<'font-palette'>

&&

<percentage [0,100]>
?
 ]
#
 )

normal

			If the 
color-scheme
 property is set to a value other than 
normal
',
			user-agents should select the first light or dark palette as appropriate.
			Otherwise, user-agents display the color font with the default palette
			or default glyph colorisation.

User-agents should take the computed value of the 
color
 property into consideration
			when a color font format requires use of the foreground color

In the 
COLR

[OPENTYPE]
 table, color index 0xFFFF should be rendered according the 
color
 property.

For 
COLR
/
CPAL

[OPENTYPE]
 fonts, 
font-palette
: 
normal
 usually means rendering the font with the palette in the font at index 0.

light

			Some color font formats include metadata
			marking certain palettes as applicable on a light (close to white) background.
			This keyword causes the user-agent
			to use the first available palette in the font file marked this way.
			If the font file format does not account for this metadata,
			or no palette in the font is marked this way,
			this value behaves as 
normal
.

dark

			Some color font formats include metadata
			marking certain palettes as applicable on a dark (close to black) background.
			This keyword causes the user-agent
			to use the first available palette in the font file marked this way.
			If the font file format does not account for this metadata,
			or no palette in the font is marked this way,
			this value behaves as 
normal
.

<palette-identifier>

			This value identifies an CSS-defined palette to use.
			Users can define a palette by using the 
@font-palette-values
 rule.
			If no applicable 
@font-palette-values
 rule is present,
			this value behaves as 
normal
.

<palette-identifier>
 is parsed as a 
<dashed-ident>
.

Note:
 Such a CSS-defined palette may
			be a reference to an existing palette already present in the font,
			be a modification of an existing palette already present in the font,
			or be an entirely new palette.

<palette-mix()>

			This value defines a position in the interpolation between 
one or more
 palette values,
			identified by 
<palette-identifier>
, by the palette keywords

normal
, 
light
, 
dark
,
			or by another 
<palette-mix()>
 value.

The glyphs of the font must be rendered with a palette that is created by
			interpolating, per 
CSS Color 4
 §  13. Color Interpolation
,
			for each palette color index, between the matching color indices
			of the list of palettes specified as arguments,
			recursively resolving 
<palette-mix()>
 functions if needed.

For each palette color, the interpolation follows
			the rules of the 
<color-mix()>
 function.

Percentages are normalized according to 
CSS Color 5
 § 3.2 Percentage Normalization
.

Tests

palette-mix-computed.html

(live test)

(source)

palette-mix-invalid.html

(live test)

(source)

palette-mix-valid.html

(live test)

(source)

Note:
 The names 
light
' and 
dark
 describe the 
background
 the color palette is usable on,
		not the colors in the color palette themselves.

When dark mode is in effect, use a dark mode palette

@media

(
prefers-color-scheme: dark
)

{

        .banner 
{
font-palette
:
 dark
;

}

}

		A font has a dark mode palette with the following three entries:

 #eee8aa

 #dd4541

 #72342e

In addition, there are two custom palettes defined, one called "--warm":

 oklch(85% 0.14 88)

 oklch(62% 0.13 28)

 oklch(32% 0.05 29.6)

and one called "--soft":

 color(display-p3 0.89 0.89 0.76)

 color(display-p3 0.75 0.55 0.55)

 color(display-p3 0.508 0.435 0.422)

this palette mix:

font-palette
:

palette-mix
(
dark 
20
%
,
 --warm 
45
%
,
 --soft
);

will create the following palette
		(the percentage of --soft is omitted, so it is 35%,
		and the color interpolation method is omitted, so it is 
oklab
):

 oklab(88.389% -0.00651 0.09474)

 oklab(64.379% 0.11148 0.05236)

 oklab(42.124% 0.04469 0.02408)

		Animate between palettes.

@font-palette-values
 --pink 
{

font-family
:
 Nabla
;

base-palette
:

1
;

}

@font-palette-values
 --yellow 
{

font-family
:
 Nabla
;

base-palette
:

7
;

}

@keyframes
 animate-palette 
{

  from 
{

font-palette
:
 --yellow
;

}

  to 
{

font-palette
:
 --pink
;

}

}

p 
{

font-family
:
 Nabla
;

animation
:
 animate-palette 
1.4
s
 infinite alternate linear
;

}

Nabla Color by typearture.com - animating between palettes 1 and 7 in the font.

Tests

font-palette-animation-not-specified-endpoints.html

(live test)

(source)

multiple-elements-font-palette-animation.html

(live test)

(source)

 Add more examples and pictures.

9.2. 

User-defined font color palettes: The 
@font-palette-values
 rule

The 
@font-palette-values
 rule defines a color palette
	and associates that color palette with a specific font.
	This allows a web author to select arbitrary 
<color>
s to use inside a color font
	rather than being limited to the preexisting palettes inside font files.

Note:
 The OpenType 
CPAL
 table is restricted to sRGB colors.
	The 
<color>
s in 
@font-palette-values
 allow any CSS color.
	Some implementations currently use APIs which are restricted to sRGB
	and may therefore map the specified colors to sRGB.
	This is expected to be a temporary limitation.
	Authors should not rely on this mapping to sRGB.

In addition, this rule’s association with a specific font
	allows a name of a palette to apply differently to different fonts,
	which allows similar colors to be used across multiple fonts
	when multiple fonts are used in an element
	(i.e. for font fallback).

Note:
 A web author might wish to create multiple palettes for a single font
	in order to create multiple themes for their web content.
	A web author might also wish to create matching palettes for multiple fonts
	to achieve a consistent design across a collection of different fonts.

A 
@font-palette-values
 rule represents a palette of colors used in a font.
	A palette consists of an ordered collection of colors.
	Using the 
@font-palette-values
 allows a web author
	to reference a palette existing within a font
	as well as creating a palette populated with author-defined colors.
	In addition, it allows overriding a set of colors from a palette in the font
	with colors described by the web author.

A palette is always 
complete
, meaning that it is impossible to describe
	a palette which has missing colors. If colors would be missing, they are taken
	from the palette within the font identified by the 
base-palette
 descriptor.

Math functions
, such as 
calc()
,
	and also 
var()
, and 
env()
,
	are valid within descriptor values in a

@font-palette-values
 rule. They are evaluated within the context of the root
	element. Relative units are also evaluated within the context of the root element.

The 
@font-palette-values
 rule consists of the 
@font-palette-values
 at-keyword
	followed by a block of descriptor declarations.
	It has the following syntax:

@font-palette-values

<dashed-ident>

{

<declaration-list>

}

Tests

palette-values-rule-add-2.html

(live test)

(source)

palette-values-rule-add.html

(live test)

(source)

palette-values-rule-delete-2.html

(live test)

(source)

palette-values-rule-delete.html

(live test)

(source)

font-palette-values-invalid.html

(live test)

(source)

font-palette-values-valid.html

(live test)

(source)

The 
@font-palette-values
 rule accepts the descriptors defined in this specification.

If multiple 
@font-palette-values
 rules are defined with the same name,
	the last one in document order wins, and all preceding ones are ignored.

		Modify Bixa Color’s color palette.

@font-palette-values
 --Cooler 
{

font-family
:
 Bixa
;

base-palette
:

1
;

override-colors
:

1
 #7EB7E4
;

}

Bixa Color by Novo Typo. Above, using the colors in the font;
				below, the orange changed to a blue.

		Modify Handover Sans’s color palette

@font-palette-values
 --Augusta 
{

font-family
:
 Handover Sans
;

base-palette
:

3
;

override-colors
:

1

rgb
(
43
,

12
,

9
),

3

var
(
--highlight
);

}

These descriptors apply solely within the context of the 
@font-palette-values
 rule in which they are defined,
	and do not apply to document language elements.
	When a given descriptor occurs multiple times in a given 
@font-palette-values
 rule,
	only the last descriptor declaration is used
	and all prior declarations for that descriptor are ignored.

Each of these palettes are applied
	to each @font-face that share a family name.

		I want to use two color fonts in a greenish palette.
		The first font, Bixxxa, already has palette that I can use,
		but for Bungeehee I need to overwrite one color
		to get my green palette.

@font-face

{

font-family
:
 Bixxxa
;

src
:

url
(
'./bixxxa.woff'
)

format
(
'woff'
);

}

@font-face

{

font-family
:
 Bungeehee
;

src
:

url
(
'./bungeehee.woff'
)

format
(
'woff'
);

}

@font-palette-values
 --ToxicGreen 
{

font-family
:
 Bixxxa
;

base-palette
:

3
;

/* This is Bixxxa's green palette */

}

@font-palette-values
 --ToxicGreen 
{

font-family
:
 Bungeehee
;

base-palette
:

7
;

/* This is Bungeehee's green palette... */

  override-colors: 
2
 lime
;

/* ...except this is pink, which I overwrite to lime */

}

h1 
{

font-family
:
 Bixxxa
;

font-palette
:
 --ToxicGreen
;

}

h2 
{

font-family
:
 Bungeehee
;

font-palette
:
 --ToxicGreen
;

}

Example by Roel Nieskens

Note:
 In the case where a family name is shared
	between multiple physical fonts,
	(such as when a compound font is created, using 
unicode-range
),
	and if those fonts have different palettes,
	the result of specifying a partial palette
	using 
@font-palette-values

	is unlikely to be what the author intended.
	In this case,
	it is better to supply a complete palette definition.

		In the above example,
		since two different font families have been set up
		to have compatible named palettes,
		one could go on to write

h3 
{

font-family
:
 Bixxxa
,
 Bungeehee
;

font-palette
:
 --ToxicGreen
;

}

Which would correctly apply the desired palette
		in each font
		even though they have different palette numbers.

A given set of 
@font-palette-values
 rules
	define which author-defined palettes are available for use
	within the documents that contain these rules.

An author-defined font color palette
	must only be available to the documents that reference it.
	Using an author-defined color palette outside of the documents that reference it
	would constitute a security leak
	since the contents of one page would be able to affect other pages,
	something an attacker could use as an attack vector.

This at-rule follows the forward-compatible parsing rules of CSS.
	Like properties in a declaration block,
	declarations of any descriptors that are not supported by the user agent
	must be ignored.

@font-palette-values
 rules require a 
font-family
 descriptor;
	if it is missing,
	the 
@font-palette-values
 rule is invalid and must be ignored entirely.

In cases where user agents have limited platform resources,
	do not implement support for color fonts,
	or implement the ability to disable color fonts,

@font-palette-values
 rules must simply be ignored;
	the behavior of individual descriptors as defined in this specification should not be altered.

9.2.1. 

Font family: the 
font-family
 descriptor

Name:

font-family

For:

@font-palette-values

Value:

<font-family-name>
#

Initial:

N/A

This descriptor defines the font families that this palette applies to,
	using the same list of font families as 
§ 5 Font Matching Algorithm
.
	This palette will only ever be applied to the fonts with these family names.
	The value of this descriptor  means that only named font families are allowed
	and rules that include generic fonts in the list of font families
	are syntax errors.
	If syntax errors occur within the font family list,
	the descriptor must be ignored
	(will still be in the CSS OM, but will not match any font families).

9.2.2. 

Specifying the base palette: the 
base-palette
 descriptor

Name:

base-palette

For:

@font-palette-values

Value:

light 
|
 dark 
|

<integer [0,∞]>

Initial:

N/A

light

			Some color font formats include metadata
			marking certain palettes as applicable on a light (close to white) background.
			This keyword identifies the first available palette in the font file marked this way.
			If the font file format does not account for this metadata,
			or no palette in the font is marked this way,
			this value behaves as 0.

dark

			Some color font formats include metadata
			marking certain palettes as applicable on a dark (close to black) background.
			This keyword identifies the first available palette in the font file marked this way.
			If the font file format does not account for this metadata,
			or no palette in the font is marked this way,
			this value behaves as 0.

<integer [0,∞]>

			Identifies a (zero-based) numerical palette index within the font.

		Modify Banner Flag’s color palette

@font-palette-values
 --Festival 
{

font-family
:
 Banner Flag
;

base-palette
:

1
;

override-colors
:

0

rgb
(
123
,

64
,

27
),

1
 darkblue
,

2

var
(
--highlight
);

}

This descriptor specifies a palette in the font
	which the containing 
@font-palette-values
 rule uses as an initial value.
	If no 
override-colors
 key is present in the 
@font-palette-values
 rule,
	then the 
@font-palette-values
 rule represents the palette in the font
	with the same index as the value of this descriptor.
	If a 
override-colors
 key is present in the 
@font-palette-values
 rule,
	each item in the value of that descriptor overrides a single color
	in the color palette represented by this 
@font-palette-values
 block.

		Rename Handover Sans’s 3rd color palette

@font-palette-values
 --Augusta 
{

font-family
:
 Handover Sans
;

base-palette
:

3
;

}

If this descriptor is not present in the 
@font-palette-values
,
	or if the font does not contain a palette at the index of the value of 
base-palette
,
	it behaves as if 
0
 were specified.
	If a font does not contain any color palettes,
	no colors are included in the initial color palette
	represented by this 
@font-palette-values
 rule.
	Colors in the palette can be overridden
	by using the 
override-colors
 descriptor in the 
@font-palette-values
 rule.

9.2.3. 

Overriding a colors from a palette: The 
override-colors
 descriptor

Name:

override-colors

For:

@font-palette-values

Value:

[ 
<integer [0,∞]>

<color>
 ]
#

Initial:

N/A

This descriptor overrides colors
	to the initial color palette represented by this 
@font-palette-values
 rule.

The 
override-colors
 descriptor takes
	a comma-separated list of palette index entries and colors.
	Each item in the comma-separated list represents a tuple of
	an entry into the palette and a color to replace it with.

Each specified 
<color>
 must be an

absolute color
,
	otherwise the descriptor is invalid.

For each key/value pair in the value of this descriptor,
	the color with that key in the initial palette (i.e. by using the 
base-palette
 descriptor)
	is overwritten by the color specified in this descriptor’s value.
	A key that is outside the range of indices of the initial palette is ignored,
	but does not make the descriptor invalid.

Palette index entries
	in the 
override-colors
 descriptor
	are a (zero-based) palette index entry.

Integer values are zero-indexed.

If the keys of multiple distinct key/value pairs identify the same color index (either by name or by integer),
	the last key is used for the purposes of rendering. However, for serialization purposes, both
	key/value pairs are present.

Note:
 This means that using 
font-palette
 with the same value on two different elements
	might result in different used palettes
	because the value of variables inside the 
@font-palette-values
 rule
	might apply differently in the context of those two elements.

Colors provided from CSS
	(as overrides, or as new entries)
	may use any supported colorspace.

		Modify Blaka Ink’s color palette

@font-palette-values
 --Festival 
{

font-family
:
 Blaka Ink
;

base-palette
:

0
;

override-colors
:

0

oklch
(
0.63

0.12

105.7
),

1

color
(
display-p3 
0.23

0.22

0.04
),

2

color
(
prophoto-rgb 
0.37

0.27

0.09
);

}

Note:
 The colors specified in versions 0 and 1 of the CPAL table are in sRGB.

9.3. 

Selecting the text presentation style: The 
font-variant-emoji
 property

Name:

font-variant-emoji

Value:

normal 
|
 text 
|
 emoji 
|
 unicode

Initial:

normal

Applies to:

all elements and text

Inherited:

yes

Percentages:

N/a

Computed value:

specified keyword

Canonical order:

per grammar

Animation type:

discrete

Tests

font-variant-emoji-1.html

(live test)

(source)

font-variant-emoji-2.html

(live test)

(source)

font-variant-emoji-003.html

(live test)

(source)

font-variant-emoji-004.html

(live test)

(source)

font-variant-emoji-005.html

(live test)

(source)

variation-sequences.html

(live test)

(source)

font-unicode-presented-as-emoji-outline.html

(live test)

(source)

font-variant-emoji-computed.html

(live test)

(source)

font-variant-emoji-invalid.html

(live test)

(source)

font-variant-emoji-valid.html

(live test)

(source)

This property allows web authors to select
	whether emoji presentation or text presentation is used
	for certain emoji code points.
	Traditionally, these presentation styles were selected
	by appending Variation Selector 15 (U+FE0E) or Variation Selector 16 (U+FE0F)
	to certain code points.
	However, 
font-variant-emoji
 allows web authors to set a default presentation style
	which can replace the variation selectors.

Only the code points 
listed
 by Unicode
	as contributing to a Unicode emoji presentation sequence
	are affected by this property.
	Within this CSS specification,
	these characters are referred to as 
Emoji Presentation Participating Code Points
.
	This property has no effect on any other characters.

This property is expected to affect font fallback;
	however, the exact nature of the interaction of font fallback with 
font-variant-emoji

	is explicitly unspecified.
	However, a variation selector must be included in a previous cluster
	as defined by the 
cluster matching
 section above.
	A natural result of this behavior
	is that a variation selector must not be rendered in a different font than the previous character.
	It thus causes font fallback to behave
	as if the respective variation selector was intended
	(as in the values description);
	then font fallback, including the cluster fallback rules, is performed,
	which must take the presentation preference
	of these "appended" variation selectors into account.

Even when 
font-variant-emoji
 is used,
	the presence of Variation Selector 15 (U+FE0E) or Variation Selector 16 (U+FE0F)
	in the contents of an element
	override the rendering specified in 
font-variant-emoji
.
	Therefore, 
font-variant-emoji
 sets a default presentation
	which the text being rendered can opt out of.

Note:
 Different platforms have different conventions about how to handle emoji presentation sequences.
	A cross-platform UA might wish to follow the conventions of each individual platform,
	or it might wish to use the same approach on all platforms.
	When tasked with a request for an emoji style rendering,
	a UA might wish to disregard fonts which do not include color tables.
	A different UA might wish instead to use the same mechanical cluster fallback algorithm
	that it would use for any arbitrary cluster.

Variation selectors other than FE0E VARIATION SELECTOR-15 and U+FE0F VARIATION SELECTOR-16
	must not have any effect on font selection.
	If one of these variation selectors is present,
	but unsupported by the font previously selected,
	the variation selector is ignored.

BCP47’s 
-u-
 extension to the language tag accepted by 
lang
 or 
xml
:
lang
 should not be
	considered when the user-agent decides whether to use emoji presentation or text presentation for a particular character.

normal

			User agents can choose to draw a 
Emoji Presentation Participating Code Point

			in either emoji style or text style.
			User agents typically follow platform conventions when performing this decision.

text

			Code points are rendered as if U+FE0E VARIATION SELECTOR-15
			was appended to every 
Emoji Presentation Participating Code Point
.

emoji

			Code points are rendered as if U+FE0F VARIATION SELECTOR-16
			was appended to every 
Emoji Presentation Participating Code Point
.

unicode

			Code points are rendered in accordance with 
[UTS51]

			as either emoji-default, text-default, or text-only,
			depending on the values of the Emoji and Emoji_Presentation
			properties for each

Emoji Presentation Participating Code Point
.
			If present, FE0E VARIATION SELECTOR-15 and U+FE0F VARIATION SELECTOR-16
			will override the default presentation of individual

Emoji Presentation Participating Code Points
.

		To show the emoji form of U+1F6CB COUCH AND LAMP,
		let CustomEmoji.ttf obey the user agent’s notion
		of supporting the emoji form of this character,
		and use the following:

@font-face

{

font-family
:

"Custom Emoji"
;

src
:

url
(
"CustomEmoji.ttf"
)

format
(
"truetype"
);

}

...
<div style=
"font-family: 'Custom Emoji'; font-variant-emoji: emoji;"
>&#x1F6CB
;
</div>

10. 

Font Taxonomy

A given font may belong in one or more of the following categories:

10.1. 

Installed Fonts

A font may be installed globally on a device. Such fonts are generally accessible in any application, even applications which have no concept of CSS. The file or files backing the font object exist on the user’s device, not as a remote resource.

Installed Fonts must not be Web Fonts, and Web Fonts must not be Installed Fonts.

10.2. 

Web Fonts

A font may be backed by a remote resource, which must be requested using the user agent’s resource fetching infrastructure. Web Fonts are represented by one of two mechanisms:

@font-face
 rules

A 
FontFace
 member of the Document’s 
FontFaceSet

A Web Font must not be accessible in any other Document from the one which either is associated with the 
@font-face
 rule or owns the 
FontFaceSet
. Other applications on the device must not be able to access Web Fonts.

Installed Fonts must not be Web Fonts, and Web Fonts must not be Installed Fonts.

Web Fonts shadow Installed Fonts, so if an Installed Font has the same family name as a Web Font, the Installed Font is not accessible.

10.3. 

Preinstalled Fonts and User-Installed Fonts

Users can choose to install fonts on their devices.
	User-Installed Fonts are installed by an explicit action by the user,
	such as clicking an "Install" button
	or copying a file into a particular directory on their device.
	Such fonts are User-Installed Fonts and also are Installed Fonts.
	Web content authors should not count on the presence of user-installed fonts,
	because there is no guarantee any user will have
	performed the action to install a specific font.

Please see the 
Font Matching Algorithm

	description of how user-installed fonts may interact with the font matching algorithm.

Any Installed Font which is not a User-Installed font is a Preinstalled Font. It is likely that all users of a particular version of a particular Operating System will have the same set of Preinstalled Fonts installed. As such, Web content authors targeting these Operating Systems may wish to use these fonts' family names inside 
font-family
 properties.

10.4. 

System Font

The System Font is the font which is used by the 
system-ui

generic font family name
. It is an example of a Preinstalled Font.

Additional font styles may also be provided as 
ui-sans-serif
, 
ui-serif
, 
ui-monospace
,
	and 
ui-rounded
 which are also Preinstalled Font(s) if the system provides them.

Tests

system-ui-ar.html

(live test)

(source)

system-ui-ja-vs-zh.html

(live test)

(source)

system-ui-ja.html

(live test)

(source)

system-ui-mixed.html

(live test)

(source)

system-ui-ur-vs-ar.html

(live test)

(source)

system-ui-ur.html

(live test)

(source)

system-ui-zh.html

(live test)

(source)

system-ui.html

(live test)

(source)

11. 

	Font Technologies and Formats

11.1. 
Font tech

The 
features-opentype
, 
features-aat
 and 
features-graphite
 techs
	refer to support for font features,
	commonly implemented in 
[OPENTYPE]
 with the

GSUB
 and the

GPOS
 tables,
	as well as in 
[AAT-FEATURES]
 using the

morx
 and

kerx
 tables
	and 
[GRAPHITE]
 with the

Silf
,

Glat 
,

Gloc 
,

Feat 
 and

Sill 
 tables
	as documented in the

Graphite Table Format
.
	The section on 
§ 6 Font Feature Properties
 describes properties that interact with these facilities.

The 
variations
 tech refers to the support of font variations,
	commonly implemented in 
[OPENTYPE]
 with the

avar
,

cvar
,

fvar
,

gvar
,

HVAR
,

MVAR
,

STAT
, and

VVAR
 tables,
	as well as in 
[AAT-FEATURES]
 using the

avar
,

cvar
,

fvar
,

gvar
 tables.
	The section on 
§ 2 Basic Font Properties
 as well as the section on 
§ 8 Font Variation Properties

	describe properties that interact with these facilities.

The 
color-colrv0
, 
color-colrv1
, 
color-svg
, 
color-sbix
 and 
color-cbdt

	technologies refers to various types of color font file technologies.
	Each one represents a table
	(
COLR
,

SVG
,

sbix
 or

CBDT
)
	inside 
[OPENTYPE]
 or 
[AAT-FEATURES]
 fonts which must be supported
	to satisfy this requirement.

The 
palettes
 tech refers to support for font palettes,
	commonly implemented in the 
[OPENTYPE]
 and 
[AAT-FEATURES]

	with the

CPAL
 table.
	The section on 
§ 9 Color Font Support
 describes properties that interact with these facilities.

The 
incremental
 tech
	refers to client support for incremental font transfer 
[IFT]
.

For background on these, see 
[PFE-report]
.

Web authors can specify the 
tech()
 function
	inside an 
@font-face

src
 descriptor
	to indicate that support is
	required for correct rendering of a font.
	This mechanism can be used for gracefully falling back
	to an ancillary font
	when requested support is not present.

		This 
@font-face
 block shows how to use a color font if support is present on the user agent,
		and falls back to a non-color-font if support is not present.

@font-face

{

font-family
:

"Trickster"
;

src
:

url
(
"trickster-COLRv1.otf"
)

format
(
opentype
)

tech
(
color-COLRv1
),

url
(
"trickster-outline.otf"
)

format
(
opentype
);

}

11.2. 
Font formats

Format strings defined by this specification are as follows.
	The 
<font-format>
 values are synonyms for the formats below.

String

Font Format

Common extensions

Common media types

"collection"

OpenType Collection

.otc,.ttc

font/collection

"embedded-opentype"

Embedded OpenType

.eot

application/vnd.ms-fontobject

"opentype"

OpenType

.ttf, .otf

font/otf
,

font/ttf

"svg"

SVG Font
 (deprecated)

.svg, .svgz

image/svg+xml

"truetype"

TrueType

.ttf

font/ttf

"woff"

WOFF 1.0 (Web Open Font Format)

.woff

font/woff

"woff2"

WOFF 2.0 (Web Open Font Format)

.woff2

font/woff2

Tests

format-specifiers-variations.html

(live test)

(source)

Given the overlap in common usage between TrueType and OpenType,
	the format hints "truetype" and "opentype"
	must be considered as synonymous;
	a format hint of "opentype" does not imply
	that the font contains Postscript CFF style glyph data
	or that it contains OpenType layout information
	(see 
Appendix A
 for more background on this).

12. 

Object Model

The contents of 
@font-face
 and 
@font-feature-values
 rules
	can be accessed via the following extensions to the CSS Object Model.

Tests

idlharness.html

(live test)

(source)

12.1. 

The 
CSSFontFaceRule
 interface

The 
CSSFontFaceRule
 interface represents a 
<@font-face>
 rule.

[
Exposed
=
Window
]

interface

CSSFontFaceDescriptors
 : 
CSSStyleDeclaration
 {

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

src
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontFamily
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-family
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontStyle
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-style
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontWeight
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-weight
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontStretch
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-stretch
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontWidth
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-width
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

unicodeRange
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

unicode-range
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontFeatureSettings
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-feature-settings
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontVariationSettings
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-variation-settings
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontNamedInstance
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-named-instance
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontDisplay
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-display
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

fontLanguageOverride
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

font-language-override
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

ascentOverride
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

ascent-override
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

descentOverride
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

descent-override
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

lineGapOverride
;

attribute
 [
LegacyNullToEmptyString
] 
CSSOMString

line-gap-override
;
};

[
Exposed
=
Window
]

interface

CSSFontFaceRule
 : 
CSSRule
 {
  [
SameObject
, 
PutForwards
=
cssText
] 
readonly

attribute

CSSFontFaceDescriptors

style
;
};

12.2. 

The 
CSSFontFeatureValuesRule
 interface

The 
CSSRule
 interface is extended as follows:

partial

interface

CSSRule
 {

const

unsigned

short

FONT_FEATURE_VALUES_RULE
 = 14;
};

The 
CSSFontFeatureValuesRule
 interface represents a 
@font-feature-values
 rule.

[
Exposed
=
Window
]

interface

CSSFontFeatureValuesRule
 : 
CSSRule
 {

attribute

CSSOMString

fontFamily
;

readonly

attribute

CSSFontFeatureValuesMap

annotation
;

readonly

attribute

CSSFontFeatureValuesMap

ornaments
;

readonly

attribute

CSSFontFeatureValuesMap

stylistic
;

readonly

attribute

CSSFontFeatureValuesMap

swash
;

readonly

attribute

CSSFontFeatureValuesMap

characterVariant
;

readonly

attribute

CSSFontFeatureValuesMap

styleset
;

readonly

attribute

CSSFontFeatureValuesMap

historicalForms
;
};

[
Exposed
=
Window
]

interface

CSSFontFeatureValuesMap
 {

maplike
<
CSSOMString
, 
sequence
<
unsigned

long
>>;

undefined

set
(
CSSOMString

featureValueName
,
    (
unsigned

long

or

sequence
<
unsigned

long
>) 
values
);
};

fontFamily
, 
 of type 
CSSOMString

The list of one or more font families for which a given set of feature values is defined.

annotation
, 
 of type 
CSSFontFeatureValuesMap
, readonly

etc.

Maps of feature values associated with feature value names for a given 
font-variant-alternates
 value type

Each value map attribute of 
CSSFontFeatureValuesRule
 reflects the values
	defined via a corresponding 
feature value block
.
	Thus, the 
annotation
 attribute
	contains the values contained within a 
@annotation

feature value block
, the

ornaments
 attribute contains the
	values contained with a 
@ornaments

feature value block
,
	and so forth.

The 
CSSFontFeatureValuesMap
 interface uses the

default map class methods

	but the 
set()
 method has different behavior.  
	It takes a sequence of unsigned integers and
	associates it with a given 
featureValueName
. The method
	behaves the same as the default map class method
	except that a single unsigned long value is treated as a sequence of a
	single value. The method throws an exception if an invalid number of
	values is passed in.  If the associated

feature value block

	only allows a limited number of values, the 
set()
 method
	throws an 
InvalidAccessError
 exception when the input
	sequence to 
set()
 contains more than the limited number of
	values.  See the
	description of 
multi-valued feature value definitions

	for details on the maximum number of values allowed for a given type
	of 
feature value block
.

Note:
 The 
get
()

	method always returns a sequence of values, even if the sequence only contains
	a single value.

Tests

font-feature-values-map-live.html

(live test)

(source)

12.3. 

The 
CSSFontPaletteValuesRule
 interface

The 
CSSFontPaletteValuesRule
 interface represents a 
@font-palette-values
 rule.

[
Exposed
=
Window
]

interface

CSSFontPaletteValuesRule
 : 
CSSRule
 {

readonly

attribute

CSSOMString

name
;

readonly

attribute

CSSOMString

fontFamily
;

readonly

attribute

CSSOMString

basePalette
;

readonly

attribute

CSSOMString

overrideColors
;
  };

13. 

Serializing

13.1. 

Serializing font-related properties

Unless specifically noted for individual properties,
	the properties defined in this module
	follow the principles of

CSSOM
 § 6.7.2 Serializing CSS Values
.

Tests

font-variant-serialization.html

(live test)

(source)

13.2. 

Serializing font-related at-rules

Unless specifically noted
	for individual descriptors,
	the descriptors defined for at-rules in this module
	follow the principles of

CSSOM
 § 6.7.2 Serializing CSS Values
.

In particular,
	following the principle of shorter representation:
	for descriptors which accept a range of values,
	if the start and end values are the same
	(the range is zero)
	the descriptor is serialized as a single value, not a range.

Tests

at-font-face-descriptors.html

(live test)

(source)

		For example, the rule

@font-face

{

font-family
:

"foo"
;

font-weight
:

200

200
;

}

would serialize as

@font-face

{

font-family
:

"foo"
;

font-weight
:

200
;

}

Also,
	following the principle of retaining only the last-defined value,
	as well as the principle of shortest representation,
	multiply-specified tuples and multiple blocks
	are serialized as a single block
	containing only the last-defined value.

		For example, the declaration:

/* Repeated declaration names, and multiple blocks of the same type*/

@font-feature-values
 foo 
{

@swash

{

pretty
:

0
;

cool
:

2
;

}

@swash

{

pretty
:

1
;

}

}

would be serialized as:

/* Canonical serialization */

@font-feature-values
 foo 
{

@swash

{

cool
:

2
;

pretty
:

1
;

}

}

Tests

font_feature_values_map_iteration.html

(live test)

(source)

Appendix A: Mapping platform font properties to CSS properties

This appendix is included as background for some of the problems and
	situations that are described in other sections.  It should be viewed as
	informative only.

Font properties in CSS are designed to be
	independent of the underlying font formats used;
	they can be used to specify bitmap fonts,
	Type1 fonts,
	SVG fonts
	in addition to the common TrueType and OpenType fonts.
	But there are facets of the TrueType and OpenType formats
	that often cause confusion for authors
	and present challenges to implementers
	on different platforms.

Originally developed at Apple,
	TrueType 
[TRUETYPE]
 was designed as an outline font format
	for both screen and print.
	Microsoft joined Apple
	in developing the TrueType format
	and both platforms have supported
	TrueType fonts since then.
	Font data in the TrueType format consists of
	a set of tables distinguished with common four-letter tag names,
	each containing a specific type of data.
	For example,
	naming information,
	including copyright and license information,
	is stored in the 
name
 table.
	The 
character map
 (
cmap
) table
	contains a mapping
	of character encodings to glyphs.
	Apple later added additional tables
	for supporting enhanced typographic functionality;
	these are now called Apple Advanced Typography, or AAT, fonts.
	Microsoft and Adobe developed
	a separate set of tables for advanced typography
	and called their format OpenType 
[OPENTYPE]
.
	The OpenType specification is standardized at ISO as the
	Open Font Format 
[OPEN-FONT-FORMAT]
.

In many cases the font data used under Microsoft Windows
	or Linux
	is slightly different from the data used under Apple’s Mac OS X
	because the TrueType format allowed for
	explicit variation across platforms.
	This includes font metrics,
	names and

character map
 data.

Specifically,
	font family name data is handled differently
	across platforms.
	For TrueType and OpenType fonts
	these names are contained in the 
name
 table,
	in name records with name ID 1.
	Multiple names can be stored for different locales,
	but Microsoft recommends fonts
	always include at least a US English version of the name.
	On Windows,
	Microsoft made the decision for backwards compatibility
	to limit this family name to a maximum of four faces;
	for larger groupings the
	"preferred family" (name ID 16) or
	"WWS family" (name ID 21)
	can be used.
	Other platforms such as OSX don’t have this limitation,
	so the family name is used to define all possible groupings.

Other name table data provides names used
	to uniquely identify a specific face within a family.
	The full font name (name ID 4) and
	the Postscript name (name ID 6)
	describe a single face uniquely.
	For example,
	the bold face of the Gill Sans family
	has a fullname of "Gill Sans Bold" and
	a Postscript name of "GillSans-Bold".
	There can be multiple localized versions of the fullname for a given face,
	but the Postscript name is always a unique name
	made from a limited set of ASCII characters.

On various platforms,
	different names are used to search for a font.
	For example,
	with the Windows GDI CreateIndirectFont API,
	either a family or fullname can be used to lookup a face,
	while on Mac OS X the CTFontCreateWithName API call is used
	to lookup a given face
	using the fullname and Postscript name.
	Under Linux,
	the fontconfig API allows
	fonts to be searched using any of these names.
	In situations where platform API’s
	automatically substitute other font choices,
	it may be necessary to
	verify a returned font matches a given name.

The weight of a given face can be determined
	via the usWeightClass field of the OS/2 table
	or inferred from the style name (name ID 2).
	Likewise, the width can be determined
	via the usWidthClass of the OS/2 table
	or inferred from the style name.
	For historical reasons
	related to synthetic bolding at weights 200 or lower with the Windows GDI API,
	font designers have sometimes skewed values in the OS/2 table
	to avoid these weights.

Rendering complex scripts that use contextual shaping
	such as Thai,
	Arabic
	and Devanagari
	requires features present only in OpenType or AAT fonts.
	Currently,
	complex script rendering is supported
	on Windows and Linux using OpenType font features
	while both OpenType and AAT font features are used
	under Mac OS X.

14. 

Security Considerations

See items 
9
, 
16
 and 
17
 in the self-review questionnaire below.

15. 

Privacy Considerations

Following 
Self-Review Questionnaire: Security and Privacy
,
	and using the 
§ 10 Font Taxonomy
:

15.1. 
What information might this feature expose to Web sites or other parties, and for what purposes is that exposure necessary?

This specification allows the use of Web Fonts,
	which are requested on demand
	but are not installed.
	In the case where the document or stylesheet has a different origin to the Web Font,
	this network request exposes information in the Referer header,
	which may be harvested by font providers.

In addition to Web Fonts, this specification continues to allow
	the use of Installed Fonts (both  Preinstalled Fonts and User-Installed Fonts)
	as introduced in CSS1.

While Web Fonts have the advantage of consistency across platforms,
	Installed Fonts have the advantage of zero download time.

In some cases, and particularly for poorly-supported or minority languages,
	Installed Fonts allow information to be displayed which could not otherwise be displayed
	because there is no freely licensable Web Font which supports that language
	or because the latency or download time would make it’s use infeasible,
	particularly for languages with a large character repertoire,
	or on slow or metered connections.

Note:
 The set of 
installed fonts

	available in the 
Font Matching Algorithm

	is explicitly undefined.
	The available set of fonts 
is

	used by trackers to fingerprint users and reduce their privacy.
	However, some 
installed fonts
,
	even some 
user-installed fonts
,
	are required to make languages readable.
	User agents may choose to make all installed fonts available
	for language support and design integrity reasons,
	or may choose to make some fonts unavailable for privacy reasons.
	In addition, user agents may have additional facilities for fine-tuning this balance,
	such as interfaces which prompt users to explicitly make
	certain requested fonts available or unavailable
	(perhaps on a per-site basis).
	Different user agents, even running on the same Operating System,
	are expected to strike different balances here.

In the case of user agents which perform rendering of local resources
	(such as an HTML and CSS to PDF renderer,
	or a Web-based wordprocessor)
	access to all Installed Fonts
	(both  Preinstalled Fonts and User-Installed Fonts)
	is necessary to provide the expected functionality.

An attacker may obtain fingerprinting information by querying the Installed Fonts.
	In contrast to older technologies
	(notably Adobe Flash, which provided a complete list of Installed Fonts
	and sent this information in HTTP headers)
	such probing must be done one font at a time,
	providing the font family name
	and then checking
	(either via script,
	or by using unicode-range to selectively download webfonts
	depending on whether the user has a font by a certain name
	that supports a certain character)
	whether the font was loaded.
	This takes time, and checking for more than a few hundred fonts
	introduces a noticeable delay in page rendering.

For 
especially privacy-sensitive contexts
,
	options would include never downloading any webfonts
	(at the risk that some characters may be rendered incorrectly, or not at all),
	or always downloading all webfonts whether needed or not
	(ignoring unicode-range,
	and potentially downloading vast quantities of unused fonts
	each time the page is viewed).

15.2. 
Is this specification exposing the minimum amount of information necessary to power the feature?

An emerging consensus is that a user agent must expose Preinstalled Fonts
	for correct functioning,
	but there is no consensus on exposing User-Installed Fonts.
	This specification 
 allows a user agent

	to ignore User-Installed Fonts for the purpose of the Font Matching Algorithm.
	Several existing user agents already do this.

The minimum amount varies by type of user and is 
currently being debated
.
	There is a useful 
taxonomy of User-Installed Font users

	which has been 
 slightly extended
.

A permissive amount of information exposes potentially more fingerprinting information;
	a restrictive amount of information reduces fingerprinting but also reduces functionality
	and in some cases, for minority languages, would break the Web completely for those users.

The possibility of a configurable, per-user opt-in to exposing some or all User-Installed Fonts,
	or a per-origin opt-in, is being discussed.

The possibility of a privacy budget, which would penalize or disable
	a malicious web page which tested a large number of fonts,
	but allow a harmless page which tested a much smaller number,
	has also been discussed.

Some user agents expose a more restricted set of Preinstalled Fonts
	in their Private Browsing, Incognito, or Resist Fingerprinting modes,
	compared to their normal mode.

15.3. 
How does this specification deal with personal information or personally-identifiable information or information derived thereof?

Personal information is not exposed by this specification.

Personally identifiable information may be exposed in some cases.
	For example, for someone in Japan, having conditionally-enabled Japanese fonts
	enumerable probably isn’t a substantial fingerprinting vector.
	For someone in Europe who has a Japanese IME in the text input menu, they are.

15.4. 
How does this specification deal with sensitive information?

Fingerprinting on Installed Fonts may expose sensitive information in some cases.
	For example, persecuted minorities risk leaking sensitive information
	by exposing that they use fonts required for a persecuted minority language;
	either by requesting a Web Font from a third party service,
	or exposing Preinstalled Fonts or User-Installed Fonts associated with that language.

15.5. 
Does this specification introduce new state for an origin that persists across browsing sessions?

No.

Specifically, Web Fonts 
must not be accessible
	in any other Document from the one which either is associated with the @font-face rule
	or owns the FontFaceSet.
	Other applications on the device must not be able to access Web Fonts.

	This avoids information leaking across origins.

Similarly, font palette values

must only be available to the documents that reference it
.
	Using an author-defined color palette outside of the documents that reference it
	would constitute a security leak since the contents of one page
	would be able to affect other pages,
	something an attacker could use as an attack vector.

15.6. 
What information from the underlying platform, e.g. configuration data, is exposed by this specification to an origin?

The 
system-ui
 keyword exposes the operating system’s default system UI font to fingerprinting mechanisms.

15.7. 
Does this specification allow an origin access to sensors on a user’s device

No.

15.8. 
What data does this specification expose to an origin? Please also document what data is identical to data exposed by other features, in the same or different contexts.

For third-party Web Fonts loaded via a stylesheet,
	the stylesheet origin may be exposed to the third party in the Referer header.
	In addition, careful pairing of unicode-range and distinct src urls
	allows the third-party to see which characters are used on a page,
	which is a privacy risk for large character repertoire scripts
	such as CJK.

For third-party Web Fonts preloaded in the HTML,
	the document origin may be similarly exposed.

15.9. 
Does this specification enable new script execution/loading mechanisms?

No.

Specifically, for SVG-in-OpenType color fonts,
	the SVG used for glyph definitions should not contain script elements,
	and any script elements that do occur will not be executed.

15.10. 
Does this specification allow an origin to access other devices?

No.

15.11. 
Does this specification allow an origin some measure of control over a user agent’s native UI?

There is some risk that an attacker can spoof a native UI feature
	by determining the Operating System
	and using native-looking fonts appropriate to that Operating System.

15.12. 
What temporary identifiers might this specification create or expose to the web?

None.

15.13. 
How does this specification distinguish between behavior in first-party and third-party contexts?

For font loads
, user agents must use the
	potentially CORS-enabled fetch method defined by the 
[HTML]
 specification
	for URLs defined within @font-face rules.
	When fetching, user agents must use "Anonymous" mode,
	set the referrer source to the stylesheet’s URL
	and set the origin to the URL of the containing document.

Thus, fonts will typically not be loaded cross-origin
	unless authors specifically take steps to permit cross-origin loads.

15.14. 
How does this specification work in the context of a user agent’s Private Browsing or "incognito" mode?

The specification makes no distinction.

Some user agents may expose a more restricted set of Installed Fonts in these modes.

15.15. 
Does this specification have a "Security Considerations" and "Privacy Considerations" section?

Yes.

15.16. 
Does this specification allow downgrading default security characteristics?

No.

15.17. 
What should this questionnaire have asked?

It should have asked whether a malicious payload could crash the application,
	or indeed the entire Operating System,
	or even cause remote code execution.

This possibility does exist for suitably crafted fonts
	on some platforms
	when fonts are installed and rendered,
	and this has been exploited in the wild.

In practice, user agents running on Operating Systems with this vulnerability
	use a font sanitizer to detect such malformed or malicious fonts
	and prevent their being used.

16. 

Accessibility Considerations

The use of fonts to provide a visual rendering of text should not, in general, impact accessibility.
	For example, people using a screen reader to render text to speech will not download fonts,
	and are unaffected by what those fonts would have contained.

However, this assumes that the semantics conveyed by the font glyphs
	and the semantics conveyed by the characters
	are the same.

Historically, this has not always been the case.
	For example, in the early days of the Web it was common to use fonts
	(such as "Symbol", though others were used)
	to make Latin letters have Greek glyphs;
	while this worked visually,
	it would not work with a screen reader
	and text was also hard to search or index
	because the mapping was font-specific.
	With the rise of Unicode, it is now standard practice to use Greek characters for Greek text,
	and for Greek glyphs in fonts to map to Greek characters.

Sadly, but avoidably, this practice persists
	with badly designed icon fonts.
	For example, such a font might put a "printer" icon on the Latin letter "P".
	This practice scatters meaningless letters through the text,
	which negatively affects text searching and indexing,
	gives hard to understand rendering if the icon font does not load,
	and impedes screen readers.
	A well designed font must assign such icons to semantically meaningful characters.
	For example, the printer icon might be assigned to the string "printer"
	or to the Unicode character 🖨 U+1F5A8 (PRINTER).

17. 

Acknowledgments

The CSS Working group would like to thank:

Peter Constable for assorted language fixes.

Optical sizing 
image
 prepared by Nick Sherman.

Urdu samples prepared by Richard Ishida.

Munira Tursunova and Dominik Röttsches developed the features for animating font-palette.

John Hudson was kind enough to take the time to explain the subtleties of OpenType language tags
	and provided the example of character variant usage for displaying text on Byzantine seals.

Elika Etemad supplied some of the initial design ideas for the '@font-feature-values' rule.

Special thanks to Tab Atkins Jr.
	for providing the text for the section on 
Font Rendering Controls

	as well as the section on the 
font-display
 descriptor.
	Special thanks to Ilya Grigorik and David Kuettel for their help in developing these sections.

18. 

Changes

18.1. 

Changes from the 
1 February 2024 working draft

Normatively stated the dependency on palt for kerning
			(
Issue 6723
)

Clarified that kerning applies to proportionally-spaced glyphs only. 
			Removed inaccurate claim that OpenType encourages that 
			kerning be on by default.
			(
Issue 6723
)

Updated palette-mix() to match color-mix() in taking a list of one or more items, rather than being restricted to exactly two
			(
Issue 14452
)

Added font-synthesis-position to the list of font-* properties which cascade independently
			(
Issue 14397
)

Clarified the suitability of system-ui
			(
PR 14326
)

Defined 'font-affecting properties', and listed which properties are in that category
			(
Issue 14306
)

Clarified range constraints on descriptor values in 
<font-feature-value-type>

			(
Issue 13324
)

Added font- prefix to production names to avoid ambiguity
			(
Issue 13263
, 

PR 13272
)

Created proper types for <absolute-size> and <relative-size>
			(
Issue 1794
)

Defined that if there are multiple @font-palette-values rules, the last one wins
			(
Issue 12981
)

Clarified that clamping to the variable range also affects implied variation axes
			(
Issue 7999
)

Add some more clarifications on the other ui-* generic font families
			(
Issue 3658
)

Add notes for the system-ui generic font family
			(
PR 12831
),
			(
Issue 3658
)

Cleaned up fetching of font resources
			(
Issue 12261
)

Clarify that non-absolute colors in override-colors 
			make the whole descriptor invalid, 
			not just the individual color
			(
Issue 9555
)

Add left and right to font-style descriptor
			(
Issue 9392
)

Add left and right to font-style property
			(
Issue 9392
)

Added oblique-only as a value of font-synthesis-style
			(
Issue 9390
)

Refered to Cascade 5 for reset-only sub-property, 
			rather than defining it independently
			(
Issue 11904
)

Clarified that override-colors are invalid if an absolute color is not specified
			(
Issue 9555
)

Fixed typo in Font Feature and Variation Resolution

Used better fonts for the Khmer example

Added generic(khmer-mul)

Used unicode-range-token instead of urange

Clarified requirement for user addition/removal of fonts

Made CSSFontFaceRule.style consistent with other CSS*Rule.style

Fixed 
font
 syntax, simplified font-variant-css2 and font-width-css3 syntaxes

Restored monospace as generic font family (it had been accidentally deleted)

Corrected syntax of generic-family

Improved wording on PostScript names as fragment identifiers for font collections

Added missing @font-face descriptors

Used different interfaces for declarations blocks that expose a different set of descriptors or properties

Updated incremental font example to latest IFT specification

Defined CSSFontFeatureValuesRule.historicalForms

18.2. 

Changes from the 
21 December 2021 Working Draft

Corrected some broken links

In font matching algorithm, distinguished use of varfont slnt axis from synthetic obliquing

 Clarified that font variations do not count as font synthesis

Clarified the effect of auto values on @font-face is to select the appropriate "normal" value

Improved font fallback on font-variant-emoji with variation selectors

Clarified that the oblique angle must be the same sign as requested

Defined synthetic oblique in vertical text

Used CSS Color 5 absolute color definition for override-colors

Made font-stretch a legacy name alias for font-width

The palette-mix() grammar requires color-interpolation-method, so removed leftover prose defining what to do if it is omitted

Add more generics samples, for fang song and kai

Listed fonts used for Urdu samples

Users must be able to modify the set of installed fonts available for rendering web pages

Added examples of Urdu text in nastaliq and in fallback naskh fonts

Clarified that keywords inside local() are an error

Clarified that the system-ui generic font family may be composite, and is affected by unicode coverage and content language

Removed culturally specific claims that particular typographic styles universally convey concepts such as formality or playfulness

Added a new generic(nastaliq) family, for Urdu, Persian, and other languages

Added a new generic(kai) family, for Simplified and Traditional Chinese

No longer claim that cursive and kaiti have identical meanings

Added a note on the historical reasons for the serif and sans-serif generic font families

Dropped the emoji generic font-family, because the font-variant-emoji property covers the desired functionality better

Added Internet Media Types to the table of font formats

Moved the consequences of installed fonts out of Taxonomy and into Font Matching Algorithm

Clarified that the font-family and src descriptors are no longer required for validity, as they can be added later by script.

Consistently use generic(fangsong) instead of fangsong, as the generic font family name. Note that it is script-specific

Defined a third type of font family name, <system-family-name> which has some constraints on how it can be specified

Added a missing at-keword in the production of @font-feature-values

Refactored the @font-feature-values grammar

Restored some acknowlegements which had been dropped when porting CSS Fonts 3 into this specification

Redefined the grammar of the src attribute to use a <font-src-list> production, rather than "see prose"

Deleted broken link to an informative reference which no longer exists

Described three classes of generic font families, including whether they are writing system (script) specific and whether they are always required to match to a locally installed font

Added a new functional notation, generic(), for new generic font families

Added a clarifying note about platform API limitations which might restrict color font rendering to sRGB

Removed leftover, no-longer applicable mention of "forcing colored glyphs not to be used"

Refined the font-palette computed value

Added an example of Nabla font with an animated palette

Described modified font-palette syntax and rules for interpolation
			and percentage normalization, referencing the CSS Color specification

Clarified that the used color-scheme affects font-palette: normal

Added missing numeric range annotations for slope angle and font-feature-settings integer

Defined a production for <family-name> 

For locally installed fonts, used local(<family-name>) 

Fixed ambiguous descriptor auto-links 

Fixed markup of the <family-name> production 

Defined feature and variation names with <opentype-tag> rather than bare strings

Clarified that general math functions (not just calc) are allowed in @font-palette-values descriptors

Added the 
font-synthesis-position
 property 

Added an example of a non-sRGB color in override-colors

Use rule-list rather than stylesheet in productions

Added URL request modifiers for crossorigin, referrerpolicy & integrity

Aligned the incremental tech keywords to match the latest Incremental Font Transfer specification

Use last-defined value for font-feature-values

font-feature-values and font-feature-settings are now de-duplicated, and sorted

Suggested user agents prompt users to make certain user-installed fonts available, or unavailable

Improved the Privacy Considerations, balancing privacy and legibility trade-offs for user-installed fonts

Clarified the font shorthand, using the terms set explicitly, reset implicitly and cascade implicitly

Clarified shorter representation for zero ranged descriptors

Tightened definition of first available font

Added emoji as a keyword to unicode-range

Allowed implementations to ignore requests to turn off font features which the OpenType specification says are always required

Gave clearer advice to authors about font-feature-settings and font-variation-settings 

Readability improvements to the grammar for font-variant sub-properties

Corrections to some examples so they again match the specification

Clarified what it means to ignore an invalid font-family descriptor 

Allowed the font-family descriptor of @font-palette-values to take a list

Added Web Platform Tests coverage

font-palette
 and '@font-palette-values' no longer at risk

Allowed limited set of string-form format specifies, for Web compatibility

Make feature-* features-* for consistency

Changed initial value of font-variant-emoji from auto to normal, for consistency with other font-variant-* properties

Added values from font-variant-emoji to font-variant shorthand

Added canonical list of font-variant-* properties affected by font-variant shorthand

Renamed "system font fallback" to "installed font fallback to avoid confusion with system font

Updated property and descriptor values to use the range notation

Fixed some examples which did not match the specification

Clarified that color fonts are not enabled by default

Added some more explanation to font-palette:light|dark

Use last declaration of key/palette index in override-colors

Removed currentColor from override-colors example

Clarified that out of range palette indexes are ignored

Assorted typo corrections and markup fixes

18.3. 

Changes from the 
29 July 2021 Working Draft

Clarified that functions and relative lengths in palettes are evaluated
			within the root element’s context

Added new section, overall changes since CSS Fonts 3

Added more font-palette-values examples

Renamed technology to tech

New 
math
 value added to 
font-size

Security and Privacy are now separate sections

Linked to OpenType, TrueType and Graphite table definitions

Updated examples which had used "supports"

Removed old "supports" from format in src descriptor, replaced with new technology production

Moved font-technology & font-format to a new section 

Formalized fetching and resource timing reporting, applied to fetching fonts

Removed the <string> values from override-color and base-palette

Defined correct processing of conflicting override-colors

Introduced concept of complete palettes

Clearer description of override-colors

Removed conflict between FONT_PALETTE_VALUES_RULE and VIEWPORT_RULE

Defined context for resolving override-color colors, no longer per-element

Allowed base-palette to reference dark and light palettes

Changed properties in CSSFontPaletteValuesRule to be read-only

The palette-identifier parses as a dashed-ident rather than custom-ident, for extensibility

Renamed override-color descriptor to override-colors, because it accepts a list of colors

Clarified that base-palette and override-color take non-negative integers

Corrected grammar of the font shorthand property

Several corrections to the IDL for CSSFontPaletteValuesRule

Removed the "none" value from font-palette 

Clarified incremental requirement

A few more examples

Added incremental font technology to supports

Reduced the critical angle for oblique font matching from 20deg to 11deg, per WG resolution

Allowed font-display in @font-feature-values (the prose allowed it but the grammar did not)

18.4. 

Changes from the 
17 November 2020 Working Draft

Added Graphite reference

Added font feature technology keywords opentype, aat, and graphite

Removed scary wording about variable fonts being new and experimental

Reference to CSS Fonts 3 in introduction is informative

Differentiated COLRv1 from COLRv0

Clarify well-designed vs badly-designed icon fonts in terms of Unicode codepoints

Added Accessibility Considerations section

Clarified that font-optical-sizing interacts with font-size-adjust

Used consistent capitalization for "user agent"

Clarified that font-stretch should serialize to a number/percentage, not a keyword

Suggested heuristics for loading 
optional
 fonts

Clarified repeated items in grammars

Replaced obsolete “potentially CORS-enabled fetch” with reference to Fetch

Added missing small-caps value to font-synthesis

Be explicit about which properties apply to text

Updated links

Fixed typos, syntax errors

18.5. 

Changes from the 
13 November 2019 Working Draft

Clarified that JS-free probing of Unicode support of fonts is possible

Clarified OpenType feature tags are 4 characters, trailing-space padded

Added font metric override descriptors

Added link to font features enabled by default

Aligned with ebIDL specification (undefined, not void)

Corrected cross-origin example to use http not https

Clarified that font-range, per OpenType, is between 1 and 999

(Privacy) added mention of unicode-range privacy exploit

Clarified use of kern vs. vkrn

Added font collection format, example of Font Collection

Added CBDT color fonts

Added Security & Privacy appendix

Added palette examples, including dark mode

Clarified colorspace of font palette entries

Avoiding cross-site font leakage amde RFC-2119 MUST

Clarified monochromatic fallback on color fonts

Removed remaining references to min-font-size, max-font-size

Clarified that color names are ASCII case insensitive

Added the value none to font-palette

Marked font-palette and @font-palette-values as at-risk

Aligned value definition reference across all specs.

Further clarified the behavior of 
optional

Clarified that not all generic font families have to map to a font

Reorganized generic font family introduction

Added some motivation for generic font families

Added a note about the generic emoji family and character support

Clarified that italic is not a fallback for oblique 

Added warning on too large x-height

Added better example for 
font-size-adjust

Added example for ui-sans-serif 

Miscellaneous editorial improvements, typo fixes, broken link fixes and markup improvements

18.6. 

Changes from the 
20 September 2018 Working Draft

Add note encouraging UAs to also implement platform-specific names for standard font families

Add ui-serif, ui-sans-serif, ui-monospace, and ui-rounded generic font families

Remove font-variant @font-face descriptor per WG resolution

Remove font-min-size and font-max-size per WG resolution

Clarify that font-style 
normal
 animates as 
oblique 0deg

Clarify why specifying incomplete color palettes for compound fonts is a bad idea

Add explicit [Exposed=Window] on interfaces

Use correct terms, Unicode emoji presentation sequence and Emoji Presentation Participating Code Points

Clarify that each string in font-variation-settings is paired with a single number

Remove stray titling-caps from definition of font-variant-numeric property

Better introduction to color fonts

Add basic multicolor example

Clarify that font variation settings do no affect font selection of fallback fonts

Clarify italic angle wrt direction of slnt axis

Better define emoji and math generic font families

Add font-size: xxx-large 

Link to CSS Values definition of ex units

Add scientific inferiors example of font-feature-settings

Clarify that letter-spacing disables optional ligatures

Port font-feature-settings property from CSS Fonts 3

Port font-variant shorthand property from CSS Fonts 3

Port font-variant-east-asian property from CSS Fonts 3

Port font-variant-numeric property from CSS Fonts 3

Port font-variant-caps property from CSS Fonts 3

Port font-variant-position property from CSS Fonts 3

Port font-variant-ligatures property from CSS Fonts 3

Port font-kerning property from CSS Fonts 3

Update IDL of The CSSFontPaletteValuesRule interface

Changed initial value of font property descriptors from normal to auto

Update syntax for font-stretch in font matching section

Update font style matching examples 

Clarify description of font palettes

Stop claiming that 
ch
 uses the first available font

Assorted formatting and markup fixes, link fixes, removal of inline closed issues

Linking to latest versions of normative references

18.7. 

Changes from the 
10 April 2018 Working Draft

Added unicode value to font-variant-emoji

Removed the media entry from property descriptions

Broke up font-synthesis into longhands, for future extensibility

Added override-color descriptor for color palettes

Defined feature-value-name for font-variant-alternates 

Clarified @font-face src parsing rules

Allow named instances from variable fonts to be used 

Appendix A: Mapping platform font properties to CSS properties ported over from CSS Fonts 3

Character handling issues ported over from CSS Fonts 3

Cluster matching ported over from CSS Fonts 3

Add new auto value for font-weight, font-style and font-stretch descriptors

Clarified font-display descriptor value names

Support named palette entries

More details on Fang Song generic family

Changed default angle of oblique fonts to 14deg.

font-feature-values ported over from CSS Fonts 3

Clarified handling of unknown or unsupported fragment identifiers

Clarified that color records in font palettes are zero-indexed

Consistently use the new generic font families

Editorial cleanup, clarifying examples, markup improvements, linkfixes,
			updating to latest references, and so on

18.8. 

Changes from the 20 September 2018 
CSS Fonts 3 Recommendation

This summarizes the changes in CSS Fonts 4, compared to CSS Fonts 3.

Added font-display descriptor for @font-face

Added @font-feature-values rule

Added font variation properties, including font-optical-sizing and font-variation-settings

Added color font support

Defined feature-value-name for font-variant-alternates

Added new auto value for font-weight, font-style and font-stretch descriptors

Added ui-serif, ui-sans-serif, ui-monospace, and ui-rounded generic font families

Added font-size: xxx-large

Added font metric override descriptors

Added some motivation for generic font families

Added font feature technology keywords opentype, aat, and graphite

Added math value to font-size


