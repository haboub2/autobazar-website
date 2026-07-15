# -*- coding: utf-8 -*-
"""Generate city x category SEO landing pages for autobazarsyria.com.
Matches the existing template (cars.html) exactly: same head/meta, navbar,
hero, steps, features, FAQ, cross-links, CTA, footer, and JSON-LD.
Each page is uniquely city-specific (title, hero, FAQ, internal links)."""
import os, json

ROOT = "/Users/haboub/Downloads/Websites/autobazar-website"
DOMAIN = "https://autobazarsyria.com"
CSSV = "18"

CITIES = [
    ("damascus",   "Damascus",    "دمشق"),
    ("aleppo",     "Aleppo",      "حلب"),
    ("homs",       "Homs",        "حمص"),
    ("latakia",    "Latakia",     "اللاذقية"),
    ("hama",       "Hama",        "حماة"),
    ("tartus",     "Tartus",      "طرطوس"),
    ("deir-ez-zor","Deir ez-Zor", "دير الزور"),
    ("raqqa",      "Raqqa",       "الرقة"),
]

APPLE = "https://apps.apple.com/us/app/%D8%A3%D9%88%D8%AA%D9%88-%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1/id6769161259"
def gplay(campaign):
    return f"https://play.google.com/store/apps/details?id=com.elenjaz.haboub&utm_source=website&utm_medium=download_button&utm_campaign={campaign}"

# Per-category content. {ce}=city EN, {ca}=city AR
CATS = {
 "cars": {
   "word_en":"Cars","word_ar":"سيارات",
   "badge_en":"Syria's #1 Car Marketplace","badge_ar":"سوق السيارات الأول في سوريا",
   "h1_en":"Cars for Sale in {ce}","h1_ar":"سيارات للبيع في {ca}",
   "sub_en":"Buy and sell new & used cars in {ce}, Syria — directly, with no middlemen",
   "sub_ar":"بيع وشراء سيارات جديدة ومستعملة في {ca} — مباشرة وبدون وسطاء",
   "desc_en":"Browse verified car listings in {ce} and across all 14 Syrian provinces. Filter by brand, model, year, mileage, and price — then message the seller directly, with no commissions.",
   "desc_ar":"تصفح إعلانات سيارات موثقة في {ca} وفي جميع المحافظات السورية الـ 14. صفِّ حسب الشركة والطراز والسنة والمسافة المقطوعة والسعر — وتواصل مع البائع مباشرة، وبدون عمولات.",
   "steps":[
     ("Download & Sign Up","حمّل التطبيق وسجّل","Get Auto Bazar free on iOS or Android and verify your email in seconds.","حمّل أوتو بازار مجاناً على iOS أو Android وفعّل بريدك الإلكتروني في ثوانٍ."),
     ("List Your Car","أضف إعلان سيارتك","Add make, model, year, mileage, price, {ce}, and clear photos.","أضف الشركة والطراز والسنة والمسافة المقطوعة والسعر ومدينة {ca} وصوراً واضحة."),
     ("Chat with Buyers","تواصل مع المشترين","Reach real buyers in {ce} and across Syria and negotiate directly in the app.","صِل إلى مشترين حقيقيين في {ca} وكل سوريا وتفاوض مباشرة داخل التطبيق."),
   ],
   "features":[
     ("Smart Filters","فلاتر ذكية","Search by brand, model, year, mileage, transmission, and price to find exactly the car you want in {ce}.","ابحث حسب الشركة والطراز والسنة والمسافة المقطوعة وناقل الحركة والسعر لتجد السيارة التي تريدها بالضبط في {ca}."),
     ("Verified Sellers","بائعون موثقون","Every account is email-verified and listings are reviewed to keep the marketplace trustworthy.","كل حساب موثق بالبريد الإلكتروني وتتم مراجعة الإعلانات للحفاظ على مصداقية السوق."),
     ("No Commissions","بدون عمولات","Message buyers and sellers directly in-app — Auto Bazar never takes a cut of your sale.","تواصل مع البائعين والمشترين مباشرة داخل التطبيق — أوتو بازار لا يأخذ أي عمولة من بيعتك."),
     ("Local to {ce}","محلي في {ca}","Filter to {ce} to see only cars for sale near you, or browse all 14 Syrian provinces.","صفِّ حسب {ca} لترى فقط السيارات المعروضة قربك، أو تصفح كل المحافظات السورية الـ 14."),
   ],
   "faq":[
     ("How do I sell my car in {ce}?","كيف أبيع سيارتي في {ca}؟","Download Auto Bazar, create a free account, then tap \"+\" to list your car. Add make, model, year, mileage, price, and set the city to {ce}, then upload clear photos. Your listing goes live instantly and reaches buyers across Syria.","حمّل أوتو بازار، أنشئ حساباً مجانياً، ثم اضغط \"+\" لإضافة إعلان سيارتك. أضف الشركة والطراز والسنة والمسافة المقطوعة والسعر واختر مدينة {ca}، ثم ارفع صوراً واضحة. يظهر إعلانك فوراً ويصل إلى مشترين في كل سوريا."),
     ("Can I find used cars for sale in {ce}?","هل يمكنني إيجاد سيارات مستعملة للبيع في {ca}؟","Yes. Filter listings by {ce} to see only new and used cars for sale in the city and nearby areas.","نعم. صفِّ الإعلانات حسب {ca} لتشاهد فقط السيارات الجديدة والمستعملة المعروضة للبيع في المدينة والمناطق المجاورة."),
     ("Is it free to list a car for sale in {ce}?","هل نشر إعلان سيارة في {ca} مجاني؟","Yes. You can post a limited number of car listings for free. Optional paid plans unlock extra listing slots and highlighted placement for faster sales.","نعم. يمكنك نشر عدد محدود من إعلانات السيارات مجاناً. خطط الاشتراك الاختيارية تفتح خانات إعلانات إضافية وتمييز الإعلان لبيع أسرع."),
     ("How do I contact a car seller in {ce} safely?","كيف أتواصل مع بائع سيارة في {ca} بأمان؟","Open the listing and tap \"Contact Seller\" to start a direct in-app chat — no phone numbers are exposed, and there are no middlemen or commissions.","افتح الإعلان واضغط \"تواصل مع البائع\" لبدء محادثة مباشرة داخل التطبيق — بدون كشف أرقام الهاتف، وبدون وسطاء أو عمولات."),
     ("Are there new cars for sale in {ce} too?","هل توجد سيارات جديدة للبيع في {ca} أيضاً؟","Both. Individual sellers and dealers list new and used cars in {ce} — filter by condition to see exactly what you're looking for.","كلاهما. يعرض البائعون الأفراد والوكلاء سيارات جديدة ومستعملة في {ca} — صفِّ حسب الحالة لترى بالضبط ما تبحث عنه."),
   ],
   "cta_en":"Ready to Buy or Sell a Car in {ce}?","cta_ar":"مستعد لشراء أو بيع سيارة في {ca}؟",
   "cta_desc_en":"Join thousands of car buyers and sellers across Syria on Auto Bazar — it's free.","cta_desc_ar":"انضم لآلاف مشتري وبائعي السيارات في سوريا على أوتو بازار — التحميل مجاني.",
 },
 "real-estate": {
   "word_en":"Real Estate","word_ar":"عقارات",
   "badge_en":"Apartments, Houses & More","badge_ar":"شقق ومنازل والمزيد",
   "h1_en":"Real Estate for Sale & Rent in {ce}","h1_ar":"عقارات للبيع والإيجار في {ca}",
   "sub_en":"Buy, sell, or rent apartments and houses in {ce}, Syria — directly with owners",
   "sub_ar":"بيع أو شراء أو إيجار شقق ومنازل في {ca} — مباشرة مع المالكين",
   "desc_en":"Browse verified real estate listings in {ce} and across all 14 Syrian provinces. Filter apartments and houses by size, rooms, and price — then message the owner directly, with no commissions.",
   "desc_ar":"تصفح إعلانات عقارية موثقة في {ca} وفي جميع المحافظات السورية الـ 14. صفِّ الشقق والمنازل حسب المساحة وعدد الغرف والسعر — وتواصل مع المالك مباشرة، وبدون عمولات.",
   "steps":[
     ("Download & Sign Up","حمّل التطبيق وسجّل","Get Auto Bazar free on iOS or Android and verify your email in seconds.","حمّل أوتو بازار مجاناً على iOS أو Android وفعّل بريدك الإلكتروني في ثوانٍ."),
     ("List Your Property","أضف إعلان عقارك","Add type, size, rooms, price, {ce}, and clear photos of your apartment or house.","أضف النوع والمساحة وعدد الغرف والسعر ومدينة {ca} وصوراً واضحة لشقتك أو منزلك."),
     ("Chat with Buyers & Renters","تواصل مع المشترين والمستأجرين","Reach real buyers and renters in {ce} and negotiate directly in the app.","صِل إلى مشترين ومستأجرين حقيقيين في {ca} وتفاوض مباشرة داخل التطبيق."),
   ],
   "features":[
     ("Smart Filters","فلاتر ذكية","Search apartments and houses by size, rooms, and price to find exactly the property you want in {ce}.","ابحث عن شقق ومنازل حسب المساحة وعدد الغرف والسعر لتجد العقار الذي تريده بالضبط في {ca}."),
     ("Verified Owners","مالكون موثقون","Every account is email-verified and listings are reviewed to keep the marketplace trustworthy.","كل حساب موثق بالبريد الإلكتروني وتتم مراجعة الإعلانات للحفاظ على مصداقية السوق."),
     ("No Commissions","بدون عمولات","Message owners and renters directly in-app — Auto Bazar never takes a cut.","تواصل مع المالكين والمستأجرين مباشرة داخل التطبيق — أوتو بازار لا يأخذ أي عمولة."),
     ("Local to {ce}","محلي في {ca}","Filter to {ce} to see only property for sale or rent near you, or browse all 14 provinces.","صفِّ حسب {ca} لترى فقط العقارات للبيع أو الإيجار قربك، أو تصفح كل المحافظات الـ 14."),
   ],
   "faq":[
     ("How do I list an apartment or house in {ce}?","كيف أعلن عن شقة أو منزل في {ca}؟","Download Auto Bazar, create a free account, then tap \"+\" to list your property. Add type, size, rooms, price, and set the city to {ce}, then upload clear photos. Your listing reaches buyers and renters across Syria.","حمّل أوتو بازار، أنشئ حساباً مجانياً، ثم اضغط \"+\" لإضافة إعلان عقارك. أضف النوع والمساحة وعدد الغرف والسعر واختر مدينة {ca}، ثم ارفع صوراً واضحة. يصل إعلانك إلى مشترين ومستأجرين في كل سوريا."),
     ("Can I find apartments for rent in {ce}?","هل يمكنني إيجاد شقق للإيجار في {ca}؟","Yes. Filter listings by {ce} and by \"for rent\" to see only apartments and houses available to rent in the city.","نعم. صفِّ الإعلانات حسب {ca} وحسب \"للإيجار\" لتشاهد فقط الشقق والمنازل المتاحة للإيجار في المدينة."),
     ("Is it free to list property in {ce}?","هل نشر إعلان عقار في {ca} مجاني؟","Yes. You can post a limited number of real estate listings for free. Optional paid plans unlock extra slots and highlighted placement.","نعم. يمكنك نشر عدد محدود من الإعلانات العقارية مجاناً. خطط الاشتراك الاختيارية تفتح خانات إضافية وتمييز الإعلان."),
     ("How do I contact a property owner in {ce} safely?","كيف أتواصل مع مالك عقار في {ca} بأمان؟","Open the listing and tap \"Contact Seller\" to start a direct in-app chat — no phone numbers are exposed, and there are no middlemen.","افتح الإعلان واضغط \"تواصل مع البائع\" لبدء محادثة مباشرة داخل التطبيق — بدون كشف أرقام الهاتف، وبدون وسطاء."),
     ("Does Auto Bazar list land and farms in {ce} too?","هل يعرض أوتو بازار أراضٍ ومزارع في {ca} أيضاً؟","Yes. Alongside apartments and houses, you can browse farms and agricultural land for sale in {ce} in the Farms & Land category.","نعم. إلى جانب الشقق والمنازل، يمكنك تصفح المزارع والأراضي الزراعية للبيع في {ca} ضمن قسم المزارع والأراضي."),
   ],
   "cta_en":"Ready to Find a Home in {ce}?","cta_ar":"مستعد لإيجاد منزل في {ca}؟",
   "cta_desc_en":"Join thousands of buyers, sellers, and renters across Syria on Auto Bazar — it's free.","cta_desc_ar":"انضم لآلاف المشترين والبائعين والمستأجرين في سوريا على أوتو بازار — التحميل مجاني.",
 },
 "farms": {
   "word_en":"Farms & Land","word_ar":"مزارع وأراضٍ",
   "badge_en":"Agricultural Land Across Syria","badge_ar":"أراضٍ زراعية في كل سوريا",
   "h1_en":"Farms & Land for Sale in {ce}","h1_ar":"مزارع وأراضٍ للبيع في {ca}",
   "sub_en":"Buy and sell farms, orchards, and agricultural land in {ce}, Syria — directly with owners",
   "sub_ar":"بيع وشراء مزارع وبساتين وأراضٍ زراعية في {ca} — مباشرة مع المالكين",
   "desc_en":"Browse verified farm and agricultural land listings in {ce} and across all 14 Syrian provinces. Filter by size, water access, and price — then message the owner directly, with no commissions.",
   "desc_ar":"تصفح إعلانات مزارع وأراضٍ زراعية موثقة في {ca} وفي جميع المحافظات السورية الـ 14. صفِّ حسب المساحة وتوفر المياه والسعر — وتواصل مع المالك مباشرة، وبدون عمولات.",
   "steps":[
     ("Download & Sign Up","حمّل التطبيق وسجّل","Get Auto Bazar free on iOS or Android and verify your email in seconds.","حمّل أوتو بازار مجاناً على iOS أو Android وفعّل بريدك الإلكتروني في ثوانٍ."),
     ("List Your Land","أضف إعلان أرضك","Add land size, location in {ce}, water access, price, and clear photos.","أضف مساحة الأرض وموقعها في {ca} وتوفر المياه والسعر وصوراً واضحة."),
     ("Chat with Buyers","تواصل مع المشترين","Reach real buyers in {ce} and across Syria and negotiate directly in the app.","صِل إلى مشترين حقيقيين في {ca} وكل سوريا وتفاوض مباشرة داخل التطبيق."),
   ],
   "features":[
     ("Smart Filters","فلاتر ذكية","Search farms and agricultural land by size, water access, and price to find exactly the plot you want in {ce}.","ابحث عن مزارع وأراضٍ زراعية حسب المساحة وتوفر المياه والسعر لتجد القطعة التي تريدها بالضبط في {ca}."),
     ("Verified Owners","مالكون موثقون","Every account is email-verified and listings are reviewed to keep the marketplace trustworthy.","كل حساب موثق بالبريد الإلكتروني وتتم مراجعة الإعلانات للحفاظ على مصداقية السوق."),
     ("No Commissions","بدون عمولات","Message owners directly in-app — Auto Bazar never takes a cut of your land sale.","تواصل مع المالكين مباشرة داخل التطبيق — أوتو بازار لا يأخذ أي عمولة من بيع أرضك."),
     ("Local to {ce}","محلي في {ca}","Filter to {ce} to see only farms and land for sale near you, or browse all 14 provinces.","صفِّ حسب {ca} لترى فقط المزارع والأراضي للبيع قربك، أو تصفح كل المحافظات الـ 14."),
   ],
   "faq":[
     ("How do I sell my farm or land in {ce}?","كيف أبيع مزرعتي أو أرضي في {ca}؟","Download Auto Bazar, create a free account, then tap \"+\" to list your land. Add size, water access, price, and set the location to {ce}, then upload clear photos. Your listing reaches buyers across Syria.","حمّل أوتو بازار، أنشئ حساباً مجانياً، ثم اضغط \"+\" لإضافة إعلان أرضك. أضف المساحة وتوفر المياه والسعر واختر موقع {ca}، ثم ارفع صوراً واضحة. يصل إعلانك إلى مشترين في كل سوريا."),
     ("Can I find agricultural land for sale in {ce}?","هل يمكنني إيجاد أراضٍ زراعية للبيع في {ca}؟","Yes. Filter listings by {ce} to see only farms, orchards, and agricultural plots for sale in the area.","نعم. صفِّ الإعلانات حسب {ca} لتشاهد فقط المزارع والبساتين والقطع الزراعية المعروضة للبيع في المنطقة."),
     ("Is it free to list land in {ce}?","هل نشر إعلان أرض في {ca} مجاني؟","Yes. You can post a limited number of land listings for free. Optional paid plans unlock extra slots and highlighted placement.","نعم. يمكنك نشر عدد محدود من إعلانات الأراضي مجاناً. خطط الاشتراك الاختيارية تفتح خانات إضافية وتمييز الإعلان."),
     ("How do I contact a land owner in {ce} safely?","كيف أتواصل مع مالك أرض في {ca} بأمان؟","Open the listing and tap \"Contact Seller\" to start a direct in-app chat — no phone numbers are exposed, and there are no middlemen.","افتح الإعلان واضغط \"تواصل مع البائع\" لبدء محادثة مباشرة داخل التطبيق — بدون كشف أرقام الهاتف، وبدون وسطاء."),
     ("What kinds of land can I find in {ce}?","ما أنواع الأراضي التي يمكنني إيجادها في {ca}؟","Farms, orchards, and rural plots of every size are listed for sale in {ce} — filter by size and price to find the right one.","تُعرض مزارع وبساتين وقطع أرض ريفية بكل المساحات للبيع في {ca} — صفِّ حسب المساحة والسعر لتجد المناسبة."),
   ],
   "cta_en":"Ready to Buy or Sell Land in {ce}?","cta_ar":"مستعد لشراء أو بيع أرض في {ca}؟",
   "cta_desc_en":"Join thousands of buyers and sellers across Syria on Auto Bazar — it's free.","cta_desc_ar":"انضم لآلاف المشترين والبائعين في سوريا على أوتو بازار — التحميل مجاني.",
 },
 "car-rental": {
   "word_en":"Car Rental","word_ar":"تأجير سيارات",
   "badge_en":"Daily, Weekly & Monthly Rentals","badge_ar":"تأجير يومي وأسبوعي وشهري",
   "h1_en":"Car Rental in {ce}","h1_ar":"تأجير سيارات في {ca}",
   "sub_en":"Rent a car directly from owners and agencies in {ce}, Syria — by the day, week, or month",
   "sub_ar":"أجّر سيارة مباشرة من أصحابها أو من شركات التأجير في {ca} — باليوم أو الأسبوع أو الشهر",
   "desc_en":"Browse verified car rental listings in {ce} and across all 14 Syrian provinces. Filter by car type, rental period, and price — then message the owner directly, with no commissions.",
   "desc_ar":"تصفح إعلانات تأجير سيارات موثقة في {ca} وفي جميع المحافظات السورية الـ 14. صفِّ حسب نوع السيارة ومدة التأجير والسعر — وتواصل مع المالك مباشرة، وبدون عمولات.",
   "steps":[
     ("Download & Sign Up","حمّل التطبيق وسجّل","Get Auto Bazar free on iOS or Android and verify your email in seconds.","حمّل أوتو بازار مجاناً على iOS أو Android وفعّل بريدك الإلكتروني في ثوانٍ."),
     ("List Your Rental Car","أعلن عن سيارتك للتأجير","Add car type, rental period, price, {ce}, and clear photos.","أضف نوع السيارة ومدة التأجير والسعر ومدينة {ca} وصوراً واضحة."),
     ("Chat with Renters","تواصل مع المستأجرين","Reach real renters in {ce} and arrange pickup directly in the app.","صِل إلى مستأجرين حقيقيين في {ca} ونسّق الاستلام مباشرة داخل التطبيق."),
   ],
   "features":[
     ("Smart Filters","فلاتر ذكية","Search rental cars by type, rental period, and price to find exactly what you need in {ce}.","ابحث عن سيارات التأجير حسب النوع ومدة التأجير والسعر لتجد ما تحتاجه بالضبط في {ca}."),
     ("Verified Owners","مالكون موثقون","Every account is email-verified and listings are reviewed to keep the marketplace trustworthy.","كل حساب موثق بالبريد الإلكتروني وتتم مراجعة الإعلانات للحفاظ على مصداقية السوق."),
     ("No Commissions","بدون عمولات","Message owners and agencies directly in-app — Auto Bazar never takes a cut.","تواصل مع المالكين وشركات التأجير مباشرة داخل التطبيق — أوتو بازار لا يأخذ أي عمولة."),
     ("Local to {ce}","محلي في {ca}","Filter to {ce} to see only rental cars available near you, or browse all 14 provinces.","صفِّ حسب {ca} لترى فقط سيارات التأجير المتاحة قربك، أو تصفح كل المحافظات الـ 14."),
   ],
   "faq":[
     ("How do I rent a car in {ce}?","كيف أستأجر سيارة في {ca}؟","Download Auto Bazar, filter rentals by {ce}, choose a car and rental period, then tap \"Contact Seller\" to arrange pickup directly with the owner or agency.","حمّل أوتو بازار، صفِّ إعلانات التأجير حسب {ca}، اختر سيارة ومدة تأجير، ثم اضغط \"تواصل مع البائع\" لتنسيق الاستلام مباشرة مع المالك أو الشركة."),
     ("Can I list my car for rent in {ce}?","هل يمكنني عرض سيارتي للتأجير في {ca}؟","Yes. Create a free account, tap \"+\", add your car type, rental period, price, and set the city to {ce}, then upload photos.","نعم. أنشئ حساباً مجانياً، اضغط \"+\", أضف نوع سيارتك ومدة التأجير والسعر واختر مدينة {ca}، ثم ارفع الصور."),
     ("Is it free to list a rental car in {ce}?","هل عرض سيارة للتأجير في {ca} مجاني؟","Yes. You can post a limited number of rental listings for free. Optional paid plans unlock extra slots and highlighted placement.","نعم. يمكنك نشر عدد محدود من إعلانات التأجير مجاناً. خطط الاشتراك الاختيارية تفتح خانات إضافية وتمييز الإعلان."),
     ("How do I contact a car owner in {ce} safely?","كيف أتواصل مع صاحب سيارة في {ca} بأمان؟","Open the listing and tap \"Contact Seller\" to start a direct in-app chat — no phone numbers are exposed, and there are no middlemen.","افتح الإعلان واضغط \"تواصل مع البائع\" لبدء محادثة مباشرة داخل التطبيق — بدون كشف أرقام الهاتف، وبدون وسطاء."),
     ("Can I rent by the day, week, or month in {ce}?","هل يمكنني التأجير باليوم أو الأسبوع أو الشهر في {ca}؟","Yes. Owners and agencies in {ce} offer daily, weekly, and monthly rentals — filter by rental period to match your needs.","نعم. يقدّم المالكون وشركات التأجير في {ca} تأجيراً يومياً وأسبوعياً وشهرياً — صفِّ حسب مدة التأجير لتناسب احتياجك."),
   ],
   "cta_en":"Ready to Rent a Car in {ce}?","cta_ar":"مستعد لتأجير سيارة في {ca}؟",
   "cta_desc_en":"Join thousands of renters and owners across Syria on Auto Bazar — it's free.","cta_desc_ar":"انضم لآلاف المستأجرين والمالكين في سوريا على أوتو بازار — التحميل مجاني.",
 },
}

# meta title/description/keywords per category (city-injected)
def meta_title(cat, ce, ca):
    m = {
      "cars": f"سيارات للبيع في {ca} | جديدة ومستعملة | أوتو بازار",
      "real-estate": f"عقارات للبيع والإيجار في {ca} | شقق ومنازل | أوتو بازار",
      "farms": f"مزارع وأراضٍ للبيع في {ca} | أراضٍ زراعية | أوتو بازار",
      "car-rental": f"تأجير سيارات في {ca} | يومي وأسبوعي وشهري | أوتو بازار",
    }
    return m[cat]

def meta_desc(cat, ce, ca):
    m = {
      "cars": f"سيارات للبيع في {ca} على أوتو بازار — سيارات جديدة ومستعملة، فلاتر حسب الشركة والطراز والسنة والسعر، وتواصل مباشر مع البائع بدون وسطاء. Cars for sale in {ce}, Syria.",
      "real-estate": f"عقارات للبيع والإيجار في {ca} على أوتو بازار — شقق ومنازل، فلاتر حسب المساحة والغرف والسعر، وتواصل مباشر مع المالك بدون عمولات. Real estate for sale & rent in {ce}, Syria.",
      "farms": f"مزارع وأراضٍ زراعية للبيع في {ca} على أوتو بازار — بساتين وقطع أرض ريفية، فلاتر حسب المساحة والمياه والسعر، وتواصل مباشر مع المالك. Farms & land for sale in {ce}, Syria.",
      "car-rental": f"تأجير سيارات في {ca} على أوتو بازار — تأجير يومي وأسبوعي وشهري مباشرة من الأصحاب وشركات التأجير بدون عمولات. Car rental in {ce}, Syria.",
    }
    return m[cat]

def meta_keywords(cat, ce, ca):
    m = {
      "cars": f"سيارات للبيع في {ca}, سيارات مستعملة {ca}, شراء سيارات {ca}, بيع سيارات {ca}, سوق سيارات {ca}, cars for sale {ce}, used cars {ce} Syria",
      "real-estate": f"عقارات للبيع في {ca}, شقق للايجار {ca}, منازل للبيع {ca}, عقارات {ca}, real estate {ce} Syria, apartments for rent {ce}",
      "farms": f"مزارع للبيع في {ca}, أراضي زراعية {ca}, أرض للبيع {ca}, بساتين {ca}, farms for sale {ce}, agricultural land {ce} Syria",
      "car-rental": f"تأجير سيارات في {ca}, ايجار سيارات {ca}, تاجير سيارة {ca}, car rental {ce}, rent a car {ce} Syria",
    }
    return m[cat]

NAV = '''  <!-- ====== NAVBAR ====== -->
  <header class="navbar">
    <div class="nav-inner">
      <div class="nav-logo-side">
        <a href="/" class="nav-logo">
          <img src="/logo-small.png" width="128" height="128" alt="Auto Bazar">
          <span class="nav-logo-text"><span class="lang-en">Auto Bazar</span><span class="lang-ar">أوتو بازار</span></span>
        </a>
      </div>
      <nav class="nav-links">
        <a href="/" class="nav-link"><span class="lang-en">Home</span><span class="lang-ar">الرئيسية</span></a>
        <a href="/#categories" class="nav-link"><span class="lang-en">Categories</span><span class="lang-ar">الأقسام</span></a>
        <a href="/privacy" class="nav-link"><span class="lang-en">Privacy</span><span class="lang-ar">الخصوصية</span></a>
        <a href="/terms" class="nav-link"><span class="lang-en">Terms</span><span class="lang-ar">الشروط</span></a>
        <a href="/support" class="nav-link"><span class="lang-en">Support</span><span class="lang-ar">الدعم</span></a>
      </nav>
      <div class="nav-actions-side">
        <div class="desktop-only" style="display:flex;gap:12px;align-items:center;">
          <a href="/dashboard" class="btn-primary" style="padding:8px 18px;font-size:0.83rem;border-radius:100px;text-decoration:none">
            <span class="lang-en">My Account</span><span class="lang-ar">حسابي</span>
          </a>
          <button class="theme-toggle" id="theme-toggle-btn" onclick="toggleTheme()" aria-label="Toggle theme"></button>
          <button onclick="toggleLang()" aria-label="تبديل اللغة | Switch language" class="lang-toggle lang-btn"></button>
        </div>
        <div class="mobile-only">
          <button id="theme-toggle-btn-m" class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle theme"></button>
          <button onclick="toggleLang()" aria-label="تبديل اللغة | Switch language" class="lang-toggle lang-btn"></button>
          <button class="hamburger" onclick="toggleMenu()" aria-label="Menu"><span></span><span></span><span></span></button>
        </div>
      </div>
    </div>
    <div class="mobile-menu">
      <a href="/"><span class="lang-en">Home</span><span class="lang-ar">الرئيسية</span></a>
      <a href="/#categories"><span class="lang-en">Categories</span><span class="lang-ar">الأقسام</span></a>
      <a href="/privacy"><span class="lang-en">Privacy</span><span class="lang-ar">الخصوصية</span></a>
      <a href="/terms"><span class="lang-en">Terms</span><span class="lang-ar">الشروط</span></a>
      <a href="/support"><span class="lang-en">Support</span><span class="lang-ar">الدعم</span></a>
      <a href="/dashboard"><span class="lang-en">My Account</span><span class="lang-ar">حسابي</span></a>
    </div>
  </header>
'''

FOOTER = '''  <footer class="footer-wrap">
    <div class="footer-inner">
      <div class="footer-grid">
        <div>
          <div class="footer-logo">
            <img src="/logo-small.png" width="128" height="128" alt="Auto Bazar">
            <span><span class="lang-en">Auto Bazar</span><span class="lang-ar">أوتو بازار</span></span>
          </div>
          <p class="footer-desc">
            <span class="lang-en">Syria's all-in-one marketplace for cars, real estate & car rentals. Connecting buyers and sellers across 14 provinces.</span>
            <span class="lang-ar">سوق سوريا الشامل للسيارات والعقارات وتأجير السيارات. نربط بين المشترين والبائعين في 14 محافظة.</span>
          </p>
        </div>
        <div>
          <p class="footer-heading"><span class="lang-en">Categories</span><span class="lang-ar">الأقسام</span></p>
          <div class="footer-links">
            <a href="/cars"><span class="lang-en">Cars</span><span class="lang-ar">سيارات</span></a>
            <a href="/real-estate"><span class="lang-en">Real Estate</span><span class="lang-ar">عقارات</span></a>
            <a href="/farms"><span class="lang-en">Farms & Land</span><span class="lang-ar">مزارع وأراضٍ</span></a>
            <a href="/car-rental"><span class="lang-en">Car Rental</span><span class="lang-ar">تأجير سيارات</span></a>
          </div>
        </div>
        <div>
          <p class="footer-heading"><span class="lang-en">Pages</span><span class="lang-ar">الصفحات</span></p>
          <div class="footer-links">
            <a href="/"><span class="lang-en">Home</span><span class="lang-ar">الرئيسية</span></a>
            <a href="/privacy"><span class="lang-en">Privacy Policy</span><span class="lang-ar">سياسة الخصوصية</span></a>
            <a href="/terms"><span class="lang-en">Terms of Service</span><span class="lang-ar">شروط الاستخدام</span></a>
            <a href="/support"><span class="lang-en">Support</span><span class="lang-ar">الدعم</span></a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <span class="lang-en">&copy; 2026 <span class="lang-en">Auto Bazar</span><span class="lang-ar">أوتو بازار</span>. All rights reserved.</span>
        <span class="lang-ar">&copy; 2026 <span class="lang-en">Auto Bazar</span><span class="lang-ar">أوتو بازار</span>. جميع الحقوق محفوظة.</span>
      </div>
    </div>
  </footer>
'''

APPLE_SVG = '<path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z" />'
GP_SVG = '<path d="M3.609 1.814L13.792 12 3.61 22.186a.996.996 0 01-.61-.92V2.734a1 1 0 01.609-.92zm10.89 10.893l2.302 2.302-10.937 6.333 8.635-8.635zm3.199-3.199l2.302 2.302c.7.4.7 1.08 0 1.48l-2.302 1.302-2.531-2.535 2.531-2.549zM5.864 2.658L16.8 8.99l-2.302 2.302L5.864 2.658z" />'
SEARCH_SVG = '<path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />'
SHIELD_SVG = '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />'
CHAT_SVG = '<path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z" />'
PIN_SVG = '<path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" /><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />'
FEATURE_SVGS = [SEARCH_SVG, SHIELD_SVG, CHAT_SVG, PIN_SVG]

CAT_LABELS = {
  "cars": ("Cars","سيارات"),
  "real-estate": ("Real Estate","عقارات"),
  "farms": ("Farms & Land","مزارع وأراضٍ"),
  "car-rental": ("Car Rental","تأجير سيارات"),
}

def fmt(s, ce, ca):
    return s.replace("{ce}", ce).replace("{ca}", ca)

def build_page(cat, city):
    slug_city, ce, ca = city
    c = CATS[cat]
    url = f"{DOMAIN}/{cat}-{slug_city}"
    campaign = f"{cat.replace('-','_')}_{slug_city.replace('-','_')}_page"
    title = meta_title(cat, ce, ca)
    desc = meta_desc(cat, ce, ca)
    kw = meta_keywords(cat, ce, ca)
    word_en, word_ar = CAT_LABELS[cat]

    # steps
    steps_html = ""
    for i,(te,ta,be,ba) in enumerate(c["steps"],1):
        steps_html += f'''        <div class="step-card fade-in">
          <div class="step-num">{i}</div>
          <h3><span class="lang-en">{fmt(te,ce,ca)}</span><span class="lang-ar">{fmt(ta,ce,ca)}</span></h3>
          <p><span class="lang-en">{fmt(be,ce,ca)}</span><span class="lang-ar">{fmt(ba,ce,ca)}</span></p>
        </div>
'''
    # features
    feats_html = ""
    for idx,(te,ta,be,ba) in enumerate(c["features"]):
        svg = FEATURE_SVGS[idx % len(FEATURE_SVGS)]
        feats_html += f'''        <div class="feature-card fade-in">
          <div class="feature-icon">
            <svg fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">{svg}</svg>
          </div>
          <h3><span class="lang-en">{fmt(te,ce,ca)}</span><span class="lang-ar">{fmt(ta,ce,ca)}</span></h3>
          <p><span class="lang-en">{fmt(be,ce,ca)}</span><span class="lang-ar">{fmt(ba,ce,ca)}</span></p>
        </div>
'''
    # faq + jsonld
    faq_html = ""
    faq_json = []
    for (qe,qa,ae,aa) in c["faq"]:
        qe,qa,ae,aa = fmt(qe,ce,ca),fmt(qa,ce,ca),fmt(ae,ce,ca),fmt(aa,ce,ca)
        faq_html += f'''        <details class="faq-item fade-in">
          <summary class="faq-question">
            <span class="lang-en">{qe}</span>
            <span class="lang-ar">{qa}</span>
          </summary>
          <p class="faq-answer">
            <span class="lang-en">{ae}</span>
            <span class="lang-ar">{aa}</span>
          </p>
        </details>
'''
        faq_json.append({"@type":"Question","name":qa,"acceptedAnswer":{"@type":"Answer","text":aa}})

    # cross-links: other categories in same city
    other_cats = [x for x in ["cars","real-estate","farms","car-rental"] if x != cat]
    oc_html = ""
    for oc in other_cats:
        oe, oa = CAT_LABELS[oc]
        oc_html += f'''        <a href="/{oc}-{slug_city}" class="feature-card fade-in">
          <h3><span class="lang-en">{oe} in {ce}</span><span class="lang-ar">{oa} في {ca}</span></h3>
        </a>
'''
    # same category, other cities
    other_cities = [x for x in CITIES if x[0] != slug_city]
    city_links_en = ""
    city_links_ar = ""
    for (sc, oce, oca) in other_cities:
        city_links_en += f'<a href="/{cat}-{sc}">{word_en} in {oce}</a>'
        city_links_ar += f'<a href="/{cat}-{sc}">{word_ar} في {oca}</a>'

    # JSON-LD
    ld = {
      "@context":"https://schema.org",
      "@graph":[
        {"@type":"BreadcrumbList","itemListElement":[
          {"@type":"ListItem","position":1,"name":"الرئيسية","item":f"{DOMAIN}/"},
          {"@type":"ListItem","position":2,"name":word_ar,"item":f"{DOMAIN}/{cat}"},
          {"@type":"ListItem","position":3,"name":f"{word_ar} في {ca}","item":url}
        ]},
        {"@type":"FAQPage","mainEntity":faq_json}
      ]
    }
    ld_str = json.dumps(ld, ensure_ascii=False, indent=2)

    hero_badge_en = fmt(c["badge_en"],ce,ca)
    hero_badge_ar = fmt(c["badge_ar"],ce,ca)

    html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="/favicon.png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <!-- ====== PRIMARY SEO ====== -->
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{kw}">
  <meta name="robots" content="index, follow">
  <meta name="author" content="Auto Bazar - El-Enjaz">
  <meta name="theme-color" content="#059669" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0a0a0f" media="(prefers-color-scheme: dark)">
  <link rel="canonical" href="{url}">

  <!-- ====== HREFLANG (Bilingual) ====== -->
  <link rel="alternate" hreflang="ar" href="{url}">
  <link rel="alternate" hreflang="en" href="{url}">
  <link rel="alternate" hreflang="x-default" href="{url}">

  <!-- ====== OPEN GRAPH ====== -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Auto Bazar | أوتو بازار">
  <meta property="og:locale" content="ar_SY">
  <meta property="og:locale:alternate" content="en_US">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{DOMAIN}/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{fmt(c['h1_ar'],ce,ca)} - أوتو بازار">

  <!-- ====== TWITTER CARD ====== -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{DOMAIN}/og-image.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Arabic:wght@400;500;600;700;800;900&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Arabic:wght@400;500;600;700;800;900&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Arabic:wght@400;500;600;700;800;900&display=swap"></noscript>
  <script>
    (function () {{ var s = localStorage.getItem('ab-theme'), d = window.matchMedia('(prefers-color-scheme:dark)').matches; document.documentElement.setAttribute('data-theme', s || (d ? 'dark' : 'light')); }})();
  </script>
  <script>(function(){{var l=localStorage.getItem('lang')||'ar',d=document.documentElement;d.lang=l;d.dir=l==='ar'?'rtl':'ltr';}})();</script>
  <link rel="stylesheet" href="css/style.css?v={CSSV}">
  <noscript>
    <style>
      .fade-in {{ opacity: 1 !important; transform: none !important; }}
    </style>
  </noscript>
</head>

<body>

{NAV}
  <main>

  <!-- ====== HERO ====== -->
  <section class="hero">
    <div class="aurora aurora-1"></div>
    <div class="aurora aurora-2"></div>
    <div class="hero-content">
      <div class="hero-badge">
        <span class="dot"></span>
        <span class="lang-en">{hero_badge_en}</span>
        <span class="lang-ar">{hero_badge_ar}</span>
      </div>
      <h1 class="hero-title">
        <span class="lang-en">{fmt(c['h1_en'],ce,ca)}</span><span class="lang-ar">{fmt(c['h1_ar'],ce,ca)}</span>
      </h1>
      <p class="hero-sub">
        <span class="lang-en">{fmt(c['sub_en'],ce,ca)}</span>
        <span class="lang-ar">{fmt(c['sub_ar'],ce,ca)}</span>
      </p>
      <p class="hero-desc">
        <span class="lang-en">{fmt(c['desc_en'],ce,ca)}</span>
        <span class="lang-ar">{fmt(c['desc_ar'],ce,ca)}</span>
      </p>
      <div class="hero-cta">
        <a href="{APPLE}" class="btn-primary" target="_blank" rel="noopener" aria-label="Download Auto Bazar on App Store">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">{APPLE_SVG}</svg>
          <span class="lang-en">App Store</span><span class="lang-ar">آب ستور</span>
        </a>
        <a href="{gplay(campaign)}" class="btn-secondary" target="_blank" rel="noopener" aria-label="Download Auto Bazar on Google Play">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">{GP_SVG}</svg>
          <span class="lang-en">Google Play</span><span class="lang-ar">جوجل بلاي</span>
        </a>
      </div>
    </div>
  </section>

  <!-- ====== HOW IT WORKS ====== -->
  <div class="section-wrap">
    <div class="section" style="text-align:center;">
      <div class="fade-in" style="max-width:560px;margin:0 auto;">
        <p class="section-label"><span class="lang-en">In {ce}, Syria</span><span class="lang-ar">في {ca}</span></p>
        <h2 class="section-title">
          <span class="lang-en">Get Started in 3 Simple Steps</span>
          <span class="lang-ar">ابدأ في 3 خطوات بسيطة</span>
        </h2>
        <p class="section-desc" style="margin:0 auto;">
          <span class="lang-en">From download to your first listing in under 5 minutes.</span>
          <span class="lang-ar">من التحميل إلى أول إعلان في أقل من 5 دقائق.</span>
        </p>
      </div>
      <div class="steps-grid">
{steps_html}      </div>
    </div>
  </div>

  <!-- ====== WHY ====== -->
  <div class="section-wrap section-wrap-alt">
    <div class="section">
      <div class="fade-in">
        <p class="section-label"><span class="lang-en">Why Auto Bazar</span><span class="lang-ar">لماذا أوتو بازار</span></p>
        <h2 class="section-title">
          <span class="lang-en">{word_en} in {ce}, Made Simple</span>
          <span class="lang-ar">{word_ar} في {ca} بكل سهولة</span>
        </h2>
      </div>
      <div class="cards-grid">
{feats_html}      </div>
    </div>
  </div>

  <!-- ====== FAQ ====== -->
  <div class="section-wrap">
    <div class="section" style="text-align:center;">
      <div class="fade-in" style="max-width:560px;margin:0 auto;">
        <p class="section-label"><span class="lang-en">Got Questions?</span><span class="lang-ar">أسئلة شائعة</span></p>
        <h2 class="section-title">
          <span class="lang-en">{word_en} in {ce} — FAQ</span>
          <span class="lang-ar">أسئلة شائعة عن {word_ar} في {ca}</span>
        </h2>
      </div>
      <div class="faq-list" style="text-align:right;">
{faq_html}      </div>
    </div>
  </div>

  <!-- ====== OTHER CATEGORIES IN CITY ====== -->
  <div class="section-wrap section-wrap-alt">
    <div class="section" style="text-align:center;">
      <p class="section-label"><span class="lang-en">More in {ce}</span><span class="lang-ar">المزيد في {ca}</span></p>
      <h2 class="section-title">
        <span class="lang-en">Explore Other Categories in {ce}</span>
        <span class="lang-ar">تصفح الأقسام الأخرى في {ca}</span>
      </h2>
      <div class="cards-grid" style="margin-top:24px;">
{oc_html}      </div>
    </div>
  </div>

  <!-- ====== SAME CATEGORY OTHER CITIES ====== -->
  <div class="section-wrap">
    <div class="section" style="text-align:center;">
      <p class="section-label"><span class="lang-en">Other Cities</span><span class="lang-ar">مدن أخرى</span></p>
      <h2 class="section-title">
        <span class="lang-en">{word_en} in Other Syrian Cities</span>
        <span class="lang-ar">{word_ar} في مدن سورية أخرى</span>
      </h2>
      <div class="footer-links" style="flex-flow:row wrap;justify-content:center;gap:14px 22px;margin-top:20px;">
        <span class="lang-en" style="display:contents">{city_links_en}</span>
        <span class="lang-ar" style="display:contents">{city_links_ar}</span>
      </div>
    </div>
  </div>

  <!-- ====== CTA ====== -->
  <section class="cta-section">
    <div class="cta-inner fade-in">
      <h2 class="cta-title">
        <span class="lang-en">{fmt(c['cta_en'],ce,ca)}</span>
        <span class="lang-ar">{fmt(c['cta_ar'],ce,ca)}</span>
      </h2>
      <p class="cta-desc">
        <span class="lang-en">{fmt(c['cta_desc_en'],ce,ca)}</span>
        <span class="lang-ar">{fmt(c['cta_desc_ar'],ce,ca)}</span>
      </p>
      <div class="cta-btn-group">
        <a href="{APPLE}" class="btn-white" target="_blank" rel="noopener" aria-label="Download Auto Bazar on App Store">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">{APPLE_SVG}</svg>
          <span class="lang-en">App Store</span><span class="lang-ar">آب ستور</span>
        </a>
        <a href="{gplay(campaign)}" class="btn-white-outline" target="_blank" rel="noopener" aria-label="Download Auto Bazar on Google Play">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">{GP_SVG}</svg>
          <span class="lang-en">Google Play</span><span class="lang-ar">جوجل بلاي</span>
        </a>
      </div>
    </div>
  </section>

  </main>

{FOOTER}
  <script src="js/lang.js"></script>
  <script src="js/theme.js"></script>

  <!-- ====== STRUCTURED DATA (JSON-LD) ====== -->
  <script type="application/ld+json">
{ld_str}
  </script>

</body>

</html>
'''
    return f"{cat}-{slug_city}.html", html

count = 0
urls = []
for cat in ["cars","real-estate","farms","car-rental"]:
    for city in CITIES:
        fname, html = build_page(cat, city)
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        urls.append(f"{DOMAIN}/{fname[:-5]}")
        count += 1

print(f"Generated {count} pages")
for u in urls: print(u)
