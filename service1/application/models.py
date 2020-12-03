class Char(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wep = db.Column(db.String(10))
    element = db.Column(db.String(200)) 
    name = db.Column(db.String(200)) '''
