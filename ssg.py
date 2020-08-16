import typer
from ssg.site import  Site
from ssg import parsers

def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest,
        "parsers": parsers.ResourceParser()
    }
    Site(**config).build()

typer.run(main)