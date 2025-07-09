import cloudinary
import cloudinary.api

# 🔧 Replace with your Cloudinary credentials
cloudinary.config(
    cloud_name="djq2ywwry",
    api_key="784146673443948",       # ← Replace with actual key
    api_secret="eJa3li703y3iACHXqXWd2wmyaoU"  # ← Replace with actual secret
)

# 📦 Fetch all images from a specific folder (or all if prefix is "")
resources = cloudinary.api.resources(type="upload", max_results=500)

# 📜 Map of image name => full URL
image_url_map = {}

for item in resources["resources"]:
    public_id = item["public_id"]
    filename = public_id.split("/")[-1]
    extension = item["format"]
    full_url = item["secure_url"]

    image_url_map[f"{filename}.{extension}"] = full_url

# ✅ Output result
for name, url in image_url_map.items():
    print(f"{name} => {url}")
