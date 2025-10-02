from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- Настройка CORS ---
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ДАННЫЕ ---

categories = [
    {"id": 1, "name": "Woman's Fashion"},
    {"id": 2, "name": "Men's Fashion"},
    {"id": 3, "name": "Electronics"},
    {"id": 4, "name": "Home & Lifestyle"},
    {"id": 5, "name": "Medicine"},
    {"id": 6, "name": "Sports & Outdoor"},
    {"id": 7, "name": "Baby's & Toys"},
    {"id": 8, "name": "Groceries & Pets"},
    {"id": 9, "name": "Health & Beauty"}
]

products = [
    # 1. Woman's Fashion
    {'id': 1, 'categoryId': 1, 'name': 'ZARA Linen Blend Dress', 'price': 49.99, 'oldPrice': 65, 'rating': 4.5, 'reviewCount': 88, 'description': 'Lightweight linen blend dress, perfect for summer.', 'image': 'https://www.pngplay.com/image/111971'},
    {'id': 2, 'categoryId': 1, 'name': 'H&M Oversized Hoodie', 'price': 29.99, 'oldPrice': 40, 'rating': 4.2, 'reviewCount': 120, 'description': 'Casual oversized hoodie with soft cotton material.', 'image': 'https://lp2.hm.com/hmgoepprod?set=source[/c6/88/c688dc5b60a7f0caa9dc1231d7f3c18bdfdd35c2.jpg]'},
    {'id': 3, 'categoryId': 1, 'name': 'Nike Air Max 270 React', 'price': 149.95, 'oldPrice': 180, 'rating': 4.8, 'reviewCount': 210, 'description': 'Trendy and comfortable sneakers with modern design.', 'image': 'https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/3b267a36-52e4-4c40-a28e-fdc0e3f0f5c7/air-max-270-womens-shoes-KkLcGR.png'},
    {'id': 4, 'categoryId': 1, 'name': 'Adidas Sports Bra', 'price': 34.90, 'oldPrice': 45, 'rating': 4.7, 'reviewCount': 95, 'description': 'Supportive sports bra suitable for training and yoga.', 'image': 'https://assets.adidas.com/images/w_600,f_auto,q_auto/85b8dcf9d6544c87a95aab1100c7aeca_9366/Powerreact_Training_Medium-Support_Bra_Black_IC2358_01_laydown.jpg'},
    {'id': 5, 'categoryId': 1, 'name': 'Mango Leather Jacket', 'price': 199.99, 'oldPrice': 250, 'rating': 4.9, 'reviewCount': 150, 'description': 'Classic biker-style leather jacket.', 'image': 'https://st.mngbcn.com/rcs/pics/static/T4/fotos/S20/47078649_99.jpg?ts=1689235966082'},
    {'id': 6, 'categoryId': 1, 'name': 'Uniqlo Down Jacket', 'price': 79.90, 'oldPrice': 100, 'rating': 4.6, 'reviewCount': 180, 'description': 'Warm yet lightweight down jacket for everyday wear.', 'image': 'https://image.uniqlo.com/UQ/ST3/WesternCommon/imagesgoods/455933/item/goods_69_455933.jpg'},
    {'id': 7, 'categoryId': 1, 'name': 'Pull&Bear Skinny Jeans', 'price': 39.99, 'oldPrice': 50, 'rating': 4.3, 'reviewCount': 110, 'description': 'High-rise skinny jeans with stretch denim.', 'image': 'https://static.pullandbear.net/2/photos//2023/I/0/1/p/5680/456/427/5680456427_2_3_8.jpg?t=1684926366799'},
    {'id': 8, 'categoryId': 1, 'name': 'Calvin Klein T-shirt', 'price': 44.50, 'oldPrice': 55, 'rating': 4.5, 'reviewCount': 130, 'description': 'Basic white T-shirt with Calvin Klein logo.', 'image': 'https://calvinklein.scene7.com/is/image/CalvinKlein/000QS6739E100_FNT'},
    {'id': 9, 'categoryId': 1, 'name': 'Gucci Sunglasses', 'price': 299.00, 'oldPrice': 350, 'rating': 5.0, 'reviewCount': 200, 'description': 'Stylish oversized sunglasses with UV protection.', 'image': 'https://media.gucci.com/style/DarkGray_Center_0_0_800x800/1601922903/623903_J0740_1016_001_100_0000_Light.jpg'},
    {'id': 10, 'categoryId': 1, 'name': 'Levi\'s 501 Original Jeans', 'price': 109.00, 'oldPrice': 120, 'rating': 4.7, 'reviewCount': 250, 'description': 'Classic Levi\'s straight fit jeans.', 'image': 'https://lsco.scene7.com/is/image/lsco/005010114-front-pdp'},

    # 2. Men's Fashion
    {'id': 11, 'categoryId': 2, 'name': 'The North Face 1996 Retro Nuptse Jacket', 'price': 280.00, 'oldPrice': 320, 'rating': 4.8, 'reviewCount': 190, 'description': 'Iconic puffer jacket for cold weather.', 'image': 'https://images.thenorthface.com/is/image/TheNorthFace/NF0A3C8D_JK3_hero'},
    {'id': 12, 'categoryId': 2, 'name': 'Polo Ralph Lauren Classic Fit Polo Shirt', 'price': 98.50, 'oldPrice': 110, 'rating': 4.9, 'reviewCount': 300, 'description': 'Signature mesh polo shirt.', 'image': 'https://www.ralphlauren.com/dw/image/v2/BFDH_PRD/on/demandware.static/-/Sites-RalphLauren_US-master-catalog/default/dw1ea2b647/POLO/202206/04_202206/20220601-m-polo-shop/20220601-m-polo-shop-header-polo-shirt-img.jpg'},
    {'id': 13, 'categoryId': 2, 'name': 'New Balance 550 Sneakers', 'price': 110.00, 'oldPrice': 120, 'rating': 4.7, 'reviewCount': 220, 'description': 'Retro-style basketball sneakers.', 'image': 'https://nb.scene7.com/is/image/NB/bb550sea_nb_02_i'},
    {'id': 14, 'categoryId': 2, 'name': 'Carhartt WIP Cargo Pants', 'price': 125.00, 'oldPrice': 140, 'rating': 4.6, 'reviewCount': 180, 'description': 'Durable and functional cargo pants.', 'image': 'https://i1.adis.ws/i/carhartt_wip/I025932_89_02/i-wip-regular-cargo-pant-black-rinsed-2.jpg'},
    {'id': 15, 'categoryId': 2, 'name': 'G-Shock GA2100-1A1 Watch', 'price': 99.00, 'oldPrice': 110, 'rating': 4.9, 'reviewCount': 450, 'description': 'Tough and stylish analog-digital watch.', 'image': 'https://www.gshock.com/content/dam/casio/product-info/watches/g-shock/en-us/product-images/GA-2100-1A1/GA-2100-1A1_l-1.png.transform/main-l/image.png'},
    {'id': 16, 'categoryId': 2, 'name': 'Ray-Ban Aviator Classic Sunglasses', 'price': 161.00, 'oldPrice': 200, 'rating': 4.8, 'reviewCount': 350, 'description': 'Timeless aviator sunglasses.', 'image': 'https://india.ray-ban.com/media/catalog/product/0/r/0rb3025l020558_1.jpg'},
    {'id': 17, 'categoryId': 2, 'name': 'Tommy Hilfiger Oxford Shirt', 'price': 89.50, 'oldPrice': 100, 'rating': 4.5, 'reviewCount': 140, 'description': 'Classic long-sleeve oxford shirt.', 'image': 'https://lp.tommy.com/common/dam/assets/2023/q4/p2/campaign/holiday-main/eu/lp-design/men/04-category-nav-men.jpg'},
    {'id': 18, 'categoryId': 2, 'name': 'Champion Reverse Weave Sweatshirt', 'price': 60.00, 'oldPrice': 75, 'rating': 4.7, 'reviewCount': 160, 'description': 'Heavyweight fleece sweatshirt.', 'image': 'https://champion.imgix.net/catalog/product/h/n/hny_gf70y06145bkcc_black_front.jpg'},
    {'id': 19, 'categoryId': 2, 'name': 'Vans Old Skool Shoes', 'price': 65.00, 'oldPrice': 70, 'rating': 4.8, 'reviewCount': 400, 'description': 'Iconic skate shoes with the classic sidestripe.', 'image': 'https://images.vans.com/is/image/Vans/VN000D3HY28-HERO'},
    {'id': 20, 'categoryId': 2, 'name': 'Patagonia Baggies Shorts', 'price': 55.00, 'oldPrice': 60, 'rating': 4.9, 'reviewCount': 280, 'description': 'Versatile shorts for water and land.', 'image': 'https://www.patagonia.com/dw/image/v2/BDJB_PRD/on/demandware.static/-/Sites-patagonia-master/default/dwe729a43a/images/hi-res/57022_BLK.jpg'},

    # 3. Electronics
    {'id': 21, 'categoryId': 3, 'name': 'Apple iPhone 14 Pro', 'price': 999.00, 'oldPrice': 1099, 'rating': 4.9, 'reviewCount': 1200, 'description': 'The latest iPhone with Pro camera system.', 'image': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-finish-select-202209-6-1inch-deeppurple'},
    {'id': 22, 'categoryId': 3, 'name': 'MacBook Pro 14" (M2 Chip)', 'price': 1999.00, 'oldPrice': 2199, 'rating': 5.0, 'reviewCount': 800, 'description': 'Powerful laptop for professionals.', 'image': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp-14-digitalmat-gallery-1-202310'},
    {'id': 23, 'categoryId': 3, 'name': 'Sony WH-1000XM5 Headphones', 'price': 399.99, 'oldPrice': 450, 'rating': 4.8, 'reviewCount': 950, 'description': 'Industry-leading noise-canceling headphones.', 'image': 'https://www.sony.com/image/5d02da5df55283f2426d085a2c381ef9?fmt=pjpeg&wid=330&bgcolor=FFFFFF&bgc=FFFFFF'},
    {'id': 24, 'categoryId': 3, 'name': 'Samsung Odyssey G9 Gaming Monitor', 'price': 1399.99, 'oldPrice': 1599, 'rating': 4.7, 'reviewCount': 550, 'description': 'Super ultrawide curved gaming monitor.', 'image': 'https://image-us.samsung.com/SamsungUS/home/computing/monitors/gaming-monitors/pdp/ls49ag952nnxza/gallery/LS49AG952NNXZA_01_700x570.jpg'},
    {'id': 25, 'categoryId': 3, 'name': 'Apple Watch Ultra 2', 'price': 799.00, 'oldPrice': 849, 'rating': 4.9, 'reviewCount': 600, 'description': 'The most rugged and capable Apple Watch ever.', 'image': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/apple-watch-ultra-2-finish-select-202309-49mm-trail-loop-blue-black'},
    {'id': 26, 'categoryId': 3, 'name': 'GoPro HERO11 Black', 'price': 499.99, 'oldPrice': 550, 'rating': 4.6, 'reviewCount': 480, 'description': 'Waterproof action camera with 5.3K video.', 'image': 'https://gopro.com/dw/image/v2/BFFJ_PRD/on/demandware.static/-/Sites-gopro-products/default/dwd3485075/product-assets/hero11-black/images/HERO11-Black-front_3-4-med.png'},
    {'id': 27, 'categoryId': 3, 'name': 'Bose SoundLink Revolve+ II', 'price': 329.00, 'oldPrice': 350, 'rating': 4.8, 'reviewCount': 700, 'description': '360° portable Bluetooth speaker.', 'image': 'https://assets.bose.com/content/dam/Bose_DAM/Web/consumer_electronics/global/products/speakers/soundlink_revolve_plus_ii/product_silo_images/soundlink_revolve_plus_ii_triple_black_EC_00.png/jcr:content/renditions/cq5dam.web.320.320.png'},
    {'id': 28, 'categoryId': 3, 'name': 'Logitech MX Master 3S Mouse', 'price': 99.99, 'oldPrice': 120, 'rating': 4.9, 'reviewCount': 1500, 'description': 'Advanced wireless mouse for creatives and coders.', 'image': 'https://resource.logitech.com/w_386,ar_1.0,c_limit,q_auto,f_auto,dpr_2.0/d_transparent.gif/content/dam/logitech/en/products/mice/mx-master-3s/gallery/mx-master-3s-mouse-top-view-graphite.png'},
    {'id': 29, 'categoryId': 3, 'name': 'Amazon Kindle Paperwhite', 'price': 139.99, 'oldPrice': 150, 'rating': 4.7, 'reviewCount': 25000, 'description': 'Waterproof e-reader with a 6.8" display.', 'image': 'https://m.media-amazon.com/images/I/41-j47TfD3L._AC_SY350_.jpg'},
    {'id': 30, 'categoryId': 3, 'name': 'Anker PowerCore 26800 Power Bank', 'price': 69.99, 'oldPrice': 80, 'rating': 4.8, 'reviewCount': 18000, 'description': 'Ultra-high capacity portable charger.', 'image': 'https://m.media-amazon.com/images/I/41lqsC0Wp5L._AC_SY350_.jpg'},

    # 4. Home & Lifestyle
    {'id': 31, 'categoryId': 4, 'name': 'Dyson V15 Detect Vacuum', 'price': 749.99, 'oldPrice': 800, 'rating': 4.9, 'reviewCount': 900, 'description': 'Cordless vacuum with laser illumination.', 'image': 'https://dyson-h.assetsadobe2.com/is/image/content/dam/dyson/products/vacuum-cleaners/cordless-stick-vacuums/v15-detect/pdp/gallery/Dyson-V15-Detect-Absolute-Nickel-PDP-Gallery-1.jpg'},
    {'id': 32, 'categoryId': 4, 'name': 'Nespresso VertuoPlus Coffee Machine', 'price': 159.00, 'oldPrice': 199, 'rating': 4.7, 'reviewCount': 1200, 'description': 'Single-serve coffee and espresso machine.', 'image': 'https://www.nespresso.com/ecom/medias/sys_master/public/14545585831966/Desktop-VertuoPlus-KV.png'},
    {'id': 33, 'categoryId': 4, 'name': 'Herman Miller Aeron Chair', 'price': 1645.00, 'oldPrice': 1800, 'rating': 5.0, 'reviewCount': 500, 'description': 'Ergonomic office chair for ultimate comfort.', 'image': 'https://www.hermanmiller.com/content/dam/hermanmiller/products/seating/office-chairs/aeron-chairs/aeron-chair-front.jpg'},
    {'id': 34, 'categoryId': 4, 'name': 'Philips Hue Starter Kit', 'price': 199.99, 'oldPrice': 220, 'rating': 4.8, 'reviewCount': 1100, 'description': 'Smart LED bulbs with millions of colors.', 'image': 'https://www.philips-hue.com/content/dam/b2c/en_US/products/20221017-starter-kit-e26-4pk/philips-hue-white-and-color-ambiance-a19-e26-starter-kit-4-pack-front.png'},
    {'id': 35, 'categoryId': 4, 'name': 'Le Creuset Dutch Oven', 'price': 390.00, 'oldPrice': 420, 'rating': 4.9, 'reviewCount': 1500, 'description': 'Enameled cast iron Dutch oven for cooking.', 'image': 'https://www.lecreuset.com/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-master-catalog/default/dw8a4f9446/images/l_ls2501-2467ss.jpg'},
    {'id': 36, 'categoryId': 4, 'name': 'Casper Original Pillow', 'price': 65.00, 'oldPrice': 75, 'rating': 4.5, 'reviewCount': 3000, 'description': 'Supportive and cooling pillow.', 'image': 'https://casper.com/media/catalog/product/cache/41a1c9817757b5612344a275464197c3/p/i/pillow-original-gallery-1-2022.jpg'},
    {'id': 37, 'categoryId': 4, 'name': 'Instant Pot Duo 7-in-1', 'price': 89.99, 'oldPrice': 100, 'rating': 4.7, 'reviewCount': 150000, 'description': 'Electric pressure cooker, slow cooker, and more.', 'image': 'https://m.media-amazon.com/images/I/716g+eOUo1L.jpg'},
    {'id': 38, 'categoryId': 4, 'name': 'iRobot Roomba j7+', 'price': 799.00, 'oldPrice': 850, 'rating': 4.6, 'reviewCount': 5000, 'description': 'Self-emptying robot vacuum.', 'image': 'https://www.irobot.com/on/demandware.static/-/Sites-master-catalog/default/dw15757134/images/primary/j7_plus_hero_2.jpg'},
    {'id': 39, 'categoryId': 4, 'name': 'Simplehuman Sensor Mirror', 'price': 200.00, 'oldPrice': 220, 'rating': 4.9, 'reviewCount': 800, 'description': 'Makeup mirror with tru-lux light system.', 'image': 'https://cdn.simplehuman.com/media/catalog/product/cache/1/image/1800x/040ec09b1e35df139433887a97daa66f/s/t/st3026_8in_round_sensor_mirror_brushed_f-940.jpg'},
    {'id': 40, 'categoryId': 4, 'name': 'Click & Grow Smart Garden 3', 'price': 99.95, 'oldPrice': 120, 'rating': 4.7, 'reviewCount': 1200, 'description': 'Self-growing indoor garden.', 'image': 'https://cdn.shopify.com/s/files/1/0244/3296/9639/products/SG9_Beige_3basils_01_1024x1024.jpg?v=1611843213'},

    # 5. Medicine
    {'id': 41, 'categoryId': 5, 'name': 'Nature Made Vitamin D3', 'price': 15.99, 'oldPrice': 20, 'rating': 4.8, 'reviewCount': 5000, 'description': 'Supports bone, teeth, muscle, and immune health.', 'image': 'https://m.media-amazon.com/images/I/71+0e2-8sPL.jpg'},
    {'id': 42, 'categoryId': 5, 'name': 'Advil Pain Reliever (200 count)', 'price': 14.99, 'oldPrice': 18, 'rating': 4.9, 'reviewCount': 10000, 'description': 'Ibuprofen tablets for pain relief.', 'image': 'https://m.media-amazon.com/images/I/81xZxoV9wSL.jpg'},
    {'id': 43, 'categoryId': 5, 'name': 'Band-Aid Brand Flexible Fabric Bandages', 'price': 6.99, 'oldPrice': 8, 'rating': 4.7, 'reviewCount': 8000, 'description': 'Assorted sizes of flexible bandages.', 'image': 'https://m.media-amazon.com/images/I/81Qp3KlZJLL.jpg'},
    {'id': 44, 'categoryId': 5, 'name': 'Metamucil 4-in-1 Fiber Supplement', 'price': 24.99, 'oldPrice': 30, 'rating': 4.6, 'reviewCount': 6000, 'description': 'Daily fiber supplement for digestive health.', 'image': 'https://m.media-amazon.com/images/I/71N-M4f26iL.jpg'},
    {'id': 45, 'categoryId': 5, 'name': 'Braun ThermoScan 7 Ear Thermometer', 'price': 59.99, 'oldPrice': 65, 'rating': 4.8, 'reviewCount': 4000, 'description': 'Digital ear thermometer for accurate readings.', 'image': 'https://m.media-amazon.com/images/I/71jS-9+q60L.jpg'},
    {'id': 46, 'categoryId': 5, 'name': 'Omron 5 Series Blood Pressure Monitor', 'price': 49.99, 'oldPrice': 55, 'rating': 4.7, 'reviewCount': 7000, 'description': 'Upper arm blood pressure monitor.', 'image': 'https://m.media-amazon.com/images/I/810zB5s2JFL.jpg'},
    {'id': 47, 'categoryId': 5, 'name': 'Purell Advanced Hand Sanitizer', 'price': 9.99, 'oldPrice': 12, 'rating': 4.9, 'reviewCount': 12000, 'description': 'Kills 99.99% of most common germs.', 'image': 'https://m.media-amazon.com/images/I/71S-3m2bJSL.jpg'},
    {'id': 48, 'categoryId': 5, 'name': 'Zyrtec 24 Hour Allergy Relief Tablets', 'price': 18.99, 'oldPrice': 22, 'rating': 4.8, 'reviewCount': 9000, 'description': 'Powerful allergy relief.', 'image': 'https://m.media-amazon.com/images/I/81w3Q7q-9yL.jpg'},
    {'id': 49, 'categoryId': 5, 'name': 'GNC Mega Men Multivitamin', 'price': 29.99, 'oldPrice': 35, 'rating': 4.6, 'reviewCount': 5000, 'description': 'Clinically studied men\'s multivitamin.', 'image': 'https://www.gnc.com/dw/image/v2/BBLB_PRD/on/demandware.static/-/Sites-master-catalog-gnc/default/dw1aa4f484/hi-res/259632_web_GNC%20Mega%20Men%20Multivitamin_Front_Bottle.jpg'},
    {'id': 50, 'categoryId': 5, 'name': 'CeraVe Moisturizing Cream', 'price': 16.99, 'oldPrice': 20, 'rating': 4.8, 'reviewCount': 20000, 'description': 'Body and face moisturizer for dry skin.', 'image': 'https://m.media-amazon.com/images/I/61S7BrCBj7L.jpg'},

    # 6. Sports & Outdoor
    {'id': 51, 'categoryId': 6, 'name': 'Yeti Tundra 45 Cooler', 'price': 325.00, 'oldPrice': 350, 'rating': 4.9, 'reviewCount': 4000, 'description': 'Indestructible cooler for outdoor adventures.', 'image': 'https://m.media-amazon.com/images/I/71C-pI5v+5L.jpg'},
    {'id': 52, 'categoryId': 6, 'name': 'The North Face Recon Backpack', 'price': 109.00, 'oldPrice': 120, 'rating': 4.8, 'reviewCount': 3000, 'description': 'Versatile backpack for daily use and travel.', 'image': 'https://images.thenorthface.com/is/image/TheNorthFace/NF0A52SH_JK3_hero'},
    {'id': 53, 'categoryId': 6, 'name': 'Hydro Flask Wide Mouth Bottle', 'price': 44.95, 'oldPrice': 50, 'rating': 4.9, 'reviewCount': 15000, 'description': 'Insulated stainless steel water bottle.', 'image': 'https://m.media-amazon.com/images/I/61ZWg3506BL.jpg'},
    {'id': 54, 'categoryId': 6, 'name': 'Manduka PRO Yoga Mat', 'price': 129.00, 'oldPrice': 140, 'rating': 4.7, 'reviewCount': 2000, 'description': 'High-performance, non-slip yoga mat.', 'image': 'https://m.media-amazon.com/images/I/81B4s346EFL.jpg'},
    {'id': 55, 'categoryId': 6, 'name': 'Bowflex SelectTech 552 Dumbbells', 'price': 429.00, 'oldPrice': 549, 'rating': 4.8, 'reviewCount': 8000, 'description': 'Adjustable dumbbells from 5 to 52.5 lbs.', 'image': 'https://m.media-amazon.com/images/I/81Iq5y4-4IL.jpg'},
    {'id': 56, 'categoryId': 6, 'name': 'Trek Marlin 5 Mountain Bike', 'price': 599.99, 'oldPrice': 650, 'rating': 4.6, 'reviewCount': 500, 'description': 'A great entry-level mountain bike.', 'image': 'https://media.trekbikes.com/image/upload/Marlin-5-29-Matte-Dnister-Black'},
    {'id': 57, 'categoryId': 6, 'name': 'Coleman Sundome Camping Tent', 'price': 69.99, 'oldPrice': 80, 'rating': 4.5, 'reviewCount': 10000, 'description': '4-person dome tent for camping.', 'image': 'https://m.media-amazon.com/images/I/81x2oQ34i6L.jpg'},
    {'id': 58, 'categoryId': 6, 'name': 'Garmin Forerunner 245 Music', 'price': 349.99, 'oldPrice': 380, 'rating': 4.7, 'reviewCount': 6000, 'description': 'GPS running watch with music.', 'image': 'https://m.media-amazon.com/images/I/61bU3so-8PL.jpg'},
    {'id': 59, 'categoryId': 6, 'name': 'Spalding NBA Street Basketball', 'price': 24.99, 'oldPrice': 30, 'rating': 4.8, 'reviewCount': 9000, 'description': 'Official size and weight outdoor basketball.', 'image': 'https://m.media-amazon.com/images/I/91t4L4+t6KL.jpg'},
    {'id': 60, 'categoryId': 6, 'name': 'Black Diamond Spot 400 Headlamp', 'price': 49.95, 'oldPrice': 55, 'rating': 4.9, 'reviewCount': 3000, 'description': 'Bright and versatile headlamp for any adventure.', 'image': 'https://m.media-amazon.com/images/I/71I6f3-p3FL.jpg'},

    # 7. Baby's & Toys
    {'id': 61, 'categoryId': 7, 'name': 'LEGO Classic Large Creative Brick Box', 'price': 59.99, 'oldPrice': 65, 'rating': 4.9, 'reviewCount': 20000, 'description': '790 pieces for endless creativity.', 'image': 'https://m.media-amazon.com/images/I/81e5y2NaVnL.jpg'},
    {'id': 62, 'categoryId': 7, 'name': 'Graco 4Ever DLX 4-in-1 Car Seat', 'price': 329.99, 'oldPrice': 350, 'rating': 4.8, 'reviewCount': 15000, 'description': '10 years of use, from infant to booster.', 'image': 'https://m.media-amazon.com/images/I/81c4a52t72L.jpg'},
    {'id': 63, 'categoryId': 7, 'name': 'Hot Wheels 20-Car Gift Pack', 'price': 21.99, 'oldPrice': 25, 'rating': 4.8, 'reviewCount': 18000, 'description': 'A collection of 20 classic Hot Wheels cars.', 'image': 'https://m.media-amazon.com/images/I/91e2s959NLL.jpg'},
    {'id': 64, 'categoryId': 7, 'name': 'Barbie Dreamhouse', 'price': 199.99, 'oldPrice': 220, 'rating': 4.7, 'reviewCount': 9000, 'description': 'Large dollhouse with 3 floors and 8 rooms.', 'image': 'https://m.media-amazon.com/images/I/81jqgWNEpWL.jpg'},
    {'id': 65, 'categoryId': 7, 'name': 'Nintendo Switch - OLED Model', 'price': 349.99, 'oldPrice': 360, 'rating': 4.9, 'reviewCount': 12000, 'description': 'Gaming console with a vibrant 7-inch OLED screen.', 'image': 'https://m.media-amazon.com/images/I/71-k6cPPMNL.jpg'},
    {'id': 66, 'categoryId': 7, 'name': 'Melissa & Doug Wooden Blocks', 'price': 24.99, 'oldPrice': 30, 'rating': 4.9, 'reviewCount': 11000, 'description': '100 solid wood blocks in 4 colors and 9 shapes.', 'image': 'https://m.media-amazon.com/images/I/81T6n26z3FL.jpg'},
    {'id': 67, 'categoryId': 7, 'name': 'Fisher-Price Kick \'n Play Piano Gym', 'price': 39.99, 'oldPrice': 50, 'rating': 4.8, 'reviewCount': 25000, 'description': 'Interactive gym for infants.', 'image': 'https://m.media-amazon.com/images/I/81-txh4V3hL.jpg'},
    {'id': 68, 'categoryId': 7, 'name': 'Play-Doh Modeling Compound 10-Pack', 'price': 7.99, 'oldPrice': 10, 'rating': 4.7, 'reviewCount': 22000, 'description': 'A case of 10 colorful Play-Doh cans.', 'image': 'https://m.media-amazon.com/images/I/91Fq8h-5B+L.jpg'},
    {'id': 69, 'categoryId': 7, 'name': 'Hatchimals Alive, Carton', 'price': 9.99, 'oldPrice': 12, 'rating': 4.6, 'reviewCount': 3000, 'description': 'Self-hatching surprise eggs.', 'image': 'https://m.media-amazon.com/images/I/81kF+vL8G3L.jpg'},
    {'id': 70, 'categoryId': 7, 'name': 'Radio Flyer Classic Red Wagon', 'price': 109.99, 'oldPrice': 120, 'rating': 4.8, 'reviewCount': 7000, 'description': 'All-steel wagon with high sides.', 'image': 'https://m.media-amazon.com/images/I/71L5c3uH-JL.jpg'},

    # 8. Groceries & Pets
    {'id': 71, 'categoryId': 8, 'name': 'Blue Buffalo Life Protection Dog Food', 'price': 59.99, 'oldPrice': 65, 'rating': 4.7, 'reviewCount': 20000, 'description': 'Natural adult dry dog food, chicken and brown rice.', 'image': 'https://m.media-amazon.com/images/I/81q2b-c8SGL.jpg'},
    {'id': 72, 'categoryId': 8, 'name': 'Nespresso Capsules VertuoLine, 30 Count', 'price': 36.00, 'oldPrice': 40, 'rating': 4.8, 'reviewCount': 18000, 'description': 'Variety pack of coffee capsules.', 'image': 'https://m.media-amazon.com/images/I/71p0wev2vaL.jpg'},
    {'id': 73, 'categoryId': 8, 'name': 'KIND Bars, Dark Chocolate Nuts & Sea Salt', 'price': 14.22, 'oldPrice': 18, 'rating': 4.7, 'reviewCount': 25000, 'description': 'Gluten-free bars, 12 count.', 'image': 'https://m.media-amazon.com/images/I/81a+m12-RhL.jpg'},
    {'id': 74, 'categoryId': 8, 'name': 'Purina Tidy Cats Clumping Cat Litter', 'price': 22.99, 'oldPrice': 25, 'rating': 4.6, 'reviewCount': 30000, 'description': '24/7 performance multi-cat litter.', 'image': 'https://m.media-amazon.com/images/I/81M6a-IZ73L.jpg'},
    {'id': 75, 'categoryId': 8, 'name': 'California Olive Ranch Extra Virgin Olive Oil', 'price': 12.99, 'oldPrice': 15, 'rating': 4.8, 'reviewCount': 10000, 'description': '100% California extra virgin olive oil.', 'image': 'https://m.media-amazon.com/images/I/71d18f5+SCL.jpg'},
    {'id': 76, 'categoryId': 8, 'name': 'Greenies Original Dental Treats for Dogs', 'price': 33.99, 'oldPrice': 40, 'rating': 4.9, 'reviewCount': 40000, 'description': 'Natural dog treats for teeth cleaning.', 'image': 'https://m.media-amazon.com/images/I/81h6tI34JLL.jpg'},
    {'id': 77, 'categoryId': 8, 'name': 'La Croix Sparkling Water, 12 Pack', 'price': 5.99, 'oldPrice': 7, 'rating': 4.7, 'reviewCount': 12000, 'description': 'Pamplemousse (grapefruit) flavored sparkling water.', 'image': 'https://m.media-amazon.com/images/I/81f51o22CqL.jpg'},
    {'id': 78, 'categoryId': 8, 'name': 'Cheerios Honey Nut Cereal', 'price': 4.50, 'oldPrice': 5, 'rating': 4.8, 'reviewCount': 15000, 'description': 'Gluten-free cereal with real honey.', 'image': 'https://m.media-amazon.com/images/I/81o-3k54J9L.jpg'},
    {'id': 79, 'categoryId': 8, 'name': 'Temptations Classic Crunchy Cat Treats', 'price': 8.49, 'oldPrice': 10, 'rating': 4.9, 'reviewCount': 50000, 'description': 'Tasty chicken flavor cat treats.', 'image': 'https://m.media-amazon.com/images/I/81h89-c4CRL.jpg'},
    {'id': 80, 'categoryId': 8, 'name': 'RXBAR, Chocolate Sea Salt, Protein Bar', 'price': 19.99, 'oldPrice': 22, 'rating': 4.6, 'reviewCount': 18000, 'description': 'High protein snack, 12 count.', 'image': 'https://m.media-amazon.com/images/I/81-y4cgrb9L.jpg'},

    # 9. Health & Beauty
    {'id': 81, 'categoryId': 9, 'name': 'CeraVe Hydrating Facial Cleanser', 'price': 14.99, 'oldPrice': 18, 'rating': 4.8, 'reviewCount': 40000, 'description': 'For normal to dry skin.', 'image': 'https://m.media-amazon.com/images/I/61k3Vz1L68L.jpg'},
    {'id': 82, 'categoryId': 9, 'name': 'Olaplex No. 3 Hair Perfector', 'price': 30.00, 'oldPrice': 35, 'rating': 4.7, 'reviewCount': 30000, 'description': 'At-home hair treatment to reduce breakage.', 'image': 'https://m.media-amazon.com/images/I/61s58n1-2VL.jpg'},
    {'id': 83, 'categoryId': 9, 'name': 'The Ordinary Niacinamide 10% + Zinc 1%', 'price': 6.50, 'oldPrice': 8, 'rating': 4.6, 'reviewCount': 50000, 'description': 'High-strength vitamin and mineral blemish formula.', 'image': 'https://m.media-amazon.com/images/I/51wD03nSt-L.jpg'},
    {'id': 84, 'categoryId': 9, 'name': 'Dior Sauvage Eau de Toilette', 'price': 95.00, 'oldPrice': 110, 'rating': 4.9, 'reviewCount': 25000, 'description': 'A radically fresh composition.', 'image': 'https://www.dior.com/dw/image/v2/BGXS_PRD/on/demandware.static/-/Sites-master_dior/default/dw1a063162/spc/dior/fragrance/y0685240_fcd-collection-eau-de-toilette-100ml_3348901250148_packshot.jpg'},
    {'id': 85, 'categoryId': 9, 'name': 'Laneige Lip Sleeping Mask', 'price': 24.00, 'oldPrice': 28, 'rating': 4.8, 'reviewCount': 35000, 'description': 'Leave-on lip mask that soothes and moisturizes.', 'image': 'https://m.media-amazon.com/images/I/61j80z5kFjL.jpg'},
    {'id': 86, 'categoryId': 9, 'name': 'Supergoop! Unseen Sunscreen SPF 40', 'price': 36.00, 'oldPrice': 40, 'rating': 4.7, 'reviewCount': 15000, 'description': 'Invisible, weightless, and scentless sunscreen.', 'image': 'https://m.media-amazon.com/images/I/61M-p3N9QEL.jpg'},
    {'id': 87, 'categoryId': 9, 'name': 'Philips Norelco OneBlade Electric Shaver', 'price': 49.99, 'oldPrice': 55, 'rating': 4.6, 'reviewCount': 40000, 'description': 'Hybrid electric trimmer and shaver.', 'image': 'https://m.media-amazon.com/images/I/719NCqG8wuL.jpg'},
    {'id': 88, 'categoryId': 9, 'name': 'Dyson Supersonic Hair Dryer', 'price': 429.00, 'oldPrice': 450, 'rating': 4.9, 'reviewCount': 8000, 'description': 'Engineered to protect hair from extreme heat damage.', 'image': 'https://dyson-h.assetsadobe2.com/is/image/content/dam/dyson/products/hair-care/dyson-supersonic-hair-dryer/pdp/gallery/Dyson-Supersonic-Hair-Dryer-Nickel-Copper-PDP-Gallery-1.jpg'},
    {'id': 89, 'categoryId': 9, 'name': 'Beautyblender Original Makeup Sponge', 'price': 20.00, 'oldPrice': 22, 'rating': 4.8, 'reviewCount': 30000, 'description': 'The original makeup sponge for flawless blend.', 'image': 'https://m.media-amazon.com/images/I/7123L2DclSL.jpg'},
    {'id': 90, 'categoryId': 9, 'name': 'Crest 3D Whitestrips', 'price': 45.99, 'oldPrice': 50, 'rating': 4.6, 'reviewCount': 50000, 'description': 'Professional effects teeth whitening strips.', 'image': 'https://m.media-amazon.com/images/I/815i+SNf5lL.jpg'},
]


# --- МАРШРУТЫ (ENDPOINTS) ---
@app.get("/")
def read_root():
    return {"message": "✅ Backend на Python работает!"}

@app.get("/api/categories")
def get_categories():
    return categories

@app.get("/api/products")
def get_all_products():
    return products

@app.get("/api/products/category/{category_id}")
def get_products_by_category(category_id: int):
    filtered_products = [p for p in products if p["categoryId"] == category_id]
    return filtered_products