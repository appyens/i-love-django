### First Step
1. django-admin and manage.py - Ref
    1. Running management commands from your code - Ref
1. Settings - Ref
1. Applications - Ref


### Handling HTTP requests
1. Writing views
    1. function based
        1. simple view
        1. mapping URL to view
        1. Request and response objects - Ref
        1. returning errors
        1. Customizing error views
        1. View decorators
            1. Allowed HTTP methods 
                1. `require_http_methods`
                1. `require_GET()`
                1. `require_POST()`
                1. `require_safe`
            1. Conditional view processing
            1. GZip compression
            1. Vary headers
            1. Caching
   
    1. class based view
        1. Introduction to class-based views
        1. Built-in class-based generic views
        1. Form handling with class-based views
        1. Using mixins with class-based views
        1. Basic examples
        1. Usage in your URLconf
        1. Subclassing generic views
        1. View decorators - Extra

1. URL dispatcher
    1. How Django processes a request
    1. Paths - `path()`
    1. Capturing values from URL - `path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail)`
    1. Path converters - `<str:a>/<int:b>/<slug:a>/<uuid:a>/`
    1. Registering custom path converters - `register_converter()`
    1. Using regular expressions - `re_path()`
        1. Using unnamed regular expression groups - `(?P<group>\S+)`
        1. Nested arguments
    1. What the URLconf searches against
    1. Specifying defaults for view arguments - `def view(request, value=3)`
    1. Syntax of the `urlpatterns` variable
    1. Error handling views - `handler400 handler403 handler404 handler500`
    1. Including other URLconfs - `include()`
        1. Captured parameters - `path(<value>/abc, include(xyz.urls))`
    1. Passing extra options to view functions - `path('blog/<int:year>/', view, {'foo': 'bar'}`
    1. Passing extra options to include - `path('blog/', include('inner'), {'blog_id': 3})`
    1. Reverse resolution of URLs
        1. from html - `url` tag
        1. from python code - `reverse('news-year-archive', args=(year,))`
    1. Naming URL patterns - `path('blog/', view, name='view_name')`
    1. URL namespaces
        1. application namespace
        1. instance namespace
        1. Reversing namespaced URLs - `'polls:index'`
        1. URL namespaces and included URLconfs
            1. Application namespaces of included URLconfs can be specified in two ways.
                1. `app_name`
                1. `(<list of path()/re_path() instances>, <application namespace>)`
    
1. File Uploads
    1. File handling - Ref
    1. Basic file uploads (with Django form)
    1. Handling uploaded files with a model (with Django form)
    1. Uploading multiple files (with Django form)
        1. implemnt post method in `FormView()`
    1. Upload Handlers
        1. `django.core.files.uploadhandler.MemoryFileUploadHandler`
        1. `django.core.files.uploadhandler.TemporaryFileUploadHandler`
    1. Where uploaded data is stored
    1. Changing upload handler behavior - through setting.py
    1. Modifying upload handlers on the fly

1. Django shortcut functions
    1. `render(request, template_name, context=None, content_type=None, status=None, using=None)`
    1. `redirect()` -  HttpResponseRedirect()
    1. `get_object_or_404()`
    1. `get_list_or_404()`

1. Middleware
    1. Middleware - Ref
    1. Writing your own middleware
    1. Marking middleware as unused
    1. Activating middleware
    1. Middleware order and layering
    1. Other middleware hooks
        1. process_view()
        1. process_exception()
        1. process_template_response()
    1. Dealing with streaming responses
    1. Dealing with streaming responses
    1. Exception handling

1. How to use sessions

### Templates

1. Support for template engines
1. The Django template language


### Models & Databases
1. Models
1. Making queries
1. Aggregation
1. Search
1. Managers
1. Performing raw SQL queries
1. Database transactions
1. Multiple databases
1. Tablespaces
1. Database access optimization
1. Database instrumentation

### Migrations

1. The Commands
1. Backend Support
1. Workflow
1. Dependencies
1. Migration files
1. Adding migrations to apps
1. Reversing migrations
1. Historical models
1. Considerations when removing model fields
1. Data Migrations
1. Squashing migrations
1. Serializing values
1. Supporting multiple Django versions

### Admin

### Working with forms

1. HTML forms
1. Django’s role in forms
1. Forms in Django
1. Building a form
1. More about Django Form classes
1. Working with form templates
1. Further topics


### Managing files

1. Using files in models
1. The File object
1. File storage

### Testing in Django

1. Writing and running tests
1. Testing tools
1. Advanced testing topics

### User authentication in Django

1. Overview
1. Installation
1. Usage

### Django’s cache framework

1. Setting up the cache
1. The per-site cache
1. The per-view cache
1. Template fragment caching
1. The low-level cache API
1. Downstream caches
1. Using Vary headers
1. Controlling cache: Using other headers
1. Order of MIDDLEWARE

### Conditional View Processing

1. The condition decorator
1. Shortcuts for only computing one value
1. Using the decorators with other HTTP methods
1. Comparison with middleware conditional processing

### Cryptographic signing

1. Protecting the SECRET_KEY
1. Using the low-level API

### Sending email

1. Quick example
1. send_mail()
1. send_mass_mail()
1. mail_admins()
1. mail_managers()
1. Examples
1. Preventing header injection
1. The EmailMessage class
1. Email backends
1. Configuring email for development

### Internationalization and localization

1. Overview
1. Definitions

### Logging

1. A quick logging primer
1. Using logging
1. Configuring logging
1. Django’s logging extensions
1. Django’s default logging configuration

### Pagination

1. The Paginator class
1. Example
1. Paginating a ListView
1. Using Paginator in a view function

### Security in Django

1. Cross site scripting (XSS) protection
1. Cross site request forgery (CSRF) protection
1. SQL injection protection
1. Clickjacking protection
1. SSL/HTTPS
1. Host header validation
1. Referrer policy
1. Session security
1. User-uploaded content
1. Additional security topics

### Performance and optimization

1. Introduction
1. General approaches
1. Caching
1. Understanding laziness
1. Databases
1. HTTP performance
1. Template performance
1. Using different versions of available software

### Serializing Django objects

1. Serializing data
1. Deserializing data
1. Serialization formats
1. Natural keys

### Django settings

1. The basics
1. Designating the settings
1. Default settings
1. Using settings in Python code
1. Altering settings at runtime
1. Security
1. Available settings
1. Creating your own settings
1. Using settings without setting DJANGO_SETTINGS_MODULE

### Signals

1. Listening to signals
1. Defining and sending signals
1. Disconnecting signals

### System check framework

1. Writing your own checks

### External packages

1. Localflavor
1. Comments
1. Formtools

### Asynchronous support

1. Async-safety
1. Async adapter functions

### Authentication

### Internationalization
### Security
### Common Web tools
1. Authentication: 
1. 1. Overview | 
1. 1. Using the authentication system
1. 1. Password management
1. 1. Customizing authentication
1. 1. JWT
1. 1. OAuth / OAuth2
1. Caching
1. Logging
1. Sending emails
1. Syndication feeds (RSS/Atom)
1. Pagination
1. Messages framework
1. Serialization
1. Sessions
1. Sitemaps
1. Static files management
1. Data validation
1. Cookie


### Writing Tests
### DevOps and Deployment
