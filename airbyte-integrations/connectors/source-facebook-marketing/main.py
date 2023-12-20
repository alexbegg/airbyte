#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_facebook_marketing import SourceFacebookMarketing
from source_facebook_marketing.config_migrations import MigrateAccountIdToArray

if __name__ == "__main__":
    source = SourceFacebookMarketing()
    MigrateAccountIdToArray.migrate(sys.argv[1:], source)
    launch(source, sys.argv[1:])
