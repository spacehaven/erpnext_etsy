## ERPNext Etsy

Etsy Connector for ERPNext

### Description

An ERPNext Etsy connector roughly modeled after the ERPNext Shopify connector.

Initial development will be a one-way, read-only sync from Etsy to ERPNext. Eventually two-way sync will be implemented.

### Rough outline of functionality:

* Settings DocType (eventually it would be nice to allow for multiple Etsy account support)
* Sync Etsy Items to ERPNext Items 
  * For each Etsy Item, create new or update existing ERPNext Item
    * Include images if possible (as attachments and set the ERPNext Item image if possible)
    * Add/update price in price list 
    * Handle variants (eventually - not to be implemented initially)
* Sync Etsy Customers to ERPNext Customers
  * For each Etsy Customer, create new or update existing ERPNext Customer
    * Eventually pull conversations if possible
    * Any additional info - photo, creation date, email if available
* Sync Etsy Orders to ERPNext Sales Orders, Invoices, Payments, and Delivery Notes
  * For each Etsy Order, create new or update existing ERPNext Sales Order, Invoice
    * If shipped, create Payment and Delivery Note
* Logging of sync batches similar to the Shopify connector
* Notifications of failures

### Future development:

* Full oauth authentication setup (i.e.: redirect to Etsy's permission screen, redirect back to ERPNext). This won't be implemented initially.
* Two-way sync:
  * Items:
    * Create items in ERPNext and push them to Etsy (including pictures). 
    * Trigger sync any time an Item is updated in ERPNext
  * Customers:
    * Nothing to sync except conversations maybe
  * Orders:
    * Possibly create Delivery Notes in ERPNext and update ETSY if possible
* Handle edge-cases like refunds
* Proper ERPNext accounting of regular (i.e.: weekly) Etsy shop payment drops 
* Whatever else the ETSY API allows, within reason 
* Stats, charts

-----

#### License

MIT
