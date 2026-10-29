<!-- SOURCE: https://practicaltypography.com/point-size.html (fetched 2026-10-29T05:16:25Z via curl + html->text) -->



point size
Smaller on paper; bigger on screen
In print, the op­ti­mal point size for 
body text
 is 10–12 point. On the web, the op­ti­mal size is 15–25 
pixels.
Point size in print
Though 12 point has be­come the de­fault size in dig­i­tal word pro­cess­ing—and also the ba­sis of many in­sti­tu­tional doc­u­ment-for­mat­ting rules—that’s mostly due to the type­writer tra­di­tion. It’s not the most com­fort­able size for read­ing. Nearly every book, news­pa­per, and mag­a­zine is set smaller than 12 point. (One ma­jor rea­son is cost: big­ger point sizes re­quire more 
paper.)
There are 72 
points
 to an inch. Word lets you spec­ify point sizes in half-point in­cre­ments. Pages al­lows finer in­cre­ments of one-tenth of a point. CSS al­lows any size, but browsers will typ­i­cally round to the near­est whole 
point.
If you’re not re­quired to use 12 point, don’t. Try sizes down to 10 point, in­clud­ing in­ter­me­di­ate sizes like 10.5 and 11.5 point—half-point dif­fer­ences are mean­ing­ful at this 
scale.
But I can’t guar­an­tee 12 point will al­ways look too big. That’s be­cause the point-size sys­tem is not ab­solute—dif­fer­ent fonts set at the same point size won’t nec­es­sar­ily ap­pear the same on the 
page.
That means you need to let your eyes be the judge. Don’t just rely on the point size. For in­stance, the three fonts be­low—Sabon, 
Times New Ro­man
, and Arno—are set at 12 point, but they’re not the same size 
visually.
You can match the length of two fonts by set­ting a block of text twice: once in the old font and once in the new font, both at the same point size. Ad­just the point size of the new font un­til each line of text breaks in roughly the same place. (You won’t be able to match them ex­actly.) Be­low, the point sizes of Sabon and Arno have been ad­justed so they oc­cupy the same space as Times New 
Roman.
Point size can be even smaller in pro­fes­sion­ally type­set ma­te­ri­als like pub­li­ca­tions and sta­tionery. Text on 
busi­ness cards
 is of­ten only 6–8 points. At these sizes, 
all caps
 text and low­er­case are equally 
legible.
Point size as emphasis
It’s fine to em­pha­size text with a larger point size (or de-em­pha­size it with a smaller point size). But use the sub­tlety that point-size ad­just­ments of­fer. If your body text is set at 11 point, no need to jump to 14 point for em­pha­sis. Start with a smaller in­crease—say, half a point—and move up in half-point in­cre­ments un­til you get the em­pha­sis you need. It’ll be less than you think.
Point size on the web
You don’t have to use pix­els as the siz­ing unit in your CSS (and in­deed, most pre­fer not to). But the pixel is the least am­bigu­ous CSS unit. Also, all CSS mea­sure­ments are even­tu­ally con­verted to pix­els in the 
browser.
For web­sites, I rec­om­mend body text of 15–25 pix­els. As with print, you’ll need to fine-tune based on the par­tic­u­lar font you’re 
using.
Why? Two rea­sons. First, we typ­i­cally read screens from fur­ther away than we read printed ma­te­r­ial, so larger point sizes help com­pen­sate. Sec­ond, screen fonts are ren­dered with a rel­a­tively small num­ber of pix­els, so each ex­tra row of pix­els im­proves the qual­ity. (See also 
screen-read­ing con­sid­er­a­tions
.)
Yes, I know the web has a long tra­di­tion of teeny fonts. It’s time to let it go. This habit arose be­cause the 14-inch mon­i­tors com­mon in the 1990s had rel­a­tively coarse res­o­lu­tion. It per­sisted be­cause web de­sign­ers con­sid­ered it vir­tu­ous to keep ac­com­mo­dat­ing peo­ple who re­fused to up­grade those 14-inch mon­i­tors. But now, it’s merely 
silly.
Also silly is the web’s tra­di­tion of enor­mous point sizes for head­ings. This habit started with the de­fault for­mat­ting of 
<h1>
 tags in browsers, which is about 200% of the de­fault point size of body text. There is no ty­po­graphic uni­verse in which you need to dou­ble the point size to achieve em­pha­sis. See 
head­ings
 for sub­tler 
techniques.
For more about the en­trenched ty­po­graphic habits of the web, see 
web­sites
.
by the way
In 
hy­phens and dashes
, I men­tioned that 
em
 refers to a ty­pog­ra­pher’s mea­sure­ment, not the let­ter M. The em size of a font is the same as its point size. Fonts are no longer made of metal, but the em con­cept per­sists. Dig­i­tal fonts are drawn in­side a rec­tan­gle called the em. To ren­der a font on screen, your com­puter scales the em to match the cur­rent point size. Two fonts set at the same point size will ap­pear to be dif­fer­ent sizes if one oc­cu­pies less space on its 
em.
Can you de­ter­mine the point size of a font by mea­sur­ing it? No. Be­cause of the dif­fer­ences in ap­par­ent siz­ing be­tween fonts, there’s noth­ing you can mea­sure that would be con­clu­sive. The only way to fig­ure it out is to set the same text, in the same font, with the same 
line length
. Then ad­just the point size so it matches the ref­er­ence 
sample.
As you re­duce point size, also re­duce 
line spac­ing
 and 
line length
. For in­stance, news­pa­per fonts are quite small, but re­main leg­i­ble be­cause they have snug line spac­ing and short line 
length.
Or­ga­ni­za­tions that need to con­trol the length of doc­u­ments (e.g., courts, col­leges) usu­ally do so with lim­its on point size and page length. In the type­writer age, this worked be­cause type­writer out­put was stan­dard­ized. In the dig­i­tal age, it makes less sense, since art­ful for­mat­ting and lay­out can make doc­u­ments ap­pear longer or shorter as nec­es­sary. Any­one who needs to set stan­dards for doc­u­ment length would be bet­ter off putting these rules in terms of word count. Un­like type­writ­ers, all word proces­sors have a word-count func­tion. Com­pared to page lim­its, word counts are harder to evade. To be fair, they’re also harder to 
verify.
In 2012, a dis­pute about 
point size
 reached the Michi­gan Supreme Court. One side ar­gued—con­trary to 400 years of ty­po­graphic cus­tom—that a law call­ing for
 “14-point
 type” on a bal­lot meant that the up­per­case let­ters of the font had to be at least 14 points tall. For­tu­nately the court did not adopt this in­ter­pre­ta­tion. As a mat­ter of law, it would’ve re­de­fined the mean­ing of point size within 
Michigan.

undock


move


Heliotrope

Equity

Valkyrie

Century Supra

Concourse

Triplicate

buy font


close


←
 all caps

top

chapter

headings 
→


