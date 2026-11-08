"""Build the fill-in workbook for the 2026-11-08 eBay batch: one row per garment, measurements across the columns.

    python tools/ebay-batch-workbook.py OUT.xlsx [OUT2.xlsx ...]

Estimates are formulas over pixel readings (sheet Pixels) and the calibration inputs (sheet Inputs).
"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

OUT = sys.argv[1:]
F = 'Arial'
font = Font(name=F, size=10); bold = Font(name=F, size=10, bold=True); blue = Font(name=F, size=10, color='0000FF')
head = Font(name=F, size=10, bold=True, color='FFFFFF'); headfill = PatternFill('solid', fgColor='333333')
yellow = PatternFill('solid', fgColor='FFFF99'); grey = PatternFill('solid', fgColor='EEEEEE'); band = PatternFill('solid', fgColor='F7F3EA')
thin = Side(style='thin', color='BBBBBB'); box = Border(top=thin, bottom=thin, left=thin, right=thin)
wrap = Alignment(wrap_text=True, vertical='top')

wb = Workbook()

# ---------------- Inputs ----------------
wi = wb.active; wi.title = 'Inputs'
wi['A1'] = 'Calibration inputs (blue = you can change; every estimate recalculates)'; wi['A1'].font = bold
rows = [
    ('black', 17.5, 'Black velvet hanger, tip to tip, inches. ASSUMED standard width. Measure yours and overwrite.'),
    ('grey', 16.5, 'Grey velvet clip hanger, tip to tip, inches. Derived from the photos (it is 0.94 of the black hanger). Measure and overwrite.'),
    ('hinge', 10.0, 'Jeep rear door: top of the upper hinge to top of the lower hinge, inches. Derived from the hanger in the slip-dress and jeans photos. One tape measurement here fixes items 1, 3 and 6.'),
    ('window', 17.0, 'Jeep rear door window opening height, glass top to glass bottom, inches. Derived (1.7 x the hinge span). Used only for the blouse, which had no hanger or hinge in frame.'),
    ('tolerance', 0.05, 'Spread shown as the low/high range. 5 percent is the reading noise of this method.'),
]
wi.append(['Reference', 'Inches', 'What it is'])
for c in 'ABC': wi[f'{c}2'].font = head; wi[f'{c}2'].fill = headfill
for i, (k, v, note) in enumerate(rows, start=3):
    wi[f'A{i}'] = k; wi[f'B{i}'] = v; wi[f'C{i}'] = note
    wi[f'A{i}'].font = font; wi[f'B{i}'].font = blue; wi[f'B{i}'].fill = yellow; wi[f'C{i}'].font = font; wi[f'C{i}'].alignment = wrap
wi['A9'] = 'How the estimates work'; wi['A9'].font = bold
wi['A10'] = ('Every photo was masked and the garment measured in pixels (sheet Pixels). Each photo has one reference object of known size in the same plane as the garment: '
             'the hanger where it is fully visible, otherwise the door hinges, otherwise the window. Inches = pixels / (reference pixels / reference inches). '
             'No published Jeep spec gives the hinge spacing, so the hinge and window sizes above are inferred from the hanger; a tape on the Jeep replaces the inference. '
             'Widths of hanging dresses (bust, hip, sweep) are NOT estimated: fabric bunches on a hanger, so only the tape gives those.')
wi['A10'].alignment = wrap; wi['A10'].font = font; wi.merge_cells('A10:C14')
wi.column_dimensions['A'].width = 12; wi.column_dimensions['B'].width = 10; wi.column_dimensions['C'].width = 110

# ---------------- Pixels ----------------
wp = wb.create_sheet('Pixels')
wp.append(['Photo', 'Item', 'Measure', 'Garment px', 'Reference', 'Reference px', 'px per inch', 'Inches'])
for c in range(1, 9): wp.cell(1, c).font = head; wp.cell(1, c).fill = headfill
px = [
    ('IMG_2298', 1, 'Length, collar base to hem (front)', 938, 'hinge', 215),
    ('IMG_2302', 1, 'Length, collar base to hem (back)', 952, 'hinge', 210),
    ('IMG_2298', 1, 'Sleeve, shoulder to cuff (short)', 225, 'hinge', 215),
    ('IMG_2312', 2, 'Length, top edge to hem (front)', 730, 'black', 400),
    ('IMG_2313', 2, 'Length, top edge to hem (back)', 707, 'black', 377),
    ('IMG_2312', 2, 'Strap, hanger to top edge, as tied', 185, 'black', 400),
    ('IMG_2315', 3, 'Length, shoulder to hem point (front)', 927, 'hinge', 205),
    ('IMG_2318', 3, 'Length, shoulder to hem point (back)', 995, 'hinge', 210),
    ('IMG_2315', 3, 'Sleeve, shoulder to cuff (front)', 490, 'hinge', 205),
    ('IMG_2318', 3, 'Sleeve, shoulder to cuff (back)', 520, 'hinge', 210),
    ('IMG_2335', 4, 'Waist flat (front)', 650, 'grey', 667),
    ('IMG_2337', 4, 'Waist flat (back)', 574, 'grey', 603),
    ('IMG_2335', 4, 'Outseam, waist top to hem (front)', 650, 'grey', 667),
    ('IMG_2337', 4, 'Outseam, waist top to hem (back)', 590, 'grey', 603),
    ('IMG_2335', 4, 'Front rise, waist top to crotch', 335, 'grey', 667),
    ('IMG_2335', 4, 'Inseam, crotch to hem', 350, 'grey', 667),
    ('IMG_2335', 4, 'Leg opening flat, one leg (front)', 419, 'grey', 667),
    ('IMG_2337', 4, 'Leg opening flat, one leg (back)', 372, 'grey', 603),
    ('IMG_2342', 5, 'Length, collar base to centre front hem', 765, 'window', 540),
    ('IMG_2343', 5, 'Length, collar base to centre back hem', 845, 'window', 530),
    ('IMG_2342', 5, 'Sleeve, shoulder to cuff', 740, 'window', 540),
    ('IMG_2345', 6, 'Length, shoulder to hem (front)', 950, 'hinge', 225),
    ('IMG_2346', 6, 'Length, shoulder to hem (back)', 895, 'hinge', 218),
    ('IMG_2345', 6, 'Sleeve, shoulder to cuff (front)', 555, 'hinge', 225),
    ('IMG_2346', 6, 'Sleeve, shoulder to cuff (back)', 525, 'hinge', 218),
    ('IMG_2345', 6, 'Elastic waist flat, relaxed (front)', 319, 'hinge', 225),
    ('IMG_2346', 6, 'Elastic waist flat, relaxed (back)', 275, 'hinge', 218),
    ('IMG_2349', 7, 'Waist flat (front)', 342, 'grey', 365),
    ('IMG_2350', 7, 'Waist flat (back)', 356, 'grey', 367),
    ('IMG_2349', 7, 'Front rise, waist top to crotch', 265, 'grey', 365),
    ('IMG_2349', 7, 'Outseam, waist top to hem (front)', 780, 'grey', 365),
    ('IMG_2350', 7, 'Outseam, waist top to hem (back)', 805, 'grey', 367),
    ('IMG_2349', 7, 'Inseam, crotch to hem', 515, 'grey', 365),
    ('IMG_2350', 7, 'Leg opening flat, one leg (back)', 224, 'grey', 367),
    ('IMG_2291', 8, 'Length, collar base to hem (front)', 745, 'window', 580),
    ('IMG_2293', 8, 'Length, collar base to hem (back)', 765, 'window', 575),
    ('IMG_2291', 8, 'Sleeve, shoulder to cuff', 800, 'window', 580),
    ('IMG_2304', 10, 'Length, collar base to hem (front)', 975, 'hinge', 215),
    ('IMG_2306', 10, 'Length, collar base to hem (back)', 960, 'hinge', 220),
    ('IMG_2304', 10, 'Sleeve (front)', 490, 'hinge', 215),
    ('IMG_2306', 10, 'Sleeve (back)', 480, 'hinge', 220),
    ('IMG_2309', 11, 'Length, collar base to hem', 830, 'window', 545),
    ('IMG_2309', 11, 'Sleeve, shoulder to cuff', 860, 'window', 545),
    ('IMG_2321', 12, 'Length, shoulder to hem', 810, 'window', 390),
    ('IMG_2321', 12, 'Sleeve', 535, 'window', 390),
    ('IMG_2325', 13, 'Length, collar base to centre front hem', 760, 'window', 510),
    ('IMG_2328', 13, 'Length, collar base to centre back hem', 805, 'window', 525),
    ('IMG_2325', 13, 'Sleeve (front)', 740, 'window', 510),
    ('IMG_2328', 13, 'Sleeve (back)', 790, 'window', 525),
    ('IMG_2330', 14, 'Length, shoulder to hem (front)', 940, 'hinge', 210),
    ('IMG_2333', 14, 'Length, shoulder to hem (back)', 975, 'hinge', 230),
    ('IMG_2330', 14, 'Sleeve (front)', 535, 'hinge', 210),
    ('IMG_2333', 14, 'Sleeve (back)', 630, 'hinge', 230),
    ('IMG_2340', 15, 'Waist flat (front)', 285, 'grey', 386),
    ('IMG_2341', 15, 'Waist flat (back)', 245, 'grey', 334),
    ('IMG_2340', 15, 'Outseam (front)', 905, 'grey', 386),
    ('IMG_2341', 15, 'Outseam (back)', 840, 'grey', 334),
    ('IMG_2340', 15, 'Front rise', 355, 'grey', 386),
    ('IMG_2340', 15, 'Inseam (front)', 550, 'grey', 386),
    ('IMG_2341', 15, 'Inseam (back)', 520, 'grey', 334),
    ('IMG_2340', 15, 'Leg opening flat, one leg', 128, 'grey', 386),
    ('IMG_2360', 17, 'Length, collar base to hem (front)', 905, 'hinge', 220),
    ('IMG_2362', 17, 'Length, collar base to hem (back)', 885, 'hinge', 205),
    ('IMG_2360', 17, 'Sleeve (front)', 557, 'hinge', 220),
    ('IMG_2362', 17, 'Sleeve (back)', 530, 'hinge', 205),
    ('IMG_2360', 17, 'Elastic waist flat, relaxed', 259, 'hinge', 220),
    ('IMG_2364', 18, 'Total length, collar base to hem (front)', 980, 'hinge', 203),
    ('IMG_2367', 18, 'Total length, collar base to hem (back)', 1025, 'hinge', 200),
    ('IMG_2364', 18, 'Waist flat at the seam (front)', 254, 'hinge', 203),
    ('IMG_2367', 18, 'Waist flat at the seam (back)', 272, 'hinge', 200),
    ('IMG_2370', 19, 'Length, collar base to centre front hem', 835, 'window', 470),
    ('IMG_2373', 19, 'Length, collar base to centre back hem', 950, 'window', 490),
    ('IMG_2370', 19, 'Sleeve, shoulder to hem (short)', 370, 'window', 470),
    ('IMG_2375', 20, 'Length, waist top to hem (front)', 780, 'grey', 482),
    ('IMG_2377', 20, 'Length, waist top to hem (back)', 740, 'grey', 474),
    ('IMG_2375', 20, 'Elastic waist flat, relaxed (front)', 410, 'grey', 482),
    ('IMG_2377', 20, 'Elastic waist flat, relaxed (back)', 405, 'grey', 474),
    ('IMG_2377', 20, 'Hip flat, widest', 486, 'grey', 474),
]
ref_in = {'black': 17.5, 'grey': 16.5, 'hinge': 10.0, 'window': 17.0}
cell = {}  # (item, key) -> Pixels inch cell
for i, (photo, item, meas, g, ref, rpx) in enumerate(px, start=2):
    wp.append([photo, item, meas, g, ref, rpx])
    wp[f'G{i}'] = f'=F{i}/INDEX(Inputs!$B$3:$B$6,MATCH(E{i},Inputs!$A$3:$A$6,0))'
    wp[f'H{i}'] = f'=D{i}/G{i}'
    wp[f'G{i}'].number_format = '0.00'; wp[f'H{i}'].number_format = '0.0'
    for c in range(1, 9): wp.cell(i, c).font = font
    cell[(item, meas)] = f'Pixels!$H${i}'
    px[i - 2] = px[i - 2] + (g / (rpx / ref_in[ref]),)  # python check value
wp[f'A{len(px) + 3}'] = 'Pixels read on 1200 px previews of the HEICs. Hinge = top of upper hinge to top of lower hinge. Hanger = tip to tip.'; wp[f'A{len(px) + 3}'].font = font
for col, w in zip('ABCDEFGH', (11, 6, 40, 11, 10, 12, 11, 9)): wp.column_dimensions[col].width = w

def est(item, *names):
    refs = [cell[(item, n)] for n in names]
    return f'=ROUND({refs[0]},1)' if len(refs) == 1 else f'=ROUND(AVERAGE({",".join(refs)}),1)'

# ---------------- To fill in ----------------
ws = wb.create_sheet('To fill in', 0)
COLS = ['Item', 'Garment', 'Length', 'Pit to pit', 'Shoulder to shoulder', 'Sleeve', 'Waist flat', 'Hip flat', 'Front rise', 'Inseam', 'Outseam',
        'Leg opening', 'Fabric (care label)', 'Other questions', 'Flaws', 'Sold comps (3 recent eBay sold)', 'List price', 'Status / eBay URL', 'Notes from the photos']
MEASURE = COLS[2:12]
ws.append(COLS)
for c in range(1, len(COLS) + 1): ws.cell(1, c).font = head; ws.cell(1, c).fill = headfill; ws.cell(1, c).alignment = Alignment(wrap_text=True, vertical='center')
ws.freeze_panes = 'C2'
items = {
    1: 'Liz Claiborne leopard shirt dress, size 8',
    2: 'Future Collective floral slip dress, size S',
    3: 'Ronny Kobo rose jacquard plunge dress, size XS',
    4: 'Brooks Brothers white chino shorts, size 10',
    5: 'The Limited green blouse, size S',
    6: 'Starlo vintage red pleated dress, no size tag',
    7: 'We The Free wide-leg jeans, size 29',
    8: 'Free People mixed print blouse, size S',
    10: 'Lew Magram black jersey faux-wrap maxi dress, size 8',
    11: 'adidas SAMPLE grey satin track jacket, size S',
    12: 'Connie Rizza orange floral jersey dress, no size',
    13: 'Jones New York ivory flap-pocket blouse, size 8',
    14: 'Ghost London geometric plunge midi dress, XXS',
    15: 'White coral-print high-waist trousers, brand unknown',
    16: 'Denim & Flower Ricky Singh cream bomber, size L (ink marks)',
    17: 'Neiman Marcus navy silk shirt dress, size 12',
    18: 'Zara cream utility jumpsuit, size S',
    19: "Columbia PFG vented fishing shirt, men's L",
    20: 'Bonnie & Norma paisley elastic-waist midi skirt, size 12',
}
# (item, need, estimate formula or None, note)
L = est
plan = [
    (1, 'Length, back collar seam to hem', L(1, 'Length, collar base to hem (front)', 'Length, collar base to hem (back)'), 'Average of front and back photos.'),
    (1, 'Pit to pit, flat', None, 'Cannot be read from a hanging photo (sleeves overlap).'),
    (1, 'Shoulder seam to shoulder seam', None, ''),
    (1, 'Sleeve, shoulder seam to cuff', L(1, 'Sleeve, shoulder to cuff (short)'), 'Short sleeve.'),
    (1, 'Waist flat, relaxed and stretched (elastic)', None, 'Write both, e.g. 13 / 17.'),
    (1, 'Flaws: stains, pulls, missing buttons, odour', None, 'Photograph each flaw in the same light.'),
    (2, 'Length, top edge to hem', L(2, 'Length, top edge to hem (front)', 'Length, top edge to hem (back)'), 'Average of front and back.'),
    (2, 'Strap length as tied (hanger to top edge)', L(2, 'Strap, hanger to top edge, as tied'), 'Adjustable ties; also note the max.'),
    (2, 'Across the top edge, flat', None, 'Hangs gathered, tape only.'),
    (2, 'Waist flat / hip flat', None, ''),
    (2, 'Slit length', None, 'Front slit, looked about 3 in.'),
    (2, 'Fabric (care label)', None, 'Not in the tag photo.'),
    (2, 'Lined? Closure (side zip or pullover)?', None, ''),
    (2, 'Flaws', None, ''),
    (3, 'Length, shoulder to hem point, front', L(3, 'Length, shoulder to hem point (front)'), 'Fishtail hem, measure to the longest point.'),
    (3, 'Length, shoulder to hem point, back', L(3, 'Length, shoulder to hem point (back)'), ''),
    (3, 'Sleeve, shoulder seam to cuff', L(3, 'Sleeve, shoulder to cuff (front)', 'Sleeve, shoulder to cuff (back)'), ''),
    (3, 'Pit to pit, flat', None, ''),
    (3, 'Waist flat / hip flat', None, 'Fitted cut: buyers will ask.'),
    (3, 'Depth of the V from shoulder', None, ''),
    (3, 'Fabric (care label)', None, 'Not in the tag photo; looks like viscose or silk blend jacquard.'),
    (3, 'Closure: back neck button, zip?', None, ''),
    (3, 'Flaws', None, ''),
    (4, 'Waist flat', L(4, 'Waist flat (front)', 'Waist flat (back)'), 'x2 for the waist size.'),
    (4, 'Outseam, waist top to hem', L(4, 'Outseam, waist top to hem (front)', 'Outseam, waist top to hem (back)'), ''),
    (4, 'Front rise, waist top to crotch seam', L(4, 'Front rise, waist top to crotch'), 'Crotch point read by eye: rough.'),
    (4, 'Inseam', L(4, 'Inseam, crotch to hem'), 'Rough, same reason.'),
    (4, 'Leg opening flat, one leg', L(4, 'Leg opening flat, one leg (front)', 'Leg opening flat, one leg (back)'), ''),
    (4, 'Hip flat', None, ''),
    (4, 'Colour: white or ivory?', None, 'Check in daylight against paper.'),
    (4, 'Flaws (white: look hard)', None, ''),
    (5, 'Length, collar base to centre front hem', L(5, 'Length, collar base to centre front hem'), 'ROUGH: no hanger or hinge in frame, scaled from the window.'),
    (5, 'Length, collar base to centre back hem', L(5, 'Length, collar base to centre back hem'), 'ROUGH, same reason.'),
    (5, 'Sleeve, shoulder seam to cuff', L(5, 'Sleeve, shoulder to cuff'), 'ROUGH.'),
    (5, 'Pit to pit, flat', None, ''),
    (5, 'Shoulder seam to shoulder seam', None, ''),
    (5, 'Fabric (care label)', None, 'Not in the tag photo; probably polyester.'),
    (5, 'Flaws', None, ''),
    (6, 'Length, shoulder to hem', L(6, 'Length, shoulder to hem (front)', 'Length, shoulder to hem (back)'), 'Pleated hem is ragged in the mask; average of front and back.'),
    (6, 'Sleeve, shoulder seam to cuff', L(6, 'Sleeve, shoulder to cuff (front)', 'Sleeve, shoulder to cuff (back)'), ''),
    (6, 'Elastic waist flat, relaxed', L(6, 'Elastic waist flat, relaxed (front)', 'Elastic waist flat, relaxed (back)'), 'x2 for the relaxed waist. Also tape it stretched.'),
    (6, 'Elastic waist flat, stretched', None, ''),
    (6, 'Pit to pit, flat', None, ''),
    (6, 'Size tag? (look at the side seam)', None, 'Starlo label has no size. If none, list by measurements.'),
    (6, 'Fabric (care label), lined?', None, 'Sheer-ish georgette; say whether lined.'),
    (6, 'Flaws', None, ''),
    (7, 'Waist flat', L(7, 'Waist flat (front)', 'Waist flat (back)'), 'x2 for the waist size.'),
    (7, 'Front rise, waist top to crotch seam', L(7, 'Front rise, waist top to crotch'), 'Reads as high rise.'),
    (7, 'Outseam, waist top to hem', L(7, 'Outseam, waist top to hem (front)', 'Outseam, waist top to hem (back)'), ''),
    (7, 'Inseam', L(7, 'Inseam, crotch to hem'), 'Reads as a CROPPED length (about 23 to 24 in). Confirm: it changes the title.'),
    (7, 'Leg opening flat, one leg', L(7, 'Leg opening flat, one leg (back)'), 'x2 for the opening. About 20 in around.'),
    (7, 'Hip flat', None, ''),
    (7, 'Fabric and stretch % (inside label), style name', None, 'Photograph the inside waistband label.'),
    (7, 'Fly: button or zip?', None, ''),
    (7, 'Flaws', None, ''),
    (8, 'Length, collar base to hem', L(8, 'Length, collar base to hem (front)', 'Length, collar base to hem (back)'), 'ROUGH: window-scaled.'),
    (8, 'Sleeve, shoulder seam to cuff', L(8, 'Sleeve, shoulder to cuff'), 'ROUGH.'),
    (8, 'Pit to pit / shoulder to shoulder', None, ''),
    (8, 'Fabric (care label)', None, ''),
    (8, 'Flaws', None, ''),
    (10, 'Length, collar base to hem', L(10, 'Length, collar base to hem (front)', 'Length, collar base to hem (back)'), 'Hinge-scaled, front and back agree.'),
    (10, 'Sleeve, shoulder seam to cuff', L(10, 'Sleeve (front)', 'Sleeve (back)'), ''),
    (10, 'Pit to pit / waist / hip', None, ''),
    (10, 'Satin collar and cuffs: yellowing?', None, ''),
    (10, 'Flaws', None, ''),
    (11, 'Length, collar base to hem', L(11, 'Length, collar base to hem'), 'ROUGH: window-scaled; the back photo gave no usable scale.'),
    (11, 'Sleeve, shoulder seam to cuff', L(11, 'Sleeve, shoulder to cuff'), 'ROUGH; reads long, tape it.'),
    (11, 'Pit to pit / shoulder to shoulder', None, ''),
    (11, 'Shell and lining fabric (care label)', None, ''),
    (11, 'Flaws', None, ''),
    (12, 'Length, shoulder to hem', L(12, 'Length, shoulder to hem'), 'ROUGH: front photo only.'),
    (12, 'Sleeve, shoulder seam to cuff', L(12, 'Sleeve'), 'ROUGH.'),
    (12, 'Pit to pit / waist / hip', None, 'No size on the label: these decide the listed size.'),
    (12, 'Any care or size tag at the side seam?', None, ''),
    (12, 'Flaws', None, ''),
    (13, 'Length, collar base to hem', L(13, 'Length, collar base to centre front hem', 'Length, collar base to centre back hem'), 'ROUGH: window-scaled.'),
    (13, 'Sleeve, shoulder seam to cuff', L(13, 'Sleeve (front)', 'Sleeve (back)'), 'ROUGH.'),
    (13, 'Pit to pit / shoulder to shoulder', None, ''),
    (13, 'Flaws (ivory: collar, underarms)', None, ''),
    (14, 'Length, shoulder to hem', L(14, 'Length, shoulder to hem (front)', 'Length, shoulder to hem (back)'), 'Hinge-scaled.'),
    (14, 'Sleeve, shoulder seam to cuff', L(14, 'Sleeve (front)', 'Sleeve (back)'), ''),
    (14, 'Pit to pit / waist / hip', None, ''),
    (14, 'Fabric (care label)', None, ''),
    (14, 'Flaws', None, ''),
    (15, 'Brand and size (no tag photo)', None, 'Photograph the labels; the title is waiting on this.'),
    (15, 'Waist flat', L(15, 'Waist flat (front)', 'Waist flat (back)'), 'x2 for the waist; reads tiny (about 24 in).'),
    (15, 'Outseam, waist top to hem', L(15, 'Outseam (front)', 'Outseam (back)'), ''),
    (15, 'Front rise', L(15, 'Front rise'), 'ROUGH: crotch point by eye.'),
    (15, 'Inseam', L(15, 'Inseam (front)', 'Inseam (back)'), ''),
    (15, 'Leg opening flat, one leg', L(15, 'Leg opening flat, one leg'), ''),
    (15, 'Hip flat', None, ''),
    (15, 'Flaws (white)', None, ''),
    (16, 'Length, collar base to hem', None, 'No reference in frame: tape.'),
    (16, 'Sleeve / pit to pit / shoulder', None, ''),
    (16, 'Ink marks: do they lift with alcohol?', None, 'Test a hidden spot first; reshoot if they lift.'),
    (16, 'Shell fabric (care label)', None, ''),
    (17, 'Length, collar base to hem', L(17, 'Length, collar base to hem (front)', 'Length, collar base to hem (back)'), 'Hinge-scaled.'),
    (17, 'Sleeve, shoulder seam to cuff', L(17, 'Sleeve (front)', 'Sleeve (back)'), ''),
    (17, 'Elastic waist flat, relaxed', L(17, 'Elastic waist flat, relaxed'), 'x2; also tape stretched.'),
    (17, 'Pit to pit / hip', None, ''),
    (17, 'Flaws (ivory collar)', None, ''),
    (18, 'Total length, collar base to hem', L(18, 'Total length, collar base to hem (front)', 'Total length, collar base to hem (back)'), 'Hinge-scaled.'),
    (18, 'Waist flat at the seam', L(18, 'Waist flat at the seam (front)', 'Waist flat at the seam (back)'), 'x2.'),
    (18, 'Inseam / rise', None, 'Legs hang together in the photo: tape.'),
    (18, 'Pit to pit / hip', None, ''),
    (18, 'Fabric (care label)', None, ''),
    (18, 'Flaws', None, ''),
    (19, 'Length, collar base to hem', L(19, 'Length, collar base to centre front hem', 'Length, collar base to centre back hem'), 'ROUGH: window-scaled.'),
    (19, 'Sleeve, shoulder seam to hem', L(19, 'Sleeve, shoulder to hem (short)'), 'ROUGH.'),
    (19, 'Pit to pit / shoulder to shoulder', None, ''),
    (19, 'Fabric (care label)', None, ''),
    (19, 'Flaws', None, ''),
    (20, 'Length, waist top to hem', L(20, 'Length, waist top to hem (front)', 'Length, waist top to hem (back)'), 'Grey hanger in frame: good.'),
    (20, 'Elastic waist flat, relaxed', L(20, 'Elastic waist flat, relaxed (front)', 'Elastic waist flat, relaxed (back)'), 'x2; also tape stretched.'),
    (20, 'Hip flat', L(20, 'Hip flat, widest'), ''),
    (20, 'Fabric, lined? (care label)', None, ''),
    (20, 'Flaws', None, ''),
]
for it in items:
    plan += [(it, 'Sold comps (3 recent eBay sold prices)', None, 'Needs the signed-in Chrome tab.'),
             (it, 'List price', None, ''), (it, 'Status (draft / measured / listed) and eBay URL', None, '')]
plan.sort(key=lambda r: r[0])

def col_of(s):
    s = s.lower()
    if s.startswith(('length', 'total length')): return 'Length'
    if any(k in s for k in ('strap', 'slit', 'depth')): return None
    for key, name in (('pit to pit', 'Pit to pit'), ('sleeve', 'Sleeve'), ('shoulder', 'Shoulder to shoulder'), ('leg opening', 'Leg opening'),
                      ('outseam', 'Outseam'), ('inseam', 'Inseam'), ('rise', 'Front rise'), ('waist', 'Waist flat'), ('hip', 'Hip flat'),
                      ('fabric', 'Fabric (care label)'), ('shell', 'Fabric (care label)'), ('flaws', 'Flaws'),
                      ('sold comps', 'Sold comps (3 recent eBay sold)'), ('list price', 'List price'), ('status', 'Status / eBay URL')):
        if key in s: return name
    return None

def cols_of(need):
    parts = [p.strip() for p in need.split(' / ')]
    cols = [col_of(p) for p in parts]
    if len(parts) > 1 and all(cols): return cols
    c = col_of(need); return [c] if c else []

inches = {(item, meas): v for photo, item, meas, g, ref, rpx, v in px}
NEED = object()
rows = {}  # item -> {col: formula | NEED | [text...]}
for item, need, f, note in plan:
    row = rows.setdefault(item, {'Other questions': [], 'Notes from the photos': []})
    cols = cols_of(need)
    if not cols:
        txt = need
        if 'strap' in need.lower(): txt += f" Photo says about {inches[(2, 'Strap, hanger to top edge, as tied')]:.1f} in."
        if note: txt += ' ' + note
        row['Other questions'].append(txt); continue
    for c in cols:
        if c == 'Fabric (care label)' and any(k in need for k in ('?', ',', ' and ')): row['Other questions'].append(need)
        cur = row.get(c)
        if f and isinstance(cur, str):  # two estimates for one column (front / back hem points)
            row[c] = f'={cur[1:]}&" / "&{f[1:]}'; row['Notes from the photos'].append(f'{c}: shown as front / back.')
        elif f: row[c] = f
        elif cur is None: row[c] = NEED
        if note and not c.startswith('Sold comps') and all(not n.endswith(note) for n in row['Notes from the photos']): row['Notes from the photos'].append(f'{c}: {note}')

r = 2
for item in sorted(rows):
    row = rows[item]
    ws[f'A{r}'] = item; ws[f'B{r}'] = items[item]
    for ci, name in enumerate(COLS, start=1):
        cell_ = ws.cell(r, ci); cell_.font = font; cell_.border = box; cell_.alignment = wrap
        v = row.get(name)
        if name in ('Other questions', 'Notes from the photos'):
            seen = []; [seen.append(x) for x in v if x not in seen]
            cell_.value = '\n'.join(seen) or None
            if name == 'Other questions' and seen: cell_.fill = yellow
        elif v is NEED: cell_.fill = yellow
        elif isinstance(v, str): cell_.value = v; cell_.fill = grey; cell_.number_format = '0.0'
        if item % 2 == 0 and cell_.fill.fgColor.rgb in (None, '00000000'): cell_.fill = band
    ws.row_dimensions[r].height = 118
    r += 1
ws[f'A{r+1}'] = 'Legend'; ws[f'A{r+1}'].font = bold
ws[f'A{r+2}'] = ('One row per piece. Yellow = you fill in (tape in inches, flat, or the answer). Grey = estimate from the photo, about 5 percent either way; type your tape over it. '
                 'White = not needed for this piece. Elastic waists: write relaxed / stretched, e.g. 13 / 17. '
                 'Sold comps need the signed-in eBay tab. Change the hanger or hinge size on the Inputs sheet and every grey number updates. Pixel readings are on the Pixels sheet.')
ws.merge_cells(f'A{r+2}:S{r+3}'); ws[f'A{r+2}'].alignment = wrap; ws[f'A{r+2}'].font = font
for ci, w in enumerate((5, 30) + (9,) * 10 + (18, 46, 18, 22, 9, 22, 50), start=1): ws.column_dimensions[get_column_letter(ci)].width = w
ws.row_dimensions[1].height = 32

# ---------------- Listings ----------------
wl = wb.create_sheet('Listings')
wl.append(['Item', 'Title (80 max)', 'Item specifics', 'Description', 'Photos', 'Ballpark (unverified)'])
for c in range(1, 7): wl.cell(1, c).font = head; wl.cell(1, c).fill = headfill
listings = [
    (1, 'Vintage 90s Liz Claiborne Blue Black Leopard Print Double Breasted Midi Shirt Dress 8',
     'Brand Liz Claiborne; Women; Size 8; Shirt Dress; Midi; Short Sleeve; Collared; Animal Print; Blue, Black; 100% Polyester; Button; Elastic Waist, Double Breasted; Vintage 1990s; Made in China; RN 52002 CA 16396',
     'Bright periwinkle blue with a black leopard spot, notched lapel collar, double row of dark buttons, short cuffed sleeves, shirred elastic waist, full midi skirt. Classic 90s Liz Claiborne Dresses label. Lightweight polyester, no ironing.',
     '01-...-front/back/tag.jpg', '$32 to $48'),
    (2, 'Future Collective Pink Cream Mixed Floral Lace Trim Tie Strap Slip Midi Dress Size S',
     'Brand Future Collective; Women; Size S; Slip Dress; Midi; Sleeveless; Square lace neckline; Floral; Pink, Cream, Black; Lace Trim, Tie Straps, Front Slit; fabric from care label',
     'Two-print slip dress: blush sprig print on top meeting a cream ditsy floral on a diagonal seam, eyelash lace at neckline and hem, tie shoulder straps, front slit. Target Future Collective, recent season.',
     '02-...', '$14 to $24'),
    (3, 'Ronny Kobo Rose Pink Leaf Jacquard Plunge V Neck Long Puff Sleeve Ruched Maxi Dress XS',
     'Brand Ronny Kobo; Women; Size XS; Maxi; Long Puff Sleeve; Plunge V; Tone-on-tone floral jacquard; Pink; Ruched front seam, Keyhole back; Cocktail, Wedding Guest',
     'Dusty rose tone-on-tone palm-leaf jacquard, deep plunge V with draped bodice, gathered puff shoulders, long fitted sleeves, ruched centre seam down a fitted skirt with a fishtail hem, keyhole back. Designer piece. Fitted: see measurements.',
     '03-...', '$65 to $120'),
    (4, "Brooks Brothers Advantage Chino White Cotton Flat Front Walking Shorts Women's Size 10",
     'Brand Brooks Brothers; Women; Size 10; Chino / Walking Shorts; White; 100% Cotton; Belt Loops, Slant Pockets, Back Darts, Hem Vents; Zip with hook and bar; Made in Malaysia',
     'Crisp white cotton twill, flat front, slant pockets, belt loops, small side vents at the hem, darted back. Brooks Brothers Advantage Chino cloth.',
     '04-...', '$16 to $28'),
    (5, 'The Limited Kelly Green Button Front Blouse Roll Tab Long Sleeves Chest Pocket Size S',
     'Brand The Limited; Women; Size S; Blouse; Button-Up; Green; Long Sleeve roll tab; Point collar over V; Solid; Chest Pocket, Back Yoke Pleat, Shirttail Hem; Made in Indonesia',
     'Saturated kelly green lightweight crepe, point collar over an open V, single chest pocket, long sleeves with button roll tabs, back yoke with box pleat, curved shirttail hem.',
     '05-...', '$12 to $20'),
    (6, 'Vintage 80s Starlo Fashions Red Black Abstract Moire Print Pleated Blouson Midi Dress USA',
     'Brand Starlo Fashions; Women; Size from measurements; Blouson Dress; Midi; Long Sleeve; Round neck; Abstract moire print; Red, Black; Elastic Waist, Accordion Pleated Skirt, Keyhole Back, Button Cuffs; Vintage 1980s; Made in USA',
     'Bold red-on-black abstract moire print, bloused bodice over an elastic waist, long sleeves with button cuffs, round neck with a button keyhole at the back, fine accordion-pleated skirt. Made in USA label.',
     '06-...', '$38 to $65'),
    (7, 'Free People We The Free Light Wash High Rise Wide Leg Jeans Flap Patch Pockets Size 29',
     'Brand Free People; Line We The Free; Women; Size 29; Jeans; Wide Leg; High Rise; Light Wash; Blue; Flap Patch Front Pockets, Seamed V Back Yoke; inseam from the sheet (reads cropped: say so in the title if confirmed)',
     'Light vintage-blue wash, high rise, full wide leg from the hip, button-flap patch pockets on the front, seamed western-style V yoke across the back. Free People We The Free denim.',
     '07-...', '$42 to $70'),
    (8, 'Free People Mixed Print Floral Paisley Button Front Blouse Long Balloon Sleeves Size S', 'Brand Free People; Women; S; Blouse; Button-Up, Boho; Long balloon sleeve; Collared; Floral, Paisley, Striped; Black, Cream, Pink; Smocked Cuffs, Gathered Hem; Vietnam', 'Mixed print: black and cream pinstripe panels with pink and cream florals and paisley borders. Pointed collar, button front, long balloon sleeves into smocked cuffs, boxy cropped shape with a gathered hem band.', '08-...', '$28 to $45'),
    (10, 'Vintage Lew Magram Collection Black Jersey Faux Wrap Maxi Dress White Satin Collar Cuffs 8', 'Brand Lew Magram; Women; 8; Maxi; Faux Wrap; Long Sleeve; Shawl Collar; Black, White; 100% Polyester; Ruched; Vintage 80s/90s; USA', 'Matte black stretch jersey, wide white satin shawl collar and turn-back cuffs, faux-wrap bodice with side ruching, long sleeves, column skirt to the ankle. Dry clean. RN 61246.', '10-...', '$45 to $75'),
    (11, 'adidas Sample Gray Satin Nylon Full Zip Track Bomber Jacket Ribbed Cuffs Drawcord Hem S', 'Brand adidas; Women; S; Track Jacket; Gray; Nylon shell, mesh lining; Full Zip, Zip Pockets, Ribbed Cuffs, Drawcord Hem, SAMPLE label; Thailand', 'SAMPLE-labelled adidas jacket: charcoal satin-finish nylon, stand collar, full zip, zip pockets, ribbed cuffs, drawcord hem, mesh lined. US S.', '11-...', '$40 to $70'),
    (12, 'Vintage 70s Connie Rizza Orange Floral Print Jersey Lace Up Collar Long Sleeve Dress', 'Brand Connie Rizza; Women; size from measurements; Shift; Knee; Long Sleeve; Collared Lace-Up; Floral; Orange; Vintage 1970s', 'Tangerine silky jersey with scattered florals, dense floral borders at hem and cuffs, white dots. Wide pointed collar with lace-up neckline, long sleeves, straight knee-length skirt. No size on the label.', '12-...', '$55 to $95'),
    (13, 'Vintage Jones New York Ivory Cream Flap Pocket Button Front Blouse Long Sleeve Size 8', 'Brand Jones New York; Women; 8; Blouse; Button-Up; Ivory; 100% Polyester; Long Sleeve; Notched Collar; Flap Chest Pockets, Button Cuffs; Vintage; Korea', 'Ivory crepe-weight polyester, notched camp collar, two buttoned flap chest pockets, button front, buttoned cuffs, shirttail hem. RN 54050.', '13-...', '$18 to $30'),
    (14, 'Ghost London Cream Olive Geometric Print Plunge V Neck Puff Sleeve Button Midi Dress XXS', 'Brand Ghost London; Women; XXS; Midi; Button-Through; Long puff-shoulder sleeve; Plunge V; Geometric; Cream, Olive, Black; fabric from care label', 'Cream crepe with an olive and black lattice print, deep plunge V, gathered puff shoulders, buttoned cuffs, button-through front, flowing midi skirt.', '14-...', '$60 to $110'),
    (15, '[Brand] White Coral Sea Print High Waist Slim Straight Trousers Gold Buttons Side Stripe', 'Brand and size from the label; Women; Trousers; Slim, High Rise, Cropped; White, Orange, Purple; Novelty print; Gold-Tone Buttons, Patch Pockets, Side Stripes', 'White cotton with an orange and purple coral-reef print, leopard patches, gold-tone buttons on the patch pockets and fly, navy and orange outseam stripes. High waist, slim straight cropped leg.', '15-...', 'unknown until the brand is known'),
    (16, "Denim & Flower Ricky Singh Men's Cream Cotton Varsity Bomber Jacket Striped Rib Trim L", 'Brand Denim & Flower; Men; L; Bomber; Cream; Cotton; Striped Rib Trim, Zip Front, Welt Pockets, Lined; flaws: ink marks', 'Stone-cream cotton canvas, black and white striped rib collar, cuffs and hem, zip front, welt pockets, printed lining. Blue ink marks by the left pocket and a faint mark on the front, photographed.', '16-...', '$18 to $30 as-is'),
    (17, 'Vintage 80s Neiman Marcus Navy 100% Silk Shirt Dress Ivory Collar Cuffs Elastic Waist 12', 'Brand Neiman Marcus; Women; 12; Shirt Dress; Midi; Long Sleeve; Notched Collar; Navy, Ivory; 100% Silk; Elastic Waist; Vintage 1980s; Hong Kong', 'Navy 100% silk with an ivory notched collar and cuffs, gathered shoulders, long sleeves, pink waist button, elastic waist, gathered skirt below the knee. Dry clean.', '17-...', '$48 to $85'),
    (18, 'Zara Cream Oatmeal Short Sleeve Utility Boilersuit Jumpsuit Button Front Chest Pocket Size S', 'Brand Zara; Women; S; Jumpsuit; Utility; Short Sleeve; Collared V; Cream; fabric from care label; Chest Pocket, Side Pockets, Button Front; Bangladesh', 'Oatmeal-cream slubbed weave, pointed collar, V neck, button front, patch chest pocket, short cuffed sleeves, seamed waist with side pockets, straight cropped legs.', '18-...', '$28 to $45'),
    (19, "Columbia PFG Men's Pale Yellow Vented Short Sleeve Fishing Shirt Button Front Size L", 'Brand Columbia; PFG; Men; L; Fishing Shirt; Short Sleeve; Yellow; Nylon; Vented Back, Mesh Lining, Chest Pockets; Vietnam', 'Pale yellow PFG fishing shirt, short sleeves, button front, chest pockets, mesh-lined vented back, logo at the back yoke.', '19-...', '$16 to $28'),
    (20, 'Vintage Bonnie & Norma Paisley Print Elastic Waist Midi Skirt Rust Teal Gold Size 12', 'Brand Bonnie & Norma; Women; 12; Midi Skirt; A-Line; Rust, Teal, Gold, Black; Paisley; fabric from care label; Elastic Waist; Vintage', 'Autumn paisley of rust, teal, gold and black on a soft lightweight weave, full elastic waist, straight-to-A-line midi.', '20-...', '$18 to $32'),
]
for i, row in enumerate(listings, start=2):
    for c, v in zip('ABCDEF', row): wl[f'{c}{i}'] = v; wl[f'{c}{i}'].font = font; wl[f'{c}{i}'].alignment = wrap; wl[f'{c}{i}'].border = box
    wl.row_dimensions[i].height = 95
for col, w in zip('ABCDEF', (5, 40, 55, 60, 16, 14)): wl.column_dimensions[col].width = w
wl[f'A{len(listings) + 3}'] = 'Prices are ballparks from memory, not sold comps. Images: assets/ebay-2026-11-08/ebay/ in the Vintage repo.'; wl[f'A{len(listings) + 3}'].font = font

wb.calculation.fullCalcOnLoad = True
for o in OUT: wb.save(o); print('saved', o)
# python check of the estimates (what Excel will show)
print('\nitem measure inches')
for photo, item, meas, g, ref, rpx, inches in px: print(f'{item} {photo} {meas}: {inches:.1f}')
