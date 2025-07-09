let uiCartItems = [];

// Normalize the URL path for better matching
const pathParts = window.location.pathname.toLowerCase().split('/').filter(Boolean);
const page = pathParts[pathParts.length - 1]; // Last part of the URL path

// ✅ Ensure consistent category detection
const categoryMap = {
    "beverage_list": "beverage",
    "food_list": "food",
    "care_list": "care",
    "beauty_list": "beauty"
};

// Detect category safely
let category = categoryMap[page] || null;

// Debugging logs
console.log("🔍 Full pathname:", window.location.pathname);
console.log("📌 Extracted page:", page);
console.log("🏷️ Detected category:", category);

// ✅ If category is missing, attempt fallback (for Beverage List issue)
if (!category && window.location.search.includes("category=beverage")) {
    console.warn("⚠️ Fallback: Detected 'beverage' from URL query string!");
    category = "beverage";
}

// Final category check
if (!category) {
    console.error("❌ No category detected! Check your URL structure.");
}




// Load Products Based on Category
const productsByCategory = {
    beverage: [
        { id: 1, name: "FRU FRU PINEAPPLE/COCONUT", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 1200, stock: 500 },
        { id: 2, name: "FRU FRU MIX", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 1200, stock: 300 },
        { id: 3, name: "ZIZOU X 40 MIX", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 5700, stock: 450 },
        { id: 4, name: "ZIZOU X 40 PEACH", image: "images/zizou-peach.jpeg", rating: "⭐⭐⭐⭐", price: 5700, stock: 450 },
        { id: 5, name: "ZIZOU X 40 PINEAPPLE/COCONUT", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 5700, stock: 450 },
        { id: 6, name: "ZIZOU APPLE 330ML CAN X 24", image: "images/zizou-apple.jpeg", rating: "⭐⭐⭐⭐", price: 7000, stock: 450 },
        { id: 7, name: "ZIZOU BLACKCURENT CAN 330ml *24", image: "images/zizou-blackcurrent.jpeg", rating: "⭐⭐⭐⭐", price: 7000, stock: 950 },
        { id: 8, name: "ZIZOU CRANBERRY CAN X24", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 7000, stock: 950 },
        { id: 9, name: "ZIZOU LEMON & MINT CAN X24", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 7000, stock: 750 },
        { id: 10, name: "ZIZOU MANGO CAN x 24", image: "images/zizou-mango.jpeg", rating: "⭐⭐⭐⭐", price: 7000, stock: 900 },
        { id: 11, name: "ZIZOU MIX 200ml x 40", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 5700, stock: 700 },
        { id: 12, name: "ZIZOU MIX FRUIT POUCH 200MLx24", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 3400, stock: 700 },
        { id: 13, name: "ZIZOU ORANGE x 40", image: "images/zizou-orange.jpeg", rating: "⭐⭐⭐⭐", price: 5700, stock: 1000 },
        { id: 14, name: "ZIZOU ORANGE CAN 330ml x 24", image: "images/zizou-orange.jpeg", rating: "⭐⭐⭐⭐", price: 7000, stock: 850 },
        { id: 15, name: "ZIZOU ORANGE POUCH 200MLx24", image: "images/zizou-pouch.jpg", rating: "⭐⭐⭐⭐", price: 3400, stock: 40 },
        { id: 16, name: "ZIZOU PEACH CAN 330ml x 24", image: "images/zizou-peach.jpeg", rating: "⭐⭐⭐⭐", price: 7000, stock: 40 },
        { id: 17, name: "ZIZOU PEACH POUCH 200MLx24", image: "images/zizou-peach.jpeg", rating: "⭐⭐⭐⭐", price: 3400, stock: 40 },
        { id: 18, name: "ZIZOU PINAPPLE POUCH 200MLx24", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 3400, stock: 40 },
        { id: 19, name: "ZIZOU PINEAPLE CAN x 24", image: "images/zizou.png", rating: "⭐⭐⭐⭐", price: 7000, stock: 700 },
        { id: 20, name: "INFINITE POWER 50CL GOLD", image: "images/Bev12.png", rating: "⭐⭐⭐⭐", price: 3900, stock: 940 },
        { id: 21, name: "INFINITE POWER BLACK", image: "images/Bev14.png", rating: "⭐⭐⭐⭐", price: 3900, stock: 640 },
        { id: 22, name: "INFINITE POWER BLUE EXTREME", image: "images/Bev11.png", rating: "⭐⭐⭐⭐", price: 3900, stock: 640 },
        { id: 23, name: "INFINITE POWER MALT", image: "images/Bev13.png", rating: "⭐⭐⭐⭐", price: 4500, stock: 640 },
        { id: 24, name: "POP APPLE 35 CL", image: "images/Bev4.png", rating: "⭐⭐⭐⭐", price: 2450, stock: 600 },
        { id: 25, name: "POP BERRIES 35CL", image: "images/Bev8.png", rating: "⭐⭐⭐⭐", price: 2450, stock: 300 },
        { id: 26, name: "POP CHAPMAN 35CL", image: "images/Bev10.png", rating: "⭐⭐⭐⭐", price: 2450, stock: 300 },
        { id: 27, name: "POP CLEAR 60cl", image: "images/Bev5.png", rating: "⭐⭐⭐⭐", price: 3400, stock: 150 },
        { id: 28, name: "POP COLA 35CL", image: "images/Bev1.png", rating: "⭐⭐⭐⭐", price: 2450, stock: 250 },
        { id: 29, name: "POP COLA 60 CL", image: "images/Bev1.png", rating: "⭐⭐⭐⭐", price: 3400, stock: 1250 },
        { id: 30, name: "POP BITTER LEM 35CL", image: "images/Bev16.png", rating: "⭐⭐⭐⭐", price: 3400, stock: 1150 },
    ],

        food: [
        { id: 31, name: "3 STAR (11G X72)", rating: "⭐⭐⭐⭐", price: 2600, stock: 100, image: "images/3 star.jpeg" },
        { id: 32, name: "3 STAR VANILLA 20g x 48", rating: "⭐⭐⭐⭐", price: 2200, stock: 800, image: "images/3 star.jpeg" },
        { id: 33, name: "3 STAR x 72", rating: "⭐⭐⭐⭐", price: 1800, stock: 500, image: "images/3 star.jpeg" },
        { id: 34, name: "7 TO 7 40g x 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 0, image: "images/Food14.jpg" },
        { id: 35, name: "7 to 7 Choco Gold x 24", rating: "⭐⭐⭐⭐", price: 2100, stock: 700, image: "images/Food14.jpg" },
        { id: 36, name: "7 TO 7 CHOCOLATE X 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 1500, image: "images/Food14.jpg" },
        { id: 37, name: "7 to 7 COCONUT GOLD x 24", rating: "⭐⭐⭐⭐", price: 2100, stock: 1500, image: "images/Food14.jpg" },
        { id: 38, name: "7 TO 7 COOKIES x 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 1500, image: "images/Food14.jpg" },
        { id: 39, name: "7 TO 7 COOKIES GOLD x 24", rating: "⭐⭐⭐⭐", price: 2100, stock: 2000, image: "images/Food14.jpg"},
        { id: 40, name: "7 TO 7 MILKY GOLD x 24", rating: "⭐⭐⭐⭐", price: 2100, stock: 0, image: "images/Food14.jpg" },
        { id: 41, name: "BIG & TASTY x 72", rating: "⭐⭐⭐⭐", price: 7600, stock: 1000, image: "images/Food6.jpg" },
        { id: 42, name: "BIG BANG 10g X 120", rating: "⭐⭐⭐⭐", price: 1120, stock: 500, image: "images/Snack-general.webp"},
        { id: 43, name: "BIG BITE x 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 600, image: "images/Food11.jpg"},
        { id: 44, name: "BIG BITE x 72", rating: "⭐⭐⭐⭐", price: 1800, stock: 400, image: "images/Food11.jpg"},
        { id: 45, name: "BIG POWER UP GOLD 24X55G", rating: "⭐⭐⭐⭐", price: 3700, stock: 900, image: "images/Food1.jpg"},
        { id: 46, name: "BUTTER BITE GOLD x 24", rating: "⭐⭐⭐⭐", price: 3700, stock: 300, image: "images/Snack-general.webp"},
        { id: 47, name: "BUTTER BITE x 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 700, image: "images/Snack-general.webp"},
        { id: 48, name: "CARAMELLA GOLD CANDY 20X50", rating: "⭐⭐⭐⭐", price: 11300, stock: 100, image: "images/Food24-sweet.jpg"},
        { id: 49, name: "CHOCO SNAP GOLD X 24", rating: "⭐⭐⭐⭐", price: 3800, stock: 800, image: "images/Snack-general.webp"},
        { id: 50, name: "CHOCOLATE SNAPS x 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 600, image: "images/Snack-general.webp"},
        { id: 51, name: "COCONUT CRUNCHY 65G X 24", rating: "⭐⭐⭐⭐", price: 5100, stock: 600, image: "images/Snack-general.webp"},
        { id: 52, name: "FULL FORCE 10g X 144", rating: "⭐⭐⭐⭐", price: 1250, stock: 700, image: "images/Snack-general.webp"},
        { id: 53, name: "GINGER SNAP 40x48", rating: "⭐⭐⭐⭐", price: 2600, stock: 950, image: "images/Food4.jpg"},
        { id: 54, name: "GINGER SNAPS 18g x 72", rating: "⭐⭐⭐⭐", price: 1700, stock: 850, image: "images/Food4.jpg"},
        { id: 55, name: "GIVE ME A BREAK 18g x 72", rating: "⭐⭐⭐⭐", price: 1700, stock: 1500, image: "images/Food10.jpg"},
        { id: 56, name: "GIVE ME A BREAK 30G X 24", rating: "⭐⭐⭐⭐", price: 2100, stock: 100, image: "images/Food10.jpg"},
        { id: 57, name: "GIVE ME A BREAK 50g x 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 600, image: "images/Food10.jpg"},
        { id: 58, name: "GOOD DAY FAMILY x 24", rating: "⭐⭐⭐⭐", price: 2100, stock: 800, image: "images/Snack-general.webp"},
        { id: 59, name: "GOOD DAYS x 72", rating: "⭐⭐⭐⭐", price: 1800, stock: 400, image: "images/Food8.jpg"},
        { id: 60, name: "GOOD DAYS 30G X 24", rating: "⭐⭐⭐⭐", price: 2100, stock: 0, image: "images/Food8.jpg"},
        { id: 61, name: "GOOD DAYS FAMILY x 48", rating: "⭐⭐⭐⭐", price: 2200, stock: 200, image: "images/Food8.jpg"},
        { id: 62, name: "HELLO BISCUIT DELIGHT x 48", rating: "⭐⭐⭐⭐", price: 2150, stock: 0, image: "images/Food18.jpg"},
        { id: 63, name: "HELLO BUISCUIT X 24", rating: "⭐⭐⭐⭐", price: 3750, stock: 0, image: "images/Food18.jpg"},
        { id: 64, name: "JOY N ENJOY x 48", rating: "⭐⭐⭐⭐", price: 2230, stock: 100, image: "images/Food7.jpg"},
        { id: 65, name: "JOY N ENJOY 20g x 72", rating: "⭐⭐⭐⭐", price: 1600, stock: 150, image: "images/Food7.jpg"},
        { id: 66, name: "JOY N ENJOY 50g x 36", rating: "⭐⭐⭐⭐", price: 1550, stock: 1050, image: "images/Food7.jpg"},
        { id: 67, name: "KINGS 60g x 48", rating: "⭐⭐⭐⭐", price: 4200, stock: 450, image: "images/Food12.jpg"},
        { id: 68, name: "KINGS COOKIES x 52", rating: "⭐⭐⭐⭐", price: 4300, stock: 650, image: "images/Food12.jpg"},
        { id: 69, name: "KINGS COOKIES 35g x 36", rating: "⭐⭐⭐⭐", price: 1700, stock: 700, image: "images/Food12.jpg"},
        { id: 70, name: "LOLA BANANA POP x 10", rating: "⭐⭐⭐⭐", price: 10200, stock: 400, image: "images/Food19-sweet.jpg"},
        { id: 71, name: "LOLA CREAM CANDY x 20", rating: "⭐⭐⭐⭐", price: 9100, stock: 400, image: "images/Food20-sweet.jpg"},
        { id: 72, name: "LOLA GINGER CARROT CANDY 10X25", rating: "⭐⭐⭐⭐", price: 11200, stock: 700, image: "images/Food22-sweet.jpg"},
        { id: 73, name: "LOLA ICE MINTS", rating: "⭐⭐⭐⭐", price: 9100, stock: 700, image: "images/Food19-sweet.jpg"},
        { id: 74, name: " LOLA MILK POP x 10", rating: "⭐⭐⭐⭐", price: 10200, stock: 700, image: "images/Food19-sweet.jpg"},
    ],
    care: [
        { id: 75, name: "CLASSIC TOO CLEAN 180g", image: "images/care4.png", rating: "⭐⭐⭐⭐", price: 7550, stock: 250 },
        { id: 76, name: "CLASSIC TOO CLEAN 22g", image: "images/care4.png", rating: "⭐⭐⭐⭐", price: 6700, stock: 300 },
        { id: 77, name: "CLASSIC TOO CLEAN 350g", image: "images/care4.png", rating: "⭐⭐⭐⭐", price: 7450, stock: 400 },
        { id: 78, name: "CLASSIC TOO CLEAN 850G", image: "images/care11.png", rating: "⭐⭐⭐⭐", price: 9700, stock: 400 },
        { id: 79, name: "CLASSIC TOO CLEAN 85g ", image: "images/care11.png", rating: "⭐⭐⭐⭐", price: 7100, stock: 400 },
    ],
    beauty: [
        { id: 80, name: "CLASSY SOAP BLUE x 30", image: "images/care16.png", rating: "⭐⭐⭐⭐", price: 12700, stock: 10 },
        { id: 81, name: "classy soap blue *72", image: "images/care16.png", rating: "⭐⭐⭐⭐", price: 11500, stock: 100 },
        { id: 82, name: "classy soap green 180*30", image: "images/care17.png", rating: "⭐⭐⭐⭐", price: 13700, stock: 100 },
        { id: 83, name: "CLASSY SOAP ORANGE 180g*30", image: "images/care13.png", rating: "⭐⭐⭐⭐", price: 13700, stock: 100 },
        { id: 84, name: "classy soap pink *72", image: "images/care15.png", rating: "⭐⭐⭐⭐", price: 11500, stock: 100 },
        { id: 85, name: "classy soap green 180*30", image: "images/care17.png", rating: "⭐⭐⭐⭐", price: 13700, stock: 300 },
        { id: 86, name: "CLASSY SOAP ORANGE 180g*30", image: "images/care13.png", rating: "⭐⭐⭐⭐", price: 13700, stock: 500 },
        { id: 87, name: "classy soap pink *72", image: "images/care15.png", rating: "⭐⭐⭐⭐", price: 11500, stock: 200 },
    ]
};


if (category in productsByCategory) {
    console.log(`✅ Found products for category "${category}"`);
    console.log("Products:", productsByCategory[category]);
} else {
    console.error(`❌ No products found for category "${category}"!`);
}

function getCSRFToken() {
    let csrfToken = null;
    const cookies = document.cookie.split(';');
    cookies.forEach(cookie => {
        let [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            csrfToken = value;
        }
    });
    console.log("🔑 CSRF Token:", csrfToken);
    return csrfToken;
}

let products = productsByCategory[category] || [];
console.log("📦 Loaded Products:", products); // ✅ Check if products array is populated

const cartKey = `cart_${category}`;
fetch('/dashboard/cart-data/')
  .then(response => response.json())
  .then(data => {
    console.log("🛒 Cart Data from Server:", data);
    if(!data.cart_items || !Array.isArray(data.cart_items)){
        console.error('cart_items is NOT an array', data);
        return;
    }
    updateCartUI(data.cart_items);
  })
  .catch(error => console.error("❌ Error fetching cart data:", error));
// Product Table and Cart Elements
const productTable = document.getElementById('productTable');
const cartDiv = document.getElementById('cart');

function createProductBadge(product) {
    // Create the badge container
    const badgeContainer = document.createElement('div');
    badgeContainer.classList.add('badge-container');

    // Check if the product is one of the specific products
    const specificProducts = [
        "7 to 7 Choco Gold x 24",
        "7 to 7 COCONUT GOLD x 24",
        "7 TO 7 COOKIES GOLD x 24",
        "7 TO 7 MILKY GOLD x 24",
    ];

    if (specificProducts.includes(product.name)) {
        // Add a special badge to these products
        const specialBadge = document.createElement('span');
        specialBadge.classList.add('badge', 'special');
        specialBadge.textContent = 'PROMO🎁✨';
        badgeContainer.appendChild(specialBadge);
    }

    return badgeContainer;
}

function getCloudinaryImageUrl(imageFileName) {
    const CLOUDINARY_BASE = "https://res.cloudinary.com/djq2ywwry/image/upload/image_products/";
    return CLOUDINARY_BASE + imageFileName;
}

// Dynamically update image links
products = products.map(product => ({
    ...product,
    image: getCloudinaryImageUrl(product.image)
}));

// Generate product table
// NOTE: Assumes each product.image is a full Cloudinary URL
// Example: "https://res.cloudinary.com/your-cloud-name/image/upload/vXYZ/image_products/product1.jpg"

// Generate product table
function generateTable() {
    if (!productTable) return;
    productTable.innerHTML = '';

    products.forEach((product, index) => {
        const row = document.createElement('tr');
        const badgeContainer = createProductBadge(product);

        row.innerHTML = `
            <td><img src="${product.image}" class="product-img" onerror="this.onerror=null; this.src='https://via.placeholder.com/150'">

            <td>
                ${badgeContainer.outerHTML}
                ${product.name}
            </td>
            <td>${product.rating}</td>
            <td>₦${product.price}</td>
            <td>${product.stock}</td>
            <td>
                <button onclick="changeQuantity(${index}, -100)">-</button>
                <input type="number" id="qty-${index}" value="100" min="100" max="${product.stock}" class="quantity-input">
                <button onclick="changeQuantity(${index}, 100)">+</button>
            </td>
            <td><button onclick="addToCart(${index}, ${product.id})" ${product.stock === 0 ? 'disabled' : ''}>Add to Cart</button></td>
        `;
        productTable.appendChild(row);
    });
}





function addToCart(index, productId) {
    console.log("🛒 addToCart() called with index:", index, "productId:", productId);
    
    const product = products[index];
    const category = document.getElementById("cart-category").value; // e.g., "care", "beverage", etc.
    const quantityInput = document.getElementById(`qty-${index}`);
    const quantity = parseInt(quantityInput.value);
    // Calculate total added so far for this product
    let alreadyInCart = 0;
    uiCartItems.forEach(item => {
        if (item.product_id === productId) {
            alreadyInCart += item.quantity;
        }
    });

    const totalRequested = alreadyInCart + quantity;

    if (totalRequested > product.stock) {
        alert(`❌ You’ve already added ${alreadyInCart}. Only ${product.stock} units of "${product.name}" are available.\n\nYou cannot add ${quantity} more.`);
        return;
    }


    console.log("📦 Product Details:", product);
    console.log("📌 Selected Category:", category);
    console.log("🔢 Quantity Selected:", quantity);


    // ✅ Check if quantity exceeds available stock
    if (quantity > product.stock) {
        alert(`❌ Only ${product.stock} units of "${product.name}" are available in stock.`);
        return;
    }
    


    let cartItem = {
        product_id: productId,
        name: product.name,
        price: product.price,
        quantity: quantity,
        category: category
    };

    console.log("📨 Sending cart request:", cartItem);

    fetch('/dashboard/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(cartItem)
    })
    .then(response => response.json())
    .then(data => {
        console.log("✅ Server Response:", data);

        if (data.message) {
            console.log("✔ Item added to backend cart successfully!");

            // Append the new item to the session-based UI cart array
            uiCartItems.push(cartItem);
            sessionStorage.setItem("uiCartItems", JSON.stringify(uiCartItems));
            updateCartUI(uiCartItems);

            // 🎯 **Start Animation**
            console.log("🚀 Starting Animation...");

            let productButton = document.querySelector(`button[onclick="addToCart(${index}, ${productId})"]`);
            let productRow = productButton ? productButton.closest("tr") : null;
            let productImg = productRow ? productRow.querySelector("td img") : null;
            let cartIcon = document.getElementById("cart-toggle");

            if (!productImg || !cartIcon) {
                console.error("❌ ERROR: Product image or cart icon not found!");
                return;
            }

            let flyingImg = productImg.cloneNode(true);
            document.body.appendChild(flyingImg);

            // Get positions
            let imgRect = productImg.getBoundingClientRect();
            let cartRect = cartIcon.getBoundingClientRect();

            // Set initial animation styles
            flyingImg.style.position = "fixed";
            flyingImg.style.left = imgRect.left + "px";
            flyingImg.style.top = imgRect.top + "px";
            flyingImg.style.width = imgRect.width + "px";
            flyingImg.style.height = imgRect.height + "px";
            flyingImg.style.transition = "left 1.8s ease-in-out, top 1.8s ease-in-out, transform 1.8s ease-in-out";
            flyingImg.style.zIndex = "1000";

            // Animate movement to cart
            setTimeout(() => {
                flyingImg.style.left = (cartRect.left + cartRect.width / 2 - imgRect.width / 2) + "px";
                flyingImg.style.top = (cartRect.top + cartRect.height / 2 - imgRect.height / 2) + "px";
                flyingImg.style.transform = "scale(0.6)";
            }, 100);

            // Start fading earlier, before reaching the cart
            setTimeout(() => {
                flyingImg.style.transition = "opacity 1s ease-in-out"; // Faster fade
                flyingImg.style.opacity = "0";
                console.log("🌫 Fading Out Early...");
            }, 1000); // Start fading after 1s (mid-air)

            // Remove cloned image after animation
            setTimeout(() => {
                document.body.removeChild(flyingImg);
                console.log("🗑 Cloned Image Removed After Animation");
            }, 3000); // Remove earlier (3s total)

            // **Cart Count Badge Update Logic**
            updateCartBadge();
        } else {
            console.error("❌ ERROR: Backend failed to add item:", data.error);
        }
    })
    .catch(error => {
        console.error("❌ ERROR Adding to Cart:", error);
    });
}

// Function to update the badge on the cart icon
function updateCartBadge() {
    // Get the cart item count
    const cartItemCount = uiCartItems.length;  // Or whatever method you're using to track cart items

    // Get the cart icon
    const cartIcon = document.querySelector("#cart-toggle .cart-icon");

    // Create the badge if it doesn't exist
    let badge = document.querySelector("#cart-toggle .cart-badge");

    if (!badge) {
        badge = document.createElement("span");
        badge.classList.add("cart-badge");
        cartIcon.appendChild(badge);
    }

    // Update the badge text with the current cart count
    badge.textContent = cartItemCount;
    badge.style.display = cartItemCount > 0 ? "inline-block" : "none";
}














document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const category = urlParams.get("category") || "default"; // Get category from URL
    fetchCartData(category); // Fetch only relevant cart items
});

function fetchCartData() {
    const category = document.getElementById("cart-category").value;
    fetch(`/dashboard/cart-data/?category=${category}`)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("🔄 Cart Data Refreshed:", data.cart_items);
        updateCartUI(data.cart_items);
    })
    .catch(error => console.error("❌ Error fetching cart data:", error));
}



// ✅ Ensure this function runs on page load
document.addEventListener("DOMContentLoaded", fetchCartData);



// Remove Items from Cart
function removeFromCart(productId) {
    console.log(`🗑️ Removing product ${productId}`);

    fetch(`/dashboard/remove-from-cart/?product_id=${productId}`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("🗑️ Remove Response:", data);
        if (data.message) {
            // Remove the item from the global UI cart array
            uiCartItems = uiCartItems.filter(item => item.product_id !== productId);
            // Update sessionStorage with the new array
            sessionStorage.setItem("uiCartItems", JSON.stringify(uiCartItems));
            // Update the cart UI based on the updated array
            updateCartUI(uiCartItems);
            updateCartBadge();
        } else {
            console.warn("⚠️ Failed to remove item from the database!", data.error);
        }
    })
    .catch(error => console.error("❌ Error removing from cart:", error));
}




// ✅ Remove from UI
function removeItemFromUI(productId) {
    const cartContainer = document.getElementById("cart_items");

    if (!cartContainer) {
        console.error("❌ Cart container not found in the DOM!");
        return;
    }

    // ✅ Find the item in the UI & remove it
    const cartItems = cartContainer.getElementsByTagName("div");
    for (let item of cartItems) {
        if (item.dataset.productId == productId) {
            item.remove();
            console.log(`✅ Product ${productId} removed from UI.`);
            break;
        }
    }

    // ✅ If cart is empty, show "No items in your cart"
    if (cartContainer.children.length === 0) {
        cartContainer.innerHTML = "<p>No items in your cart</p>";
    }
}





 
function updateCartUI(cartItems) {
    console.log("🛒 Updating Cart UI with Data:", cartItems);

    // Get the cart container element from your HTML
    const cartContainer = document.getElementById("cart_items");
    if (!cartContainer) {
        console.error("❌ Cart container not found in the DOM!");
        return;
    }
    // Clear previous cart UI
    cartContainer.innerHTML = "";

    let total = 0;

    if (cartItems.length === 0) {
        cartContainer.innerHTML = "<p>No items in your cart</p>";
    } else {
        cartItems.forEach(item => {
            const price = parseFloat(item.price) || 0;
            const quantity = parseInt(item.quantity) || 0;
            const itemTotal = price * quantity;
            total += itemTotal;

            // Create a container for the cart item
            const cartItemElement = document.createElement("div");
            cartItemElement.className = "cart-item";
            // Optionally, add a data attribute for removal
            cartItemElement.dataset.productId = item.product_id;
            cartItemElement.innerHTML = `
                <p><strong>${item.name}</strong></p>
                <p>Price: ₦${price}</p>
                <p>Quantity: ${quantity}</p>
                <p>Total: ₦${itemTotal.toFixed(2)}</p>
                <button onclick="removeFromCart(${item.product_id})">Remove</button>
            `;
            cartContainer.appendChild(cartItemElement);
        });
    }

    const totalElement = document.getElementById("cart-total");
    if (totalElement) {
        totalElement.innerText = `Total: ₦${total.toFixed(2)}`;
    } else {
        console.error("❌ Cart total element not found in the DOM!");
    }

    console.log("✅ Cart UI Updated Successfully!");
}

// Quantity Input Handler
function changeQuantity(index, change) {
    const input = document.getElementById(`qty-${index}`);
    let newValue = parseInt(input.value) + change;

    if (!products[index]) {
        console.error(`❌ Product at index ${index} is undefined!`);
        return;
    }

    if (newValue < 100) newValue = 100;
    if (newValue > products[index].stock) newValue = products[index].stock;
    input.value = newValue;
    console.log(`🔢 Updated quantity for index ${index}: ${newValue}`);
}

// Initialize
if (productTable) generateTable();
if (cartDiv) updateCartUI({});
