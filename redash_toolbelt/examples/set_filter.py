import click

from redash_toolbelt import Redash


def set_filter(client, slug):
    """Adjust all the filters in a dashboard to the same value
    """

    current_dashboard = client.dashboard(slug)

    # This is a version of the same logic from Redash.duplicate_dashboard
    # But it substitutes in the new visualiation ID pointing at the copied query.
    for widget in current_dashboard["widgets"]:
        if "visualization" in widget:
            widget["options"]["parameterMappings"]["vertriebspatner"] = {
                "name": "vertriebspatner",
                "type": "dashboard-level",
                "mapTo": "vertriebspatner",
                "value": ["---"],
                "title": ""
            }
            client.update_widget(widget["id"], widget)


@click.command()
@click.argument("redash_host")
@click.argument("slug")
@click.option(
    "--api-key",
    "api_key",
    envvar="REDASH_API_KEY",
    show_envvar=True,
    prompt="API Key",
    help="User API Key",
)
def main(redash_host, slug, api_key):
    """Calls the duplicate function using Click commands"""

    client = Redash(redash_host, api_key)
    set_filter(client, slug)


if __name__ == "__main__":
    main()
