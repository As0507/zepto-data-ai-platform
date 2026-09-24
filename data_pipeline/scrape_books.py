import requests, sqlite3
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
books = []

for page in range(1,6):  # scrape 5 pages
    res = requests.get(BASE_URL.format(page))
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select(".product_pod")
    for item in items:
        title = item.h3.a["title"]
        price = item.select_one(".price_color").text.strip("£")
        rating = item.p["class"][1]
        availability = item.select_one(".availability").text.strip()
        category = "All Products"
        books.append([title, float(price), rating, availability, category])

df = pd.DataFrame(books, columns=["title","price_gbp","rating_txt","availability","category"])
df["rating"] = df["rating_txt"].map({"One":1,"Two":2,"Three":3,"Four":4,"Five":5})
df["in_stock"] = df["availability"].str.contains("In stock")
df["price_inr"] = df["price_gbp"] * 105.50

# SQLite schema
conn = sqlite3.connect("books.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
cur.execute("""CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    price_gbp REAL,
    price_inr REAL,
    rating INTEGER,
    in_stock INTEGER,
    category_id INTEGER REFERENCES categories(id))""")

# Insert categories + books
for cat in df["category"].unique():
    cur.execute("INSERT OR IGNORE INTO categories(name) VALUES(?)",(cat,))
for _,row in df.iterrows():
    cat_id = cur.execute("SELECT id FROM categories WHERE name=?",(row["category"],)).fetchone()[0]
    cur.execute("INSERT INTO books(title,price_gbp,price_inr,rating,in_stock,category_id) VALUES(?,?,?,?,?,?)",
                (row["title"],row["price_gbp"],row["price_inr"],row["rating"],int(row["in_stock"]),cat_id))
conn.commit()
