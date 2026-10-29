**Note** : You are viewing the development version of [Schema.org](https://schema.org). See [how we work](https://schema.org/docs/howwework.html) for more details. 
[Schema.org](https://schema.org/)
  * [Docs](https://schema.org/docs/documents.html)
  * [Schemas](https://schema.org/docs/schemas.html)
  * [Validate](https://validator.schema.org)
  * [About](https://schema.org/docs/about.html)


[ ](javascript:void\(0\);)
# SoldOut
A Schema.org Enumeration Member
[Thing](https://schema.org/Thing "Thing") > [Intangible](https://schema.org/Intangible "Intangible") > [Enumeration](https://schema.org/Enumeration "Enumeration") > [ItemAvailability](https://schema.org/ItemAvailability "ItemAvailability") ::  [SoldOut](https://schema.org/SoldOut "SoldOut")   

**[more...]**
  * Canonical URL: https://schema.org/SoldOut
  * [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SoldOut)


Indicates that the item has sold out.
  
A member value for enumeration type: [ItemAvailability](https://schema.org/ItemAvailability "ItemAvailability")
### Examples
![Copy to clipboard](https://schema.org/docs/clipboard/clippy.svg) [Example 1](https://schema.org/SoldOut#eg-0173 "Link: #eg-0173")
Copied
No Markup Microdata RDFa JSON-LD Structure
Example notes or example HTML without markup.

```



  1. 
<div class="event-wrapper">  




  2. 
  <div class="event-date">Sat Sep 14</div>  




  3. 
  <div class="event-title">SOLD OUT! Typhoon with Radiation City</div>  




  4. 
  <div class="event-venue">  




  5. 
    The Hi-Dive  




  6. 
    <div class="address">  




  7. 
      7 S. Broadway<br>  




  8. 
      Denver, CO 80209  




  9. 
    </div>  




  10. 
  </div>  




  11. 
  <div class="event-time">10:00 PM</div>  




  12. 
 <span>  




  13. 
  <div class="event-price">$13.00</div>  




  14. 
  <a href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  15. 
 </span>  




  16. 
</div>




```

Example encoded as [Microdata](https://en.wikipedia.org/wiki/Microdata_\(HTML\)) embedded in HTML.

```



  1. 
<div class="event-wrapper" itemscope itemtype="https://schema.org/Event">  




  2. 
    <div class="event-date" itemprop="startDate" content="2013-09-14T21:30">  




  3. 
        Sat Sep 14  




  4. 
    </div>  




  5. 
    <div class="event-title" itemprop="name">  




  6. 
        SOLD OUT! Typhoon with Radiation City  




  7. 
    </div>  




  8. 
    <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place">  




  9. 
        <span itemprop="name">The Hi-Dive</span>  




  10. 
        <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">  




  11. 
            <span itemprop="streetAddress">7 S. Broadway</span><br>  




  12. 
            <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span>  




  13. 
        </div>  




  14. 
    </div>  




  15. 
    <div class="event-time">9:30 PM</div>  




  16. 
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">  




  17. 
        <meta itemprop="availability" content="https://schema.org/SoldOut">  




  18. 
        <div class="event-price" itemprop="price" content="13.00">$13.00</div>  




  19. 
        <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  20. 
    </div>  




  21. 
</div>




```

Example encoded as [RDFa](https://en.wikipedia.org/wiki/RDFa) embedded in HTML.

```



  1. 
<div vocab="https://schema.org/" class="event-wrapper" typeof="Event">  




  2. 
  




  3. 
  <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div>  




  4. 
  <div class="event-title" property="name">SOLD OUT! Typhoon with Radiation City</div>  




  5. 
  




  6. 
  <div class="event-venue" property="location" typeof="Place">  




  7. 
    <span property="name">The Hi-Dive</span>  




  8. 
    <div class="address" property="address" typeof="PostalAddress">  




  9. 
      <span property="streetAddress">7 S. Broadway</span><br>  




  10. 
      <span property="addressLocality">Denver</span>,  




  11. 
      <span property="addressRegion">CO</span>  




  12. 
      <span property="postalCode">80209</span>  




  13. 
    </div>  




  14. 
  </div>  




  15. 
  




  16. 
  <div class="event-time">9:30 PM</div>  




  17. 
  




  18. 
 <span property="offers" typeof="Offer">  




  19. 
  <meta property="availability" content="https://schema.org/SoldOut">  




  20. 
  <div class="event-price">  




  21. 
    <meta property="priceCurrency" content="USD" />$  




  22. 
    <meta property="price" content="13.00" />13.00  




  23. 
  </div>  




  24. 
  <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>  




  25. 
 </span>  




  26. 
</div>




```

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

```



  1. 
<script type="application/ld+json">  




  2. 
{  




  3. 
  "@context": "https://schema.org",  




  4. 
  "@type": "Event",  




  5. 
  "location": {  




  6. 
    "@type": "Place",  




  7. 
    "address": {  




  8. 
      "@type": "PostalAddress",  




  9. 
      "addressLocality": "Denver",  




  10. 
      "addressRegion": "CO",  




  11. 
      "postalCode": "80209",  




  12. 
      "streetAddress": "7 S. Broadway"  




  13. 
    },  




  14. 
    "name": "The Hi-Dive"  




  15. 
  },  




  16. 
  "name": "SOLD OUT! Typhoon with Radiation City",  




  17. 
  "offers": {  




  18. 
    "@type": "Offer",  




  19. 
    "availability": "https://schema.org/SoldOut",  




  20. 
    "price": "13.00",  




  21. 
    "priceCurrency": "USD",  




  22. 
    "url": "http://www.ticketfly.com/purchase/309433"  




  23. 
  },  




  24. 
  "startDate": "2013-09-14T21:30"  




  25. 
}  




  26. 
</script>




```

Structured representation of the JSON-LD example.
{ "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "SOLD OUT! Typhoon with Radiation City", "offers": { "@type": "Offer", "availability": "https://schema.org/SoldOut", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" }
[Terms and conditions](https://schema.org/docs/terms.html)
• Schema.org • V30.1 | 2026-09-16 

