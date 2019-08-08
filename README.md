Steps:

1. Take a pull, install the required software and install packages from requirements.txt
2. Do makemigrations and migrate. Create a superuser
3. Run this project and login to Admin page- http://localhost:8000/admin/ (Login is not required to access this app).
4. Add Users with Active(Non-Admin), Staff status(Admin), Superuser status(Admin) permissions.
5. App main/home user is - http://localhost:8000/
6. Any user can create, update and delete records.
7. For deleting any record, need to update is_delete field is True(select is_delete checkbox and update).
8. Staff status, Superuser status users(consider as admin) can see all records but Active users or without login this app (considering as non-admin) are able to see only undelete records.
9. Filters are made on title and description fields for the admin users only.
10. Admin user can able to download the records in CSV.