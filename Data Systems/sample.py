import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb+srv://sg965:test123@cluster0.ixuvc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db= client["myDatabase"]
print("Connected to MongoDB!")
#db.myNewCollection.insert_one({"name":	"Jane	Doe",	"age":	28,	"email":"janedoe@example.com"})
#db.myNewCollection.insert_many([
#                    {"name":	"John	Smith",	"age":	30,	"email":	"johnsmith@example.com"},
#                    {"name":	"Alice	Johnson",	"age":	22,	"email":	"alicejohnson@example.com"}
#    ])
for	doc	in	db.myNewCollection.find():
    print(doc)
for	doc	in	db.myNewCollection.find({"name":	"Jane	Doe"}):
    print(doc)
#db.myNewCollection.update_one({"name":	"Jane	Doe"},	{"$set":	{"age":	29}})
#db.myNewCollection.update_many({},	{"$inc":	{"age":	1}})
#db.myNewCollection.delete_one({"name":	"Alice	Johnson"})
#db.myNewCollection.delete_many({"age":	{"$gt":	30}})
db.myNewCollection.insert_many([
		{
			"Title": "The Great Gatsby",
			"Author": "F.Scott Fitzgerald",
			"ISBN": "978-0743273565",
			"Publication date":1925,
			"Genre": "Fiction, Drama",
			"Publisher": "Scribner"
		},
		{
			"Title": "1984",
			"Author": "George Orwell",
			"ISBN": "978-0451524935",
			"Publication date": 1949,
			"Genre": "Dystopian, Political",
			"Publisher": "Penguin"
		},
		{
			"Title": "To Kill a Mockingbird",
			"Author": "Harper Lee",
			"ISBN": "978-0060935467",
			"Publication date":1960,
			"Genre": "Fiction, Legal Drama",
			"Publisher": "Harper Perennial Modern"
		},
		{
			"Title": "Brave New World",
			"Author": "Aldous Huxley",
			"ISBN": "978-0060850524",
			"Publication date": 1932,
			"Genre": "Dystopian, Sci-Fi",
			"Publisher": "Harper Perennial Modern"
		},
		{
			"Title": "Animal Farm",
			"Author": "George Orwell",
			"ISBN": "978-0451526342",
			"Publication date": 1945,
			"Genre": "Political Satire",
			"Publisher": "Penguin"
		},
		{
			"Title": "Pride and Prejudice",
			"Author": "Jane Austen",
			"ISBN": "978-0141439518",
			"Publication date": 1813,
			"Genre": "Romance, Fiction",
			"Publisher": "Penguin Classics"
		}
	])
print("Done")