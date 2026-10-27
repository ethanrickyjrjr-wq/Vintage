[Help](https://help.shopify.com/en)
[Start for free](https://admin.shopify.com/signup?language=en)
[Log in](https://help.shopify.com/en/user/login)
Contents
# Importing products with a CSV file
Importing products into your Shopify store using a comma-separated values (CSV) file is useful when you switch to Shopify from another platform or when you want to make many changes to your products or inventory.
When you import products, the data is converted from the [CSV file](https://help.shopify.com/en/manual/products/import-export/using-csv#product-csv-file-format) into products and you can select whether you want to publish your new products to all sales channels or only to your online store.
#### Tip
To see more videos, visit our [YouTube channel](https://www.youtube.com/channel/UCSG_dVp-hi_hWP-Z7DlpRgQ). 
## On this page
  * [Before you begin](https://help.shopify.com/en/manual/products/import-export/import-products#before-you-begin)
  * [Testing imports using a dev store](https://help.shopify.com/en/manual/products/import-export/import-products#testing-imports-using-a-dev-store)
  * [Considerations for overwriting your product details using an import CSV file](https://help.shopify.com/en/manual/products/import-export/import-products#overwriting-csv-file)
  * [Import products from another store](https://help.shopify.com/en/manual/products/import-export/import-products#import-products-from-another-store)
  * [Import products using a CSV file](https://help.shopify.com/en/manual/products/import-export/import-products#import-products-using-a-csv-file)
  * [Troubleshooting CSV imports](https://help.shopify.com/en/manual/products/import-export/import-products#troubleshooting-csv-imports)


## Before you begin
Before you import products using a CSV file, make sure that you've read the following topics:
  * [Explanation of CSV files](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/csv-files)
  * [Explanation of the product CSV fields](https://help.shopify.com/en/manual/products/import-export/using-csv#csv-file-description)
  * [Guidelines for attaching multiple images](https://help.shopify.com/en/manual/products/import-export/using-csv#adding-multiple-product-images)


Product imports started with a CSV file can't be canceled once they begin, and you can't view a history of past imports. To review recent changes made by an import, check your store's [activity log](https://help.shopify.com/en/manual/shopify-admin/activity-logs#store-activity-log).
#### Caution
Before you start your import, make sure that you have a [backup of your product data](https://help.shopify.com/en/manual/products/import-export/export-products).
Importing a CSV file that has been sorted by a spreadsheet editor such as Microsoft Excel or Apple Numbers might cause your products to be removed from their relevant image links on the CSV, and your product's images will be lost.
#### Note
If you use a third-party [fulfillment service](https://help.shopify.com/en/manual/fulfillment/fulfilling-orders) and set **Fulfillment service** to a specific fulfillment service handle (for example, `joans-fulfillment`) in your product CSV, then importing activates the variant's inventory at that fulfillment service location. Any other locations where the variant is already stocked remain stocked — nothing is unstocked.
After the import, the **Fulfillment service** column continues to show `manual` for these variants when you re-export.
To manage inventory at specific fulfillment service locations directly, import the [inventory CSV file](https://help.shopify.com/en/manual/inventory-and-locations/setup/inventory-csv#import-inventory). Or, if you're working with a developer, you can use the [Inventory API](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps) instead. Learn more about [how these columns work](https://help.shopify.com/en/manual/products/import-export/using-csv#csv-file-description).
## Testing imports using a dev store
If you're a Shopify Partner and you're performing a large scale import for a merchant, then make sure that you test a small subset of changes first using a [dev store](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores) before you perform the actual import job.
## Considerations for overwriting your product details using an import CSV file
When you import a CSV file, you can select the option **Overwrite products with matching handles.** If you select this option, then when the handle in the import CSV file matches an existing handle in your products list, the values in the CSV file overwrite the values in the matching columns in the existing product list. If the overwrite option isn't selected, then the products that match an existing handle are ignored during CSV import.
  * If a non-required column in the import CSV file is blank, then the matching value in the product list is overwritten as blank.
    * For example, the **Vendor** value in your existing product list is `John's Apparel`, but the **Vendor** column is blank in the CSV file that you import, then the `John's Apparel` is overwritten as blank.
  * If a non-required column isn't included in the import CSV file, but is included in the existing product list, then the value in the product list remains the same.
    * For example, if the **Variant image URL** column is included in the existing product list, but that column isn't included in the import CSV file, then the value in the product list remains the same.
  * If a non-required column is included in the import CSV file that relies on other column data not included in the file, then existing data is deleted or removed.
    * For example, if the **SKU** column is included in the import CSV file, but not the **Option1 value** and **Option1 name** columns, then the product variant option is deleted.
  * CSV files can't be used to delete products in bulk. If you want to bulk-delete products, then you can use [bulk actions](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-actions) in the **Products** section of your admin.
  * CSV files can't be used to bulk update product availability on other sales channels. Learn more about [setting product availability in other sales channels](https://help.shopify.com/en/manual/products/add-update-products#product-availability).


#### Caution
Changing data in the **Option1 value** , **Option2 value** , or **Option3 value** columns of the product CSV file deletes existing variant IDs, and creates new variant IDs. Any change to variant IDs values can break third-party dependencies on variant IDs.
## Import products from another store
If you have a CSV file that was exported from another store or came from another source, then verify that it matches the [CSV file format](https://help.shopify.com/en/manual/products/import-export/using-csv#product-csv-file-format). If the format doesn't match, or if there are any missing headers, then the import fails.
Your product CSV can't exceed 15 MB. If you get an error after trying to upload a new CSV file, or if the upload times out, split the CSV file it into multiple smaller files, and then upload each file.
#### Steps:
  1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
  2. Click **Import**.
  3. Click **Add file** , and then select the CSV file that you want to import.
  4. Optional: If you want to publish new products only to your online store instead of to all of your sales channels, then deselect **Publish new products to all sales channels**.
  5. Optional: To change the URLs by [overwriting the values for the existing handles](https://help.shopify.com/en/manual/products/import-export/import-products#overwriting-csv-file), select **Overwrite products with matching handles.** Existing values will be replaced for all columns included in the CSV.
  6. Click **Upload and continue**.
  7. Review the details about the import, and then click **Import products**.


When your CSV file is uploaded, you receive a confirmation email from Shopify to the email address of your user account. Read some [solutions to common problems](https://help.shopify.com/en/manual/products/import-export/common-import-issues).
## Import products using a CSV file
If you want to make changes to your products using a CSV file, then you need to [export your products](https://help.shopify.com/en/manual/products/import-export/export-products) first. You can [make changes to your CSV file](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/csv-files#import-csv-files-into-google-sheets) in a spreadsheet program, such as [Google Sheets](https://docs.google.com/spreadsheets), then import your updated CSV into the Shopify admin.
#### Steps
  1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
  2. Click **Import**.
  3. Click **Add file** , and then select the CSV file that you want to import.
  4. Optional: If you want to publish new products only to your online store instead of to all of your sales channels, then deselect **Publish new products to all sales channels**.
  5. Optional: To change the URLs by [overwriting the values for the existing handles](https://help.shopify.com/en/manual/products/import-export/import-products#overwriting-csv-file), select **Overwrite products with matching handles.** Existing values will be replaced for all columns included in the CSV.
  6. Click **Upload and continue**.
  7. Review the details about the import, and then click **Import products**.


After your CSV file is uploaded, you receive a confirmation email from Shopify at the email account used to set up your Shopify store. Read some [solutions to common problems](https://help.shopify.com/en/manual/products/import-export/common-import-issues).
#### Tip
To avoid issues when you upload your product CSV file, use the [Google Chrome](https://google.com/intl/en/chrome/browser/desktop/index.html) browser.
## Troubleshooting CSV imports
If you're experiencing issues when importing a CSV file, then review the following troubleshooting information.
Unexpected characters or symbols appear in imported content
If you notice unexpected characters or symbols in your product descriptions, titles, or other content after importing a CSV file, then the file might not have been saved with UTF-8 (Unicode Transformation Format - 8-bit) encoding.
UTF-8 encoding is required to prevent unexpected characters from appearing in your content. By default, Google Sheets saves files with UTF-8 encoding automatically. Other spreadsheet software might require an extra step to save with UTF-8 encoding.
#### Manually fix the affected items
Go through each affected product and manually change or remove the characters. This works best if only a few items are affected.
#### Import an older version
If you have a previous version of the CSV file that was saved with proper encoding, then import that version instead.
#### Re-save with proper encoding
Open the improperly encoded CSV file and save it again with UTF-8 encoding. The process varies depending on your operating system and spreadsheet program. For instructions, refer to [CSV files](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/csv-files).
Network error: Unexpected token in JSON at position 0
If you receive an error message `Network error: Unexpected token < in JSON at position 0`, then the CSV column titles don't match exactly with the required CSV template headers. Column header names are case-sensitive.
#### Review and correct column headers
  1. Review the [CSV format guide](https://help.shopify.com/en/manual/products/import-export/using-csv#download-a-sample-csv-file) for correct CSV formatting.
  2. Compare your CSV column titles against the sample file.
  3. Confirm that your CSV file headers match the sample file exactly, including case sensitivity. For example, use `Handle` instead of `handle`.
  4. Correct your CSV file headers to match the sample file headers. You can download a copy of the sample file from the [CSV format guide](https://help.shopify.com/en/manual/products/import-export/using-csv#download-a-sample-csv-file).

Illegal quoting error
An illegal quoting error occurs when there are non-UTF-8 encoded commas and quotation marks in your CSV file.
For a product CSV to import correctly, all quotes and apostrophes must be UTF-8 encoded and in the correct position. For example, non-UTF-8 quotation marks display curled: “ ”, and UTF-8 quotation marks are straight: " ".
#### Save your file with UTF-8 encoding
Save your original file with UTF-8 encoding before importing.
Import fails with error "Line is invalid (No details)"
If you receive an error indicating that specific lines are invalid without additional details, then the issue might be caused by conflicts with existing product variant options. This occurs when you attempt to change an option value from one option position to another.
#### What causes this issue
The CSV import fails when a file tries to assign an existing option value to a new option position, creating a conflict as variant options must be unique. For example, if you attempt to move `Size` from Option 1 to Option 2, and add `Type` as the new Option 1, then the database validates for duplicate names before importing new values, and the process fails.
#### Resolve the conflict
Use a temporary option name during the import, and then update it afterward:
  1. In your CSV file, use an alternative temporary name for the option that's causing the conflict. For example, use `Size.` (with a period) instead of `Size`.
  2. Import the CSV file with the temporary option name.
  3. After the import completes successfully, create a new CSV file that changes the temporary option name to your desired name.
  4. Import the updated CSV file to apply the final option name.


Leave feedback

