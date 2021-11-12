from ssg.site import typer, Site


def main(source, dest):
   source = "content"
   dest = "dist"
   config = {"source": source, "dest": dest}
   Site(**config).build()


typer.run(main)