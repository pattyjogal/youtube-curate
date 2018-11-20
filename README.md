# YouTube Curate

Sometimes, you and a group of friends/a community want to come together and find your favorite videos on YouTube. In my case, I wanted to compile some of the best SiivaGunner HQ Rips that my friends enjoyed into an "album" of sorts. However, getting all of that data together can be a real pain. This website + API should make that easier, providing a list of videos for users to rate, and keeping a leaderboard of the top X videos.

## API - Getting Started
This project used the Django REST-Framework for its backend. This will require some setup to get going on your side. 

### Environment
Like with all good Python projects, first create and activate a virtualenv. I would follow [this guide](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) if you're not very familiar with this.

Once you've the environment working, run:

```
pip install -r api/requirements.txt
```

which will get all of the requirements installed.

### Database
Now, get the database up and running. You will need to have postgresql installed first.

Start off by creating the database and user to go along with is. The database name by default is `curate`, and the role name is `db_admin`. You can change this in the `settings.py`. Run these commands to get the database up as well as the user.

```
sudo -u postgres createuser curate
```

```
sudo -u postgres createdb db_admin
```

### Running the server
The first time you run the server, you will also need to migrate the models to the database. Change directory into the `api` folder, and run these commands:

```
python manage.py migrate
```

```
python manage.py runserver
```

You should now see the standard Django log output, showing that everything is working fine!
