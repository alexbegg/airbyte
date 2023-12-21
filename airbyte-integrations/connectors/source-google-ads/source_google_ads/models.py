#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Union

from pendulum import timezone
from pendulum.tz.timezone import Timezone


@dataclass
class CustomerModel:
    id: str
    time_zone: Union[timezone, str] = "local"
    is_manager_account: bool = False
    login_customer_id: str = None

    @classmethod
    def from_accounts(cls, accounts: Iterable[Mapping[str, Any]], table_name: str = "customer_client") -> Iterable["CustomerModel"]:
        data_objects = []
        for account in accounts:
            time_zone_name = account.get(f"{table_name}.time_zone")
            tz = Timezone(time_zone_name) if time_zone_name else "local"

            data_objects.append(
                cls(
                    id=str(account[f"{table_name}.id"]),
                    time_zone=tz,
                    is_manager_account=bool(account.get(f"{table_name}.manager")),
                    login_customer_id=account.get("login_customer_id"),
                )
            )
        return data_objects
