from database.database import db

# Notez que tous les champs de mock-data ne sont pas pris en compte
class Engineer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    site = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Engineer {}>'.format(self.username)
