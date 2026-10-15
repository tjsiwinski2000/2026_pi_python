1015-2026
- adding chess to django app
- template folder will be catch all for HTML like this
1002-2026
- issue with some piece images
The images were missing because chessboard.js defaults to searching for image files on your local server relative path (img/chesspieces/wikipedia/{piece}.png). When hosted strictly inside a single file without downloading local assets, those image calls fail.
- otherwise seems decent all-in-one chess file solution


CLAUDE NOTES
Django can load templates from any folder you point it at, and a URL can serve a template directly.

Step 1: tell Django where the folder is. Create a templates folder next to manage.py and put index.html in it (you could name it chess.html to avoid clashing with other pages). Then in settings.py, find the TEMPLATES setting and change the DIRS line:

python
'DIRS': [BASE_DIR / 'templates'],

(If your BASE_DIR comes from os.path, use os.path.join(BASE_DIR, 'templates') instead.)

Django will now look in that folder when you ask for a template by name.

Next comes the URL. Django has a built-in TemplateView that renders a template with no view function needed. Can you guess which file the URL goes in, and what you’d import from django.views.generic? Try it, or tell me what your project’s urls.py looks like and we’ll write it together.