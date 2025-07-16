# camus/cli.py
import typer
import shutil
from pathlib import Path
from camus.core import CamusApp

cli = typer.Typer(help="Camus – real-time app framework")

@cli.command()
def init(project_name: str):
    """
    Scaffold a new example chat app in ./examples/chat/
    """
    tpl_dir = Path(__file__).parent / ".." / "examples" / "chat"
    dest_dir = Path.cwd() / project_name
    if dest_dir.exists():
        typer.secho(f"Directory {dest_dir} already exists", fg="red")
        raise typer.Exit(1)
    shutil.copytree(tpl_dir, dest_dir)
    typer.secho(f"Scaffolded example in {dest_dir}", fg="green")

@cli.command()
def serve(host: str = None, port: int = None):
    """
    Load config.yaml and run your app
    """
    cfg = Path("config.yaml")
    if not cfg.exists():
        typer.secho("Missing config.yaml in current directory", fg="red")
        raise typer.Exit(1)
    # If you have a single example, we default to running examples/chat/app.py
    # Otherwise you can import your own CamusApp instance here.
    import examples.chat.app as app_module
    app: CamusApp = app_module.app  # expect `app = CamusApp(...)`
    typer.secho(f"Serving {app.name} on {host or app.config['server']['host']}:{port or app.config['server']['port']}", fg="blue")
    app.run(host=host, port=port)

@cli.command()
def build(tag: str):
    """
    Build a Docker image tagged TAG
    """
    import subprocess
    subprocess.run(["docker", "build", "-t", tag, "."], check=True)
    typer.secho(f"Docker image built: {tag}", fg="green")

if __name__ == "__main__":
    cli()
