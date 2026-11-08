# eBay items in Google Drive: one folder per item

**Rule (Ricky, 2026-11-08):** every item that goes on eBay gets its own folder in Drive before it is listed:

```
G:\My Drive\Holliewood eBay\Items\<NN slug>\
    <slug>-front.jpg, -back.jpg, -tag.jpg, -detail.jpg ...   Photoroom output only (white background)
    listing.txt                                               title, description, item specifics, "before you publish" notes
```

An item is **set up** when the folder exists with a front photo and `listing.txt`. Numbers continue the listing
numbers (1 to 46 are the 2026-11-08 batch); the slug is the photo file-name stem. On the phone, Files > Google Drive >
Holliewood eBay > Items > one folder = one eBay listing: pick the photos, paste the text.

## How it is built and checked

`tools/ebay-drive-items.py <batch dir> [--check]` reads `listings-copy.md` and the `ebay/` and `other-items/` photo folders
of a batch, writes the item folders (copies only what is missing or changed, so it is safe to rerun) and prints one row per
item: photos, front, copy, status. Exit 1 if any item is not set up. `--check` reports without writing.

```
python -I tools/ebay-drive-items.py assets/ebay-2026-11-08
```

For a new batch: Photoroom cuts into `assets/ebay-<date>/ebay/` (clothes, `NN-slug-view.jpg`) or `other-items/`
(`slug-view.jpg`), listing copy into `listings-copy.md` as `# N. Title` sections, non-clothing slugs added to the `OTHER`
map in the script, then run it. The flat batch folders (`2026-11-08 batch images`, `2026-11-08 other items`) stay as the
batch record; the fill-in workbook and listings docx stay at the top of `Holliewood eBay`.

## Check on 2026-11-08

45 of 46 items set up, 97 photos and 45 listing texts written in 2.3 s. Not set up:

- **46 Crystal Glass wall art box**: one photo, no listing copy. Open question from the workbook: is it the box for item 21
  (the Louvre dogs glass art) or a second boxed piece? Ricky opens the box; if it is item 21's box, delete the folder and
  mention the box in listing 21.

Notes: item 9 was merged into item 11 and gets no folder. Items 38 (jewelry box) and 39 (the costume jewelry lot inside it)
share the one `jewelry-case-open-front.jpg` until the lot is shot on its own.
