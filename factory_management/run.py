from factory import create_app, db

app = create_app('DevelopmentConfig')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
