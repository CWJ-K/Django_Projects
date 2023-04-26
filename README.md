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
### Features
* save posts as a draft until ready for publication
  * status of blog posts


# QuerySet
* Each Django model has at least one manager
  * the default manager is called **object**
    * can create a custom manager
      1. add extra manager methods to an existing manager
        * `Post.objects.my_manager()`
      2. create a new manager by modifying the initial QuerySet that the manager returns
        * `Post.my_manager.all()`
  * get a QuerySet object using model manager
  * e.g. `Post.objects.all()`

* QuerySet are lazy. You can concatenate as many filters and will not hit database unitl the QuerySet is evaluated(`save()`), which translates into an SQL query to the database


# URLs
## SEO-friendly URLs
* `unique_for_date`: not enforced at the database level => migrate is not required, but use migrate to store the process