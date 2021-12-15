from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Operations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_1 = db.Column(db.String(64), index=True)
    input_2 = db.Column(db.Integer, index=True)
    operation = db.Column(db.String(256))
    result = db.Column(db.String(20))

    def to_dict(self):
        return {
            'id': self.id,
            'input_1': self.input_1,
            'input_2': self.input_2,
            'operation': self.operation,
            'result': self.result
        }


db.create_all()


@app.route('/')
def index():
    return render_template('table.html')


@app.route('/api/data')
def data():
    query = Operations.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            Operations.name.like(f'%{search}%'),
            Operations.email.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['input_1', 'input_2', 'operation']:
            col_name = 'id'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(Operations, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [user.to_dict() for user in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Operations.query.count(),
        'draw': request.args.get('draw', type=int),
    }


if __name__ == '__main__':
    app.run()
