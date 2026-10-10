        if image_path != (item['image_path'] or ''):
            remove_lost_found_photo(item['image_path'])
        flash('Your listing has been updated.', 'success')
        return redirect(url_for('lost_found_page', mine='1'))
    con.close()
    body = render_template_string(r'''<div class="page-head"><div><div class="eyebrow">YOUR LISTING</div><h1>Edit item</h1><p>Update the details or replace the item photo.</p></div><a class="btn btn-light" href="{{url_for('lost_found_page',mine='1')}}">← My listings</a></div><div class="card"><form method="POST" enctype="multipart/form-data" class="form-grid"><div><label>Listing type</label><select name="item_type"><option {{'selected' if item['item_type']=='Lost' else ''}}>Lost</option><option {{'selected' if item['item_type']=='Found' else ''}}>Found</option></select></div><div><label>Category</label><select name="category">{% for c in categories_lf %}<option {{'selected' if (item['category'] or 'Other')==c else ''}}>{{c}}</option>{% endfor %}</select></div><div><label>Item name</label><input name="title" required maxlength="140" value="{{item['title']}}"></div><div><label>Location</label><input name="location" required maxlength="200" value="{{item['location']}}"></div><div><label>Date lost/found</label><input type="date" name="item_date" value="{{item['item_date'] or ''}}"></div><div class="full"><label>Description</label><textarea name="description" required maxlength="2000">{{item['description']}}</textarea></div>{% if item['image_data'] or item['image_path'] %}<div class="full"><label>Current photo</label><img src="{{url_for('lost_found_image',item_id=item['id'])}}" alt="Current item photo" style="display:block;max-width:260px;max-height:220px;object-fit:contain;border-radius:14px;border:1px solid #e7dcd2"><label style="margin-top:10px"><input type="checkbox" name="remove_photo" value="yes" style="width:auto"> Remove current photo if no replacement is uploaded</label></div>{% endif %}<div class="full"><label>Replace photo (optional, up to 5 MB)</label><input type="file" name="item_photo" accept="image/png,image/jpeg,image/gif,image/webp"></div><div class="full"><button class="btn btn-primary" type="submit">Save changes →</button></div></form></div>''', item=item, categories_lf=LOST_FOUND_CATEGORIES)
    return render_page(body, 'Edit Lost & Found Item', 'COMMUNITY CARE')


@app.route('/lost-found/<int:item_id>/close', methods=['POST'])
def lost_found_close(item_id):
    if not session.get('user_id') and not session.get('worker_id'):
        return redirect(url_for('login'))
    con = get_db()
    if require('admin'):
        item = con.execute("SELECT id,user_id,title FROM lost_found WHERE id=? AND status='Open'", (item_id,)).fetchone()
    elif require('student'):
        item = con.execute("SELECT id,user_id,title FROM lost_found WHERE id=? AND user_id=? AND status='Open'", (item_id, session['user_id'])).fetchone()
    else:
        item = None
    if not item:
        con.close(); flash('Listing not found or you do not have permission to close it.', 'error')
        return redirect(url_for('lost_found_page'))
    con.execute("UPDATE lost_found SET status='Closed' WHERE id=?", (item_id,))
    con.commit(); con.close()
    flash('Listing marked as resolved.', 'success')
    return redirect(url_for('lost_found_page', mine='1') if require('student') else url_for('lost_found_page'))

def clean_map_form():
    name = request.form.get('name', '').strip()[:140]
    category = request.form.get('category', 'General').strip()[:60]
    building = request.form.get('building', '').strip()[:140]
    description = request.form.get('description', '').strip()[:1000]
    hours = request.form.get('hours', '').strip()[:100]
    phone = re.sub(r'[^0-9+ -]', '', request.form.get('phone', ''))[:30]
    map_url = request.form.get('map_url', '').strip()[:500]
    if map_url and not (map_url.startswith('https://') or map_url.startswith('http://')):
        raise ValueError('Map links must start with http:// or https://.')
    if not name:
        raise ValueError('Enter a location name.')
    return (name, category or 'General', building, description, hours, phone, map_url)


@app.route('/campus-map', methods=['GET', 'POST'])
def campus_map():
    if not session.get('user_id') and not session.get('worker_id'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        if not require('admin'):
            flash('Only administrators can add campus locations.', 'error')
            return redirect(url_for('campus_map'))
        try:
            values = clean_map_form()
        except ValueError as exc:
            flash(str(exc), 'error')
            return redirect(url_for('campus_map'))
        con = get_db()
        con.execute('INSERT INTO campus_locations(name,category,building,description,hours,phone,map_url) VALUES(?,?,?,?,?,?,?)', values)
        con.commit(); con.close()
        flash('Campus location added.', 'success')
        return redirect(url_for('campus_map'))
    query = request.args.get('q', '').strip()[:100]
    con = get_db(); sql = 'SELECT * FROM campus_locations WHERE active=1'; params = []
    if query:
        sql += ' AND (name LIKE ? OR category LIKE ? OR building LIKE ? OR description LIKE ?)'; params += [f'%{query}%'] * 4
    sql += ' ORDER BY category,name'; locations = con.execute(sql, params).fetchall(); con.close()
    body = render_template_string(r'''<div class="page-head"><div><div class="eyebrow">FIND YOUR WAY</div><h1>Campus map & services</h1><p>Find campus buildings and support services. Administrators can add, edit and remove outdated locations.</p></div><span class="chip submitted">{{locations|length}} locations</span></div>
    <div class="help-hero"><div class="hero-kicker">CAMPUS NAVIGATION</div><h2>Know where to go.</h2><p>Search by building, service or category. Open a saved map link, or use Google Maps search for the location name. Only add verified campus details.</p></div>
    {% if session.get('role')=='admin' %}<div class="card" style="margin-bottom:20px"><h3 style="margin-top:0">＋ Add a campus location</h3><form method="POST" class="form-grid"><div><label>Place name *</label><input name="name" required placeholder="Central Library"></div><div><label>Category</label><select name="category"><option>Academic</option><option>Library</option><option>Hostel</option><option>Food & Mess</option><option>Medical</option><option>Security</option><option>Administration</option><option>Sports</option><option>Transport</option><option>Other</option></select></div><div><label>Building / block</label><input name="building" placeholder="Block A"></div><div><label>Opening hours</label><input name="hours" placeholder="9 AM – 6 PM"></div><div><label>Contact phone (optional)</label><input name="phone" placeholder="Verified campus number"></div><div><label>Google Maps link (optional)</label><input name="map_url" type="url" placeholder="https://maps.google.com/…"></div><div class="full"><label>Description / directions</label><textarea name="description" placeholder="Floor, landmark or service details"></textarea></div><div><button class="btn btn-primary" type="submit">Save location →</button></div></form></div>{% endif %}
    <form class="searchbar"><input name="q" value="{{query}}" placeholder="Search library, hostel, medical centre, block…"><button class="btn btn-light">Search</button></form><div class="contact-grid">{% for loc in locations %}<article class="contact-card"><div class="tile-icon">⌖</div><span class="chip submitted">{{loc['category']}}</span><h3 style="margin-top:12px">{{loc['name']}}</h3>{% if loc['building'] %}<p class="muted"><b>Building:</b> {{loc['building']}}</p>{% endif %}<p class="muted">{{loc['description']}}</p>{% if loc['hours'] %}<p class="muted">Hours: {{loc['hours']}}</p>{% endif %}{% if loc['phone'] %}<a class="phone" href="tel:{{loc['phone']}}">☎ {{loc['phone']}}</a>{% endif %}<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:14px"><a class="btn btn-primary" target="_blank" rel="noopener noreferrer" href="{{loc['map_url'] or ('https://www.google.com/maps/search/?api=1&query=' ~ (loc['name'] ~ ' ' ~ loc['building'])|urlencode)}}">Open map / directions ↗</a>{% if session.get('role')=='admin' %}<a class="btn btn-light" href="#edit-location-{{loc['id']}}">Edit details</a>{% endif %}</div>
    {% if session.get('role')=='admin' %}<details id="edit-location-{{loc['id']}}" style="margin-top:14px;border-top:1px solid #e7dcd2;padding-top:14px"><summary style="font-size:12px;font-weight:850;cursor:pointer">Update this location</summary><form method="POST" action="{{url_for('campus_map_update',location_id=loc['id'])}}" class="form-grid" style="margin-top:12px"><div><label>Place name</label><input name="name" required value="{{loc['name']}}"></div><div><label>Category</label><input name="category" required value="{{loc['category']}}"></div><div><label>Building / block</label><input name="building" value="{{loc['building']}}"></div><div><label>Opening hours</label><input name="hours" value="{{loc['hours']}}"></div><div><label>Phone</label><input name="phone" value="{{loc['phone']}}"></div><div><label>Map link</label><input name="map_url" type="url" value="{{loc['map_url']}}" placeholder="https://…"></div><div class="full"><label>Description / directions</label><textarea name="description">{{loc['description']}}</textarea></div><div><button class="btn btn-primary" type="submit">Save changes</button></div></form><form method="POST" action="{{url_for('campus_map_remove',location_id=loc['id'])}}" onsubmit="return confirm('Remove this location from the campus map?')" style="margin-top:10px"><button class="btn btn-light" type="submit">Remove location</button></form></details>{% endif %}</article>{% else %}<div class="empty">No locations have been added yet. Ask an administrator to add verified campus locations.</div>{% endfor %}</div>''', locations=locations, query=query)
    return render_page(body, 'Campus Map', 'FIND YOUR WAY')


@app.route('/campus-map/<int:location_id>/update', methods=['POST'])
def campus_map_update(location_id):
    if not require('admin'):
        return redirect(url_for('login'))
    try:
        values = clean_map_form()
    except ValueError as exc:
        flash(str(exc), 'error')
        return redirect(url_for('campus_map'))
    con = get_db()
    cur = con.execute('UPDATE campus_locations SET name=?,category=?,building=?,description=?,hours=?,phone=?,map_url=? WHERE id=? AND active=1', values + (location_id,))
    con.commit(); con.close()
    flash('Campus location updated.' if getattr(cur, 'rowcount', 1) else 'Location not found or already removed.', 'success')
    return redirect(url_for('campus_map'))


@app.route('/campus-map/<int:location_id>/remove', methods=['POST'])
def campus_map_remove(location_id):
    if not require('admin'):
        return redirect(url_for('login'))
    con = get_db(); con.execute('UPDATE campus_locations SET active=0 WHERE id=?', (location_id,)); con.commit(); con.close()
    flash('Location removed from the active campus map.', 'success')
    return redirect(url_for('campus_map'))


initialize_database()
if os.environ.get("VERCEL") and not DATABASE_URL:
    logging.warning("DATABASE_URL is not configured: SQLite data in /tmp is temporary and may disappear across Vercel instances. Configure a managed PostgreSQL database for persistent records.")
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
