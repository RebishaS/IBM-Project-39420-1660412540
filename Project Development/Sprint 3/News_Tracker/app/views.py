# import ibm_db
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, login_required, logout_user
from app import app,db,User,RegisterForm,LoginForm,bcrypt
from .request import (businessArticles, entArticles, get_news_source,
                      healthArticles, publishedArticles, randomArticles,
                      scienceArticles, sportArticles, techArticles,
                      topHeadlines)

# conn = ibm_db.connect(
#     'DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rzf07928;PWD=Gsmx9dW4PeOQMqze', '', ''
# )


    
@app.route('/', methods = ['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     # getting user data
    #     email = request.form.get('email')
    #     password = request.form.get('password')
    #     sql_check_query = "SELECT * FROM user WHERE email = ?"
    #     stmt = ibm_db.prepare(conn, sql_check_query)
    #     ibm_db.bind_param(stmt, 1, email)
    #     ibm_db.execute(stmt)
    #     account = ibm_db.fetch_assoc(stmt)
    #     print(account)
    #     if account:
    #         # email id exists
    #         # checking if the password is correct
    #         if not account['PASSWORD'] == password:
    #             flash('Invalid password', category='error')

    #         else:
    #             # user entered the correct password
    #             # redirecting the user to the dashboard
    #             return render_template('home.html', account=account)

    #     else:
    #         # email id does not exist in the database
    #         flash('Email invalid... Try Again', category='error')
            
    #     return render_template('login.html')
    
    # return render_template('login.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/publishedArticles')
def home():
    articles = publishedArticles()
    
    todays_news = articles[0]
    top_headlines = articles[1]
    business_articles = articles[2]
    tech_articles = articles[3]
    entertainment_articles = articles[4]
    science_articles = articles[5]
    sport_articles = articles[6]
    health_articles = articles[7]
        
    return  render_template('home.html', 
                            todays_news = todays_news, 
                            top_headlines = top_headlines,
                            business_articles = business_articles,
                            tech_articles = tech_articles,
                            entertainment_articles = entertainment_articles,
                            science_articles = science_articles,
                            sport_articles = sport_articles,
                            health_articles = health_articles,)

@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return  render_template('headlines.html', headlines = headlines)

@app.route('/articles')
def articles():
    random = randomArticles()

    return  render_template('articles.html', random = random)

@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return  render_template('sources.html', newsSource = newsSource)

@app.route('/category/business')
def business():
    sources = businessArticles()

    return  render_template('business.html', sources = sources)

@app.route('/category/tech')
def tech():
    sources = techArticles()

    return  render_template('tech.html', sources = sources)

@app.route('/category/entertainment')
def entertainment():
    sources = entArticles()

    return  render_template('entertainment.html', sources = sources)

@app.route('/category/science')
def science():
    sources = scienceArticles()

    return  render_template('science.html', sources = sources)

@app.route('/category/sports')
def sports():
    sources = sportArticles()

    return  render_template('sport.html', sources = sources)

@app.route('/category/health')
def health():
    sources = healthArticles()

    return  render_template('health.html', sources = sources)