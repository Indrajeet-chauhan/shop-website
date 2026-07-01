from database.database import db
from datetime import datetime

class Quotation(db.Model):
    __tablename__ = 'quotations'
    
    id = db.Column(db.Integer, primary_key=True)
    quotation_no = db.Column(db.String(50), unique=True, nullable=False)
    company_name = db.Column(db.String(100), nullable=False, default="GRIHA ENTERPRISES")
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    date = db.Column(db.String(20), nullable=False)
    items_json = db.Column(db.Text, nullable=False)  # Stores list of structural components
    subtotal = db.Column(db.Float, nullable=False)
    gst_rate = db.Column(db.Float, nullable=False, default=18.0)
    gst_amount = db.Column(db.Float, nullable=False)
    grand_total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)