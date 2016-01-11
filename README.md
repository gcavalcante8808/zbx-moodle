Moodle Zabbix Userparams
------------------------
Simple scripts and userparameter conf to use with zabbix agent and moodle installations.

Introduction
------------
Moodle Userparams is a simple set of scripts that supports moodle course discovery and attr introspection.

With this solution, you can start to monitor the moodle's in you Zabbix Server.

Requirements
------------
For now, you'll need to setup you moodle to properly answer REST requests.

The scripts can be used with python 2.7+ (including python3), but in case of python 2, you'll need to install the 'argparse' module (python 3 already have argparse in its library).

If you don't have the argparse installed on your python 2.7+ installation, you can install it through the following statement (requires 'pip' or 'easy_install'):

```
# pip install argparse
```

In this case the 'argparse' package will be installed system-wide.

Installation
------------

To install this solution you'll need to do the following steps:

1. Clone the repository into a folder (using git clone command);
2. Copy 'docker.conf' into your zabbix agent configuration directory (/etc/zabbix/zabbix.conf.d/ if using official packages from zabbix sia);
3. Create a '/data' directory;
4. Copy 'moodle_discover.py' to '/data';
5. Copy 'mdl_course_discovery.py' to '/data';
6. Import Zabbix Template you Zabbix Server;
7. Link the template against the hosts that have moodle running.

Testing the solution
--------------------

If the target host was configured correctly and the zabbix has received the templates, in some minutes (10 per default) new hosts will appear in the 'Moodle Portals' Group automatically; for now, the templates monitor the 'release' of the moodle installations and creates Web Scenarios for the 'siteurl'.

If you want to implement another items, verify the output of the command '/data/moodle_info.py --server <server> --token <token> --function <function> ' where the params are:

 * Server: server address of your server (without http(s):// prefix);
 * Token: token generated for the moodle webservice;
 * Function: One of many moodle functions. Its possible to get only the needed item value using the '.' separator; in this case, you can use, for exempla, core_webservice_get_site_info.release to get the release number of moodle; if you want to inspect for any attribute you can just put the function or check de documentation of the moodle itself (which need to be enabled);
 * Data: some aditional data that needs to be put the request (like course id, user id, etc) in json format, like {'courseid':1};
 * SSL: If your server is using https to server the site, use this in the following way: --ssl on. If your site dont need ssl, just dont provide it in the arguments.

