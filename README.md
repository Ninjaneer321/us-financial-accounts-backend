# financial_accounts_us
Visualization tool for the financial accounts of the United States 

# Pre-requisites
Python3, Django, Node and Webpack

# Backend Dev Setup
assuming linux platfrom
```shell
django-admin startproject <$project_name>
cd <$project_name> 
git clone https://github.com/cjackie/financial_accounts_us.git
```
Open up `<$project_name>/settings.py` and add `financial_accounts_us` to `INSTALLED_APPS`. Do other configurations if needed(like db related)
```
python3 manage.py migrate         # create db tables from models.py.
python3 manage.py faus_make       # my customized command to populate data. This will take a while. Go out and get a lunch.
```
Now, it is ready to do development. See official django for more(like creating a new model, html page view, and static content) 

# Frontend Dev Setup
We use Redux + React as our framework, and webpack for bundling source code. For more, see [Redux](http://redux.js.org/) and [React](https://facebook.github.io/react/)

Frontend is in `node/` directory. to compile, run
```
cd node/
webpack
```
then, the resulting javascript file will be in `node/dist` directory. 

