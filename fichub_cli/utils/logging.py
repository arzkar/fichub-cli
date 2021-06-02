import click
from loguru import logger


def init_log(debug: bool, force: bool):
    if debug:
        logger.info(
            "Download Started. Will update existing epub files if found. Use --force flag to overwrite.")
        if force:
            logger.warning(
                "--force flag was passed. Files will be overwritten.")
    else:
        click.secho("Download Started", fg='green')
        if force:
            click.secho(
                "WARNING: --force flag was passed. Files will be overwritten.", fg='yellow')


def downloaded_log(debug: bool, file_name: str):
    if debug:
        logger.info(f"Downloaded {file_name}")
    else:
        click.secho(
            f"Downloaded {file_name}", fg='green')


def download_processing_log(debug: bool, url: str):
    if debug:
        logger.info(f"Processing {url}")
    else:
        click.secho(
            f"\n\nProcessing {url}", fg='blue')