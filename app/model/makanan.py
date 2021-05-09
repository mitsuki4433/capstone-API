from app import db

class Makanan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    kalori = db.Column(db.Integer, nullable=False)

    def __ref__(self):
        return '<Makanan {}>'.format(self.name)
