from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.responsecode import RESPONSECODE
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_desc import EngineDesc


T = TypeVar("T", bound="EngineListResp")


@_attrs_define
class EngineListResp:
    """
    Attributes:
        code (RESPONSECODE):
        message (str):
        data (Union[Unset, list['EngineDesc']]):
    """

    code: RESPONSECODE
    message: str
    data: Union[Unset, list["EngineDesc"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.engine_desc import EngineDesc

        d = dict(src_dict)
        code = RESPONSECODE(d.pop("code"))

        message = d.pop("message")

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = EngineDesc.from_dict(data_item_data)

            data.append(data_item)

        engine_list_resp = cls(
            code=code,
            message=message,
            data=data,
        )

        engine_list_resp.additional_properties = d
        return engine_list_resp

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
