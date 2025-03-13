import sqlite3
import redis
from pathlib import Path

CACHE_KEY_PREFIX = "quote"
DB_PATH = Path(__file__).parent / Path("quotes.sqlite3")
cache = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)


def get_quote(quote_id: str) -> str:
	"""
	Fetch a quote by its identifier.
	If the quote was not found in the cache,
	query the database to get it
	and put the result in the cache before returning it.
	"""
	out = []
	quote = cache.get(f"{CACHE_KEY_PREFIX}.{quote_id}")

	if quote is None:
		# Get quote from the database
		query = f"SELECT text FROM quotes WHERE id = {quote_id}"
		try:
			with sqlite3.connect(DB_PATH) as db:
				cursor = db.cursor()
				res = cursor.execute(query).fetchone()
				if not res:
					return "There was no quote stored matching that id!"
				quote = res[0]
				out.append(f"Got '{quote}' FROM DB.")
		except Exception as e:
			print(e)
		else:
			# Add to the cache
			cache_key = f"{CACHE_KEY_PREFIX}.{quote_id}"
			cache.set(cache_key, quote, ex=60)
			out.append(f"Added TO CACHE, with key '{cache_key}'.")
	else:
		# Use quote from the cache
		out.append(f"Got '{quote}' FROM CACHE.")

	return "\n".join(out) if out else ""


def main():
	while True:
		quote_id = input("Enter the ID of the quote: ")
		if quote_id.isdigit():
			out = get_quote(quote_id)
			print(out)
		else:
			print("You must enter a number. Please retry.")


if __name__ == "__main__":
	main()
	"""
	Enter the ID of the quote: 2
	Got 'Reality kitchen set step tend.' FROM DB.
	Added TO CACHE, with key 'quote.2'.
	Enter the ID of the quote: 2
	Got 'Reality kitchen set step tend.' FROM CACHE.
	Enter the ID of the quote: 
	"""
