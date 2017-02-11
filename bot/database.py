from bot import db

class Database():

	@staticmethod
	def clear_db():
		meta = db.metadata
		for table in reversed(meta.sorted_tables):
			db.session.execute(table.delete())
		commit_db.__func__()

	@staticmethod
	def commit_db():
		db.session.commit()

	@staticmethod
	def add_to_db(obj):
		db.session.add(obj)
		commit_db.__func__()