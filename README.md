MFE Pictures Website

A website for MFE Pictures (Mmenyane Family Entertainment), a film and television production company based in Limpopo, South Africa.

The company wanted a classic, formal site in their brand colours (green, white and black) where they can introduce themselves and keep their audience up to date with news and photos. This is that site.

 What is on the site

- Home: the company profile: who they are, what they do, their mission and vision, and how to reach them
- News: blog posts the team can write and publish themselves
- Gallery: a photo gallery with bulk photo upload
- About: links to their Instagram, Facebook and TikTok pages
- Admin area: a simple, password-protected place where the team adds posts and photos, with no coding needed

 Built with

- Python and Django 5.2
- SQLite for the database
- Pillow for handling uploaded images
- Plain HTML and CSS (no front-end framework)
- Hosted on PythonAnywhere

 Running it on your own computer

You'll need Python 3.10 or newer and Git.

1. Get the code

bash
----------------------------------------------------------------------------
git clone https://github.com/Hope-Net-Nerd/Mmenyane_Family_Entertainment.git
cd Mmenyane_Family_Entertainment
----------------------------------------------------------------------------

2. Create a virtual environment and install the packages

On Windows:

bash
-------------------------------
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
-------------------------------

On Mac or Linux, activate it with source .venv/bin/activate instead.

3. Add your settings

Create a file called .env in the same folder as manage.py:

----------------------------------------------
DJANGO_SECRET_KEY='put-a-long-random-key-here'

DJANGO_DEBUG=True
----------------------------------------------

You can generate a key with:

bash
----------------------------------------------------------------------------------------------------------
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
----------------------------------------------------------------------------------------------------------

The .env file is private and is already in .gitignore, so it never gets uploaded to GitHub.

4. Set up the database and start the site

bash
--------------------------------
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
--------------------------------

Then open http://127.0.0.1:8000 in your browser.

Adding posts and photos

1. Log in to the admin area with your superuser account.
2. Posts: add a title and text. A cover image and short summary are optional. Untick Published to keep a post as a draft.
3. Gallery images: add one photo at a time, or use the Upload multiple photos button to add many at once.

New content shows up on the site straight away.

Putting it online

The site runs on PythonAnywhere (https://223040589.pythonanywhere.com/). In short:

1. Clone the repo on the server and create a virtual environment.
2. Install the packages and create the .env file there, with its own secret key and DJANGO_DEBUG=False.
3. Run migrate, collectstatic and createsuperuser.
4. On the Web tab, point the app at the project folder, the virtual environment and the WSGI file. Add static file mappings for /static/ ( staticfiles folder) and /media/ ( media folder).
5. Press Reload.

To update the live site later, run git pull on the server, then press Reload.

Good to know

- Back things up. The posts live in `db.sqlite3` and the uploaded photos live in the `media/` folder. Neither is stored on GitHub, so download copies now and then.
- Keep secrets out of Git. Never commit the `.env` file or the database.
- Make the admin login strong. Use a long, unique password for every account that can log in.

Project layout

----------------------------------------------------------------------------
core/                              Django settings and main URLs
mmenyane_family_entertainment/     The app: pages, models, templates, styles
manage.py                          Django's command-line tool
requirements.txt                   Python packages the site needs
----------------------------------------------------------------------------

Credits and Appretiations

Designed and built by Hope for MFE Pictures. Thank you to the MFE Pictures team for trusting me with their site.
