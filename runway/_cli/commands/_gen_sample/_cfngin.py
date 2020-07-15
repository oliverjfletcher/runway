"""``runway gen-sample cfngin`` command."""
import logging
import shutil
import sys

import click

from .utils import ROOT, TEMPLATES, copy_sample

if sys.version_info.major > 2:
    from pathlib import Path  # pylint: disable=E
else:
    from pathlib2 import Path  # pylint: disable=E

LOGGER = logging.getLogger(__name__.replace('._', '.'))


@click.command('cfngin',
               short_help="cfngin + troposphere (sampleapp.cfn)")
@click.pass_context
def cfngin(ctx):
    # type: (click.Context) -> None
    """Generate a sample CFNgin project using Blueprints."""
    src = TEMPLATES / 'cfngin'
    src_blueprints = ROOT / 'blueprints'
    dest = Path.cwd() / 'sampleapp.cfn'
    blueprints = dest / 'tfstate_blueprints'
    tf_state = blueprints / 'tf_state.py'

    copy_sample(ctx, src, dest)

    blueprints.mkdir()
    LOGGER.debug('copying blueprint from "%s" to "%s"', src_blueprints,
                 blueprints)
    shutil.copyfile(str(src_blueprints / '__init__.py'),
                    str(blueprints / '__init__.py'))
    shutil.copyfile(str(src_blueprints / 'tf_state.py'), str(tf_state))
    tf_state.chmod(tf_state.stat().st_mode | 0o0111)
    LOGGER.info("Sample CFNgin module created at %s",
                dest)