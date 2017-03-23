import click

from globus_cli.safeio import safeprint
from globus_cli.parsing import common_options, endpoint_id_arg
from globus_cli.helpers import outformat_is_json, print_json_response

from globus_cli.services.transfer import get_client


@click.command('deactivate', help='Deactivate an Endpoint')
@common_options
@endpoint_id_arg
def endpoint_deactivate(endpoint_id):
    """
    Executor for `globus endpoint deactivate`
    """
    client = get_client()
    res = client.endpoint_deactivate(endpoint_id)

    if outformat_is_json():
        print_json_response(res)
    else:
        safeprint(res["message"])
