### Introduction
1. What is Django?
1. History of Django Framework
1. Features of Django Framework
    1. Stability
    1. Excellent Documentation
    1. Highly Scalable
    1. Huge Library of Packages
    1. Allows Pragmatic and Robust Design
    1. Django has Evolved Over Time
    1. Open-Source Technology
    1. One of the World’s Best Software Community
    1. Django has Lots of Pre-Made Apps
    1. Loose Coupling
    1. Lesser Code
    1. Doesn’t Repeat
    1. Consistency
    1. SEO Optimised
    1. Versatile in Nature
    1. Offers High Security
    1. Thoroughly Tested
    1. Provides Rapid Development
    1. Implemented in Python
    1. Better CDN connectivity and Content Management
    1. Batteries Included Framework
    1. Fast Processing

1. Cons
    1. Django is Monolithic
    2. Not for smaller projects
    3. Uses Regular Expression for URLs

1. Architecture
    1. MVC Pattern in Django Structure
    1. MTV Pattern
        1. Model --> Model
        1. View --> Template
        1. Controller --> Views
    1. Benefits of Django Architecture
        1. Rapid Development
        2. Loosely Coupled
        3. Ease of Modification

### Development Process
1. Installation
1. Creating project
1. Applications - Ref
1. Settings - Ref
1. Exceptions
1. django-admin and manage.py - Ref
    1. Running management commands from your code - Ref
1. Testing
1. Deployment

## View
1. URL confs
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

1. Writing views
    1. simple view
    1. mapping URL to view
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

1. Django shortcut functions
    1. `render(request, template_name, context=None, content_type=None, status=None, using=None)`
    1. `redirect()` -  HttpResponseRedirect()
    1. `get_object_or_404()`
    1. `get_list_or_404()`

1. View Decorators
    1. Allowed HTTP methods
        1. `require_http_methods`
        1. `require_GET()`
        1. `require_POST()`
        1. `require_safe()`

    1. Conditional view processing
        1. `condition(etag_func=None, last_modified_func=None)`
        1. `etag(etag_func)`
        1. `last_modified(last_modified_func)`

    1. GZip compression
        1. `gzip_page()`

    1. Vary headers
        1.  `vary_on_cookie(func)`
        1.  `vary_on_headers(*headers)`

    1. Caching
        1. `cache_control(**kwargs)`
        1. `never_cache(view_func)`

1. Built-in Views
    1. Serving files in development
        * `static.serve(request, path, document_root, show_indexes=False)`
    
    1. Error views
        1. The 404 (page not found) view
            * `defaults.page_not_found(request, exception, template_name='404.html')`
        1. The 500 (server error) view
            * `defaults.server_error(request, template_name='500.html')`
        1. The 403 (HTTP Forbidden) view
            * `defaults.permission_denied(request, exception, template_name='403.html')`
        1. The 400 (bad request) view
            * `defaults.bad_request(request, exception, template_name='400.html')`

1. Request-Response objects
    1. Attribute
        1. HttpRequest.scheme
        1. HttpRequest.body
        1. HttpRequest.path
        1. HttpRequest.path_info
        1. HttpRequest.method
        1. HttpRequest.encoding
        1. HttpRequest.content_type
        1. HttpRequest.content_params
        1. HttpRequest.GET
        1. HttpRequest.POST
        1. HttpRequest.COOKIES
        1. HttpRequest.FILES
        1. HttpRequest.META
        1. HttpRequest.headers
        1. HttpRequest.resolver_match

    1. Attributes set by middleware
        1. HttpRequest.current_app
        1. HttpRequest.urlconf

    1. Attributes set by middleware
        1. HttpRequest.session
        1. HttpRequest.site
        1. HttpRequest.user
        

1. TemplateResponse objects

    
1. File Uploads
    1. Overview
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
    
    1. File Object
        1. The File class
        1. The ContentFile class
        1. The ImageFile class
        1. Additional methods on files attached to objects
            1.  File.save(name, content, save=True)
            1.  File.delete(save=True)
    
    1. File storage API
        1. Getting the current storage class
            1.  class DefaultStorage
        1. The FileSystemStorage class
            * `class FileSystemStorage(location=None, base_url=None, file_permissions_mode=None, directory_permissions_mode=None)`
        1. The Storage class

1. class based view
    1. Introduction to class-based views
    1. Built-in class-based generic views
        1. display views
        1. editing views
    1. Form handling with class-based views
    1. Using mixins with class-based views
    1. Flattened index
    1. Basic examples
    1. Usage in your URLconf
    1. Subclassing generic views
    1. View decorators - Extra

1. Advanced: 
    1. Generating CSV
    1. Generating PDF

1. Middleware
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

### Templates

1. Support for template engines
1. The Django template language
1. Built-in tags and filters
1. Humanization
1. Template API
1. Custom tags and filters


### Models & Databases
1. Introduction
    1. Field types
    1. Field Option
    1. Automatic primary key fields
    1. Verbose field names
    1. Relationships
        1. Many-to-one relationships
        1. Many-to-many relationships
        1. One-to-one relationships
    1. Models across files
    1. Field name restrictions
    1. Custom field types
    1. Meta options
    1. Model attributes - `objects`
    1. Model methods - 
        1. `custom methods provides row level functionality`
        1. `_str__()`
        1. `get_absolute_url()`
    1. Overriding predefined model methods
    1. Executing custom SQL
    1. Model inheritance
        1. Abstract base classes
            1. Meta inheritance
            1. Be careful with related_name and related_query_name
        1. Multi-table inheritance
            1. Meta and multi-table inheritance
            1. Inheritance and reverse relations
            1. Specifying the parent link field
        1. Proxy models
            1. QuerySets still return the model that was requested
            1. Base class restrictions
            1. Proxy model managers
            1. Differences between proxy inheritance and unmanaged models
        1. Multiple inheritance
            1. Field name “hiding” is not permitted
    1. Organizing models in a package

1. Field Types

    1. `AutoField`
    1. `BigAutoField`
    1. `BigIntegerField`
    1. `BinaryField`
    1. `BooleanField`
    1. `CharField`
    1. `DateField`
    1. `DateTimeField`
    1. `DecimalField`
    1. `DurationField`
    1. `EmailField`
    1. `FileField`
        FileField and FieldFile
    1. `FilePathField`
    1. `FloatField`
    1. `ImageField`
    1. `IntegerField`
    1. `GenericIPAddressField`
    1. `NullBooleanField`
    1. `PositiveIntegerField`
    1. `PositiveSmallIntegerField`
    1. `SlugField`
    1. `SmallAutoField`
    1. `SmallIntegerField`
    1. `TextField`
    1. `TimeField`
    1. `URLField`
    1. `UUIDField`

    1. Relationship fields

        1. ForeignKey
            1. Database Representation
                1. `class ForeignKey(to, on_delete, **options)`
            1. Arguments
                1. `on_delete`
                1. `limit_choices_to`
                1. `related_name`
                1. `related_query_name1`
                1. `to_field`
                1. `db_constraint`
                1. `swappable`
            
        1. ManyToManyField
            1. Database Representation
                1. `class ManyToManyField(to, **options)`
            1. Arguments
                1. `related_name`
                1. `related_query_name`
                1. `limit_choices_to`
                1. `symmetrical`
                1. `through`
                1. `through_fields`
                1. `db_table`
                1. `db_constraint`
                1. `swappable`
        1. OneToOneField
            1. Database Representation
                1. `class OneToOneField(to, on_delete, parent_link=False, **options)`
                1. It is same as ForeignKey with unique = True
            1. Arguments
                1. `parent_link`

1. Field Option
    1. `null`
    1. `blank`
    1. `choices`
    1. Enumeration types
    1. `db_column`
    1. `db_index`
    1. `db_tablespace`
    1. `default`
    1. `editable`
    1. `error_messages`
    1. `help_text`
    1. `primary_key`
    1. `unique`
    1. `unique_for_date`
    1. `unique_for_month`
    1. `unique_for_year`
    1. `verbose_name`
    1. `validators`

1. Field Class
    1. Methods
        1. `get_internal_type()`
        1. `db_type(connection)`
        1. `rel_db_type(connection)`
        1. `get_prep_value(value)`
        1. `get_db_prep_value(value, connection, prepared=False)`
        1. `from_db_value(value, expression, connection)`
        1. `get_db_prep_save(value, connection)`
        1. `pre_save(model_instance, add)`
        1. `to_python(value)`
        1. `value_from_object(obj)`
        1. `value_to_string(obj)`
        1. `formfield(form_class=None, choices_form_class=None, **kwargs)`
        1. `deconstruct()`
    1. Attributes
        1. `auto_created`
        1. `concrete`
        1. `hidden`
        1. `is_realation`
        1. `model`
    1. Attributes for fields with relation
        1. `many_to_many`
        1. `many_to_one`
        1. `one_to_many`
        1. `one_to_one`
        1. `related_model`

1. Model Meta options
    1. `abstract`
    1. `app_label`
    1. `base_manager_name`
    1. `db_table`
    1. `db_tablespace`
    1. `default_manager_name`
    1. `default_related_name`
    1. `default_related_name`
    1. `order_with_respect_to`
    1. `ordering`
    1. `permissions`
    1. `default_permissions`
    1. `proxy`
    1. `required_db_features`
    1. `required_db_vendor`
    1. `select_on_save`
    1. `indexes`
        1. Model index reference
        1. `class Index(fields=(), name=None, db_tablespace=None, opclasses=(), condition=None)`
        1. It is given in Meta option
    1. `unique_together`
    1. `constraints`
    1. `verbose_name`
    1. `verbose_name_plural`
    1. `label`
    1. `label_lower`

1. Model class reference
    1. `Model.objects`

1. Querysets:
    1. Making Queries
        1. Creating objects
        1. Saving changes to objects
            1. Saving ForeignKey and ManyToManyField fields
        1. Retrieving objects
            1. Retrieving all objects
            1. Retrieving specific objects with filters
            1. Chaining filters
            1. Filtered QuerySets are unique
            1. QuerySets are lazy
            1. Retrieving a single object with get()
            1. Other QuerySet methods
            1. Limiting QuerySets
            1. Field lookups
            1. Lookups that span relationships
                1. Spanning multi-valued relationships
            1. Filters can reference fields on the model
            1. The pk lookup shortcut
            1. Escaping percent signs and underscores in LIKE statements
            1. Caching and QuerySets
                1. When QuerySets are not cached
            1. Complex lookups with Q objects
        1. Comparing objects
        1. Deleting objects
        1. Copying model instances
        1. Updating multiple objects at once
        1. Related objects
            1. One-to-many relationships
                1. Forward
                1. Following relationships “backward”
                1. Using a custom reverse manager
                1. Additional methods to handle related objects
            1. Many-to-many relationships
            1. One-to-one relationships
        1. How are the backward relationships possible?
        1. Queries over related objects
        1. Falling back to raw SQL
    
    1. Queryset Methods
        1. When QuerySets are evaluated
            1. Iteration
            1. Slicing
            1. Pickling/Caching
            1. repr()
            1. len()
            1. list()
            1. bool()
        1. Pickling QuerySets
        1.  class QuerySet(model=None, query=None, using=None, hints=None)
            1. two public attributes - ordered and db
        1. Methods that return new QuerySets
        1. Operators that return new QuerySets
            1. AND
            1. OR
        1. Methods that do not return QuerySets
            1. get
            1. create()
            1. get_or_create()
            1. update_or_create()
            1. bulk_create()
            1. bulk_update()
            1. count()
            1. in_bulk()
            1. iterator()
            1. latest()
            1. earliest()
            1. first()
            1. last()
            1. aggregate()
            1. exists()
            1. update()
            1. delete()
            1. as_manager()
            1. explain()
        1. Field Lookups
        1. Aggregation functions
        1. Query-related tools

    1. Lookup Expressions (Lookup API reference)
        1. Registration API
        1. The Query Expression API
        1. Transform reference
        1. Lookup reference

### Admin
1. ModelAdmin objects
1. The register decorator
1. Discovery of admin files
1. ModelAdmin options
    1.  ModelAdmin.actions
    1.  ModelAdmin.actions_on_top
    1.  ModelAdmin.actions_on_bottom
    1.  ModelAdmin.actions_selection_counter
    1.  ModelAdmin.date_hierarchy
    1.  ModelAdmin.empty_value_display
    1.  ModelAdmin.exclude
    1.  ModelAdmin.fields
    1.  ModelAdmin.fieldsets
    1.  ModelAdmin.filter_horizontal
    1.  ModelAdmin.filter_vertical
    1.  ModelAdmin.form
    1.  ModelAdmin.formfield_overrides
    1.  ModelAdmin.inlines
    1.  ModelAdmin.list_display
    1.  ModelAdmin.list_display_links
    1.  ModelAdmin.list_editable
    1.  ModelAdmin.list_filter
    1.  ModelAdmin.list_max_show_all
    1.  ModelAdmin.list_per_page
    1.  ModelAdmin.list_select_related
    1.  ModelAdmin.ordering
    1.  ModelAdmin.paginator
    1.  ModelAdmin.prepopulated_fields
    1.  ModelAdmin.preserve_filters
    1.  ModelAdmin.radio_fields
    1.  ModelAdmin.autocomplete_fields
    1.  ModelAdmin.raw_id_fields
    1.  ModelAdmin.readonly_fields
    1.  ModelAdmin.save_as
    1.  ModelAdmin.save_as_continue
    1.  ModelAdmin.save_on_top
    1.  ModelAdmin.search_fields
    1.  ModelAdmin.show_full_result_count
    1.  ModelAdmin.sortable_by
    1.  ModelAdmin.view_on_site

1. Custom template options
    1. ModelAdmin.add_form_template
    1. ModelAdmin.change_form_template
    1. ModelAdmin.change_list_template
    1. ModelAdmin.delete_confirmation_template
    1. ModelAdmin.delete_selected_confirmation_template
    1. ModelAdmin.object_history_template
    1. ModelAdmin.popup_response_template

1. ModelAdmin methods
    1.  ModelAdmin.save_model(request, obj, form, change)
    1.  ModelAdmin.delete_model(request, obj)
    1.  ModelAdmin.delete_queryset(request, queryset)
    1.  ModelAdmin.save_formset(request, form, formset, change)
    1.  ModelAdmin.get_ordering(request)
    1.  ModelAdmin.get_search_results(request, queryset, search_term)
    1.  ModelAdmin.save_related(request, form, formsets, change)
    1.  ModelAdmin.get_autocomplete_fields(request)
    1.  ModelAdmin.get_readonly_fields(request, obj=None)
    1.  ModelAdmin.get_prepopulated_fields(request, obj=None)
    1.  ModelAdmin.get_list_display(request)
    1.  ModelAdmin.get_list_display_links(request, list_display)
    1.  ModelAdmin.get_exclude(request, obj=None)
    1.  ModelAdmin.get_fields(request, obj=None)
    1.  ModelAdmin.get_fieldsets(request, obj=None)
    1.  ModelAdmin.get_list_filter(request)
    1.  ModelAdmin.get_list_select_related(request)
    1.  ModelAdmin.get_search_fields(request)
    1.  ModelAdmin.get_sortable_by(request)
    1.  ModelAdmin.get_inline_instances(request, obj=None)
    1.  ModelAdmin.get_inlines(request, obj)
    1.  ModelAdmin.get_urls()
    1.  ModelAdmin.get_form(request, obj=None, **kwargs)
    1.  ModelAdmin.get_formsets_with_inlines(request, obj=None)
    1.  ModelAdmin.formfield_for_foreignkey(db_field, request, **kwargs)
    1.  ModelAdmin.formfield_for_manytomany(db_field, request, **kwargs)
    1.  ModelAdmin.formfield_for_choice_field(db_field, request, **kwargs)
    1.  ModelAdmin.get_changelist(request, **kwargs)
    1.  ModelAdmin.get_changelist_form(request, **kwargs)
    1.  ModelAdmin.get_changelist_formset(request, **kwargs)
    1.  ModelAdmin.lookup_allowed(lookup, value)
    1.  ModelAdmin.has_view_permission(request, obj=None)
    1.  ModelAdmin.has_add_permission(request)
    1.  ModelAdmin.has_change_permission(request, obj=None)
    1.  ModelAdmin.has_delete_permission(request, obj=None)
    1.  ModelAdmin.has_module_permission(request)
    1.  ModelAdmin.get_queryset(request)
    1.  ModelAdmin.message_user(request, message, level=messages.INFO, extra_tags='', fail_silently=False)
    1.  ModelAdmin.get_paginator(request, queryset, per_page, orphans=0, allow_empty_first_page=True)
    1.  ModelAdmin.response_add(request, obj, post_url_continue=None)
    1.  ModelAdmin.response_change(request, obj)
    1.  ModelAdmin.response_delete(request, obj_display, obj_id)
    1.  ModelAdmin.get_changeform_initial_data(request)
    1.  ModelAdmin.get_deleted_objects(objs, request)

1. Other methods

    1. ModelAdmin.add_view(request, form_url='', extra_context=None)
    1. ModelAdmin.change_view(request, object_id, form_url='', extra_context=None)
    1. ModelAdmin.changelist_view(request, extra_context=None)
    1. ModelAdmin.delete_view(request, object_id, extra_context=None)
    1. ModelAdmin.history_view(request, object_id, extra_context=None)

1. ModelAdmin asset definitions
    1. class Media 
    1. django.jQuery

1. Adding custom validation to the admin
    1. using django model form

1. InlineModelAdmin objects

    1. InlineModelAdmin options
    1. Working with a model with two or more foreign keys to the same parent model
    1. Working with many-to-many models
    1. Working with many-to-many intermediary models
    1. Using generic relations as an inline

1. Overriding admin templates

    1. Set up your projects admin template directories
    1. Overriding vs. replacing an admin template
    1. Templates which may be overridden per app or model
    1. Root and login templates

1. AdminSite objects

    1. AdminSite attributes
    1. AdminSite methods
    1. Hooking AdminSite instances into your URLconf
    1. Customizing the AdminSite class
    1. Overriding the default admin site
    1. Multiple admin sites in the same URLconf
    1. Adding views to admin sites
    1. Adding a password reset feature

1. LogEntry objects

    1. LogEntry attributes
    1. LogEntry methods

1. Reversing admin URLs
1. The staff_member_required decorator

### Working with forms

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
