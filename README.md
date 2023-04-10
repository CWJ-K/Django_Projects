# Step
1.  Build django project
```bash
django-admin startproject mysite

```
2. Mirgrate
* build tables for the applications in the INSTALLED_APPS
```bash
python manage.py migrate

```
3. run the development server
```bash
python manage.py runserver

```
4. create an application
```bash
    python manage.py startapp <app>
```


# Project Structure
## Blog
* Post Model: store blog posts in the database
* Post are displayed in reverse chronological order (newest -> oldest)