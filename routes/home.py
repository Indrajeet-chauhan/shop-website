from flask import Blueprint, render_template, request, redirect, url_for, json
from database.database import db
from database.models import Quotation
from datetime import datetime

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form.get('company_name', 'GRIHA ENTERPRISES')
        customer_name = request.form.get('customer_name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        date_str = request.form.get('date')
        gst_rate = float(request.form.get('gst_rate', 18.0))
        
        item_names = request.form.getlist('item_name[]')
        widths = request.form.getlist('width[]')
        heights = request.form.getlist('height[]')
        pallas = request.form.getlist('palla[]')
        h_lines = request.form.getlist('h_lines[]')
        v_lines = request.form.getlist('v_lines[]')
        lock_systems = request.form.getlist('lock_system[]')
        rates = request.form.getlist('rate[]')
        
        glass_types = request.form.getlist('glass_type[]')
        frame_colors = request.form.getlist('frame_color[]')
        mosquito_nets = request.form.getlist('mosquito_net[]')
        accessories_list = request.form.getlist('accessories[]')
        jobs_list = request.form.getlist('jobs[]')
        
        items_list = []
        subtotal = 0.0
        
        for i in range(len(item_names)):
            if item_names[i]:
                w = float(widths[i] or 0)
                h = float(heights[i] or 0)
                p = int(pallas[i] if pallas[i] else 1)
                r = float(rates[i] or 0)
                area = w * h
                total_item_price = area * r
                subtotal += total_item_price
                
                items_list.append({
                    'name': item_names[i],
                    'width': w,
                    'height': h,
                    'palla': p,
                    'h_lines': int(h_lines[i] if h_lines[i] else 0),
                    'v_lines': int(v_lines[i] if v_lines[i] else 0),
                    'lock_system': lock_systems[i],
                    'rate': r,
                    'total': total_item_price,
                    'area': area,
                    'glass_type': glass_types[i] if i < len(glass_types) else '',
                    'frame_color': frame_colors[i] if i < len(frame_colors) else '',
                    'mosquito_net': mosquito_nets[i] if i < len(mosquito_nets) else '',
                    'accessories': accessories_list[i] if i < len(accessories_list) else '',
                    'jobs': jobs_list[i] if i < len(jobs_list) else ''
                })
        
        gst_amount = subtotal * (gst_rate / 100)
        grand_total = subtotal + gst_amount
        
        quote_count = Quotation.query.count() + 1
        quotation_no = f"QT-{datetime.now().strftime('%Y')}{quote_count:04d}"
        
        new_quote = Quotation(
            quotation_no=quotation_no,
            company_name=company_name,
            customer_name=customer_name,
            address=address,
            phone=phone,
            date=date_str,
            items_json=json.dumps(items_list),
            subtotal=round(subtotal, 2),
            gst_rate=gst_rate,
            gst_amount=round(gst_amount, 2),
            grand_total=round(grand_total, 2)
        )
        db.session.add(new_quote)
        db.session.commit()
        
        return redirect(url_for('home.view_quotation', id=new_quote.id))
        
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('home/index.html', current_date=current_date)

@home_bp.route('/quotation/<int:id>')
def view_quotation(id):
    quote = Quotation.query.get_or_404(id)
    items = json.loads(quote.items_json)
    return render_template('home/services.html', quote=quote, items=items) # standard quotation view path