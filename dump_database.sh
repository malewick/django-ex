python manage.py dumpdata > out.json
echo "delete from auth_permission; delete from django_content_type;" | python manage.py dbshell
echo "delete from django_content_type;" | python manage.py dbshell

# --- This to be done on server: --- 
# python manage.py loaddata out.json
