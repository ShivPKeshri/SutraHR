
Steps:

1. Take pull, install required softwares and install packages from requirements.txt
2. Do makemigrations and migrate. Create a super user
3. Run this project and login to Admin page(Login is not required to access this app).
4. Add Users with Active(Non-Admin), Staff status(Admin), Superuser status(Admin) Permissions.(Don't create with combinations)
5. Any user can create, update and delete records.
6. For deleting any record, need to update is_delete field is True(select is_delete checkbox and update).
6. Staff status,Superuser status users(considering as admin) are able to see all records but Active users or without login this app (considering as non-admin) are able see only undelete records.
7. Filters are made on title and description fileds for the admin users only.
8. Admin user can able to download the records in CSV.
