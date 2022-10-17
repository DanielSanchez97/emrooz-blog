# Generated as part of Quick Start project template 
 
from cdev.aws.frontend import Site
from cdev import Project as cdev_project

from src.project_settings import EmroozSettings 

myProject = cdev_project.instance()
settings: EmroozSettings = myProject.settings


ssl_certificate_arn = 'arn:aws:acm:us-east-1:936870855874:certificate/3d6a85e0-7357-41f4-b782-a9990b26a06f'
domain_name = settings.DOMAIN 

myFrontend = Site(
    "emrooz_site", 
    content_folder="public", 
    index_document='index.html', 
    ssl_certificate_arn=ssl_certificate_arn, 
    domain_name=domain_name
)
 

myProject.display_output("Static Site URl", myFrontend.output.site_url)