import sqlite3
import redis

from pathlib import Path
from faker import Faker

CACHE_KEY_PREFIX = "quote"
DB_PATH = Path(__file__).parent / Path("quotes.sqlite3")
quote_count = 0
fake = Faker()
cache = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)


def setup_db():
	try:
		with sqlite3.connect(DB_PATH) as db:
			cursor = db.cursor()
			cursor.execute("CREATE TABLE quotes(id INTEGER PRIMARY KEY, text TEXT)")
			db.commit()
			print("Table 'quotes' created")
	except Exception as e:
		print(e)


def add_quotes(quotes_list):
	global quote_count
	added_quotes_list = []
	try:
		with sqlite3.connect(DB_PATH) as db:
			cursor = db.cursor()
			for quote in quotes_list:
				quote_count += 1
				cursor.execute("INSERT OR IGNORE INTO quotes(id, text) VALUES(?, ?)", (quote_count, quote))
				added_quotes_list.append((quote_count, quote))
			db.commit()
	except Exception as e:
		print(e)

	return added_quotes_list


def main():
	msg = "Choose your mode! Enter 'init' or 'update_db_only' or 'update_all': "
	mode = input(msg)
	mode = mode.lower()

	if mode == "init":
		# Creates the table in the database
		setup_db()
	elif mode == "update_all":
		# Inject the quotes into the database and add them to the cache
		quotes_list = [fake.sentence() for _ in range(1, 11)]
		added_quotes_list = add_quotes(quotes_list)
		if added_quotes_list:
			print("New (fake) quotes added to the database.")
			for quote_id, quote in added_quotes_list:
				cache_key = f"CACHE_KEY_PREFIX.{quote_id}"
				# Add a quote to the Redis cache with a lifespan of 1 minute (60 seconds).
				# After this period, Redis will automatically delete the key.
				cache.set(cache_key, quote, ex=60)
				print(f"Added: '{(quote_id, quote)}'.")
	elif mode == "update_db_only":
		# Inject the quotes into the database only
		quotes_list = [fake.sentence() for _ in range(1, 11)]
		added_quotes_list = add_quotes(quotes_list)
		if added_quotes_list:
			print("New (fake) quotes added to the database ONLY.")
			for quote_id, quote in added_quotes_list:
				print(f"Added: '{(quote_id, quote)}'.")


if __name__ == "__main__":
	main()
	"""
	Choose your mode! Enter 'init' or 'update_db_only' or 'update_all': init
	Table 'quotes' created
	"""

	"""
	Choose your mode! Enter 'init' or 'update_db_only' or 'update_all': update_db_only
	New (fake) quotes added to the database ONLY.
	Added: '(1, 'Town might cover level.')'.
	Added: '(2, 'Reality kitchen set step tend.')'.
	Added: '(3, 'Year significant policy imagine low debate.')'.
	Added: '(4, 'Old truth compare customer whole.')'.
	Added: '(5, 'Ahead order agent win make.')'.
	Added: '(6, 'Practice particularly she start almost.')'.
	Added: '(7, 'Window forget building group hand tough never.')'.
	Added: '(8, 'Month or bit letter bag.')'.
	Added: '(9, 'Water imagine move item.')'.
	Added: '(10, 'Stop stage particularly name life who region.')'.
	"""
